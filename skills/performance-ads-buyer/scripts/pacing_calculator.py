#!/usr/bin/env python3
"""Budget pacing for a paid campaign period.

Given the period budget, how far into the period the account is, what has been
spent and what it bought, this prints the projection, the allowable CPA for the
remaining days and a pacing verdict. Arithmetic instead of anxiety.

Usage:
    python3 pacing_calculator.py --budget 200000 --days 30 --elapsed 18 \
        --spent 121000 --conversions 240 --target-cpa 450
    python3 pacing_calculator.py --self-test

Exit 0 on success, 1 when the projection breaks the ceiling CPA (a decision is
needed today).
"""
import argparse
import sys


def project(budget, days, elapsed, spent, conversions, target_cpa, ceiling_cpa=None):
    if days <= 0 or elapsed < 0 or elapsed > days:
        raise ValueError("elapsed must be between 0 and days")
    remaining_days = days - elapsed
    remaining_budget = budget - spent
    spend_rate = spent / elapsed if elapsed else 0.0
    projected_spend = spent + spend_rate * remaining_days
    cpa = spent / conversions if conversions else None
    conv_rate = conversions / spent if spent else 0.0
    projected_conversions = round(projected_spend * conv_rate, 1) if spent else 0.0
    orders_needed = (budget / target_cpa) if target_cpa else None
    allowable_cpa = (remaining_budget / max(orders_needed - conversions, 0.0001)) if orders_needed else None

    if projected_spend > budget * 1.05:
        pacing = "overspending - cap the daily budget"
    elif projected_spend < budget * 0.85:
        pacing = "underspending - delivery or bid is constrained"
    else:
        pacing = "on pace"

    verdict = "ok"
    if cpa is not None and ceiling_cpa and cpa > ceiling_cpa:
        verdict = "above ceiling - a decision is needed today"
    elif cpa is not None and target_cpa and cpa > target_cpa:
        verdict = "above target - fix before scaling"

    return {
        "remaining_days": remaining_days,
        "remaining_budget": remaining_budget,
        "spend_rate": spend_rate,
        "projected_spend": projected_spend,
        "cpa": cpa,
        "projected_conversions": projected_conversions,
        "orders_needed": orders_needed,
        "allowable_cpa": allowable_cpa,
        "pacing": pacing,
        "verdict": verdict,
    }


def render(r, budget, target_cpa):
    lines = [
        "spend to date       %.0f of %.0f budget (%.0f%%)" % (
            budget - r["remaining_budget"], budget,
            100.0 * (budget - r["remaining_budget"]) / budget if budget else 0),
        "days remaining      %d" % r["remaining_days"],
        "daily spend rate    %.0f" % r["spend_rate"],
        "projected spend     %.0f" % r["projected_spend"],
        "current CPA         %s" % ("n/a" if r["cpa"] is None else "%.0f" % r["cpa"]),
        "projected orders    %.1f" % r["projected_conversions"],
        "orders needed       %s" % ("n/a" if r["orders_needed"] is None else "%.1f" % r["orders_needed"]),
        "allowable CPA now   %s" % ("n/a" if r["allowable_cpa"] is None else "%.0f" % r["allowable_cpa"]),
        "pacing              %s" % r["pacing"],
        "verdict             %s" % r["verdict"],
    ]
    if r["allowable_cpa"] is not None and target_cpa and r["allowable_cpa"] < target_cpa * 0.7:
        lines.append("note: the allowable CPA is far below target - the budget or the "
                     "target has to change, not the bid.")
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

    r = project(200000, 30, 18, 121000, 240, 450, 550)
    check("remaining days", r["remaining_days"], 12)
    check("remaining budget", r["remaining_budget"], 79000)
    check("spend rate rounds", round(r["spend_rate"]), 6722)
    check("projected spend", round(r["projected_spend"]), 201667)
    check("current CPA", round(r["cpa"], 2), 504.17)
    check("pacing within the band", r["pacing"], "on pace")
    check("verdict above target", r["verdict"], "above target - fix before scaling")
    check("orders needed at target", round(r["orders_needed"], 2), 444.44)
    check("allowable CPA", round(r["allowable_cpa"], 2), 386.41)

    r = project(100000, 30, 10, 20000, 100, 300, 400)
    check("underspend detected", r["pacing"], "underspending - delivery or bid is constrained")
    check("CPA at target is ok", r["verdict"], "ok")

    r = project(100000, 30, 10, 20000, 40, 300, 400)
    check("above ceiling needs a decision", r["verdict"], "above ceiling - a decision is needed today")

    r = project(50000, 30, 30, 48000, 0, 400, 500)
    check("zero conversions is handled", r["cpa"], None)
    check("zero conversions projects zero orders", r["projected_conversions"], 0.0)

    try:
        project(1000, 10, 11, 100, 1, 100, 200)
    except ValueError:
        check("elapsed beyond period rejected", True, True)
    else:
        check("elapsed beyond period rejected", False, True)

    print("SELF-TEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Paid media budget pacing")
    ap.add_argument("--budget", type=float)
    ap.add_argument("--days", type=int)
    ap.add_argument("--elapsed", type=int)
    ap.add_argument("--spent", type=float)
    ap.add_argument("--conversions", type=float)
    ap.add_argument("--target-cpa", type=float, required=False)
    ap.add_argument("--ceiling-cpa", type=float, default=None)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    missing = [k for k in ("budget", "days", "elapsed", "spent", "conversions", "target_cpa")
               if getattr(args, k) is None]
    if missing:
        ap.error("missing: " + ", ".join("--" + m.replace("_", "-") for m in missing))
    try:
        r = project(args.budget, args.days, args.elapsed, args.spent, args.conversions,
                    args.target_cpa, args.ceiling_cpa)
    except ValueError as exc:
        print("error: %s" % exc)
        return 2
    print(render(r, args.budget, args.target_cpa))
    return 1 if r["verdict"].startswith("above ceiling") else 0


if __name__ == "__main__":
    sys.exit(main())
