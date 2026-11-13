# learnings.schema - shape only, no experience recorded

This file defines what a learning must look like. It carries no entries on purpose: an employee that
ships with invented experience is an employee whose notes cannot be trusted later.

## Format

```
N. **<the rule, in one sentence, imperative>** <the evidence that would have produced it, in one or
   two lines: what failed, in what kind of situation, and what to do instead.>
```

## Rules for an entry

| Field | Requirement |
|---|---|
| Rule | One sentence, checkable, no hedging |
| Trigger | The situation in which the rule applies, in the words a person would use |
| Evidence | Where it came from - a task, a failed filing, an attorney's correction |
| Date | dd/mm/yyyy of the task that produced it |

## What does not belong here

- A story with no rule in it.
- A rule with no situation attached - it will never be recalled at the right moment.
- Anything about a specific client, mark or applicant that identifies them.
- A restatement of the SKILL.md guardrails. Those are design; this file is experience.
