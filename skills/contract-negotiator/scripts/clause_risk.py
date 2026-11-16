#!/usr/bin/env python3
"""Score a contract's clauses against the playbook, and say what to do with each.

Reads a clause register (one row per material clause) and returns, per clause, a
risk level and a decision:

    ok          within our preferred position            -> accept
    negotiate   inside the hard bound, off preferred      -> redline, with a trade
    escalate    outside the hard bound                    -> founder or lawyer decides
    unreadable  the value is missing or not a number      -> ask for the clause again

The playbook here is the commercial position in references/redline-playbook.md,
not legal advice. Deterministic: no network, no randomness, no wall clock.

Register CSV: clause_id, clause, clause_type, value, value_at_risk
    value          the number or the text being tested (12, 45, "none", ...)
    value_at_risk  rupees, or 0 when it cannot be priced

Usage:
    python3 clause_risk.py --register clauses.csv
    python3 clause_risk.py --self-test
"""
import csv
import sys

COLUMNS = ["clause_id", "clause", "clause_type", "value", "value_at_risk"]

# kind: num tests a number against ok_/hard_ bounds; text tests membership.
PLAYBOOK = {
    "liability_cap_months": {
        "kind": "num", "ok_min": 12, "hard_min": 3,
        "why": "a cap under three months of fees is not a cap"},
    "payment_terms_days": {
        "kind": "num", "ok_max": 30, "hard_max": 60,
        "why": "every 15 extra days is working capital"},
    "termination_notice_days": {
        "kind": "num", "ok_max": 45, "hard_max": 90,
        "why": "a long notice period is a lock-in"},
    "auto_renewal_months": {
        "kind": "num", "ok_max": 0, "hard_max": 12,
        "why": "auto-renewal turns a decision into a default"},
    "price_escalation_pct": {
        "kind": "num", "ok_max": 5, "hard_max": 10,
        "why": "an uncapped escalation is a price not yet agreed"},
    "uptime_pct": {
        "kind": "num", "ok_min": 99, "hard_min": 95,
        "why": "below 95% the service is not a service"},
    "penalty_late_fee_pct": {
        "kind": "num", "ok_max": 0, "hard_max": 2,
        "why": "a penalty should price a risk, not transfer business risk"},
    "ip_ownership": {
        "kind": "text",
        "ok": ["we_own_background_ip_and_license_deliverables"],
        "hard": ["customer_owns_deliverables", "joint"],
        "why": "the reusable parts are the business"},
    "exclusivity": {
        "kind": "text", "ok": ["none"], "hard": [],
        "why": "exclusivity is a permanent cost against a temporary order"},
    "jurisdiction": {
        "kind": "text", "ok": ["our_city"], "hard": ["neutral"],
        "why": "enforcing abroad costs more than most disputes"},
}

ORDER = {"escalate": 0, "negotiate": 1, "unreadable": 2, "ok": 3}
DECISION = {"ok": "accept", "negotiate": "redline", "escalate": "escalate",
            "unreadable": "ask again"}


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("missing columns: %s" % ", ".join(missing))
        for raw in reader:
            rows.append({
                "clause_id": raw["clause_id"].strip(),
                "clause": raw["clause"].strip(),
                "clause_type": raw["clause_type"].strip(),
                "value": raw["value"].strip(),
                "value_at_risk": float(raw["value_at_risk"] or 0),
            })
    return rows


def score(clause_type, value):
    """Return (risk, reason). Anything unrecognised is unreadable, never ok."""
    rule = PLAYBOOK.get(clause_type)
    if rule is None:
        return "unreadable", "clause type %r is not in the playbook" % clause_type
    if rule["kind"] == "num":
        try:
            v = float(value)
        except (TypeError, ValueError):
            return "unreadable", "value %r is not a number" % value
        if "ok_min" in rule and v < rule["hard_min"]:
            return "escalate", "%g is under the hard floor of %g - %s" % (v, rule["hard_min"], rule["why"])
        if "ok_max" in rule and v > rule["hard_max"]:
            return "escalate", "%g is over the hard ceiling of %g - %s" % (v, rule["hard_max"], rule["why"])
        if "ok_min" in rule and v < rule["ok_min"]:
            return "negotiate", "%g is under our ask of %g - %s" % (v, rule["ok_min"], rule["why"])
        if "ok_max" in rule and v > rule["ok_max"]:
            return "negotiate", "%g is over our ask of %g - %s" % (v, rule["ok_max"], rule["why"])
        return "ok", "within our preferred position"
    text = value.lower()
    if text in [x.lower() for x in rule["ok"]]:
        return "ok", "within our preferred position"
    if text in [x.lower() for x in rule["hard"]]:
        return "negotiate", "acceptable but off preferred - %s" % rule["why"]
    return "escalate", "%r is outside anything we can accept - %s" % (value, rule["why"])


