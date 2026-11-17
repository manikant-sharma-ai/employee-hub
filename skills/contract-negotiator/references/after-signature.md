# After signature: the obligations register

A contract is not finished when it is signed. It is finished when every date in it has an owner.

## The register, one row per obligation

| Field | Example |
|---|---|
| Obligation | Give 60 days' written notice to avoid auto-renewal |
| Clause | 4.2 |
| Type | Notice / payment / deliverable / audit / reporting |
| Due | 15 March, or "60 days before 14 May" |
| Owner | Named person, not a department |
| Calendar event | Created, with two reminders (60 and 30 days before) |
| Status | Open / done / waived |

Everything with a date goes in. Everything with a recurring obligation gets a recurring event. Anything with a
penalty gets two reminders.

## The dates that cost money

| Date type | Consequence of missing it |
|---|---|
| Auto-renewal notice window | A year of committed spend |
| Price escalation | An unplanned increase nobody budgeted |
| SLA measurement period | A credit claim that lapses |
| Deliverable deadlines | A breach, and sometimes a penalty |
| Insurance or compliance certificate | A termination right for the other side |
| Data deletion on exit | A DPDP obligation and a breach risk |

## Version control

- **One signed copy**, PDF, in a folder the business will find: by counterparty, then by date.
- **The final redline is kept beside it**, so the negotiated position can be reconstructed.
- **Drafts are archived, not deleted** - a dispute about what was agreed starts with what was sent.
- **A filename convention**: `YYYY-MM-DD <counterparty> <type> <signed|draft vN>.pdf`.
- **The register links to the file**, so the obligation and the document live together.

## Handoffs on signature day

| Who | Gets |
|---|---|
| Finance | Payment terms, invoicing schedule, committed spend, any indexation |
| Data privacy officer | Processing terms, sub-processors, breach notice window |
| Compliance watch | Filing or reporting obligations created by the contract |
| The delivery owner | Deliverables, SLAs, acceptance criteria |
| The founder | The one-page summary: what we signed, what it costs, what to watch |

A contract handed to nobody is a contract nobody performs, and the first performance failure is discovered by the
counterparty.

## The renewal run

Start 90 days before any renewal date, not 30:

1. **Is the thing still worth having?** Usage, cost, alternatives.
2. **What is the price now, and what should it be?** A renewal is the only time a price can be renegotiated without
   a new vendor search.
3. **What did the last year's SLA actually deliver?** Credits owed, breaches unrecorded.
4. **Notice date and owner confirmed**, in writing, to the counterparty.

## Anti-patterns

- A register in a spreadsheet nobody opens, with no calendar events.
- Renewal reminders set for the renewal date rather than the notice date.
- A signed contract in an inbox, findable only by searching a person's name.
- No handoff to finance, so the first invoice arrives with terms nobody expected.
- Treating signature as the end of the work, which is how the same bad clause is signed again next year.
