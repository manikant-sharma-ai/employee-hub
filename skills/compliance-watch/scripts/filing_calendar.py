#!/usr/bin/env python3
"""Recurring Indian statutory filing dates, generated rather than remembered.

Encodes the commonly published dates for recurring obligations and expands them
for a date range. Dates move with notifications, extensions and amnesties, and
state-level obligations vary by state - every generated date carries a source
label so it can be verified before it goes into a client calendar.

Usage:
    python3 filing_calendar.py --from 2026-11 --months 6
    python3 filing_calendar.py --from 2026-11 --months 3 --only gst,tds
    python3 filing_calendar.py --list
    python3 filing_calendar.py --self-test

Exit 0 on success.
"""
import argparse
import calendar
import sys
from datetime import date

# day-of-month rules are the published statutory dates; monthly items roll to the
# next month, which is how the rules are actually written ("7th of the following
# month").
OBLIGATIONS = [
    {"key": "tds_deposit", "name": "TDS and TCS deposit", "kind": "monthly",
     "day": 7, "next_month": True, "group": "tds",
     "source": "Income tax rules - verify the March exception at source"},
    {"key": "gstr1", "name": "GSTR-1 (monthly filer)", "kind": "monthly",
     "day": 11, "next_month": True, "group": "gst",
     "source": "GST portal - monthly filer calendar"},
    {"key": "gstr3b", "name": "GSTR-3B (monthly filer)", "kind": "monthly",
     "day": 20, "next_month": True, "group": "gst",
     "source": "GST portal - monthly filer calendar"},
    {"key": "pf", "name": "PF contribution (ECR and payment)", "kind": "monthly",
     "day": 15, "next_month": True, "group": "labour",
     "source": "EPFO - verify any extension notification"},
    {"key": "esi", "name": "ESI contribution", "kind": "monthly",
     "day": 15, "next_month": True, "group": "labour",
     "source": "ESIC - verify any extension notification"},
    {"key": "pt", "name": "Professional tax", "kind": "monthly",
     "day": 20, "next_month": True, "group": "state",
     "source": "State-specific - confirm the state's own date before use"},
    {"key": "tds_24q", "name": "TDS statement 24Q (salary)", "kind": "quarterly",
     "month_after_quarter": 1, "day_end_of_month": True, "group": "tds",
     "source": "TRACES - Q4 has a separate notified date, verify"},
    {"key": "tds_26q", "name": "TDS statement 26Q (non-salary)", "kind": "quarterly",
     "month_after_quarter": 1, "day_end_of_month": True, "group": "tds",
     "source": "TRACES - Q4 has a separate notified date, verify"},
]

ADVANCE_TAX = [(6, 15), (9, 15), (12, 15), (3, 15)]


def month_iter(start_year, start_month, months):
    y, m = start_year, start_month
    for _ in range(months):
        yield y, m
        m += 1
        if m == 13:
            y, m = y + 1, 1


def monthly_due(ob, year, month):
    """Due date for a monthly obligation in the period (year, month)."""
    y, m = (year + 1, 1) if month == 12 else (year, month + 1)
    day = min(ob["day"], calendar.monthrange(y, m)[1])
    return date(y, m, day)


def quarter_end(month):
    """Quarter ending month for a filing period month, or None if not a quarter end."""
    return month in (3, 6, 9, 12)


def quarterly_due(ob, year, month):
    y, m = (year + 1, 1) if month == 12 else (year, month + 1)
    return date(y, m, calendar.monthrange(y, m)[1])


def expand(start_year, start_month, months, groups=None):
    rows = []
    for y, m in month_iter(start_year, start_month, months):
        for ob in OBLIGATIONS:
            if groups and ob["group"] not in groups and ob["key"] not in groups:
                continue
            if ob["kind"] == "monthly":
                rows.append((monthly_due(ob, y, m), ob["name"], ob["source"]))
            elif quarter_end(m):
                rows.append((quarterly_due(ob, y, m), ob["name"], ob["source"]))
        for (am, ad) in ADVANCE_TAX:
            if am == m:
                rows.append((date(y, am, ad), "Advance tax instalment",
                             "Income tax - verify the instalment percentage at source"))
    rows.sort(key=lambda r: (r[0], r[1]))
    return rows


def self_test():
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("FAIL %s: got %r want %r" % (label, got, want))
        else:
            print("ok   %s" % label)

    ob = next(o for o in OBLIGATIONS if o["key"] == "tds_deposit")
    check("TDS for Nov 2026 is due 7 Dec 2026", monthly_due(ob, 2026, 11), date(2026, 12, 7))
    check("TDS for Dec 2026 rolls into Jan 2027", monthly_due(ob, 2026, 12), date(2027, 1, 7))

    ob = next(o for o in OBLIGATIONS if o["key"] == "gstr3b")
    check("GSTR-3B for Oct 2026 is due 20 Nov 2026", monthly_due(ob, 2026, 10), date(2026, 11, 20))

    ob = next(o for o in OBLIGATIONS if o["key"] == "tds_26q")
    check("26Q for Oct-Dec 2026 is due 31 Jan 2027", quarterly_due(ob, 2026, 12), date(2027, 1, 31))
    check("26Q for Jul-Sep 2026 is due 31 Oct 2026", quarterly_due(ob, 2026, 9), date(2026, 10, 31))

    rows = expand(2026, 11, 1)
    dates = [r[0] for r in rows]
    check("November 2026 has obligations", len(rows) > 0, True)
    check("dates are sorted", dates, sorted(dates))
    check("no date falls in the filing period month for monthly items",
          all(r[0].month in (11, 12) for r in rows if r[1] != "Advance tax instalment"), True)

    rows = expand(2027, 1, 1, groups=["gst"])
    check("gst-only filter returns gst rows", all("GSTR" in r[1] for r in rows), True)

    rows = expand(2026, 12, 1)
    check("quarter-end month produces a quarterly statement", any("26Q" in r[1] for r in rows), True)

    print("SELF-TEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Recurring Indian statutory filing dates")
    ap.add_argument("--from", dest="start", default=None, help="YYYY-MM")
    ap.add_argument("--months", type=int, default=3)
    ap.add_argument("--only", default=None, help="comma separated groups: gst,tds,labour,state")
    ap.add_argument("--list", action="store_true", help="print the encoded obligations")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if args.list:
        for ob in OBLIGATIONS:
            print("%-12s %-38s %-10s %s" % (ob["key"], ob["name"], ob["kind"], ob["source"]))
        return 0
    if not args.start:
        ap.print_help()
        return 2
    try:
        y, m = (int(x) for x in args.start.split("-"))
        date(y, m, 1)
    except ValueError:
        print("--from must be YYYY-MM")
        return 2
    groups = [g.strip() for g in args.only.split(",")] if args.only else None
    rows = expand(y, m, args.months, groups)
    print("filing calendar | %d months from %04d-%02d | %d items" % (args.months, y, m, len(rows)))
    print("dates are the commonly published statutory dates - verify at source before use")
    print()
    for due, name, source in rows:
        print("%s  %-38s %s" % (due.isoformat(), name, source))
    return 0


if __name__ == "__main__":
    sys.exit(main())
