# Consistency across documents

One document is a copy edit. A set is an audit. The audit is what makes this role
worth hiring, and it needs an artefact, not an opinion.

## The terminology ledger

| Preferred | Banned variants | Meaning | Where found |
|---|---|---|---|
| customer | client, user, buyer | The person who pays | site/pricing, proposal-v3, help/faq |
| plan | package, tier, subscription | A priced bundle | site/pricing, deck-q3 |
| onboarding | implementation, setup | First 30 days | handbook p12, proposal-v3 |
| GSTIN | GST number, GST no. | Registration | invoice template |

Rules: one preferred term per concept, at most three banned variants recorded,
and a location for each. The ledger is what the next document starts from.

## The audit method, in five moves

1. **List the set** - every document, its owner, its date, its status. Undated documents are a finding in themselves.
2. **Extract the facts that must not vary**: legal entity name, registered address, GSTIN, product and plan names, prices, key dates, headcount, certifications, the leadership names and spellings.
3. **Search each fact across the set** and record every variant with its location. Search, do not read - reading finds half.
4. **Rank the findings by cost.** A wrong GSTIN on an invoice is expensive; "e-mail" vs "email" is not. Fix in that order.
5. **Write the rule that prevents the recurrence**, and put it on the style sheet.

## What to audit, in priority order

| Class | Example | Cost if wrong |
|---|---|---|
| Legal identity | Entity name, CIN, GSTIN, address | Contract or filing rejected |
| Prices and commercials | ₹4,999 vs ₹4,900 vs "under ₹5,000" | Dispute, refund, lost trust |
| Product and plan names | "Pro" vs "Professional" vs "PRO" | Search, support, billing confusion |
| Dates and deadlines | 6 Nov vs 11/6 vs November 6 | Missed filing, missed launch |
| Numbers and units | 40% vs 40 per cent vs 0.4 | Credibility |
| Roles and titles | "Head of Sales" vs "Sales Head" | Internal friction, wrong signature |
| Terminology | customer vs client | Reader uncertainty |
| Mechanics | -ise vs -ize, serial comma | Polish only |

## Findings format

| # | Fact | Correct | Variant found | Location | Severity |
|---|---|---|---|---|---|
| 1 | Entity name | Sharma Retail Pvt Ltd | Sharma Retail Private Limited | proposal p2 | High |
| 2 | Plan name | Pro | Professional | site/pricing | High |
| 3 | Serial comma | none | used in 4 of 12 docs | multiple | Low |

## Version control for a set

- **Name files with a date and a status**: `proposal-2026-11-06-final.docx`. "final-final" is how the wrong version gets sent.
- **One source of truth per fact.** Prices live in one sheet; every document references it.
- **Freeze the set before the proof.** Editing a document that is still being edited is how the same error returns after you fixed it.

## Worked finding, written the way an author can act on it

```
F3 - HIGH - Legal entity name
Correct:  Sharma Retail Private Limited
Found:    "Sharma Retail Pvt Ltd" (proposal v3 p2, invoice template footer),
          "Sharma Retail Pvt. Ltd." (site /about)
Action:   fix all three to the registered form; the GSTIN and CIN must match it
Owner:    <name>, by <date>
```

The finding names the correct form, every location, the action and the owner. A
finding without an owner is a comment.

## The two-document test

Before auditing twenty documents, run the method on two. It surfaces the classes
of inconsistency in about twenty minutes and tells you whether the set is worth a
full pass:

1. Take the two most-read documents - usually the site and the last proposal.
2. Extract the legal name, the price list, the plan names and the top five terms.
3. Compare them field by field.
4. If three or more differ, the set needs the full audit before it goes out again.

## What "consistent" does not mean

- **Not identical.** A help article and a contract can describe the same thing differently and both be right.
- **Not one voice.** Consistency is about terms, facts, formats and rules - voice stays with the author.
- **Not frozen.** The ledger is a living list; a term changes when the business changes, with a date and a sweep of every document.

## Anti-patterns

- **A find-and-replace across a set.** It changes "client" inside "clients only" and inside a legal definition. Search to find, then change each with a query or a decision.
- **Fixing the small variants first.** The reader notices the entity name, not the serial comma.
- **Auditing without the owners' names.** Every finding needs a person who can approve the fix.
- **A ledger that is never consulted.** If it is not the first thing opened on the next job, it is a document, not a tool.
- **Treating consistency as uniformity.** Two documents for two audiences may legitimately differ; the ledger says where.
