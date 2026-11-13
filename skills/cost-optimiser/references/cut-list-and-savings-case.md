# Cut list and savings case

A cut list is an instruction document. Every line has to be executable by someone who was not in the
conversation.

## The ladder, cheapest risk first

| Rung | Action | Typical saving | Risk |
|---|---|---|---|
| 1 | Cancel a converted trial nobody uses | 100% of that line | None |
| 2 | Remove never-logged-in seats | 5-20% of that tool | None |
| 3 | Downgrade a plan to the tier actually used | 20-50% of that tool | Loss of a feature someone uses daily |
| 4 | Consolidate a duplicate tool | 30-100% of the smaller line | Migration effort, data export |
| 5 | Remove cloud waste and orphaned resources | 5-20% of the cloud bill | None if genuinely idle |
| 6 | Right-size instances and storage tiers | 15-40% of compute and storage | Peak-load behaviour |
| 7 | Renegotiate at renewal | 10-30% of contract | Nothing if done before the date |
| 8 | Commit to a reserved or annual plan | 20-50% of the stable baseline | Lock-in |

Never start at rung 8. It is the rung that is easiest to sell and hardest to undo, and it commits the
waste you have not yet removed.

## The cut-list row

| Field | Content | Why it is mandatory |
|---|---|---|
| Tool | Normalised vendor and plan | Ambiguity in a cancellation is how the wrong thing is cancelled |
| Current cost | Annualised | Comparisons only work in one period |
| Action | Cancel / downgrade / remove seats / consolidate / renegotiate | One verb per row |
| Saving per year | Net of migration cost | A gross saving is a claim, a net saving is a number |
| What breaks | The specific workflow or person affected | The line that prevents the support ticket |
| Owner | Who executes | Not "the team" |
| Approver | Who signs | Usually the founder above a threshold |
| By when | A date before the renewal or notice period | A cut after renewal is a cut next year |

## Sizing the case

Three numbers, always together:

1. **Identified** - the sum of every row's saving. This is the ceiling and it is not a plan.
2. **Capturable in 30 days** - rungs 1-5 only, with no migration. Usually 30-60% of identified.
3. **Capturable in 90 days** - adds rungs 6-7. Rung 8 only if the founder wants the lock-in.

Then the effort column: hours per row, whose hours, and whether that person has those hours this
month. A saving that needs the only engineer during a launch month is a saving for next quarter, and
saying so is the difference between a plan and a wish.

## Sequencing

1. **This week** - cancel the trials and remove the never-used seats. No approvals needed, no risk,
   and it funds the credibility of the rest.
2. **This month** - the duplicates and the cloud waste. Needs a migration decision per tool.
3. **Before the next renewal** - the renegotiations. Each one needs 60 days of runway.
4. **Only after the baseline is clean** - commitments.

## The conversation with the founder

Four sentences, in this order:

1. What the business spends a year on technology, and how many separate subscriptions that is.
2. What is being paid for and not used, in rupees, with the two largest examples.
3. What can be cut in 30 days without a project, and what needs a decision.
4. The one thing that must happen this week or the next renewal repeats the problem.

Then stop. A founder who is shown a correct number and a short list acts; a founder shown a
forty-row spreadsheet forwards it to somebody else.

## Anti-patterns

- **A cut list with no owners.** It becomes a document that everyone agrees with and nobody executes.
- **Savings measured before they are realised.** Track identified separately from realised, or the
  next review reports the same savings again - which is the most common way this role loses trust.
- **Cutting the tool the loudest person defends** to demonstrate rigour. Cut on usage, not on volume
  of complaint.
- **A migration recommended without the export path.** Half-migrated tools are paid for twice.
- **Reporting a monthly saving as an annual one**, or the reverse. One period, stated on every page.
- **Forgetting the taxes and the FX.** A USD subscription's rupee cost moves with the rate; state the
  rate used.
