#!/usr/bin/env python3
"""Sample size, payback and CAC ceiling arithmetic for growth tests.

Three calculations a growth decision actually needs, done the same way every time:

  1. sample size per variant for a two-variant test at 95% confidence, 80% power
  2. months to pay back CAC at a given contribution per customer per month
  3. the CAC ceiling that a target payback implies

Usage:
    python3 experiment_power.py sample --baseline 0.05 --mde 0.01
    python3 experiment_power.py payback --cac 1200 --contribution 300
    python3 experiment_power.py ceiling --contribution 300 --target-months 4
    python3 experiment_power.py --self-test

The sample formula is the standard normal approximation
n = 16 * p(1-p) / delta^2, rounded up. It is accurate for the rates and effects a
small business tests; it is not a substitute for a statistician on a large
programme.
"""
import argparse
import math
import sys


def sample_size(baseline, mde):
    """Users per variant. mde is an absolute lift, not a relative one."""
    if not 0 < baseline < 1:
        raise ValueError("baseline must be between 0 and 1")
    if mde <= 0:
        raise ValueError("mde must be positive")
    n = 16.0 * baseline * (1 - baseline) / (mde ** 2)
    return math.ceil(round(n, 6))


def relative_to_absolute(baseline, relative_lift):
    return round(baseline * relative_lift, 10)


def payback_months(cac, monthly_contribution):
    if monthly_contribution <= 0:
        raise ValueError("monthly contribution must be positive")
    return cac / monthly_contribution


def cac_ceiling(monthly_contribution, target_months):
    if monthly_contribution <= 0:
        raise ValueError("monthly contribution must be positive")
    if target_months <= 0:
        raise ValueError("target months must be positive")
    return monthly_contribution * target_months


def verdict(payback, cash_available_months):
    if payback <= cash_available_months:
        return "affordable"
    return "unaffordable - payback exceeds the cash the business can fund"


def self_test():
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("FAIL %s: got %r want %r" % (label, got, want))
        else:
            print("ok   %s" % label)

    check("5% to 6% needs 7600 per variant", sample_size(0.05, 0.01), 7600)
    check("2% to 2.4% needs 19600 per variant", sample_size(0.02, 0.004), 19600)
    check("10% to 12% needs 3600 per variant", sample_size(0.10, 0.02), 3600)
    check("relative lift converts to absolute", relative_to_absolute(0.05, 0.2), 0.01)
    check("payback 1200/300 is 4 months", payback_months(1200, 300), 4.0)
    check("ceiling for 4 months at 300 is 1200", cac_ceiling(300, 4), 1200)
    check("affordable verdict", verdict(4.0, 6), "affordable")
    check("unaffordable verdict", verdict(9.0, 6).startswith("unaffordable"), True)
    try:
        sample_size(0, 0.01)
    except ValueError:
        check("zero baseline rejected", True, True)
    else:
        check("zero baseline rejected", False, True)
    print("SELF-TEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Growth test arithmetic")
    sub = ap.add_subparsers(dest="cmd")

    s = sub.add_parser("sample", help="users per variant")
    s.add_argument("--baseline", type=float, required=True, help="current rate, e.g. 0.05")
    s.add_argument("--mde", type=float, required=True, help="absolute lift, e.g. 0.01")
    s.add_argument("--daily", type=int, default=None, help="daily users per variant")

    p = sub.add_parser("payback", help="months to pay back CAC")
    p.add_argument("--cac", type=float, required=True)
    p.add_argument("--contribution", type=float, required=True, help="contribution per customer per month")
    p.add_argument("--cash-months", type=float, default=6.0, help="months of payback the business can fund")

    c = sub.add_parser("ceiling", help="CAC the target payback implies")
    c.add_argument("--contribution", type=float, required=True)
    c.add_argument("--target-months", type=float, required=True)

    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if args.cmd == "sample":
        n = sample_size(args.baseline, args.mde)
        print("baseline %.4f | absolute lift %.4f | per variant: %d users" % (args.baseline, args.mde, n))
        print("both variants: %d users" % (2 * n))
        if args.daily:
            print("at %d users per variant per day: %d days" % (args.daily, math.ceil(n / args.daily)))
        if args.mde / args.baseline < 0.15:
            print("note: that is a lift under 15% relative - most small accounts cannot "
                  "detect it. Test a bigger change instead.")
        return 0
    if args.cmd == "payback":
        months = payback_months(args.cac, args.contribution)
        print("CAC %.0f | contribution %.0f/month | payback %.1f months | %s"
              % (args.cac, args.contribution, months, verdict(months, args.cash_months)))
        return 0
    if args.cmd == "ceiling":
        print("contribution %.0f/month | target %s months | CAC ceiling %.0f"
              % (args.contribution, args.target_months, cac_ceiling(args.contribution, args.target_months)))
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
