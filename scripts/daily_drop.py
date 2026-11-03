#!/usr/bin/env python3
"""Build the brief for today's 06:00 IST drop.

Reads BACKLOG.md, takes the five roles that are due - rows marked `next` first,
then the first `queued` rows - and prints a markdown issue body with the
procedure, the mix rule and the validation command.

This script does not write skills. It opens the job; a human or an agent does
the work. Nothing here claims an employee shipped.

Usage: python3 scripts/daily_drop.py [--count 5]
"""
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*`([a-z0-9-]+)`\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")

count = 5
if "--count" in sys.argv:
    count = int(sys.argv[sys.argv.index("--count") + 1])

rows = []
with open(os.path.join(ROOT, "BACKLOG.md"), encoding="utf-8") as f:
    for line in f:
        m = ROW.match(line.strip())
        if m:
            rows.append({"n": int(m.group(1)), "name": m.group(2),
                         "accountable": m.group(3), "status": m.group(4).strip()})

nexts = [r for r in rows if r["status"].lower().startswith("next")]
queued = [r for r in rows if r["status"].lower().startswith("queued")]
picked = (nexts + queued)[:count]

shipped = [r for r in rows if r["status"].lower().startswith("shipped")]
ist = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
today = datetime.datetime.now(ist).strftime("%Y-%m-%d")

print("## Daily drop - %s (06:00 IST)" % today)
print()
print("Five roles are due. The mix is two revenue-facing, two operations, one founder-leverage.")
print("Queued: %d | shipped: %d | next up: %d" % (len(queued), len(shipped), len(nexts)))
print()
print("| # | Employee | Accountable for |")
print("|---|---|---|")
for r in picked:
    print("| %d | `%s` | %s |" % (r["n"], r["name"], r["accountable"]))
print()
print("### Procedure (docs/daily-drop.md)")
print()
for step in [
    "Write `skills/<role>/SKILL.md` - routing, workflow, standards, output contract, guardrails, trigger test.",
    "Wire the Employee Standard: `core/connector-preflight.md` before the first substantive step, `core/memory-and-notes.md` and `core/performance-tracking.md` before the output contract.",
    "Three to six `references/` files, one per discipline, 60-120 lines each.",
    "Seed `notes/learnings.md`, `notes/contacts.md`, `notes/decisions.md`, `notes/journal/YYYY-MM.md`.",
    "One `assets/` template of the role's own good output.",
    "`python3 scripts/validate_repo.py` must pass with zero errors.",
    "Register in `registry.json`, add a CHANGELOG block with the reasoning, mark the backlog rows `shipped %s`." % today,
]:
    print("- [ ] " + step)
print()
print("Close this issue with a one-paragraph report: what shipped, what it can do that yesterday's could not, which one to use first, what is next.")
