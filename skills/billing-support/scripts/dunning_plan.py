#!/usr/bin/env python3
"""Place every failed payment on the dunning ladder, as of a date you supply.

Reads a failed-payment export, classifies each invoice by the gateway failure
code, works out which rung of the ladder it is on and what the next action is,
and totals the value still recoverable. Deterministic: the as-of date is an
argument, never the wall clock.

CSV columns (header required, order free):
    invoice_id, account_id, amount, currency, failed_on, attempt_count,
    failure_code, plan

Usage:
    python3 dunning_plan.py failures.csv --as-of 2026-11-16
    python3 dunning_plan.py failures.csv --as-of 2026-11-16 --ladder 0,3,7,14,21
    python3 dunning_plan.py --self-test
"""
import csv
import sys
from datetime import date, timedelta

COLUMNS = ["invoice_id", "account_id", "amount", "currency", "failed_on",
           "attempt_count", "failure_code", "plan"]

DEFAULT_LADDER = [0, 3, 7, 14, 21]

# What each code means for the customer, from references/failed-payments-and-dunning.md.
CODES = {
    "insufficient_funds": ("retry", "Bank declined for insufficient funds; retry after a salary date"),
    "card_expired": ("new_card", "The card on file has expired; ask for a new one, never retry"),
    "do_not_honor": ("retry_once", "Issuer declined; one retry, then a new card request"),
    "authentication_required": ("fresh_link", "The bank needs the customer to approve once"),
    "invalid_account": ("ours", "Usually a configuration error on our side; check before replying"),
    "processing_error": ("ours", "Gateway or configuration error; check before replying"),
    "mandate_revoked": ("fresh_mandate", "The standing instruction was cancelled; ask for a new mandate"),
}

RUNG_MESSAGE = {
    0: "day-0 email: what failed, why, the link",
    1: "day-3 email + WhatsApp: one retry has happened, ask again with the reason",
    2: "day-7 email copying the account owner: name the consequence and the date",
    3: "day-14 call by the owner: find the real blocker",
    4: "day-21 final notice: suspend at a stated date, say what it stops",
}


def parse_date(value):
    y, m, d = value.split("-")
    return date(int(y), int(m), int(d))


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("missing columns: %s" % ", ".join(missing))
        for raw in reader:
            code = raw["failure_code"].strip()
            action, meaning = CODES.get(code, ("manual", "Unrecognised code; read the gateway message"))
            rows.append({
                "invoice_id": raw["invoice_id"].strip(),
                "account_id": raw["account_id"].strip(),
                "amount": float(raw["amount"]),
                "currency": raw["currency"].strip(),
                "failed_on": parse_date(raw["failed_on"].strip()),
                "attempts": int(raw["attempt_count"]),
                "code": code,
                "plan": raw["plan"].strip(),
                "action": action,
                "meaning": meaning,
            })
    return rows


def rung_for(days_since, ladder):
    rung = 0
    for i, day in enumerate(ladder):
        if days_since >= day:
            rung = i
    return rung


def plan(rows, as_of, ladder=None):
    ladder = ladder or DEFAULT_LADDER
    out = []
    for r in rows:
        days = (as_of - r["failed_on"]).days
        rung = rung_for(days, ladder)
        next_day = ladder[rung + 1] if rung + 1 < len(ladder) else None
        item = dict(r)
        item["days"] = days
        item["rung"] = rung
        item["message"] = RUNG_MESSAGE[rung]
        item["next_action_on"] = (r["failed_on"] + timedelta(days=next_day)) if next_day is not None else None
        item["recoverable"] = rung < len(ladder) - 1 or days < ladder[-1] + 7
        out.append(item)
    out.sort(key=lambda x: (x["rung"], -x["amount"], x["invoice_id"]))
    return out


def summarise(items):
    by_rung = {}
    for i in items:
        by_rung.setdefault(i["rung"], []).append(i)
    by_code = {}
    for i in items:
        by_code[i["code"]] = by_code.get(i["code"], 0) + 1
    return {
        "count": len(items),
        "value": sum(i["amount"] for i in items),
        "recoverable_value": sum(i["amount"] for i in items if i["recoverable"]),
        "by_rung": by_rung,
        "by_code": by_code,
        "ours": [i for i in items if i["action"] == "ours"],
    }


