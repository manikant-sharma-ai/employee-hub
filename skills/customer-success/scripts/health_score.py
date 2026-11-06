#!/usr/bin/env python3
"""Deterministic account health score.

Six signals, fixed weights, one band, one obligation. No model in the loop, so two
people scoring the same account on the same data get the same number.

Signals are scored 0-4 (see references/health-scoring.md). Only the signals you
actually have are used; the weights are re-normalised over what is present, and
the missing ones are reported rather than scored as zero.

Usage:
  python3 health_score.py --signals core=4,seats=2,support=1,payment=3,champion=2,outcome=1 \
      --value 1800000 --renewal 2026-12-31 [--today 2026-11-06]
  python3 health_score.py --self-test

Exit 0 = scored, 1 = bad input.
"""
import argparse
import datetime
import sys

WEIGHTS = {
    "core": 0.30,      # core-action trend
    "seats": 0.20,     # seat utilisation
    "support": 0.15,   # ticket load and repeats
    "payment": 0.15,   # days late on the last two invoices
    "champion": 0.10,  # champion present and engaged
    "outcome": 0.10,   # progress on the outcome they bought
}

BANDS = [
    (75, "green", "expansion conversation at the next QBR", "next QBR"),
    (50, "amber", "value check-in with the champion, agenda in writing", "14 days"),
    (25, "red", "save play chosen by cause, founder informed", "5 working days"),
    (0, "critical", "exit-safe conversation; retain only if the cause is fixable", "48 hours"),
]


def parse_signals(spec):
    signals = {}
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError("signal %r is not name=score" % part)
        name, raw = part.split("=", 1)
        name = name.strip()
        if name not in WEIGHTS:
            raise ValueError("unknown signal %r (known: %s)" % (name, ", ".join(WEIGHTS)))
        try:
            score = int(raw)
        except ValueError:
            raise ValueError("signal %r has a non-integer score" % name)
        if not 0 <= score <= 4:
            raise ValueError("signal %r is %d, must be 0-4" % (name, score))
        signals[name] = score
    if not signals:
        raise ValueError("no signals given")
    return signals


def score(signals):
    present = [k for k in WEIGHTS if k in signals]
    total_weight = sum(WEIGHTS[k] for k in present)
    weighted = sum(signals[k] * WEIGHTS[k] for k in present)
    value = round(weighted / total_weight * 25, 1)
    band, action, deadline = "critical", "", ""
    for floor, name, act, due in BANDS:
        if value >= floor:
            band, action, deadline = name, act, due
            break
    return {
        "score": value,
        "band": band,
        "action": action,
        "deadline": deadline,
        "missing": [k for k in WEIGHTS if k not in signals],
        "coverage": round(total_weight, 2),
    }


def days_to(date_str, today):
    target = datetime.date.fromisoformat(date_str)
    return (target - today).days


def main(argv=None):
    parser = argparse.ArgumentParser(description="Account health score")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--signals", help="core=4,seats=2,support=1,payment=3,champion=2,outcome=1")
    parser.add_argument("--value", type=float, default=0.0, help="annual contract value in rupees")
    parser.add_argument("--renewal", help="renewal date, YYYY-MM-DD")
    parser.add_argument("--today", help="override today, YYYY-MM-DD")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.signals:
        parser.print_help()
        return 1
    try:
        result = score(parse_signals(args.signals))
        today = (datetime.date.fromisoformat(args.today) if args.today
                 else datetime.date.today())
        print("health score  %s / 100  (%s band)" % (result["score"], result["band"]))
        print("  signals used   %d of 6 (weight coverage %.2f)" % (6 - len(result["missing"]), result["coverage"]))
        if result["missing"]:
            print("  NOT SCORED     %s - re-weight and say so, never score them as zero"
                  % ", ".join(result["missing"]))
        print("  obligation     %s, within %s" % (result["action"], result["deadline"]))
        if args.value:
            at_risk = round(args.value * (1 - result["score"] / 100))
            print("  revenue at risk Rs %s of Rs %s" % (format(at_risk, ","), format(int(args.value), ",")))
        if args.renewal:
            left = days_to(args.renewal, today)
            flag = " - renewal inside 90 days outranks a lower-risk account" if left <= 90 else ""
            print("  renewal in     %d days%s" % (left, flag))
        return 0
    except ValueError as exc:
        print("ERROR: %s" % exc)
        return 1


def self_test():
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("  FAIL %s: got %r want %r" % (label, got, want))

    all_four = score({k: 4 for k in WEIGHTS})
    check("all fours is 100", all_four["score"], 100.0)
    check("all fours is green", all_four["band"], "green")

    all_zero = score({k: 0 for k in WEIGHTS})
    check("all zeros is 0", all_zero["score"], 0.0)
    check("all zeros is critical", all_zero["band"], "critical")

    core_only = score({"core": 4})
    check("core only re-normalises", core_only["score"], 100.0)
    check("five signals reported missing", len(core_only["missing"]), 5)

    mixed = score({"core": 4, "seats": 2, "support": 1, "payment": 3, "champion": 2, "outcome": 1})
    # (1.2 + 0.4 + 0.15 + 0.45 + 0.2 + 0.1) = 2.5 / 1.0 * 25 = 62.5
    check("mixed score", mixed["score"], 62.5)
    check("mixed band", mixed["band"], "amber")

    check("90 days counted", days_to("2026-12-31", datetime.date(2026, 11, 6)), 55)

    for bad in ("core=5", "core", "nonsense=3", ""):
        try:
            parse_signals(bad)
            check("bad input %r raises" % bad, "no error", "ValueError")
        except ValueError:
            pass

    print("health_score self-test: %s (11 checks)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
