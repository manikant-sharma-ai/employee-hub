# The cut list and the savings case

A cut list is a ranked set of dated decisions, not a list of tools the founder dislikes. This file is the
arithmetic and the sequencing.

## The four kinds of saving, and why they rank differently

| Kind | Example | Risk | Effort | Owner |
|---|---|---|---|---|
| Waste | 19 unused seats, an idle staging cluster | Low | Low | The line's owner |
| Size | A tier or instance one step too large | Low | Low-medium | Engineering or ops |
| Price | A renewal discount, a true-up, a flat hold | Low | Medium - a conversation | Founder or finance |
| Structure | Two tools that do one job, a vendor that should not exist | High | High - a migration | The function head |

Rank by **net saving ÷ effort**, then break ties by the deadline. Structure changes are the biggest numbers
and the ones that fail; they need a plan, not a line on a list.

## The row that makes a cut defensible

| Field | Rule |
|---|---|
| Line | Vendor and plan, exactly as on the statement |
| Action | Cancel / downgrade / consolidate / renegotiate / hold |
| Gross annual saving | Rupees, from the inventory, GST-excluded |
| Switch cost | Migration hours × a real hourly rate, plus exit fees, plus overlap period |
| Net annual saving | Gross minus switch cost, first year |
| Risk | What breaks, and who notices |
| Deadline | The notice date, or the date after which the saving is lost |
| Owner | One person, named |
| Next step | The specific action: who emails whom, by when |

The switch cost line is what separates a credible case from a slide. A ₹1.2 lakh annual saving that needs 25
engineering hours at ₹2,000 an hour nets ₹70,000 - still worth doing, but say the number.

## Sequencing: three waves

| Wave | Timeline | Contents | Why first |
|---|---|---|---|
| 1 | This week | Waste: unused seats, idle resources, orphaned storage, an unopened tool | No dependency, no risk, immediate cash |
| 2 | This quarter | Price and size: true-ups, tier corrections, renewal holds, right-sizing | Needs a conversation or a change window, not a migration |
| 3 | This half | Structure: consolidation, a build-versus-buy call, an architecture change | Needs a plan, an owner and a migration |

A review that opens with wave 3 produces a document and no savings. Wave 1 funds the credibility for the rest.

## The savings tracker

| Line | Estimated annual | Action date | Realised annual | Verified on | Note |
|---|---|---|---|---|---|
| | | | | The invoice date it showed up on | Why it differed |

The tracker is the role's reputation. Two rules: a line is "realised" only when an invoice proves it, and a
line that did not materialise stays in the table with the reason.

## What must not be cut, ever

| Line | Why |
|---|---|
| Backups and off-site copies | The only thing between a business and a bad afternoon |
| Security tooling and the password manager | A breach costs more than every subscription combined |
| Monitoring and alerting for anything customer-facing | You find out from customers instead |
| Statutory and compliance software | The penalty is not a line item |
| The tools the business sells on | Cost reduction that breaks revenue is not a saving |
| Support tooling during a peak season | The queue is the business |

Put this table in the brief. A founder reading a cut list needs to see what was deliberately protected.

## The consolidation test

Before recommending that two tools become one:

1. Who uses each, daily? Names, not teams.
2. What data lives in the one being retired, and where does it go?
3. What is the migration in hours, honestly?
4. What does the surviving tool not do that people use today?
5. What is the date after which the retired tool's data is gone?

If question 4 has an answer people care about, it is not a consolidation. It is a decision to lose a
capability, and it should be priced as one.

## Writing the case in one page

1. **The number** - recurring spend now, the target, the gap.
2. **Where it is** - the top lines and the four kinds of saving, with the split.
3. **The wave 1 list** - what happens this week, with owners.
4. **The wave 2 asks** - what needs a conversation, with the date.
5. **What is protected** - the do-not-cut table, with the reason.
6. **What it assumes** - headcount, volume, a renewal date, a contract term.
7. **How it will be verified** - which invoice, on which date, proves each line.

## Anti-patterns

- **A percentage target with no line items.** "Cut 20%" is a mood; eleven dated actions is a plan.
- **Savings counted before the notice period passes.** The renewal already ran and the saving is next year's.
- **Cutting the observability bill in a month with an incident.** The saving is real and the timing is a
  disaster.
- **Consolidating to a tool nobody has migrated to yet.** Two subscriptions become one subscription and one
  parallel spreadsheet that never dies.
- **A tracker with only successes.** The lines that failed are the ones that teach the next review.
