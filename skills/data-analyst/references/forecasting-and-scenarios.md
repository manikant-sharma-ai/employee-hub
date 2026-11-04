# Forecasting and scenarios

A forecast is a claim about the future with a stated uncertainty. Most business
forecasts are a straight line drawn through hope; the job is to make the
assumption visible so it can be argued with.

## Pick the method from the question

| Question | Method | Note |
|---|---|---|
| "What will next month be?" | Trend + seasonality on 24+ months of history | Needs at least two cycles of season |
| "What if we raise prices 10%?" | Scenario model with an elasticity assumption | State the assumption, do not hide it |
| "How long is the runway?" | Cash bridge: opening + inflows - outflows, week by week | Cash, not profit |
| "When do we hit ₹1 crore ARR?" | Bottom-up: new customers × ARPU × churn | Top-down is a wish |
| "Is this month unusual?" | Compare against the same month last year and the trend band | Not against last month |

## The three-part forecast

1. **Base case** - the trend continuing, with seasonality applied.
2. **Range** - low and high from the historical variance, not from ±10% for symmetry. Say "70% likely between X and Y" only if you actually computed it.
3. **The assumptions list** - five lines maximum, each falsifiable: "renewal rate holds at 88%", "no new hire before March", "the Diwali spike is 1.6x last year".

A forecast without the assumptions list cannot be reviewed, so it cannot be trusted.

## Scenario rules

- **Change one variable at a time**, and show the isolated effect.
- **Distinguish driver from outcome.** Price is a driver; revenue is an outcome. Scenario the drivers.
- **State elasticity explicitly**, and where the number came from. If it is a guess, label it "assumption, unverified".
- **Show the break-even**, not just the outcome: "a 10% price rise works if churn rises less than 4 points".
- **Never present a scenario as a prediction.** "If we do X, we expect Y" is a scenario; "we will do Y" is a promise.

## Cash runway, the one forecast every SMB needs

```
week n closing cash = opening cash + collections - payables - payroll - tax set-aside
```

Rules: use collections, not invoiced revenue; put GST and TDS aside in the week
they fall due; include the one-off costs that are always forgotten (advance tax,
insurance renewal, Diwali bonus). A runway in months is misleading if collections
are lumpy - show weeks.

## Presenting it

- One chart, one table, one sentence: "base ₹42L, range ₹36-48L, and the assumption that matters is renewal rate".
- Show the last forecast against what happened. Track record is what earns the next forecast.

## Anti-patterns

- A single number with no range.
- A hockey stick with no stated driver.
- A forecast built on last month's growth continuing, when last month was a festival.
- Confidence intervals invented for symmetry.
- A runway that ignores tax and payroll dates.
