# Methods, holdouts and the error that makes a forecast usable

Pick the method by the shape of the series, and prove it beat the naive one. This file is the discipline.

## The method ladder

| Method | Works when | Fails when | Effort |
|---|---|---|---|
| Naive (same period last year) | Strong seasonality, stable business | Trend changes, new products | None |
| Moving average (3-6 periods) | Flat, noisy series | Seasonality, trend | Low |
| Seasonal naive + trend adjustment | Clear seasonality, modest trend | Volatile demand, short history | Low |
| Exponential smoothing (Holt-Winters) | Level, trend and seasonality all present | Lumpy or intermittent demand | Medium |
| Regression with seasonal dummies and drivers | Known drivers (price, outlets, media) | Drivers that are themselves forecast | Medium |
| Croston or similar for intermittent demand | Many zero periods, spare parts | Steady sellers | Medium |
| Judgemental adjustment on top of any of these | A known event the history cannot see | Used to hide a bad model | Low |

For most small businesses the answer is seasonal naive or Holt-Winters, with a judgemental overlay for known
events. A neural network on 24 monthly points is a way to fit noise and lose trust.

## Classify the series first

| Class | Shape | Method |
|---|---|---|
| Smooth | Low variance, no zeros | Exponential smoothing or moving average |
| Seasonal | Clear repeating shape | Seasonal naive, or Holt-Winters |
| Trend with seasonality | Rising or falling, with a shape | Holt-Winters with damped trend |
| Intermittent | Many zero periods, occasional spikes | Croston-type, or a family-level forecast |
| Lumpy | Intermittent with large spikes | Family level, plus known orders separately |
| New | No history | Analogue, two tranches, early review |

Classify every SKU family and print the class in the output. It explains to the planner why one family has a wide
range and another a narrow one.

## Out-of-sample testing

1. Hold out the last 20% of the history - at least 6 periods, and at least one full seasonal cycle where possible.
2. Fit on the rest, forecast the holdout, compare.
3. Report the error on the holdout, never on the fitted period.
4. Compare against the naive benchmark on the same holdout. If the model does not beat it, use the naive one and
   say so - it is not a failure, it is a finding about how much signal the data holds.

| Metric | Formula | Reads as |
|---|---|---|
| MAPE | mean(|actual − forecast| / actual) | Percentage error; breaks down near zero actuals |
| WMAPE | sum|error| / sum(actual) | The robust choice for low-volume SKUs |
| Bias | sum(forecast − actual) / sum(actual) | Positive means over-forecast, negative under |
| Tracking signal | cumulative error / mean absolute deviation | Persistent sign = a model that has drifted |
| FVA | 1 − (model error / naive error) | Share of the naive error removed; negative means the model is worse |

Use WMAPE for portfolios with many low-volume SKUs, and never report MAPE for a series with zeros.

## Interpreting the error

| Result | Meaning | Action |
|---|---|---|
| MAPE 15-25%, bias near zero | Normal for a retail SKU | Plan against the interval |
| MAPE 40%+, bias near zero | Noisy but unbiased | Family level, wider range |
| Bias −20% consistently | Systematic under-forecast | Check stockouts and the trend; this is the expensive one |
| Bias +20% consistently | Over-forecast | Check the promo history and the lost channel |
| Model worse than naive | The method is adding noise | Use naive, simplify |
| Error rising over three cycles | Something changed | Re-examine the history for a break |

Bias matters more than error in a purchase plan. An unbiased 30% error averages out across SKUs; a 15% under-forecast
on every SKU means a stockout on every SKU in the peak.

## Turning the error into a planning interval

The interval is what the planner holds safety stock against, so it must come from the measured error, not from a
round number.

- If the error is roughly symmetric, use ±1.28 × the standard deviation of the forecast error for an 80% interval,
  and ±1.65 × for 90%.
- For a seasonal SKU, compute the error per season, not across the year: the peak error is larger than the trough
  error, and averaging them hides exactly the risk that matters.
- For intermittent demand, use the empirical distribution of errors rather than a normal assumption.
- State the interval as "80%: 1,200 to 1,600 units" in the output. A planner can use that; "1,400" alone invites a
  purchase order that is wrong half the time.

## Judgemental adjustment, with a leash

- Allowed for: a known large order, a known outlet opening, a known competitor exit, a festival date shift.
- Not allowed for: "sales feel optimistic this year", a target, or a founder's expectation.
- Every adjustment is written as a line: the amount, the reason, who asked, and the date. At the review, the
  adjustment's accuracy is scored separately from the model's - people are usually worse forecasters than the
  model, and the record proves it either way.

## Anti-patterns

- Reporting R² or in-sample fit as accuracy.
- Choosing the method with the lowest error on the same data used to fit it.
- A different method for every SKU, so nobody can explain the total.
- Reporting one MAPE across the whole portfolio, dominated by the largest SKU.
- Ignoring a tracking signal that has pointed the same way for four months.
- Widening the interval until it is meaningless, then calling the forecast safe.
- Adjusting the model's output silently, then blaming the model when the plan misses.
