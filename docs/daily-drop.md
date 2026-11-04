# The daily drop

The standing procedure for adding five employees a day. Follow it exactly; the point is that day 30 looks like day 1.

## 06:00 IST, every day

1. **Pick five.** From `BACKLOG.md`, take the next roles honouring the mix: two revenue-facing, two operations, one founder-leverage. Skip any role whose trigger phrases would collide with a shipped employee - note the collision and take the next one.
2. **Write each skill.** `skills/<role>/SKILL.md` with the sections in `references/skill-authoring.md`: accountability, inputs required, routing, workflow, standards, output contract, guardrails, trigger test. Wire in the Employee Standard - link `core/connector-preflight.md` in the workflow, `core/memory-and-notes.md` and `core/performance-tracking.md` before the output contract. The description gets the most care; it decides whether the skill ever fires.
3. **References.** Three to six craft files per employee, one per discipline the role actually needs, 60-120 lines each, dense, with tables and anti-patterns.
4. **Notes.** Seed `notes/learnings.md`, `notes/contacts.md`, `notes/decisions.md` and `notes/journal/YYYY-MM.md` with the two or three rules that follow from how the skill was designed.
5. **Assets.** One template of the role's own good output, where the role produces a document.
6. **Validate.** `python3 scripts/validate_repo_v2.py --strict` must pass with zero errors and zero warnings, and `validate_repo.py` must pass inside it. A skill that fails the standard is fixed, not shipped - if a role cannot clear the bar today, it returns to the queue and the next one is taken.
7. **Register.** Add five entries to `registry.json`.
8. **Changelog.** One dated block for the batch, with a line per employee on why it is shaped that way. Not a file list - the reasoning.
9. **Backlog.** Mark the five `shipped <date>`, promote the next five to `next`.
10. **Commit to a branch and open a pull request.** Branch `drop/YYYY-MM-DD`, commit `feat: daily drop <YYYY-MM-DD> - five employees`, open a PR against `main` with the drop report as the body. Never push to `main` - the gate runs on the PR, and a bad drop should be reviewable before it lands.
11. **Report** one paragraph: the five that shipped, what they can do that yesterday's could not, which one to use first, and what is next.

## Non-negotiables

- Five, and every one usable on day one with at least one connector the person already has.
- Every claim in a skill must be operational. If a line cannot change what the employee does, delete it.
- Every employee names its connectors honestly. No skill may imply access it does not have.
- No credentials, no customer data, no client names in the repo.
- If a role needs a paid tool, ship it anyway and list the connector under *Tools it assumes*.

## Every tenth drop

Review the whole repo: description collisions, references gone stale against current models and connectors, registry against folders, and whether the notes files are being written at all. Fix drift in the same commit.
