# learnings.schema - shape only, no experience recorded

Defines what a learning must look like. No entries on purpose: an employee that ships with invented
experience is an employee whose notes cannot be trusted later.

## Format

```
N. **<the rule, in one sentence, imperative>** <the evidence: which synthesis showed it, in what kind
   of business, and what to do instead.>
```

## Rules for an entry

| Field | Requirement |
|---|---|
| Rule | One sentence, checkable, no hedging |
| Trigger | The situation in which it applies |
| Evidence | The readout, the unmatched share, or the decision that followed |
| Date | dd/mm/yyyy |

## What does not belong here

- A story with no rule in it, or a rule with no situation attached.
- Any customer's words, name, ticket id or company.
- A restatement of the SKILL.md guardrails. Those are design; this file is experience.
