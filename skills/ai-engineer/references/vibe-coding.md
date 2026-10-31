# Vibe coding

Building by intent - describe it, let the model write it, run it, iterate. It is the fastest way to get an internal tool, a prototype or a glue script. It is not a way to ship anything that touches money, authentication or customer data without a proper review pass.

The difference between people who vibe-code successfully and people who drown in broken files is discipline, not talent.

## The five rules

1. **One screen of spec first.** What it does, what goes in, what comes out, what it must not do. Written down, in the repo, before code. This is the file you paste at the start of every session.
2. **Smallest runnable slice.** Make the thinnest end-to-end path work - input to output, even with hardcoded values - before adding a single feature. A working skeleton beats a beautiful half-module.
3. **Run after every change.** Never accept a diff you have not executed. Errors compound; the tenth unrun change is unrecoverable by reading.
4. **Real data early.** Fake data hides every parsing bug you will actually hit.
5. **Commit before every risky edit.** Cheap insurance. When the model mangles a working file, you want a one-command return.

## How to ask for code

State four things every time: the file, the stack with versions, the constraint, and the acceptance test.

- "Edit `src/parse.py` only. Python 3.12, pandas 2.x. It must handle a CSV with a BOM and a blank final line. Test: the sample file in `fixtures/` returns 14 rows."

Vague asks produce plausible code that does not run. The acceptance test is what makes the request checkable.

## Plan before diff

For anything over roughly a hundred lines, ask for the plan first - files touched, functions added, dependencies - then approve, then ask for the code. This catches the wrong architecture before it is written into five files.

## Debugging loop

Reproduce -> isolate -> shrink -> fix -> regression test. Never paste a stack trace and accept a rewrite. Ask for the smallest failing case first; a fix that changes eight things is a guess.

## Repo hygiene

- Single entry point (`main.py`, `npm start`). If a session cannot find where it starts, every session restarts confused.
- `.env.example` committed, `.env` ignored. No key ever enters a file, a prompt, or a commit.
- Pin dependencies. "Latest" is a future outage.
- One README section: how to run it. Written for you in three weeks.

## Review bar

Read every line you ship. If you cannot explain what a block does, do not ship it - delete it and ask again, or write it yourself. Vibe coding debt is not the code you did not write; it is the code you cannot read.

## When to stop vibe coding

Stop and build properly when any of these is true: it handles customer data, it moves money, it needs to run unattended for months, more than one person edits it, or it has had three bugs that a test would have caught. At that point write tests, add types, and get a review.

## Deployment

Preview environment first, always. Feature-flag anything user-facing so a bad deploy is a flag flip rather than a rollback. Keep the previous working version deployable for at least a week.
