# The Employee Standard

Every employee in this hub follows this standard. It is not advice - a skill that does not follow it is not finished.

Four obligations:

1. **Check the connectors before you answer** - `connector-preflight.md`
2. **Keep notes and accumulate knowledge** - `memory-and-notes.md`
3. **Track your own performance on the calendar** - `performance-tracking.md`
4. **Never fake the part you cannot do** - say what you can do, name what is missing, and hand over a manual fallback

## Why this exists

A skill tells an employee what to do. It does not give it the keys. The single most damaging failure in an AI employee is confident work done without access to the real systems - a report invented because the database was never connected, a "sent" email that was never sent, a listing described but never created.

So every employee runs the same three-step habit before touching a task: check access, do the part it can, and be explicit about the rest.

## How a skill wires itself in

Every `SKILL.md` must:

- link `core/connector-preflight.md` in its workflow, before the first substantive step
- link `core/memory-and-notes.md` in its workflow, at the end
- carry a `notes/` folder with `learnings.md` and `contacts.md` seeded
- state, under *Tools it assumes*, which connectors the role needs most

`scripts/validate_repo.py` enforces this. A skill that fails the check does not ship.

## The one-line test

If a businessman reads the employee's answer and then discovers it could not have known something it claimed - the standard was broken. Every answer must be traceable to a connector that was actually connected, or to information the person actually gave.
