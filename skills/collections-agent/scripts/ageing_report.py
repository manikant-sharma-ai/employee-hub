#!/usr/bin/env python3
"""Deterministic receivables ageing, ranking and forecast.

Reads a ledger CSV and produces the same buckets, the same ranking and the same
DSO every week, so the argument is about the invoices and not about the arithmetic.

CSV columns (header required):
  invoice,customer,amount,invoice_date,due_date,received,disputed,promised_date
Dates are YYYY-MM-DD. `received` and `disputed` default to 0. `promised_date`
may be empty. The disputed amount is excluded from the chase figure and reported
separately - it is owed, it is just argued about.

Usage:
  python3 ageing_report.py ledger.csv [--today 2026-11-06] [--top 5]
  python3 ageing_report.py --self-test

Exit 0 = report produced, 1 = bad input, 2 = file not readable.
"""
import csv
import datetime
import os
import sys
import tempfile

BUCKETS = [("current", None, 0), ("1-30", 1, 30), ("31-60", 31, 60),
           ("61-90", 61, 90), ("90+", 91, 10 ** 6)]
STAGES = [(45, "stage 5 - final"), (30, "stage 4 - formal"), (15, "stage 3 - call"),
          (7, "stage 2 - dated"), (1, "stage 1 - oversight"), (0, "none - not due")]


def bucket_for(days_past_due):
    if days_past_due <= 0:
        return "current"
    for name, low, high in BUCKETS[1:]:
        if low <= days_past_due <= high:
            return name
    return "90+"


def stage_for(days_past_due):
    for floor, name in STAGES:
        if days_past_due >= floor:
            return name
    return "none - not due"


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for raw in csv.DictReader(fh):
            try:
                amount = float(raw["amount"])
                received = float(raw.get("received") or 0)
                disputed = float(raw.get("disputed") or 0)
                inv_date = datetime.date.fromisoformat(raw["invoice_date"].strip())
                due_date = datetime.date.fromisoformat(raw["due_date"].strip())
            except (KeyError, ValueError) as exc:
                raise ValueError("bad row %r: %s" % (raw.get("invoice"), exc))
            promised = (raw.get("promised_date") or "").strip()
            rows.append({
                "invoice": raw.get("invoice", "").strip(),
                "customer": raw.get("customer", "").strip(),
                "amount": amount,
                "received": received,
                "disputed": disputed,
                "balance": round(amount - received, 2),
                "invoice_date": inv_date,
                "due_date": due_date,
                "promised_date": datetime.date.fromisoformat(promised) if promised else None,
            })
    if not rows:
        raise ValueError("ledger has no rows")
    return rows


def analyse(rows, today):
    total_balance = sum(r["balance"] for r in rows if r["balance"] > 0)
    weighted_days = 0.0
    buckets = {name: {"count": 0, "amount": 0.0} for name, _, _ in BUCKETS}
    for r in rows:
        if r["balance"] <= 0:
            continue
        dpd = (today - r["due_date"]).days
        r["days_past_due"] = dpd
        r["bucket"] = bucket_for(dpd)
        r["stage"] = stage_for(dpd)
        r["chase_now"] = round(max(r["balance"] - r["disputed"], 0), 2)
        r["money_days"] = round(r["balance"] * max(dpd, 0))
        r["days_outstanding"] = (today - r["invoice_date"]).days
        weighted_days += r["balance"] * r["days_outstanding"]
        buckets[r["bucket"]]["count"] += 1
        buckets[r["bucket"]]["amount"] += r["balance"]
    dso = round(weighted_days / total_balance, 1) if total_balance else 0.0
    ranked = sorted([r for r in rows if r["balance"] > 0],
                    key=lambda r: (-r["money_days"], -r["balance"]))
    week = today + datetime.timedelta(days=7)
    promised = [r for r in ranked if r["promised_date"] and today <= r["promised_date"] <= week]
    return {
        "buckets": buckets,
        "dso": dso,
        "total": round(total_balance, 2),
        "ranked": ranked,
        "promised_this_week": round(sum(r["balance"] for r in promised), 2),
        "disputed_total": round(sum(r["disputed"] for r in rows), 2),
    }


