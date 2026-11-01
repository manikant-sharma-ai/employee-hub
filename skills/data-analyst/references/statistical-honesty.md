# Statistical honesty

Small samples, seasonal businesses and selective memory produce most of the confident wrong numbers in a company. This file is the set of checks that stop you adding to them.

## The sample size reality

| n | What you can say |
|---|---|
| 1-5 | Anecdote. Useful for hypothesis generation only. Never a rate |
| 6-20 | Direction, if the effect is large and consistent. No percentages in a headline |
| 20-100 | Usable rates with wide error. Always show n |
| 100-1,000 | Reasonable rates for a single segment. Beware splitting further |
| 1,000+ | Rates are stable; the risk moves to definition and bias |

Rule: **if a segment has fewer than 30 rows, report the count, not the percentage.** "3 of 4 customers churned" is honest. "75% churn in that segment" is a headline someone will act on.

## The base-rate trap

A test that is 99% accurate, applied to 1,000 people where 1% have the condition, produces 10 true positives and about 10 false positives. Half the positives are wrong.

In business terms: a churn-prediction model that is "95% accurate" on a base churn rate of 4% is mostly flagging people who were going to stay. Always ask: **what is the base rate, and what does the model add over just knowing it?**

## Correlation, cause, and the third variable

When two things move together, there are four possibilities and you must say which you believe and why:

1. **A causes B.** Needs a mechanism and, ideally, a test.
2. **B causes A.** Often more likely than it looks - e.g. support contact and churn: unhappy customers contact support, support does not cause churn.
3. **C causes both.** Seasonality, a promotion, a price change, a new competitor, a data-collection change.
4. **Coincidence.** With enough pairs of metrics, some will correlate.

The tell for a confounder: the relationship appears across the whole business at once. A festival, a price change, a courier change or an accounting change usually explains it.

**What establishes cause:** a controlled test, a natural experiment (one city changed, others did not), or a plausible mechanism plus a dose-response. What does not: a scatter plot, a regression with 12 rows, or a strong feeling.

## Simpson's paradox

An aggregate trend can reverse inside every subgroup. The classic business case: overall conversion falls while every channel's conversion rises, because spend shifted to a low-converting channel.

Check: **does the conclusion hold in every major segment?** If it reverses in one, that reversal is the story.

## Seasonality and comparison windows

- **Compare year on year for anything seasonal.** Indian retail, education, agriculture, travel and B2B all have strong annual cycles.
- **Compare like-for-like days.** A 28-day February against a 31-day March is not growth.
- **A festival month is not a month.** Diwali moves between October and November, which wrecks naive comparisons.
- **Distinguish a level shift from a spike.** A spike returns; a level shift does not. Three months of the new level is evidence; one is not.

## Regression and forecasting, used honestly

- **Never fit a trend to fewer than 12 points** and present it as a forecast. With 6 points you can fit a line to anything.
- **Report the range, not the point.** "₹42-51 lakh next quarter" is a forecast; "₹46.3 lakh" is a guess wearing a suit.
- **State the assumptions** - no price change, no new competitor, normal monsoon, festival timing.
- **Backtest.** If the model would have predicted the last three months badly, do not use it.
- **A forecast exists to be revised.** Say when you will revise it and on what evidence.

## The checks before you report

```
[ ] n is stated next to every rate
[ ] The base rate is known and stated where relevant
[ ] The comparison is like-for-like (period, definition, population)
[ ] The direction holds in the major segments, or the reversal is reported
[ ] Confounders named: seasonality, price change, promotion, system change
[ ] Any forecast has a range and stated assumptions
[ ] Numbers reconcile to the source total
[ ] The difference between "moved together" and "caused" is respected in the wording
```

## Language that keeps you honest

| Instead of | Write |
|---|---|
| "X causes churn" | "Churn is 3x higher among X; we do not yet know why" |
| "Conversion improved" | "Conversion rose from 2.1% to 2.4% (n=1,840), within the same channel mix" |
| "Customers love the new design" | "4 of 6 interviewed preferred it; no quantitative test yet" |
| "Sales will be ₹50 lakh" | "Sales will be ₹42-51 lakh if the current run rate holds and no new discount is run" |
| "The data shows" | "The data is consistent with" |

## Anti-patterns

- A percentage computed on nine rows, in a slide with no n.
- Presenting a segment that happens to support the recommendation, out of twenty segments tested.
- Comparing a peak month to a trough month to show growth.
- Fitting a straight line through a seasonal series and calling the gap a shortfall.
- Reporting a correlation as a cause because the mechanism "makes sense".
- Silently dropping the outlier that ruins the story.
- Reporting a 3-month trend as a strategy outcome.
- Using a benchmark from a different market or business model as the target.
