# founder-skills

A repo of AI employees for any business.

Every folder under `skills/` is one employee. You install the repo once, and each employee becomes a skill your agent can pick up - the way a new hire picks up a role, with the experience already in place.

## The idea

A person you hire brings four things: experience, tool access, a brief about your business, and a schedule. An AI employee is the same four parts.

| Part | Where it lives |
|---|---|
| Experience | `SKILL.md` + `references/` - the craft, written down |
| Tool access | MCP servers you authorise (Gmail, Canva, Sheets, your own APIs) |
| The brief | Your context files, brand assets, examples of good output |
| The schedule | A cron run, a webhook, or you asking it |

The skill file is the part that carries the experience. That is why it is written as a briefing document - what the employee is accountable for, what it must be handed, the sequence it follows, the standard it holds itself to, and what it must never do without asking - rather than as a prompt.

## What's in here

```
skills/<employee>/
  SKILL.md          the employee: accountability, inputs, routing, workflow, standards, guardrails
  references/       the craft, one file per discipline, loaded only when needed
  scripts/          anything deterministic, so the model does not have to reason about it
  assets/           templates and examples of good output
registry.json       machine-readable index: name, version, date added, tools required
CHANGELOG.md        one dated block per daily drop
BACKLOG.md          the queue of employees still to be built
.claude-plugin/     plugin manifest, so the whole repo installs as one unit
docs/daily-drop.md  the standing procedure for adding tomorrow's employee
```

## Employees

| Employee | What it does | Added |
|---|---|---|
| [`ai-engineer`](skills/ai-engineer/SKILL.md) | Designs, builds and ships AI systems - prompts, context, loops, graphs, MCP tools, images, evals and automation. | 2026-10-31 |

## Install

**As a plugin (Claude Code and compatible hosts):**

```
/plugin marketplace add manikant-sharma-ai/founder-skills
/plugin install founder-skills
```

**Manually:** copy the folder you want into your skills directory - `~/.claude/skills/` or `.claude/skills/` inside a project. One folder per employee, nothing else required.

**Tools are separate.** A skill tells the employee what to do; it does not grant access. Connect the MCP servers listed under each employee's *Tools it assumes* before expecting it to act. This is deliberate - the same employee should be usable by a business that has Gmail and one that has Outlook.

## Using an employee

Give it the five things in its *What you must be handed* section - the job, a definition of done, tool access, a budget, and the blast radius. Then let it work. The employees are written to ask for what is missing rather than invent it, so a thin brief produces a question, not a confident wrong answer.

## The daily drop

One new employee is added every day at 06:00 IST, following `docs/daily-drop.md`: pick the next role off the backlog, write the skill and its references, validate, update registry and changelog, commit. See `CHANGELOG.md` for what has shipped.

## Adding your own

Run the validator before you commit:

```
python3 scripts/validate_repo.py
```

It checks frontmatter, description quality (the description is what makes a skill trigger), required sections, and that every reference link resolves.

## Licence

MIT. Take what is useful.
