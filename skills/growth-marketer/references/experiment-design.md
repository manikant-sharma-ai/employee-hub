# Experiment design

An experiment is a bet with a written reason and a stated way to lose. Everything
else is activity with a dashboard attached.

## The brief, in eight lines

```
Hypothesis: <change> will move <metric> from <x> to <y> for <segment>
Because:    <the evidence or mechanism>
Variable:   <the one thing that changes>
Control:    <what stays the same>
Sample:     <n per arm, and how it was calculated>
Duration:   <start, end, and the minimum runtime>
Stop rule:  <when to stop early, in either direction>
Decision:   <what we do if it wins, loses or is inconclusive>
```

The "Because" line is what separates an experiment from a guess. "Because the ad
promises same-day delivery and the page never repeats it" is testable. "Because
blue buttons convert better" is folklore.

## Sample size, without the statistics degree

Rough rules for a two-variant test on a conversion rate:

| Baseline rate | Minimum per arm | What it detects |
|---|---|---|
| 2% | ~8,000 | A doubling (2% to 4%) |
| 5% | ~3,000 | 5% to 6.5% |
| 10% | ~1,500 | 10% to 12% |
| 20% | ~700 | 20% to 24% |
| 40% | ~350 | 40% to 48% |

Read it as: small baseline rates need large samples, and a test you cannot power
is a test you should not run. If traffic is short, change the metric to something
denser - add-to-cart instead of purchase, reply instead of close - or test the
message qualitatively first.

## What can be tested cheaply, in order

| Test | Cost | Signal |
|---|---|---|
| Message on a call or in five customer conversations | Hours | Strong, qualitative |
| Ad copy variant, same audience | Low | Which promise earns the click |
| Landing page headline, same traffic | Low | Which promise survives the click |
| Offer or bundle framing | Low | Which value framing converts |
| Price | Medium, and needs care | Use `pricing-analyst` |
| New channel | Medium | Whether it clears the CAC ceiling |
| New product surface | High | Needs `product-manager` |

## Running it without fooling yourself

- **One variable.** Two changes at once and the result belongs to neither.
- **Run for full weeks.** Weekends and weekdays behave differently; a five-day test measures the weekday.
- **Do not peek and stop.** Checking daily and stopping at the first good day is how noise becomes a strategy.
- **Keep the audience constant.** If targeting changes mid-test, the test is over.
- **Watch for seasonality and stock.** A festive week is not a baseline week; a sold-out variant is not a losing variant.
- **Record the confounders.** A price change, an outage, a festival, a competitor's sale - write them down at the time, not later.

## Reading the result

| Result | Decision |
|---|---|
| Lift above threshold, sample met | Scale, and re-test at the new level |
| Flat, sample met | Kill the idea; write down why it seemed plausible |
| Flat, sample not met | Inconclusive - do not call it a loss, and do not scale |
| Worse, sample met | Kill, and check whether the control itself can be improved |
| Wildly better | Suspect a measurement error before celebrating |

## The experiment log

One row per test: date, hypothesis, spend, sample, result, decision, and the
lesson in one line. Twelve rows is a year of institutional memory, and it stops the
same "blue button" idea returning in eighteen months.

## Anti-patterns

- **Testing without a metric definition.** The same word measured two ways produces two winners.
- **The endless test.** No end date, no sample, no decision - it becomes a permanent excuse.
- **Testing something the business will not implement.** Do not test a price you cannot charge.
- **Concluding from a screenshot.** A single day's dashboard is an anecdote.
- **Calling a loss a "learning"** when the sample was too small to know anything.
