# journal.schema - shape only, no days recorded

One file per month, `notes/journal/YYYY-MM.md`. One bullet per task, written before the reply is
sent, not after.

```
- **YYYY-MM-DD** - <what was asked> | <what was delivered> | <what the next run should do
  differently, or "nothing">
```

## Rules

| Field | Requirement |
|---|---|
| Date | dd/mm/yyyy, the day the work was done |
| Asked | The question in the requester's words, shortened |
| Delivered | The artefact and the one decision it supported |
| Next time | A change in method, or the word "nothing". Never a diary entry |

## What does not belong here

- Anything that identifies a client, a mark under consideration, or a filing number.
- A summary of the search results. The log belongs with the brief, not in the journal.
