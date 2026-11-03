# Putting an employee on a schedule

A skill is the experience. A schedule is what turns it into a colleague that
shows up on Monday without being asked. This page is the missing half of
"hire an AI employee": how the work actually fires.

**Read this first:** a schedule does not grant access. If the employee cannot
reach the connector at 07:00 on Monday, it produces a draft and a note saying
what it could not do - it does not produce a sent email. `core/connector-preflight.md`
runs on every scheduled task exactly as it does on an interactive one.

## The four ways to schedule

| Way | Best for | Fails when |
|---|---|---|
| Your agent host's own cron (Claude Code, Codex, a local runner) | Personal daily or weekly jobs on your own machine | The machine is asleep, or the session has no connectors |
| GitHub Actions schedule | Repo work - validation, the daily drop, a report committed to a branch | The job needs your private connectors; secrets must be added to the repo |
| A webhook from an automation tool (n8n, Make, Zapier) | Multi-step flows that touch several systems and need retries | Nobody owns the flow; it silently dies and no one notices |
| A platform scheduler (Cloudflare Cron Trigger, Supabase pg_cron) | Small deterministic jobs that must run without you | The work needs judgement - these run code, not a skill |

## Pattern 1 - your own machine

The simplest schedule that works. One line in `crontab -e`:

```
30 6 * * 1-5 cd ~/work && claude -p "Use the data-analyst skill on ~/work/sales.xlsx. Weekly readout, five bullets, name anything you could not verify." >> ~/logs/data-analyst.log 2>&1
```

Rules that make this survive:

- **Absolute paths everywhere.** cron runs with a bare environment and a different working directory.
- **Redirect the output.** A scheduled run you cannot read afterwards did not happen.
- **One job, one skill, one output file.** Two skills in one prompt produce a mush nobody reads.
- **A schedule you cannot keep is a schedule you will turn off.** Weekly beats daily if weekly is what you will actually read.

## Pattern 2 - GitHub Actions

Right when the output belongs in the repo: a Monday metrics commit, a weekly
link check, the daily drop itself (see `.github/workflows/daily-drop.yml`).

```yaml
on:
  schedule:
    - cron: "30 3 * * 1"   # Monday 09:00 IST
  workflow_dispatch:        # always add this so you can test it now
```

- GitHub cron is UTC. IST is UTC+5:30, so 09:00 IST is `30 3`.
- Scheduled workflows are **disabled after 60 days of repo inactivity**, and can be delayed at busy times. Do not schedule anything that must land in the same minute.
- Anything the job needs to reach outside the repo goes in repo secrets, and the job prints what it could not reach instead of failing silently.

## Pattern 3 - webhook from an automation tool

The flow, in order: **trigger → gather → skill → deliver → log**.

1. Trigger: schedule, new row in a sheet, new email, new form entry.
2. Gather: pull the inputs the skill's *What you must be handed* section asks for.
3. Skill: call the model with the skill and the gathered inputs, nothing else.
4. Deliver: write to the sheet, draft the email, post the message - only after the preflight says the connector is reachable.
5. Log: one line per run with what it produced and what it could not.

Step 5 is the one everyone skips, and the only one that tells you the flow is alive.

## The weekly and monthly layer

`core/performance-tracking.md` assumes two recurring runs. Schedule them, or the
employee never learns anything:

| Cadence | Job | Output |
|---|---|---|
| Weekly, 15 minutes | Read `notes/journal/`, list what was accepted first time, what was redone | one line per task, one repeat mistake named |
| Monthly, 30 minutes | Score the month, pick one thing to fix | scorecard appended to `notes/learnings.md` |

## Anti-patterns

- **Scheduling an employee that has never run manually.** Run it by hand twice first; a schedule amplifies a bad output.
- **Scheduling a write action.** Sending, publishing, paying and deleting do not belong on a timer until the same job has run in draft mode for two weeks.
- **A schedule with no reader.** If nobody opens the output, delete the job - it is costing attention.
- **Silent failure.** Every scheduled job must leave a log line on success and on failure. A job that fails quietly teaches you to trust an empty folder.
