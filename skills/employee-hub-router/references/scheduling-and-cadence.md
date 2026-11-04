# Scheduling and cadence

Most jobs people describe as "ongoing" are one job plus a review. Deciding which
one you are looking at is part of routing, because a scheduled job that nobody
reads is a cost with no owner.

## The three answers

| The job | Cadence | What it needs |
|---|---|---|
| A one-off deliverable | Once, with a date | A brief and an approver |
| A repeating deliverable | Weekly or monthly, fixed day | A schedule, an input source, and a reader |
| A watch | On an event - new ticket, new order, price change | A trigger and a destination |

Ask one question to tell them apart: **"what would make you not want this next
week?"** If the answer is "nothing", it is a watch, not a report.

## Before you schedule anything

1. **Has it run manually twice?** A schedule amplifies a bad output.
2. **Is the input there every time?** A report built on a file that arrives "usually by Monday" fails on the Monday it does not.
3. **Who reads it?** Name the person. No reader, no job.
4. **What happens when it fails?** Skip, ask, or report the gap - decide now, in the brief.
5. **Does it write anything?** Send, publish, pay, delete - those need a human until the job has run in draft mode for two weeks.

## Where the schedule lives

`docs/scheduling.md` carries the four mechanisms - the agent host's own cron, a
GitHub Actions schedule, a webhook from n8n or Make, a platform cron - with the
exact lines. Pick by what the job must reach, not by preference.

## The cadence rules

- **Weekly beats daily** when the reader will not read daily. Most readouts are weekly.
- **Same day, same time**, because predictability is the product.
- **One job per schedule.** Two skills in one prompt produce a mush nobody reads.
- **A monthly review of the schedules themselves**: which ran, which were read, which should be deleted.
- **Silent failure is the enemy.** Every scheduled job logs a line on success and on failure.

## What you hand over with a schedule

The employee, the trigger, the inputs, the output destination, the reader, the
failure behaviour, and the date of the first manual run. Six lines, and the job is
real rather than aspirational.

## Anti-patterns

- Scheduling a write action because it is convenient.
- A daily digest nobody opens, kept alive because it looks productive.
- A job that fails silently and is discovered a month later.
- Five schedules for one employee, each with a different input format.
- A "real-time" dashboard that is a manual refresh.
