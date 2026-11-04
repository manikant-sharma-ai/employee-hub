#!/usr/bin/env python3
"""Commitment register sweep.

Reads an actions register and reports what is overdue, what is due, what has no
owner and who is carrying too much. Deterministic on purpose: the sweep is the
part of follow-up that should never depend on how the week felt.

Input CSV columns (header row required):
    action,owner,due,status,source
    status is one of open, done, dropped, superseded (blank counts as open)
    due is YYYY-MM-DD; a blank due date is reported as undated, never guessed

Usage:
    python3 commitment_tracker.py register.csv
    python3 commitment_tracker.py register.csv --as-of 2026-11-04 --cap 5
    python3 commitment_tracker.py --self-test

Exit 0 on success, 1 when the sweep finds something that needs a decision today
(overdue by more than --alert-after days, or an action with no owner).
"""
import argparse
import csv
import sys
from collections import Counter
from datetime import date

OPEN = {"open", "in progress", "in-progress", ""}
CLOSED = {"done", "dropped", "superseded"}


def escalate(days_late):
    if days_late <= 0:
        return "due"
    if days_late < 2:
        return "nudge"
    if days_late < 7:
        return "name in review"
    if days_late < 14:
        return "re-date once or drop"
    return "decision: reassign, reduce or cancel"


def classify(rec, as_of):
    action = (rec.get("action") or "").strip()
    owner = (rec.get("owner") or "").strip()
    raw_due = (rec.get("due") or "").strip()
    status = (rec.get("status") or "").strip().lower()
    if status in CLOSED:
        return None
    due = None
    if raw_due:
        try:
            due = date.fromisoformat(raw_due)
        except ValueError:
            raise SystemExit("bad due date %r on action %r" % (raw_due, action))
    days_late = (as_of - due).days if due else None
    return {
        "action": action,
        "owner": owner,
        "due": raw_due or None,
        "days_late": days_late,
        "undated": due is None,
        "unowned": not owner,
        "escalation": escalate(days_late) if days_late is not None else "undated",
    }


def sweep(records, as_of):
    items = [i for i in (classify(r, as_of) for r in records) if i]
    items.sort(key=lambda i: (i["days_late"] is None, -(i["days_late"] or 0)))
    return items


def summarise(items, cap):
    load = Counter(i["owner"] for i in items if not i["unowned"])
    return {
        "open": len(items),
        "overdue": len([i for i in items if i["days_late"] is not None and i["days_late"] > 0]),
        "due_today_or_later": len([i for i in items if i["days_late"] is not None and i["days_late"] <= 0]),
        "undated": len([i for i in items if i["undated"]]),
        "unowned": len([i for i in items if i["unowned"]]),
        "over_cap": {o: n for o, n in load.items() if n > cap},
    }


def render(items, stats, as_of, cap):
    lines = ["commitment sweep | as of %s | open %d | overdue %d | undated %d | unowned %d"
             % (as_of.isoformat(), stats["open"], stats["overdue"], stats["undated"], stats["unowned"]), ""]
    if not items:
        lines.append("nothing open - the register is clean")
        return "\n".join(lines)
    header = "%-52s %-14s %-12s %-6s %s" % ("action", "owner", "due", "late", "escalation")
    lines.append(header)
    lines.append("-" * len(header))
    for i in items:
        lines.append("%-52s %-14s %-12s %-6s %s" % (
            i["action"][:52], (i["owner"] or "-")[:14], i["due"] or "-",
            "-" if i["days_late"] is None else i["days_late"], i["escalation"]))
    if stats["over_cap"]:
        lines.append("")
        lines.append("over the cap of %d open items: %s" % (
            cap, ", ".join("%s (%d)" % (o, n) for o, n in sorted(stats["over_cap"].items()))))
    return "\n".join(lines)


def load(path):
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames or "action" not in reader.fieldnames:
            raise SystemExit("register needs at least an 'action' column, got %r" % (reader.fieldnames,))
        return list(reader)


def self_test():
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("FAIL %s: got %r want %r" % (label, got, want))
        else:
            print("ok   %s" % label)

    as_of = date(2026, 11, 4)
    recs = [
        {"action": "send quote", "owner": "Asha", "due": "2026-11-01", "status": "open"},
        {"action": "close books", "owner": "Ravi", "due": "2026-11-04", "status": "open"},
        {"action": "hire analyst", "owner": "", "due": "2026-11-10", "status": "open"},
        {"action": "revise deck", "owner": "Asha", "due": "", "status": "open"},
        {"action": "pay vendor", "owner": "Ravi", "due": "2026-10-20", "status": "done"},
        {"action": "old idea", "owner": "Asha", "due": "2026-10-01", "status": "dropped"},
    ]
    items = sweep(recs, as_of)
    stats = summarise(items, cap=5)
    check("closed actions are excluded", stats["open"], 4)
    check("one overdue", stats["overdue"], 1)
    check("one unowned", stats["unowned"], 1)
    check("one undated", stats["undated"], 1)
    check("most overdue sorts first", items[0]["days_late"], 3)
    check("undated sorts last", items[-1]["undated"], True)
    check("3 days late names it in review", escalate(3), "name in review")
    check("1 day late is a nudge", escalate(1), "nudge")
    check("15 days late is a decision", escalate(15), "decision: reassign, reduce or cancel")
    check("cap breach detected", summarise(items, cap=1)["over_cap"], {"Asha": 2})
    check("undated escalation label", [i["escalation"] for i in items if i["undated"]], ["undated"])
    print("SELF-TEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Commitment register sweep")
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--as-of", default=None, help="YYYY-MM-DD, defaults to today")
    ap.add_argument("--cap", type=int, default=5, help="open items per person before it is flagged")
    ap.add_argument("--alert-after", type=int, default=7, help="days late that force a decision")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.csv:
        ap.print_help()
        return 2
    as_of = date.fromisoformat(args.as_of) if args.as_of else date.today()
    items = sweep(load(args.csv), as_of)
    stats = summarise(items, args.cap)
    print(render(items, stats, as_of, args.cap))
    needs_decision = stats["unowned"] > 0 or any(
        i["days_late"] is not None and i["days_late"] > args.alert_after for i in items)
    return 1 if needs_decision else 0


if __name__ == "__main__":
    sys.exit(main())