def report(result, top):
    print("ageing report - total outstanding Rs %s, DSO %.1f days"
          % (format(int(result["total"]), ","), result["dso"]))
    print("  bucket     count        amount")
    for name, _, _ in BUCKETS:
        b = result["buckets"][name]
        print("  %-9s %6d  %12s" % (name, b["count"], format(int(b["amount"]), ",")))
    print("  disputed (separate, still owed): Rs %s" % format(int(result["disputed_total"]), ","))
    print("  promised inside 7 days:         Rs %s" % format(int(result["promised_this_week"]), ","))
    print("\ntop %d by money-days:" % top)
    print("  invoice    customer            balance   dpd  bucket  stage             chase now")
    for r in result["ranked"][:top]:
        print("  %-10s %-18s %9s %5d  %-6s  %-16s %9s"
              % (r["invoice"], r["customer"][:18], format(int(r["balance"]), ","),
                 r["days_past_due"], r["bucket"], r["stage"],
                 format(int(r["chase_now"]), ",")))


def self_test():
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("  FAIL %s: got %r want %r" % (label, got, want))

    body = (
        "invoice,customer,amount,invoice_date,due_date,received,disputed,promised_date\n"
        "INV-1,Alpha,800000,2026-10-01,2026-10-15,0,0,\n"
        "INV-2,Beta,240000,2026-08-20,2026-09-06,0,0,\n"
        "INV-3,Gamma,45000,2026-07-20,2026-08-03,0,0,\n"
        "INV-4,Delta,1200000,2026-10-28,2026-11-03,0,0,\n"
        "INV-5,Epsilon,100000,2026-09-01,2026-09-16,60000,5000,2026-11-10\n"
    )
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, "ledger.csv")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)

    today = datetime.date(2026, 11, 6)
    result = analyse(load(path), today)

    check("total outstanding", result["total"], 2325000.0)
    check("DSO", result["dso"], 28.3)
    check("1-30 bucket count", result["buckets"]["1-30"]["count"], 2)
    check("31-60 amount", result["buckets"]["31-60"]["amount"], 40000.0)
    check("90+ count", result["buckets"]["90+"]["count"], 1)
    check("top invoice is INV-1", result["ranked"][0]["invoice"], "INV-1")
    check("INV-4 is stage 1",
          next(r["stage"] for r in result["ranked"] if r["invoice"] == "INV-4"),
          "stage 1 - oversight")
    check("disputed split on INV-5",
          next(r["chase_now"] for r in result["ranked"] if r["invoice"] == "INV-5"), 35000.0)
    check("promised this week", result["promised_this_week"], 40000.0)
    check("bucket boundaries", (bucket_for(0), bucket_for(1), bucket_for(31), bucket_for(91)),
          ("current", "1-30", "31-60", "90+"))
    check("stage boundaries", (stage_for(0), stage_for(1), stage_for(45)),
          ("none - not due", "stage 1 - oversight", "stage 5 - final"))

    print("ageing_report self-test: %s (11 checks)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return self_test()
    if not argv:
        print(__doc__.strip())
        return 1
    path = argv[0]
    today = datetime.date.today()
    top = 5
    if "--today" in argv:
        today = datetime.date.fromisoformat(argv[argv.index("--today") + 1])
    if "--top" in argv:
        top = int(argv[argv.index("--top") + 1])
    try:
        result = analyse(load(path), today)
    except ValueError as exc:
        print("ERROR: %s" % exc)
        return 1
    except OSError as exc:
        print("ERROR: %s" % exc)
        return 2
    report(result, top)
    return 0


if __name__ == "__main__":
    sys.exit(main())