def analyse(rows):
    items = []
    for r in rows:
        risk, reason = score(r["clause_type"], r["value"])
        item = dict(r)
        item["risk"] = risk
        item["reason"] = reason
        item["decision"] = DECISION[risk]
        items.append(item)
    items.sort(key=lambda x: (ORDER[x["risk"]], -x["value_at_risk"], x["clause_id"]))
    return items


def summarise(items):
    counts = {}
    for i in items:
        counts[i["risk"]] = counts.get(i["risk"], 0) + 1
    return {
        "count": len(items),
        "counts": counts,
        "exposed": sum(i["value_at_risk"] for i in items if i["risk"] in ("escalate", "negotiate")),
        "escalations": [i for i in items if i["risk"] == "escalate"],
    }


def render(items, summary):
    out = ["# Clause risk read", ""]
    out.append("Clauses read: **%d** | ok: %d | negotiate: %d | escalate: %d | unreadable: %d"
               % (summary["count"], summary["counts"].get("ok", 0),
                  summary["counts"].get("negotiate", 0),
                  summary["counts"].get("escalate", 0),
                  summary["counts"].get("unreadable", 0)))
    out.append("Value at risk across negotiate and escalate: **₹%.0f**" % summary["exposed"])
    out.append("")
    if summary["escalations"]:
        out.append("**Escalate before anything else:** "
                   + ", ".join("%s (₹%.0f)" % (i["clause_id"], i["value_at_risk"])
                               for i in summary["escalations"]))
        out.append("")
    out.append("| # | Clause | Type | Value | Risk | Decision | Why |")
    out.append("|---|---|---|---|---|---|---|")
    for i in items:
        out.append("| %s | %s | %s | %s | %s | %s | %s |"
                   % (i["clause_id"], i["clause"].replace("|", "/"), i["clause_type"],
                      i["value"], i["risk"], i["decision"], i["reason"]))
    out.append("")
    out.append("_Computed by scripts/clause_risk.py against the playbook in "
               "references/redline-playbook.md. A commercial position, not a legal opinion: "
               "enforceability, jurisdiction and stamp duty go to a lawyer._")
    return "\n".join(out)


FIXTURE = """clause_id,clause,clause_type,value,value_at_risk
9.2,Limitation of liability,liability_cap_months,6,400000
5.1,Payment terms,payment_terms_days,45,250000
11.4,Termination for convenience,termination_notice_days,120,100000
3.7,Renewal,auto_renewal_months,12,0
14.1,Intellectual property,ip_ownership,we_assign_all_ip,800000
7.3,Exclusivity,exclusivity,none,0
4.2,Service levels,uptime_pct,99.5,0
16.2,Governing law,jurisdiction,their_city,50000
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
    check("rows", len(rows), 8)
    items = analyse(rows)
    by_id = {i["clause_id"]: i for i in items}

    check("9.2 negotiate", by_id["9.2"]["risk"], "negotiate")
    check("9.2 decision", by_id["9.2"]["decision"], "redline")
    check("5.1 negotiate", by_id["5.1"]["risk"], "negotiate")
    check("11.4 escalate", by_id["11.4"]["risk"], "escalate")
    check("3.7 negotiate", by_id["3.7"]["risk"], "negotiate")
    check("14.1 escalate", by_id["14.1"]["risk"], "escalate")
    check("7.3 ok", by_id["7.3"]["risk"], "ok")
    check("4.2 ok", by_id["4.2"]["risk"], "ok")
    check("16.2 escalate", by_id["16.2"]["risk"], "escalate")
    check("order", [i["clause_id"] for i in items],
          ["14.1", "11.4", "16.2", "9.2", "5.1", "3.7", "4.2", "7.3"])

    summary = summarise(items)
    check("counts escalate", summary["counts"]["escalate"], 3)
    check("counts negotiate", summary["counts"]["negotiate"], 3)
    check("counts ok", summary["counts"]["ok"], 2)
    check("exposed", summary["exposed"], 1600000.0)
    check("escalation ids", [i["clause_id"] for i in summary["escalations"]],
          ["14.1", "11.4", "16.2"])

    check("bad number unreadable", score("payment_terms_days", "ninety")[0], "unreadable")
    check("unknown type unreadable", score("arbitration_seat", "delhi")[0], "unreadable")
    check("hard floor breach", score("liability_cap_months", "2")[0], "escalate")
    check("text hard bound", score("ip_ownership", "joint")[0], "negotiate")

    text = render(items, summary)
    check("report names escalation", "14.1" in text, True)
    check("determinism", render(analyse(load(path)), summarise(analyse(load(path)))) == text, True)
    print("self-test: %s" % ("PASS (25 checks)" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if len(argv) < 2 or "--register" not in argv:
        print(__doc__)
        return 2
    path = argv[argv.index("--register") + 1]
    try:
        rows = load(path)
    except (ValueError, KeyError) as exc:
        print("cannot read %s: %s" % (path, exc))
        return 2
    items = analyse(rows)
    print(render(items, summarise(items)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
