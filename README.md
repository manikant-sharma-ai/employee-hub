# Employee Hub

AI employees for any business. One folder per employee, five new ones every morning at 06:00 IST.

You install the hub once. Each employee becomes a skill your agent picks up - the way a new hire picks up a role, with the experience already in place, and with the habit of telling you what it needs before it starts.

## The idea

A person you hire brings four things: experience, tool access, a brief about your business, and a schedule. An AI employee is the same four parts.

| Part | Where it lives |
|---|---|
| Experience | `SKILL.md` + `references/` - the craft, written down |
| Tool access | Connectors you authorise (IndiaMART, Shopify, Gmail, Sheets, Canva, Razorpay...) |
| The brief | Your context files, brand assets, examples of good output |
| The schedule | A cron run, a webhook, or you asking it |

The skill file carries the experience. The hub carries something else that most skill collections miss: a shared standard for how every employee behaves when it lacks access.

## The Employee Standard

Every employee here follows `core/employee-standard.md`. Four obligations:

1. **Check the connectors before answering.** No employee produces a report it had no way to compute, or claims to have sent something it never sent. It says what it needs, by name.
2. **Keep notes.** `notes/learnings.md`, `notes/contacts.md`, a dated journal, a decision log. It reads them at the start of a task and writes them at the end, so it gets better instead of repeating itself.
3. **Track itself on the calendar.** One event per task, a weekly review, a monthly scorecard. It knows its own first-pass acceptance rate and its repeat mistakes.
4. **Never fake the part it cannot do.** It delivers the part it can, names the gap, and offers a manual fallback.

### What that looks like in practice

You are a clothing brand with leftover stock. You hand over your sales file and ask what to do.

The employee answers in three lines:

```
Right now I can: from your sales file, 9 of 22 SKUs have not moved in 90 days and are
holding roughly ₹X at your stated cost; clearing those in bulk protects your retail price.
To finish it, connect: IndiaMART - unlocks live verified bulk buyers and enquiries.
Best tool for this job: IndiaMART - because surplus apparel in India sells to wholesale
buyers, not to your D2C storefront.
```

No invented market prices. No "I've listed it". A real answer from the one connector it had, plus the specific connector that would finish the job, plus a reason grounded in your market. That behaviour is written down in `core/connector-preflight.md`, and every skill is required to wire it in.

## What's in here

```
skills/<employee>/
  SKILL.md          accountability, inputs, routing, workflow, standards, guardrails
  references/       the craft, one file per discipline, loaded only when needed
  scripts/          anything deterministic, so the model does not reason about it
  assets/           templates and examples of good output
  notes/            learnings, contacts, journal, decisions - the employee's memory
core/               the Employee Standard every skill follows
registry.json       machine-readable index: name, version, date added, connectors
CHANGELOG.md        one dated block per drop
BACKLOG.md          150 roles queued, five a day
.claude-plugin/     plugin manifest, so the hub installs as one unit
docs/daily-drop.md  the standing procedure for the 06:00 drop
```

## Employees

| Employee | What it does | Added |
|---|---|---|
| [`ai-engineer`](skills/ai-engineer/SKILL.md) | Designs, builds and ships AI systems - prompts, context, loops, graphs, MCP tools, images, evals and automation. | 2026-10-31 |

## Install

**As a plugin (Claude Code and compatible hosts):**

```
/plugin marketplace add manikant-sharma-ai/employee-hub
/plugin install employee-hub
```

**Manually:** copy the employee folder you want into your skills directory - `~/.claude/skills/` or `.claude/skills/` inside a project.

**Connectors are separate, on purpose.** A skill tells the employee what to do; it does not grant access. Connect the connectors listed under each employee's *Tools it assumes* before expecting it to act. The same employee then works for a business with Gmail and one with Outlook - and it will tell you which connector it needs for the job in front of you.

## Using an employee

Give it the five things in its *What you must be handed* section - the job, a definition of done, connector access, a budget, and what happens if it is wrong. Then let it work. The employees ask for what is missing rather than invent it, so a thin brief produces a question, not a confident wrong answer.

## The daily drop

Five new employees every morning at 06:00 IST, following `docs/daily-drop.md`. The mix is fixed: two revenue-facing, two operations, one founder-leverage. See `CHANGELOG.md` for what has shipped.

## Adding your own

```
python3 scripts/validate_repo.py
```

It checks the core standard, frontmatter, description quality, required sections, reference links, the standard wiring (preflight, notes, tracking), registry drift, backlog runway and accidental secrets.

## Licence

MIT. Take what is useful.
