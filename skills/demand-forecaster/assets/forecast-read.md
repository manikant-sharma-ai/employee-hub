# Demand forecast - <horizon, e.g. Jan-Mar 2027>

Prepared by demand-forecaster. Grain: <SKU-week / family-month>. Horizon: <n periods>. Lead time used: <n weeks>.

## 1. The headline

| Family | Period | Central units | 80% range | Method | Class | Error (WMAPE) | Bias |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

One line: **<what the number means against the same period last year, and the single biggest reason for the
difference>.**

## 2. What changed in the history

| Adjustment | Period | Effect on units | Why | Reversible |
|---|---|---|---|---|
| Stockout restored | | | | Yes - column `adj_stockout` |
| One-off order removed | | | | Yes - kept separately |
| Returns netted | | | | Yes |
| Structural break | | | | No - forecast from the break |

## 3. Seasonality used

| Period | Index | Years of data behind it | Trust |
|---|---|---|---|
| | | | |

Festival dates used: <festival, date, year, source>. Aligned by <weeks relative to the festival / calendar month>.

## 4. Promotions and known events

| Event | Date | Measured uplift | Net of pull-forward | Confidence | Stock must arrive by |
|---|---|---|---|---|---|
| | | | | | |

## 5. Accuracy of the last forecast

| Family | Forecast | Actual | Error % | Bias | Cause of the largest miss |
|---|---|---|---|---|---|
| | | | | | |

Benchmark: naive (same period last year) error <x>% · model error <x>% · FVA <x>%.

## 6. The three assumptions that would change this number

1. <assumption> - if it is wrong, the number moves by <x> units.
2. <assumption>
3. <assumption>

## 7. Handover

| Consumer | What they get | Grain | Action by |
|---|---|---|---|
| inventory-planner | Units + interval for reorder policy | | |
| procurement | Purchase quantity against lead time | | |
| budget-planner | Value by month with range | | |
| finance | Cash timing of the purchase | | |

## 8. What I could not verify

- <secondary sales not available - this is a forecast of channel purchases, not market consumption>
- <stockouts not logged for these SKUs - forecast biased low, advisory only>
- <connector that would close it>
