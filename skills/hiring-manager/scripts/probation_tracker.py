#!/usr/bin/env python3
"""Probation and review tracker.

Turns a joiner sheet into dates: the three check-ins, the probation expiry, the
confirmation due date and what is due in the next N days. Dates are arithmetic,
not memory - which is the whole point, because a lapsed probation is both a legal
problem and a management one.

Input CSV columns (header row required):
    name,start_date,probation_months,manager

Usage:
    python3 probation_tracker.py joiners.csv
    python3 probation_tracker.py joiners.csv --as-of 2026-11-04 --window 30
    python3 probation_tracker.py --self-test

Exit 0 on success. Dates follow the appointment letter, not this script: it
computes from the probation length you give it and never assumes one.
"""
import argparse
import calendar
import csv
import sys
from datetime import date, timedelta

DEFAULT_WINDOW = 30


def add_months(d, months):
    """Add whole months, clamping to the last day of the target month."""
    total = d.month - 1 + months
    year = d.year + total // 12
    month = total % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def schedule(start, probation_months):
    expiry = add_months(start, probation_months)
    return {
        "start": start,
        "day7": start + timedelta(days=7),
        "day30": start + timedelta(days=30),
        "day60": start + timedelta(days=60),
        "day85": start + timedelta(days=85),
        "expiry": expiry,
        # the letter should issue on or before expiry; 5 working days of margin
        "confirmation_due": expiry - timedelta(days=5),
    }


def status(rows, as_of):
    out = []
    for name, manager, sched in rows:
        days = (sched["expiry"] - as_of).days
        if days < 0:
            state = "OVERDUE - probation lapsed %d days ago, decide now" % (-days)
        elif days <= 14:
            state = "DECIDE - expires in %d days" % days
        else:
            state = "on track"
        out.append({
            "name": name,
            "manager": manager,
            "start": sched["start"].isoformat(),
            "day30": sched["day30"].isoformat(),
            "day60": sched["day60"].isoformat(),
            "day85": sched["day85"].isoformat(),
            "expiry": sched["expiry"].isoformat(),
            "confirmation_due": sched["confirmation_due"].isoformat(),
            "days_left": days,
            "status": state,
        })
    return out


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for i, rec in enumerate(csv.DictReader(fh), start=2):
            name = (rec.get("name") or "").strip()
            raw = (rec.get("start_date") or "").strip()
            months = (rec.get("probation_months") or "").strip()
            if not name or not raw:
                raise SystemExit("row %d: name and start_date are required" % i)
            try:
                start = date.fromisoformat(raw)
            except ValueError:
                raise SystemExit("row %d: start_date %r is not YYYY-MM-DD" % (i, raw))
            try:
                n = int(months)
            except ValueError:
                raise SystemExit("row %d: probation_months %r is not a whole number" % (i, months))
            if not 0 < n <= 24:
                raise SystemExit("row %d: probation_months %d is out of range" % (i, n))
            rows.append((name, (rec.get("manager") or "").strip() or "-", schedule(start, n)))
    return rows


def render(items, as_of, window):
    due = [r for r in items if -10**6 < r["days_left"] <= window]
    lines = ["probation tracker | as of %s | %d joiners | %d due within %d days"
             % (as_of.isoformat(), len(items), len(due), window), ""]
    header = "%-22s %-12s %-12s %-12s %-12s %-8s %s" % (
        "name", "start", "day85", "expiry", "confirm_by", "days", "status")
    lines.append(header)
    lines.append("-" * len(header))
    for r in sorted(items, key=lambda x: x["days_left"]):
        lines.append("%-22s %-12s %-12s %-12s %-12s %-8d %s" % (
            r["name"][:22], r["start"], r["day85"], r["expiry"],
            r["confirmation_due"], r["days_left"], r["status"]))
    return "\n".join(lines)


def self_test():
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("FAIL %s: got %r want %r" % (label, got, want))
        else:
            print("ok   %s" % label)

    s = schedule(date(2026, 1, 15), 3)
    check("3-month expiry from 15 Jan", s["expiry"], date(2026, 4, 15))
    check("day30 from 15 Jan", s["day30"], date(2026, 2, 14))
    check("day85 from 15 Jan", s["day85"], date(2026, 4, 10))
    check("confirmation due 5 days early", s["confirmation_due"], date(2026, 4, 10))

    s = schedule(date(2026, 11, 30), 3)
    check("month-end clamps to 28 Feb", s["expiry"], date(2027, 2, 28))

    s = schedule(date(2026, 8, 31), 6)
    check("31 Aug + 6 months clamps to Feb", s["expiry"], date(2027, 2, 28))

    s = schedule(date(2026, 12, 31), 1)
    check("31 Dec + 1 month clamps to 31 Jan", s["expiry"], date(2027, 1, 31))

    rows = [("Test Person", "Manager", schedule(date(2026, 9, 1), 3))]
    item = status(rows, date(2026, 11, 20))[0]
    check("11 days left is a DECIDE", item["status"].split(" -")[0], "DECIDE")
    item = status(rows, date(2026, 12, 5))[0]
    check("lapsed probation is OVERDUE", item["status"].split(" -")[0], "OVERDUE")
    check("days left negative after expiry", item["days_left"] < 0, True)

    print("SELF-TEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Probation and review tracker")
    ap.add_argument("csv", nargs="?", help="joiner sheet")
    ap.add_argument("--as-of", default=None, help="YYYY-MM-DD, defaults to today")
    ap.add_argument("--window", type=int, default=DEFAULT_WINDOW, help="days ahead to flag")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.csv:
        ap.print_help()
        return 2
    as_of = date.fromisoformat(args.as_of) if args.as_of else date.today()
    items = status(load(args.csv), as_of)
    print(render(items, as_of, args.window))
    return 0


if __name__ == "__main__":
    sys.exit(main())
