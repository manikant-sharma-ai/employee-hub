# learnings.schema - shape only, no experience recorded

This file defines what a learning must look like. It carries no entries on purpose: an employee that
ships with invented experience is an employee whose notes cannot be trusted later.

## Format

```
N. **<the rule, in one sentence, imperative>** <the evidence that would have produced it: what the
   number was, in what kind of business, and what to do instead.>
```

## Rules for an entry

| Field | Requirement |
|---|---|
| Rule | One sentence, checkable, no hedging |
| Trigger | The situation in which it applies, in the requester's words |
| Evidence | The review, invoice or failed cut that produced it |
| Date | dd/mm/yyyy |

## What does not belong here

- A story with no rule in it.
- A rule with no situation attached.
- Any vendor's contract terms, discount or NDA pricing.
- A restatement of the SKILL.md guardrails. Those are design; this file is experience.
