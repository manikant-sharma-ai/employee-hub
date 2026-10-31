# Automation engineering

Automate the loop, not the task. The question is not "can this be automated" but "is this worth automating" - frequency x time per run x cost of error.

- Once a year: do it by hand.
- Once a week: a script you run.
- Once a day or more: a scheduled job with logging and alerts.
- Multiple times a day, with judgement: an AI employee with tools.

## Before you automate

Write the manual procedure and run it three times by hand. Automating a process you have not done is how you automate a misunderstanding. If you cannot write the steps down, you cannot automate them - the written procedure is the spec.

## Triggers

- **Schedule** - cron. Mind the timezone: a 6 AM IST job is 00:30 UTC, and DST-shifting servers will silently move it.
- **Webhook** - an event from a system. Verify signatures; treat the payload as untrusted.
- **File drop** - an upload or a new row. Dedupe by content hash, not filename.
- **Threshold** - a metric crossing a line. Add hysteresis or it will fire all night.

## Assume every step runs twice

Idempotency is not optional. Network timeouts, retries and duplicate webhooks will replay your job.

- Write with a **dedupe key** - `invoice_id + date`, not a random id.
- Use **upsert** semantics, not blind inserts.
- Make side effects checkable before repeating them - "was this email already sent" is a lookup, not a guess.

## Failure handling

- **Retries** with exponential backoff and jitter, capped at three.
- **Dead-letter** - after the cap, park the item with its error, do not drop it.
- **Alert on silence.** The most dangerous failure is the job that stops running and nobody notices. A daily heartbeat that expects a success record, and pages when it is absent, is worth more than any error alert.
- **Partial failure** must be visible - report what succeeded and what did not, per item.

## Secrets

Environment variables or a secrets store. Never in the prompt, never in the repo, never in a log line. Rotate on a schedule; an automation with an expired token fails silently at 3 AM.

## Observability

One run log per execution: trigger, items processed, per-item outcome, duration, cost, errors. Keep 30 days. When someone asks "did it run yesterday", the answer must be a lookup, not a memory.

## Cost control

Track cost per run and cost per item. A daily job that costs ₹40 per run is ₹1,200 a month - fine. The same job with an accidental retry loop is a different conversation. Set a hard cap and alert at 80%.

## Human in the loop

Anything irreversible gets a gate: a draft that a human approves, a preview link, a dry-run mode. Build dry-run first - it is also the fastest way to debug.

## Kill switch

Every automation needs one: an env flag or a paused schedule, documented, that stops it without a code deploy. Know it before you need it.

## Common failure modes

Date and timezone bugs, especially month-end and DST. Rate limits discovered at scale. Tokens expiring quietly. Duplicate sends. Silent no-ops where the job "succeeds" with zero items because a filter changed upstream. Schema drift in an upstream API. And the classic: the job works, so nobody looks at it for eight months, and it has been writing to the wrong sheet since March.
