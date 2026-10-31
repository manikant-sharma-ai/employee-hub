# The daily drop

The standing procedure for adding one employee a day. Follow it exactly; the point is that day 40 looks like day 1.

## 06:00 IST, every day

1. **Pick.** Take the next `queued` role from `BACKLOG.md`. Skip anything whose trigger phrases would collide with a shipped employee - note the collision and move to the next.
2. **Write the skill.** `skills/<role>/SKILL.md` with the eight sections in `references/skill-authoring.md`: accountability, inputs required, routing, workflow, standards, output contract, guardrails, trigger test. The description gets the most care - it decides whether the skill ever fires.
3. **Write the references.** Three to six craft files, one per discipline the role actually needs. Each 60-120 lines, dense, with tables and anti-patterns. No theory about how models work.
4. **Add an asset** if the role produces a document - a template of its own good output.
5. **Validate.** `python3 scripts/validate_repo.py` must pass with zero errors. Warnings are acceptable only with a reason in the changelog.
6. **Register.** Add the entry to `registry.json` (name, version 1.0.0, today's date, path, tagline, skills_inside, tools_required, outputs, best_for).
7. **Changelog.** A dated block: what shipped, and one line on why it is shaped that way. Not a file list - the reasoning.
8. **Backlog.** Mark the role `shipped <date>`, promote the next to `next`.
9. **Commit and push** to `main` with the message `feat(<role>): daily drop <YYYY-MM-DD>`.
10. **Report** one paragraph to the user: what shipped, what it does that yesterday's could not, and what is next.

## Non-negotiables

- One employee per day. A day that ships nothing is better than a day that ships a thin skill - quality of the description is what makes the repo worth installing.
- Every claim in a skill must be operational. If a line cannot change what the employee does, delete it.
- No credentials, no customer data, no client names in the repo.
- If a role genuinely needs a paid tool or a private API, ship it anyway and list the tool under *Tools it assumes*.

## Every tenth drop

Review the whole repo: descriptions for trigger collisions, references that have gone stale against current models and tools, and the registry against the folders. Fix drift in the same commit.
