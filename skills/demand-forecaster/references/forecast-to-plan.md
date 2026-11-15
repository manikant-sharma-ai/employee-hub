# From forecast to plan: the handover and the review

A forecast that does not change an order, a rota or a cash plan is a spreadsheet. This file makes it an input.

## What each consumer needs

| Consumer | What they need from the forecast | Grain | What they do with it |
|---|---|---|---|
| `inventory-planner` | Units by SKU by period, with the error | SKU-week or SKU-month | Reorder point, safety stock, purchase quantity |
| `procurement` | The purchase quantity and the lead time it must fit | SKU, by order cycle | Quote, negotiate, place |
| `budget-planner` | Value by month, with the range | Family-month | Revenue and cash plan |
| Production or `manufacturing-planner` | Units by period and the capacity implication | SKU or family-week | Schedule, shifts, capacity |
| Staffing or store ops | Peak volumes by week | Category-week | Rota, stock on the floor |
| Finance | The cash timing of the purchase | Month | Working capital, credit line |

Each consumer gets the same number in their own grain, and the same assumptions line. If two consumers are given
different numbers from different files, the forecast has failed regardless of its accuracy.

## The one-page output

`assets/forecast-read.md` is the template. It carries the number, the range, the method, the error, the
assumptions and the dates - and it fits on a page, because a planner reads it at 9am with a purchase order open.

## The monthly cycle

| When | What happens | Who |
|---|---|---|
| Week 1 | Last month's actuals land; the forecast is scored | Forecaster |
| Week 1 | The accuracy review: MAPE, bias, the two biggest misses and why | Forecaster + planner |
| Week 2 | The forecast is refreshed for the next horizon, adjustments logged | Forecaster |
| Week 2 | Purchase quantities are computed against lead time and policy | Inventory planner |
| Week 3 | The purchase plan and the cash implication are reviewed together | Founder + finance |
| Week 4 | The next month's promo and event plan is confirmed and fed back in | Marketing + forecaster |

That cycle is the whole of sales and operations planning for a small business. It does not need software; it needs
four dates and one page.

## The accuracy review, in twenty minutes

1. Print the forecast against actual, by family, for the period that closed.
2. Mark every miss above 25% and ask one question of each: was it the model, a known event, a stockout, or a
   change in the business?
3. Score the judgemental adjustments separately - did the human overlay help or hurt?
4. Record one change for next month: a method, an index, a data fix.
5. Write it in the journal. Three misses with the same cause is a rule, not an incident.

## Thresholds that make the forecast safe to use

Write these in `notes/decisions.md` and hold to them:

| Threshold | Meaning | Consequence |
|---|---|---|
| Bias beyond ±10% for two cycles | The model is systematically wrong | Do not use for ordering until corrected |
| MAPE beyond 40% on a family with history | The signal is too weak at this grain | Forecast at family level or use the naive benchmark |
| Model worse than naive for two cycles | The method is adding noise | Switch to naive and say so |
| No stockout record available | The history is censored | Forecast is advisory only, never an ordering basis |
| Under 12 months of history | No seasonality can be measured | Naive only, with a review date |

## Communicating the number

| Audience | Say | Do not say |
|---|---|---|
| Buyer placing an order | "1,400 units for October, 80% range 1,200-1,600, method seasonal, error 18%" | "About 1,400" |
| Founder | "October is the peak; we are forecasting 1,400 against 1,050 last October, mostly the outlet we added in June" | "Demand is up 33%" |
| Finance | "The purchase for October is ₹42 lakh, and it lands in September's cash" | "Stock will be higher" |
| Sales team | "The forecast is 1,400; your target is a separate number" | Anything that mixes the two |

The last line matters. A forecast that is quietly the target is not a forecast, and everyone in the room knows it.

## Anti-patterns

- A forecast delivered as a spreadsheet with 60 tabs and no summary.
- Three functions using three versions of the number.
- A forecast never scored, so its accuracy is a matter of opinion.
- A purchase plan built on the point forecast with no interval, then a stockout blamed on "unexpected demand".
- A monthly cycle that skips the accuracy review in a busy month - which is exactly the month it was needed.
- Reporting the forecast only when it is good.
- Feeding the target back into the model as demand.
