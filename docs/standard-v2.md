# The v2 standard

From the drop of 2026-11-03, a new employee ships as a tree a reviewer can check mechanically, not just read. `scripts/validate_repo_v2.py --strict` is the gate.

v1 asked whether a skill was well written. v2 asks whether it can be tested, trusted with a scope, and held to a level. A skill that does not declare `standard_version: 2` is checked against the v1 baseline only and listed under DRIFT - that list is the next tenth-drop's work, not an exemption.

## The tree

```
skills/<role>/
  SKILL.md                  fixed section order, description under 1024 chars
  references/*.md           3-6 craft files, every one routed from SKILL.md
  scripts/<name>.py         at least one deterministic script with --self-test
  assets/<template>.md      one template of the role's own good output
  evals.json                five cases, five types
  notes.seed/               schema only, no invented experience
    learnings.md
    contacts.md
    decisions.md
    journal/YYYY-MM.md
```

## The fixed section order

The nine H2s, in this order. A reviewer reads *Routing* to see what the employee thinks the request is, and *Guardrails* to see what it will refuse - those two must always be in the same place.

1. What you are accountable for
2. What you must be handed before you start
3. Tools it assumes
4. Routing: read the request, load the craft
5. The workflow
6. Standards you hold yourself to
7. Output contract
8. Guardrails
9. Trigger test

`core/connector-preflight.md` must appear in the workflow before the first substantive step, and `core/memory-and-notes.md` plus `core/performance-tracking.md` before the output contract.

## The description

Under 1024 characters, and it carries: what the role owns, the situations it fires on, at least five literal trigger phrases in the user's own words, and a "Not for ... (use X)" boundary for every adjacent employee. The boundary is what stops two employees fighting over the same request.

## The deterministic script

At least one, in `scripts/`, that does real work with no model and no network: a linter, a matrix generator, a triage rule table, a margin model. It must support `--self-test` and pass it. The self-test asserts on fixtures embedded in the file, including a determinism check and at least one guard against bad input.

The point is not automation. It is that part of the employee's judgement is written down as rules a reviewer can read and change, instead of living in a prompt that drifts.

## evals.json

Five cases, one of each type. A case is a prompt, the connector state it runs in, what the answer must contain, what it must not contain, and how it is scored.

| Type | What it proves |
|---|---|
| `happy_path` | The employee does the job when given a real brief and its connectors |
| `thin_brief` | It asks for the right few things instead of inventing the rest |
| `missing_connector` | It names the connector, refuses to fabricate, and still delivers the part it can |
| `wrong_tool` | It hands the request to the right employee instead of doing it badly |
| `handoff` | It splits a request that belongs to two employees and takes only its part |

`must_name_connector` on the missing-connector case, and `routes_to` on the wrong-tool and handoff cases, must name a role that exists in the registry or the backlog. That is what keeps routing honest as the hub grows.

## notes.seed, not notes

v2 ships an empty schema. The files carry column headers, a "How to fill this" section, and nothing else. An employee that has not run a task has no learnings, and a seeded file full of plausible-looking experience is the most damaging kind of fabrication in this repo: it reads as memory.

The first real task populates `notes/`. Until then the seed says what to write and why.

## The level ladder

Level is a permission scope, not a rank. It answers one question: what may this employee do without a human saying yes?

| Level | Name | May do | May not |
|---|---|---|---|
| L0 | Observe | Read connected systems, produce analysis and recommendations | Write anywhere, or produce a document for sending |
| L1 | Draft | Produce documents, files and models for a human to act on | Write to any external system |
| L2 | Operate | Write to connected systems it has been granted - labels, notes, issues, drafts - with confirmation per action | Send, publish, pay or delete |
| L3 | Act | Send, publish, create and schedule on the user's behalf, with confirmation per action | Spend money or run unattended |
| L4 | Autonomous | Run on a schedule within a stated budget and scope | Act outside the stated scope, or spend beyond the budget |

Every new employee ships at `status: probation` and `reliability: unverified`. Probation means the output needs a human read before it is used. Reliability becomes `measured` only when the evals have been run against real tasks and the pass rate is recorded - not because the skill looks good.

## Registry fields

Every entry with `standard_version: 2` carries:

| Field | Meaning |
|---|---|
| `level` | L0-L4, from the ladder above |
| `category` | revenue-facing, operations, or founder-leverage - the mix the drop is balanced on |
| `permissions` | The explicit read / draft / write / never list, matching the level |
| `cost` | A tier (low, medium, high) and the basis - what one typical task spends |
| `connectors` | `required`, `available_in_catalog` (which of the required ones the catalog names), `requires_paid`, and `works_without` - what the employee can still do with nothing connected |
| `status` | probation, stable, deprecated |
| `reliability` | unverified, measured, disputed |

`works_without` is not decoration. Rule 4 of the backlog says every employee must be usable on day one with a connector the user already has - and the honest version of that is a sentence saying what it does with none.

## What the gate checks

`python3 scripts/validate_repo_v2.py --strict` fails on: a broken standard link, a missing or reordered section, a description at or over 1024 characters, a reference count outside 3-6, an unrouted reference or asset, a missing or failing `--self-test`, an eval set that is not five cases of five types, a `routes_to` that names nothing, a `notes.seed` with content in it, and a registry entry missing a v2 field or requiring a connector the catalog does not name.

It prints three lists: errors (the gate), warnings (promoted to errors under `--strict`), and drift (v1 skills that would not pass v2). Drift is not a pass - it is a queue.
