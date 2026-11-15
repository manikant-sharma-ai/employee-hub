# Cohorts, retention and the two churn numbers

A churn percentage computed on a moving base is the most common way a small business misleads itself. This file
makes the number defensible.

## Define before you compute

Write these four lines down before any calculation. They go in `notes/decisions.md` and they do not change
mid-year without a dated entry.

| Definition | Options | Pick one and say which |
|---|---|---|
| Who counts as a customer | Paying account, active account, seat, subscription | The unit the business is actually run on |
| What counts as churn | Voluntary cancellation only, or also failed payment and non-renewal | Both are reported; the headline is named |
| When churn is dated | The request date, the end-of-service date, the last payment date | The end-of-service date, so the revenue matches |
| Period grain | Monthly, with the annual view derived | Monthly, always |

## The base table

Every report starts with this, because the percentage is meaningless without it.

| Line | Value |
|---|---|
| Customers at period start | 412 |
| New customers added | 38 |
| Reactivations | 6 |
| Churned (voluntary) | 24 |
| Churned (failed payment / non-renewal) | 9 |
| Customers at period end | 423 |
| Logo churn % | (24 + 9) / 412 = 8.0% |
| MRR at start / end | ₹18.4L / ₹19.1L |
| Gross revenue churn | ₹1.62L / ₹18.4L = 8.8% |
| Expansion (upgrades, seats) | ₹1.05L |
| Net revenue churn | (1.62 - 1.05) / 18.4 = 3.1% |

Two churn numbers, one table. A business that reports only net churn can look healthy while its smallest segment
disappears, because expansion from ten accounts hides the loss of a hundred.

## The cohort matrix

Rows are the month the customer started; columns are months since start; each cell is the percentage of that row
still active.

| Cohort | M0 | M1 | M2 | M3 | M6 | M12 |
|---|---|---|---|---|---|---|
| 2025-11 | 100% | 78% | 71% | 68% | 61% | 54% |
| 2025-12 | 100% | 74% | 66% | 63% | 57% | - |
| 2026-01 | 100% | 71% | 64% | 60% | 55% | - |
| 2026-06 | 100% | 88% | 84% | 82% | - | - |

Read the matrix in three ways:

- **Down a column** is the same age across different signup months - this is the fair comparison, and it is what
  tells you whether the business is getting better at keeping customers.
- **Across a row** is the decay curve for one cohort - this is where the cliff lives, and it is usually M1.
- **The diagonal** is what actually happened in each calendar month - useful for storytelling, useless for
  comparison, because every cell is a different age.

## Reading the curve, not the average

| Shape | What it means | What to do |
|---|---|---|
| Steep M0-M1 drop | Onboarding never reached first value | `onboarding-failure` codes; fix activation, not retention offers |
| Flat then a cliff at renewal | The annual renewal is the real decision point | Work the 90 days before renewal, not the month after |
| Slow constant decay | Product is useful but not essential | Expansion and habit, or accept a shorter lifetime and price for it |
| A plateau after M6 | A stable core exists | Protect the core; the churn is a segment problem |
| Newer cohorts worse than older | Something changed - price, onboarding, mix, quality | Compare by channel and plan before blaming the product |

## Survival and lifetime

- **Median lifetime** is the month in which the cohort falls below 50%. Use the median, not the mean; one
  ten-year contract distorts a mean badly.
- **Average lifetime** for a constant monthly churn rate c is roughly 1/c months. At 4% monthly that is 25
  months - and the approximation breaks for high churn, so do not use it above 10%.
- **LTV** = ARPA × gross margin % × lifetime. State the churn rate used and the period it came from. An LTV
  built on the best quarter's churn is a sales document.

## Segment cuts that earn their keep

Cut by these, in this order, and stop when the table gets too small to read:

1. **Plan or price band** - the cheapest plan usually churns hardest and matters least; check the rupee impact.
2. **Acquisition channel** - marketplace, referral, paid, organic. Channel churn is usually an expectation problem.
3. **Tenure** - first 90 days against later; the fixes are entirely different.
4. **Geography or language** - a support gap shows up here first.
5. **Size of account** - small accounts churn by count, large ones by revenue.

A cut with fewer than 30 customers in a cell is noise. Say so rather than reporting a 50% churn rate on four
customers.

## Anti-patterns

- Reporting churn as "we lost 24 customers" without the base, so a growing business looks like a shrinking one.
- Using net revenue churn as the headline: expansion hides a dying segment.
- Comparing this month's churn to last month's: monthly churn on a small base swings wildly. Compare quarters, or
  use a three-month rolling average.
- Counting a downgrade as churn or an upgrade as a save. They are expansion and contraction, reported separately.
- Cohort matrices with fewer than six cohorts: there is nothing to compare.
- Deleting the customers who left from the base and calling the remainder retention.
