# Contributing an employee

The hub is a collection of employees, and an employee that does not follow
`core/employee-standard.md` is not finished. This page is the contract.

## Before you write anything

1. Read `core/employee-standard.md` and one shipped skill end to end - `skills/graphic-designer/SKILL.md` is the reference implementation.
2. Check `BACKLOG.md` for the role. If it is already there, take the row and mark it, do not invent a parallel name.
3. Check for a **trigger collision**: does an existing employee already fire on the phrases this one would? Read the *Trigger test* section of the closest three skills. A collision is fixed by narrowing the new description, not by adding "also" clauses.

## What a skill must contain

```
skills/<role>/
  SKILL.md            frontmatter + the body
  references/         3-6 craft files, one per discipline, 60-120 lines each
  assets/             one template of this role's own good output
  notes/              learnings.md, contacts.md, decisions.md, journal/YYYY-MM.md
```

`SKILL.md` sections, in this order: what you are accountable for, what you must
be handed, routing table, the workflow, standards, notes and self-tracking,
output contract, guardrails, trigger test.

Three links are mandatory and `scripts/validate_repo.py` enforces them:

- `core/connector-preflight.md` - before the first substantive step
- `core/memory-and-notes.md` - in the notes section
- `core/performance-tracking.md` - in the notes section

## The description is the product

The description decides whether the skill ever fires. It needs:

- what the employee produces, in the words a business owner would use;
- **"Use when"** with three to six real trigger phrases, quoted as the person would type them;
- **"Not for"** with the specific neighbouring employee to use instead.

25 to 170 words. No adjectives that do not change behaviour. No "powerful", no "comprehensive".

## The bar

Every line must be operational: if deleting it would not change what the
employee does, delete it. No invented market data, no implied access, no
credential, no client name, no customer data. If a role needs a paid tool, ship
it anyway and name the connector under *Tools it assumes*.

## Checklist before you open a PR

- [ ] `python3 scripts/validate_repo.py` passes with **zero errors and zero warnings**
- [ ] `python3 scripts/validate_manifests.py` passes
- [ ] `registry.json` has the entry: name, version, added, status, path, tagline, skills_inside, tools_required, follows_standard, keeps_notes, tracks_performance, outputs, best_for
- [ ] `CHANGELOG.md` has a dated block that explains the reasoning, not a file list
- [ ] `BACKLOG.md` row marked `shipped <date>`
- [ ] `README.md` table row added
- [ ] Notes are seeded with two or three real rules, not lorem ipsum
- [ ] Trigger test has four "should load" and four "should not load" lines, each naming the employee that should handle it instead

## Versioning

- A new employee starts at `1.0.0`.
- A change that alters behaviour - a new guardrail, a rewritten workflow - bumps the minor version in both `SKILL.md` and `registry.json`.
- Typos and link fixes do not bump anything.
- `registry.json`, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` carry the same hub version. Bump all three together; `scripts/validate_manifests.py` fails the build if they drift.

## Adding a connector

Connectors live in `core/connector-catalog.md` and nowhere else. Add a row with
the job, the connector and one honest note on when it is the right choice in
India. Never add a connector to a skill's workflow that the catalog does not list.