def render(items, summary, as_of):
    out = ["# Dunning plan - as of %s" % as_of.isoformat(), ""]
    out.append("Failed invoices: **%d** | value **%.0f** | still recoverable **%.0f**"
               % (summary["count"], summary["value"], summary["recoverable_value"]))
    out.append("")
    if summary["ours"]:
        out.append("**Our error, reply first:** " + ", ".join(i["invoice_id"] for i in summary["ours"]))
        out.append("")
    out.append("| Rung | Invoices | Value | Message for this rung |")
    out.append("|---|---|---|---|")
    for rung in sorted(summary["by_rung"]):
        items_at = summary["by_rung"][rung]
        out.append("| %d | %d | %.0f | %s |" % (rung, len(items_at),
                                                sum(i["amount"] for i in items_at),
                                                RUNG_MESSAGE[rung]))
    out.append("")
    out.append("## Failures by code")
    out.append("")
    out.append("| Code | Invoices | What it means | Action |")
    out.append("|---|---|---|---|")
    seen = {}
    for i in items:
        seen.setdefault(i["code"], i)
    for code in sorted(summary["by_code"]):
        sample = seen[code]
        out.append("| %s | %d | %s | %s |" % (code, summary["by_code"][code],
                                              sample["meaning"], sample["action"]))
    out.append("")
    out.append("## Per invoice")
    out.append("")
    out.append("| Invoice | Account | Amount | Days | Rung | Action | Next action on |")
    out.append("|---|---|---|---|---|---|---|")
    for i in items:
        nxt = i["next_action_on"].isoformat() if i["next_action_on"] else "-"
        out.append("| %s | %s | %s %.0f | %d | %d | %s | %s |"
                   % (i["invoice_id"], i["account_id"], i["currency"], i["amount"],
                      i["days"], i["rung"], i["action"], nxt))
    out.append("")
    out.append("_Computed by scripts/dunning_plan.py. Replies are drafts; the owner sends them. "
               "Refunds and retries are prepared here, never executed._")
    return "\n".join(out)


FIXTURE = """invoice_id,account_id,amount,currency,failed_on,attempt_count,failure_code,plan
INV-9001,A-101,25000,INR,2026-11-14,1,insufficient_funds,growth
INV-9002,A-102,8000,INR,2026-11-02,3,card_expired,starter
INV-9003,A-103,25000,INR,2026-10-26,2,do_not_honor,growth
INV-9004,A-104,8000,INR,2026-11-16,1,invalid_account,starter
INV-9005,A-105,12000,INR,2026-11-09,2,authentication_required,starter
"""


def self_test():
    import tempfile
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("FAIL %s: got %r, want %r" % (label, got, want))

    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        fh.write(FIXTURE)
        path = fh.name
    rows = load(path)
    check("rows", len(rows), 5)
    check("unknown code defaults", _unknown_code(path), "manual")

    items = plan(rows, date(2026, 11, 16))
    by_id = {i["invoice_id"]: i for i in items}
    check("INV-9001 rung 0", by_id["INV-9001"]["rung"], 0)
    check("INV-9001 days", by_id["INV-9001"]["days"], 2)
    check("INV-9001 next", by_id["INV-9001"]["next_action_on"], date(2026, 11, 17))
    check("INV-9002 rung 3", by_id["INV-9002"]["rung"], 3)
    check("INV-9002 action", by_id["INV-9002"]["action"], "new_card")
    check("INV-9003 rung 4", by_id["INV-9003"]["rung"], 4)
    check("INV-9003 next", by_id["INV-9003"]["next_action_on"], None)
    check("INV-9004 ours", by_id["INV-9004"]["action"], "ours")
    check("INV-9005 rung 2", by_id["INV-9005"]["rung"], 2)
    check("INV-9005 next", by_id["INV-9005"]["next_action_on"], date(2026, 11, 23))
    check("sorted by rung then value", [i["invoice_id"] for i in items],
          ["INV-9001", "INV-9004", "INV-9005", "INV-9002", "INV-9003"])

    summary = summarise(items)
    check("count", summary["count"], 5)
    check("total value", summary["value"], 78000.0)
    check("ours count", len(summary["ours"]), 1)
    check("code counts", summary["by_code"]["insufficient_funds"], 1)
    check("custom ladder", _custom_ladder(rows), 2)

    text = render(items, summary, date(2026, 11, 16))
    check("report names ours", "INV-9004" in text, True)
    check("report has rung table", "| 4 |" in text, True)
    check("determinism", render(plan(load(path), date(2026, 11, 16)),
                                summarise(plan(load(path), date(2026, 11, 16))),
                                date(2026, 11, 16)) == text, True)
    print("self-test: %s" % ("PASS (21 checks)" if ok else "FAIL"))
    return 0 if ok else 1


def _unknown_code(path):
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        fh.write("invoice_id,account_id,amount,currency,failed_on,attempt_count,failure_code,plan\n"
                 "INV-1,A-1,100,INR,2026-11-01,1,some_new_code,starter\n")
        p = fh.name
    return load(p)[0]["action"]


def _custom_ladder(rows):
    items = plan(rows, date(2026, 11, 16), [0, 1, 2])
    return {i["invoice_id"]: i["rung"] for i in items}["INV-9003"]


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if len(argv) < 2 or "--as-of" not in argv:
        print(__doc__)
        return 2
    path = argv[1]
    as_of = parse_date(argv[argv.index("--as-of") + 1])
    ladder = None
    if "--ladder" in argv:
        ladder = [int(x) for x in argv[argv.index("--ladder") + 1].split(",")]
    try:
        rows = load(path)
    except (ValueError, KeyError) as exc:
        print("cannot read %s: %s" % (path, exc))
        return 2
    items = plan(rows, as_of, ladder)
    print(render(items, summarise(items), as_of))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
