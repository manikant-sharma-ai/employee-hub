# Spend inventory and tagging

The inventory is the role. Every other output is derived from it, and a recommendation made without one is a
guess with a percentage attached.

## Build it from the money, not from the app list

| Source | What it gives you | What it misses |
|---|---|---|
| Bank and card statements, 12 months | Everything that was actually paid, including the lines nobody remembers | Annual prepayments in one month, refunds, personal cards |
| Accounting ledger expense lines | Categorised, with the vendor name as recorded | Miscoding, and the subscriptions booked under "miscellaneous" |
| Vendor admin consoles | Seats, plan, renewal date, usage | The tools nobody has admin rights to any more |
| SSO or directory | Who logs in, and to what | The tools outside SSO - which are usually the waste |
| Cloud billing export | Cost by service, tag and month | Anything paid on a separate invoice |

Start from the statements and reconcile to the ledger. The difference between the two is itself a finding: a
subscription paid on a personal card and reimbursed never appears in a vendor review, and it is usually the
one that renews for four years.

## The inventory columns

| Column | Rule |
|---|---|
| Vendor | The name on the statement, not the marketing name |
| What it does | One phrase, in business language |
| Function | Design, sales, support, engineering, finance, ops, marketing |
| Monthly cost | Normalised: annual prepay ÷ 12 |
| Annual cost | The number the founder decides on |
| Seats bought | From the console |
| Seats active (30d) | From the SSO or admin log, with the source named |
| Owner | One named person, not a team |
| Renewal date | The date the card is charged, not the contract end |
| Notice period | Days before renewal that notice must be given |
| Contract term | Monthly, annual, multi-year |
| Criticality | Load-bearing / replaceable / unclear |

"Unclear" is a legitimate value and a useful one. A line whose criticality nobody can state is a line with
no owner, and it is the first place to look.

## Normalising so the total is honest

| Situation | How to record it |
|---|---|
| Annual prepay | ÷ 12 for the monthly figure, full amount in the annual column |
| Usage-based cloud | Average the last three months; state the peak separately |
| Multi-year with a discount | Amortise over the term; note the commitment remaining |
| Refund or credit | Net it against the same vendor |
| GST | Record exclusive of GST; input credit is not a cost |
| Forex-billed | Convert at the month's rate and note the exposure |
| Paid in a foreign currency on an Indian card | Add the card markup; it is 2-3.5% and invisible |

## Tagging, if the business has none

Two dimensions are enough to start: **function** (who benefits) and **environment** (prod, staging, dev,
internal). A third - **cost centre** - only earns its keep once there are several teams.

| Tag | Values | Why |
|---|---|---|
| function | eng, sales, mktg, support, finance, ops | Answers "which team's budget is this" |
| env | prod, stage, dev, sandbox | Finds the 30% of cloud spend that serves nobody |
| owner | a person's handle | Answers "who do we ask" |
| criticality | p0, p1, p2 | Decides what may be cut |

Retro-tagging a year of bills is not worth it. Tag the last full month, then let it accumulate.

## The five lines that are always there

In almost every Indian SMB review these five appear, and they are worth a specific look every time:

1. **Seats bought for a team that shrank.** The licence was sized at the peak headcount and never revisited.
2. **Two tools that do the same thing.** A design tool plus another design tool, two CRMs, three analytics.
3. **A staging or dev environment running at production size**, 24x7, for a team that works ten hours a day.
4. **A subscription paid annually and used monthly** - or used once, in the month it was bought.
5. **The tool the founder's previous company used.** It arrived with a habit, not a decision.

## The reconciliation line

End the inventory with three numbers: total from statements, total from ledger, difference. If the difference
is more than a rounding error, the review is not finished - an unexplained line is either a miscoding or a
subscription nobody has looked at, and both are the point of the exercise.

## Anti-patterns

- **Starting with the vendor's dashboard.** It shows you what you pay them; it cannot show you what you pay
  everyone.
- **Recording list price.** The statement is the truth; list price is a negotiating position.
- **Leaving GST in the cost.** It overstates spend by 18% and makes every ratio wrong.
- **A monthly number for an annual prepay.** The month it is charged looks like a spike and every other month
  looks free.
- **No owner column.** The single most predictive field in the whole table.
- **Building the inventory once.** It is stale in six weeks; the renewal calendar is what keeps it alive.
