#!/usr/bin/env python3
"""Deterministic investor metrics pack and update check.

Two jobs, no model in the loop:

  metrics  - month-on-month growth, churn, plan variance and runway from one CSV,
             so the same figures appear in every update and every answer
  check    - verify an update draft carries the five sections, in order

CSV columns (header required):
  month,revenue,cash,burn,customers,new_customers,churned_customers,gross_margin_pct,plan_revenue
`month` is YYYY-MM. Rows are sorted oldest first.

Usage:
  python3 update_pack.py metrics.csv
  python3 update_pack.py --check update.md
  python3 update_pack.py --self-test

Exit 0 = ok, 1 = bad input or a failing draft, 2 = file not readable.
"""
import csv
import sys

REQUIRED = ["month", "revenue", "cash", "burn", "customers",
            "new_customers", "churned_customers", "gross_margin_pct", "plan_revenue"]
SECTIONS = ["what changed", "the numbers", "where we are short",
            "what we are doing", "the ask"]


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("CSV missing column(s): %s" % ", ".join(missing))
        for raw in reader:
            try:
                rows.append({
                    "month": raw["month"].strip(),
                    "revenue": float(raw["revenue"]),
                    "cash": float(raw["cash"]),
                    "burn": float(raw["burn"]),
                    "customers": int(float(raw["customers"])),
                    "new": int(float(raw["new_customers"])),
                    "churned": int(float(raw["churned_customers"])),
                    "gm": float(raw["gross_margin_pct"]),
                    "plan": float(raw["plan_revenue"]),
                })
            except ValueError as exc:
                raise ValueError("bad row for month %r: %s" % (raw.get("month"), exc))
    if not rows:
        raise ValueError("no rows")
    return sorted(rows, key=lambda r: r["month"])


def analyse(rows):
    out = []
    for i, r in enumerate(rows):
        prev = rows[i - 1] if i else None
        mom = round((r["revenue"] - prev["revenue"]) / prev["revenue"] * 100, 1) if prev else None
        churn = round(r["churned"] / prev["customers"] * 100, 1) if prev else None
        variance = round((r["revenue"] - r["plan"]) / r["plan"] * 100, 1) if r["plan"] else None
        window = rows[max(0, i - 2):i + 1]
        avg_burn = sum(x["burn"] for x in window) / len(window)
        runway = round(r["cash"] / avg_burn, 1) if avg_burn > 0 else None
        flags = []
        if runway is not None and runway < 9:
            flags.append("runway under 9 months - tell the lead before the update")
        if variance is not None and variance < -10:
            flags.append("revenue %.1f%% under plan - state it in the first paragraph" % variance)
        if churn is not None and churn > 5:
            flags.append("logo churn %.1f%% - name the accounts and the save play" % churn)
        if r["new"] - r["churned"] != r["customers"] - (prev["customers"] if prev else r["customers"]):
            flags.append("customer count does not reconcile: new %d - churned %d vs net %d"
                         % (r["new"], r["churned"],
                            r["customers"] - (prev["customers"] if prev else r["customers"])))
        out.append(dict(r, mom=mom, churn=churn, variance=variance,
                        runway=runway, avg_burn=round(avg_burn), flags=flags))
    return out


def print_metrics(analysis):
    print("month     revenue      MoM     plan var   gm%%   cust  churn%%  runway  cash")
    for r in analysis:
        print("%-9s %10s %7s %10s %5.1f %6d %7s %7s %11s" % (
            r["month"], format(int(r["revenue"]), ","),
            "-" if r["mom"] is None else "%+.1f%%" % r["mom"],
            "-" if r["variance"] is None else "%+.1f%%" % r["variance"],
            r["gm"], r["customers"],
            "-" if r["churn"] is None else "%.1f" % r["churn"],
            "-" if r["runway"] is None else "%.1f" % r["runway"],
            format(int(r["cash"]), ",")))
    latest = analysis[-1]
    print("\nlatest: %s | runway %.1f months at avg burn %s | customers %d"
          % (latest["month"], latest["runway"] or 0,
             format(latest["avg_burn"], ","), latest["customers"]))
    for r in analysis:
        for f in r["flags"]:
            print("  flag %s: %s" % (r["month"], f))


def check(path):
    text = open(path, encoding="utf-8").read().lower()
    missing = [s for s in SECTIONS if s not in text]
    order = [text.find(s) for s in SECTIONS if s in text]
    out_of_order = order != sorted(order)
    words = len(text.split())
    print("update check: %s" % path)
    print("  sections present %d of %d" % (len(SECTIONS) - len(missing), len(SECTIONS)))
    if missing:
        print("  ERROR   missing section(s): %s" % ", ".join(missing))
    if out_of_order:
        print("  ERROR   sections are out of order - the reader cannot find the miss")
    if words > 800:
        print("  warning draft is %d words - one page is under 500 plus the table" % words)
    ok = not missing and not out_of_order
    print("RESULT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def self_test():
    ok = True

    def check_eq(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("  FAIL %s: got %r want %r" % (label, got, want))

    rows = [
        {"month": "2026-09", "revenue": 4000000, "cash": 25000000, "burn": 1000000,
         "customers": 100, "new": 8, "churned": 3, "gm": 55.0, "plan": 4200000},
        {"month": "2026-10", "revenue": 4240000, "cash": 24000000, "burn": 1200000,
         "customers": 105, "new": 9, "churned": 4, "gm": 54.0, "plan": 4600000},
        {"month": "2026-11", "revenue": 4260000, "cash": 22800000, "burn": 1250000,
         "customers": 107, "new": 6, "churned": 4, "gm": 53.0, "plan": 5000000},
    ]
    a = analyse(rows)
    check_eq("october MoM", a[1]["mom"], 6.0)
    check_eq("november MoM", a[2]["mom"], 0.5)
    check_eq("october churn", a[1]["churn"], 4.0)
    check_eq("november plan variance", a[2]["variance"], -14.8)
    check_eq("november runway", a[2]["runway"], 19.8)
    check_eq("november avg burn", a[2]["avg_burn"], 1150000)
    check_eq("revenue miss flagged", any("under plan" in f for f in a[2]["flags"]), True)
    check_eq("first row has no MoM", a[0]["mom"], None)

    bad = [dict(rows[0], customers=99)]
    check_eq("reconciliation flag fires",
             any("does not reconcile" in f for f in analyse(bad)[0]["flags"]), True)

    import os
    import tempfile
    tmp = tempfile.mkdtemp()
    good = os.path.join(tmp, "good.md")
    with open(good, "w", encoding="utf-8") as fh:
        fh.write("# Update 14\n\n## What changed\nWe missed.\n\n## The numbers\n\n"
                 "## Where we are short\n\n## What we are doing\n\n## The ask\n")
    check_eq("complete draft passes", check(good), 0)

    short = os.path.join(tmp, "short.md")
    with open(short, "w", encoding="utf-8") as fh:
        fh.write("# Update 14\n\n## What changed\nAll good.\n\n## The ask\n")
    check_eq("incomplete draft fails", check(short), 1)

    print("update_pack self-test: %s (10 checks)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return self_test()
    if not argv:
        print(__doc__.strip())
        return 1
    try:
        if "--check" in argv:
            return check(argv[argv.index("--check") + 1])
        rows = load(argv[0])
    except ValueError as exc:
        print("ERROR: %s" % exc)
        return 1
    except OSError as exc:
        print("ERROR: %s" % exc)
        return 2
    print_metrics(analyse(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
