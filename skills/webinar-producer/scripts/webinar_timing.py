#!/usr/bin/env python3
"""Deterministic helpers for a webinar: run-of-show timings and the promotion forecast.

Two jobs, no model in the loop:

  schedule  - turn "name:minutes" segments into a clock, and check the shape
  forecast  - work backwards from a target room to invitations needed

Usage:
  python3 webinar_timing.py schedule --segments "opening:2,teach1:15,poll:3,teach2:15,offer:5,qa:9,close:5" --total 60
  python3 webinar_timing.py forecast --target 30 --stay 0.55 --attend 0.35 --register 0.05
  python3 webinar_timing.py --self-test

Exit 0 = plan is internally consistent, 2 = it is not, 1 = bad input.
"""
import argparse
import math
import sys


def parse_segments(spec):
    segments = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            raise ValueError("segment %r is not name:minutes" % part)
        name, minutes = part.rsplit(":", 1)
        name = name.strip()
        if not name:
            raise ValueError("segment %r has no name" % part)
        minutes = int(minutes)
        if minutes <= 0:
            raise ValueError("segment %r has non-positive minutes" % name)
        segments.append((name, minutes))
    if not segments:
        raise ValueError("no segments given")
    return segments


def schedule(segments, total):
    """Return (rows, errors, warnings) for a segment list against a slot length."""
    rows, errors, warnings = [], [], []
    clock = 0
    for name, minutes in segments:
        rows.append((clock, clock + minutes, name, minutes))
        clock += minutes
    if clock > total:
        errors.append("segments total %d min but the slot is %d min - the close gets cut"
                      % (clock, total))
    elif clock < total - 5:
        warnings.append("segments total %d min of a %d min slot - %d min unplanned"
                        % (clock, total, total - clock))
    names = [n.lower() for n, _ in segments]
    if not any("offer" in n for n in names):
        errors.append("no offer segment - a session without an offer is a brand exercise")
    content = sum(m for n, m in segments
                  if "teach" in n.lower() or "demo" in n.lower() or "content" in n.lower())
    if content > 40 and total <= 60:
        warnings.append("content is %d min of a %d min slot - keep it to 35-40 and the offer survives"
                        % (content, total))
    if segments[0][1] > 3:
        warnings.append("opening is %d min - the promise, credibility, agenda and reward fit in 2"
                        % segments[0][1])
    return rows, errors, warnings


def forecast(target, stay, attend, register):
    """Work backwards from attended-and-stayed to registrations and invitations."""
    for label, value in (("stay", stay), ("attend", attend), ("register", register)):
        if not 0 < value <= 1:
            raise ValueError("%s rate must be in (0, 1], got %r" % (label, value))
    if target <= 0:
        raise ValueError("target must be positive")
    registrations = math.ceil(target / (stay * attend))
    invitations = math.ceil(registrations / register)
    return {
        "target": target,
        "registrations": registrations,
        "invitations": invitations,
        "expected_attendees": int(round(registrations * attend)),
        "expected_stayers": int(round(registrations * attend * stay)),
    }


def _print_schedule(rows, errors, warnings, total):
    print("run of show (%d min slot)" % total)
    print("  start  end  min  segment")
    for start, end, name, minutes in rows:
        print("  %5d %4d %4d  %s" % (start, end, minutes, name))
    for e in errors:
        print("  ERROR   " + e)
    for w in warnings:
        print("  warning " + w)
    print("RESULT: %s" % ("PASS" if not errors else "FAIL"))


def self_test():
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("  FAIL %s: got %r want %r" % (label, got, want))

    f = forecast(30, 0.55, 0.35, 0.05)
    check("registrations for 30 stayers", f["registrations"], 156)
    check("invitations at 5%", f["invitations"], 3120)
    check("expected attendees", f["expected_attendees"], 55)

    rows, errors, warnings = schedule(
        parse_segments("opening:2,teach1:15,poll:3,teach2:15,offer:5,qa:9,close:5"), 60)
    check("no errors on a sound plan", errors, [])
    check("clock ends at 54", rows[-1][1], 54)
    check("teach2 starts at 20", rows[3][0], 20)
    check("one warning for unplanned minutes", len(warnings), 1)

    _, errors, _ = schedule(parse_segments("opening:5,teach1:40,qa:20,close:5"), 60)
    check("overrun is an error", any("slot is 60" in e for e in errors), True)
    check("missing offer is an error",
          any("no offer segment" in e for e in errors), True)

    try:
        forecast(30, 1.4, 0.35, 0.05)
        check("bad rate raises", "no error", "ValueError")
    except ValueError:
        pass
    try:
        parse_segments("opening")
        check("bad segment raises", "no error", "ValueError")
    except ValueError:
        pass

    print("webinar_timing self-test: %s (8 checks)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description="Webinar timings and promotion forecast")
    parser.add_argument("--self-test", action="store_true")
    sub = parser.add_subparsers(dest="command")
    s = sub.add_parser("schedule")
    s.add_argument("--segments", required=True)
    s.add_argument("--total", type=int, default=60)
    f = sub.add_parser("forecast")
    f.add_argument("--target", type=int, required=True)
    f.add_argument("--stay", type=float, default=0.55)
    f.add_argument("--attend", type=float, default=0.35)
    f.add_argument("--register", type=float, default=0.05)
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()
    try:
        if args.command == "schedule":
            rows, errors, warnings = schedule(parse_segments(args.segments), args.total)
            _print_schedule(rows, errors, warnings, args.total)
            return 0 if not errors else 2
        if args.command == "forecast":
            r = forecast(args.target, args.stay, args.attend, args.register)
            print("to have %d people at the offer:" % r["target"])
            print("  registrations needed   %d" % r["registrations"])
            print("  invitations needed     %d" % r["invitations"])
            print("  expected in the room   %d" % r["expected_attendees"])
            print("  expected at the offer  %d" % r["expected_stayers"])
            return 0
    except ValueError as exc:
        print("ERROR: %s" % exc)
        return 1
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
