# Variance and reforecast

A variance report that says "12% over" is an alarm. One that says which line, which month and
whether it will repeat is a decision.

## The monthly review, in one page

| Line | Plan | Actual | Var ₹ | Var % | Timing or structural | Cause | Owner | Action |
|---|---|---|---|---|---|---|---|---|
| Revenue | 42.0L | 38.6L | -3.4L | -8% | Timing | Two POs slipped to next month | Sales | Confirm dates |
| Gross margin | 38% | 33% | -5pp | -13% | Structural | Freight moved to air for festive | Ops | Renegotiate rate card |
| People | 9.8L | 9.8L | 0 | 0% | - | - | - | - |
| Selling | 4.2L | 5.9L | +1.7L | +40% | Structural | Ad spend scaled early | Growth | Re-set budget |

Two rules: every line gets a **timing or structural** verdict, and every structural line gets
an **owner and an action**. Timing lines do not trigger a reforecast; structural ones do.

## Decompose before you explain

Revenue variance splits into four causes that need four different responses:

```
Price effect   = (actual price - plan price) x actual units
Volume effect  = (actual units - plan units) x plan price
Mix effect     = shift between products at different margins
One-off        = a single order, a cancelled order, a stock-out
```

| Cause | Response |
|---|---|
| Price | A discounting habit or a price change - `pricing-analyst` |
| Volume | Demand, stock-out, listing, sales capacity |
| Mix | Merchandising or sales targeting, and it moves margin more than revenue |
| One-off | Exclude from the run rate, or the next plan inherits a spike |

Cost variance splits the same way: **rate** (price per unit paid), **quantity** (used more),
**timing** (paid early or late), **scope** (something new was bought).

## Reforecast triggers

Do not reforecast monthly by habit - it becomes a ritual nobody trusts. Reforecast when one
of these fires:

| Trigger | Threshold (set at approval) |
|---|---|
| Revenue run rate | Off plan by more than 10% for two consecutive months |
| Gross margin | Moves more than 3 percentage points for two months |
| Cash low point | Falls below 1.5 months of fixed cost |
| A committed cost changes | Rent reset, loan reset, a hire brought forward |
| A plan assumption is falsified | A launch date, a price, a channel |
| A structural variance | Any line that is structural and above 5% of that head |

Each trigger has a named person who decides, and a reforecast takes one page: what changed,
what it does to the year, what it does to cash, and what decision is needed.

## The rolling forecast

From month three onward, keep a **rolling 12-month** view beside the annual plan:

| | Plan year | Actual YTD | Forecast rest | Full-year forecast | vs plan |
|---|---|---|---|---|---|
| Revenue | 5.00 Cr | 1.62 Cr | 3.30 Cr | 4.92 Cr | -1.6% |

The rolling view is what stops the December panic: by September the year is 75% known, and the
remaining quarter is a much smaller guess.

## Forecast accuracy is the scorecard

Measure it, or nobody learns:

| Metric | Formula | Target |
|---|---|---|
| Revenue forecast error | \|forecast - actual\| ÷ actual | < 10% at 3 months out |
| Cost forecast error | Same, on total cost | < 5% - cost is more controllable |
| Cash low-point error | \|forecast low - actual low\| | < 1 month of fixed cost |
| Reforecast count | Number per year | 2-4; more means the plan was a guess |

Write the error into `notes/learnings.md` with the cause. A forecast that is always 15% high is
not bad luck - it is an optimistic bias, and it is correctable.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Variance without a cause | The review becomes an argument about the number |
| Timing called structural | A permanent cost cut is made for a temporary problem |
| Structural called timing | A real problem gets three more months of runway |
| Reforecast every month | The plan loses authority; everyone waits for the next version |
| Never reforecast | The plan is fiction by September and decisions are made without one |
| One-line "other expenses" variance | The cause is buried in the line nobody split |
| Accuracy never measured | The same optimistic bias recurs every year |
