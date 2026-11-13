# decisions.schema - shape only, no decisions recorded

Columns for `notes/decisions.md`. A decision is recorded when it was contested, not when it was
obvious.

| Column | Requirement |
|---|---|
| Date | dd/mm/yyyy |
| Decision | The choice, in one line, stated as a rule |
| Why | The reason that will still be true in six months |
| What would reverse it | The specific change in circumstance that reopens it |

## What does not belong here

- A decision nobody argued about.
- A decision with no reversal condition - that is a belief, not a decision.
- A decision that belongs to the attorney or the founder. Record that it was theirs, not what it was.
