#!/usr/bin/env python3
"""Turn an account export into onboarding numbers.

Reads a CSV of accounts in onboarding and reports, as of a date you supply:

  * time to first value per account, and the median and worst case
  * activation rate by day 7, 14 and 30 from the signed date
  * the stalled list - accounts past a milestone date with no first value

The as-of date is an argument, never the wall clock, so the same file always
produces the same report. No network, no randomness.

CSV columns (header required, order free):
    account_id, signed_date, plan, mrr, kickoff_date, first_value_date,
    go_live_target

Dates are YYYY-MM-DD. first_value_date may be empty. go_live_target may be
empty. Everything else is required.

Usage:
    python3 activation_report.py accounts.csv --as-of 2026-11-16
    python3 activation_report.py --self-test
"""
import csv
import sys
from datetime import date

COLUMNS = ["account_id", "signed_date", "plan", "mrr", "kickoff_date",
           "first_value_date", "go_live_target"]


def parse_date(value):
    if not value:
        return None
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
            rows.append({
                "account_id": raw["account_id"].strip(),
                "signed": parse_date(raw["signed_date"].strip()),
                "plan": raw["plan"].strip(),
                "mrr": float(raw["mrr"] or 0),
                "kickoff": parse_date(raw["kickoff_date"].strip()),
                "first_value": parse_date(raw["first_value_date"].strip()),
                "target": parse_date(raw["go_live_target"].strip()),
            })
    return rows


def median(values):
    if not values:
        return None
    s = sorted(values)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2.0


def analyse(rows, as_of):
    out = {"accounts": len(rows), "ttfv": [], "live_7": 0, "live_14": 0,
           "live_30": 0, "stalled": [], "median": None, "worst": None,
           "worst_id": None, "open": 0}
    for r in rows:
        if r["first_value"]:
            days = (r["first_value"] - r["signed"]).days
            out["ttfv"].append((r["account_id"], days))
            for mark in (7, 14, 30):
                if days <= mark:
                    out["live_%d" % mark] += 1
        else:
            out["open"] += 1
            if r["target"] and as_of > r["target"]:
                out["stalled"].append({
                    "account_id": r["account_id"],
                    "plan": r["plan"],
                    "mrr": r["mrr"],
                    "overdue_days": (as_of - r["target"]).days,
                    "reason": "past go-live target with no first value",
                })
            elif r["kickoff"] is None and (as_of - r["signed"]).days > 5:
                out["stalled"].append({
                    "account_id": r["account_id"],
                    "plan": r["plan"],
                    "mrr": r["mrr"],
                    "overdue_days": (as_of - r["signed"]).days - 5,
                    "reason": "no kickoff within 5 days of signature",
                })
    days = [d for _, d in out["ttfv"]]
    out["median"] = median(days)
    if days:
        wid, wd = max(out["ttfv"], key=lambda x: (x[1], x[0]))
        out["worst"], out["worst_id"] = wd, wid
    out["stalled"].sort(key=lambda s: (-s["mrr"], -s["overdue_days"]))
    return out


def render(res, as_of):
    def rate(n, d):
        return "0%" if not d else "%.0f%%" % (100.0 * n / d)
    lines = []
    lines.append("# Onboarding activation report - as of %s" % as_of.isoformat())
    lines.append("")
    lines.append("Accounts in onboarding: **%d** | live: %d | still open: %d"
                 % (res["accounts"], len(res["ttfv"]), res["open"]))
    med = "-" if res["median"] is None else ("%g" % res["median"])
    worst = "-" if res["worst"] is None else "%d days (%s)" % (res["worst"], res["worst_id"])
    lines.append("Time to first value: median **%s days**, worst **%s**" % (med, worst))
    lines.append("")
    lines.append("| Activated by | Accounts | Share of all |")
    lines.append("|---|---|---|")
    for mark in (7, 14, 30):
        lines.append("| day %d | %d | %s |" % (mark, res["live_%d" % mark],
                                               rate(res["live_%d" % mark], res["accounts"])))
    lines.append("")
    if res["stalled"]:
        lines.append("## Stalled, ordered by value at risk")
        lines.append("")
        lines.append("| Account | Plan | MRR | Overdue (days) | Reason |")
        lines.append("|---|---|---|---|---|")
        for s in res["stalled"]:
            lines.append("| %s | %s | %.0f | %d | %s |"
                         % (s["account_id"], s["plan"], s["mrr"], s["overdue_days"], s["reason"]))
    else:
        lines.append("## Stalled")
        lines.append("")
        lines.append("None past a dated milestone as of %s." % as_of.isoformat())
    lines.append("")
    lines.append("_Computed by scripts/activation_report.py from the account export. "
                 "Accounts without a first-value date are unverified, not live._")
    return "\n".join(lines)


FIXTURE = """account_id,signed_date,plan,mrr,kickoff_date,first_value_date,go_live_target
A-101,2026-10-01,growth,25000,2026-10-02,2026-10-06,2026-10-20
A-102,2026-10-03,starter,8000,2026-10-05,2026-10-15,2026-10-25
A-103,2026-10-08,growth,25000,2026-10-12,2026-11-02,2026-11-01
A-104,2026-10-20,starter,8000,2026-10-21,,2026-11-10
A-105,2026-11-10,growth,25000,,,2026-12-01
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
    res = analyse(rows, date(2026, 11, 16))

    check("accounts", res["accounts"], 5)
    check("live", len(res["ttfv"]), 3)
    check("open", res["open"], 2)
    check("ttfv A-101", dict(res["ttfv"])["A-101"], 5)
    check("ttfv A-102", dict(res["ttfv"])["A-102"], 12)
    check("ttfv A-103", dict(res["ttfv"])["A-103"], 25)
    check("median", res["median"], 12)
    check("worst", res["worst"], 25)
    check("worst_id", res["worst_id"], "A-103")
    check("live by 7", res["live_7"], 1)
    check("live by 14", res["live_14"], 2)
    check("live by 30", res["live_30"], 3)
    check("stalled count", len(res["stalled"]), 2)
    # ordered by value at risk: A-105 is the 25,000 growth account, A-104 the 8,000 starter
    check("stalled order", [s["account_id"] for s in res["stalled"]], ["A-105", "A-104"])
    check("A-105 reason", res["stalled"][0]["reason"], "no kickoff within 5 days of signature")
    check("A-105 overdue", res["stalled"][0]["overdue_days"], 1)
    check("A-104 overdue", res["stalled"][1]["overdue_days"], 6)

    text = render(res, date(2026, 11, 16))
    check("report has median line", "median **12 days**" in text, True)
    check("report lists A-104", "| A-104 |" in text, True)
    check("determinism", render(analyse(load(path), date(2026, 11, 16)),
                                date(2026, 11, 16)) == text, True)
    check("bad columns rejected", _rejects_bad_columns(), True)

    print("self-test: %s" % ("PASS (17 checks)" if ok else "FAIL"))
    return 0 if ok else 1


def _rejects_bad_columns():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        fh.write("account_id,signed_date\nA-1,2026-10-01\n")
        path = fh.name
    try:
        load(path)
    except ValueError:
        return True
    return False


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    if "--as-of" not in argv:
        print("--as-of YYYY-MM-DD is required: the report has no wall clock")
        return 2
    as_of = parse_date(argv[argv.index("--as-of") + 1])
    try:
        rows = load(path)
    except (ValueError, KeyError) as exc:
        print("cannot read %s: %s" % (path, exc))
        return 2
    print(render(analyse(rows, as_of), as_of))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
