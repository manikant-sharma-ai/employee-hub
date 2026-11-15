# Preparing the history before you forecast it

A model fitted to uncleaned history reproduces the mistakes of the past year. This file cleans the series and
keeps the cleaning reversible.

## The demand series you actually want

Not sales. **Demand** is what customers wanted; sales is what the business managed to deliver. The difference is
the stockout, and it is where forecasts fail.

| Series | What it holds | Use it for |
|---|---|---|
| Invoiced units | What was billed | Reconciliation and revenue |
| Shipped units | What left the warehouse | Demand, when nothing was out of stock |
| Ordered units (including backorders) | What customers asked for | The best available demand proxy |
| Secondary or offtake | What the channel sold onward | True market demand, and rarely available |

State which one was used in the output. A forecast of shipped units when the item was out of stock for six weeks
is a forecast of the business's supply, not of its customers.

## The cleaning checklist, in order

| Step | What to look for | What to do | What to log |
|---|---|---|---|
| 1. Grain and completeness | Missing periods, duplicated rows, mixed SKU codes | Rebuild the calendar, sum duplicates, map old codes to current | The mapping table |
| 2. Returns and cancellations | Negative rows, credit notes | Net them into the period they were sold, not the period returned | The netting rule |
| 3. One-off orders | A single order 10x the normal week | Flag, do not delete; forecast the base, add the known order separately | The order and the reason |
| 4. Stockouts | Zero sales in a normally-selling period | Mark the period and restore an estimate, or model at family level | The stockout dates and the method |
| 5. Price and pack changes | A change in pack size, unit of measure, or price | Convert to a consistent unit; do not compare 500g months to 1kg months | The conversion |
| 6. Structural breaks | A new outlet, a lost distributor, a channel added | Forecast from the break, or model the channels separately | The break date |
| 7. Outliers | A spike with a known cause | Keep, flag, and exclude from the seasonal index only | The cause |
| 8. Trend distortion | A launch ramp inside the history | Use only the post-ramp history, or model the ramp explicitly | The ramp window |

## Handling a stockout, three ways

| Method | When | Cost |
|---|---|---|
| Family-level forecast, allocate down | The SKU is part of a family with full availability | Requires a family with similar behaviour |
| Restore an estimate - average of the surrounding comparable periods | The stockout is short and the season is flat | Slightly smooths a real peak |
| Treat as missing, exclude the period | Long outages, or a series too short to estimate | Breaks the seasonal index; needs a note |

Never do the fourth thing: leave the zero in and let the model learn it. That zero becomes a downward seasonal
index and a permanent under-order in the peak.

## Hierarchy, and where to forecast

Forecast where the signal is. A SKU with 6 units a month has no readable pattern; its family has one.

| Level | Forecast when | Then |
|---|---|---|
| SKU | High volume, stable, long history | Directly |
| Family or category | Low volume per SKU, shared seasonality | Allocate down by recent share, reviewed monthly |
| Channel | Channels behave differently (marketplace vs retail vs B2B) | Forecast by channel and add |
| Region | Regional festivals and climate differ | Forecast by region where data allows |

Top-down, bottom-up and middle-out all work; mixing them without saying which is how the totals stop reconciling.
Pick one, write it down, and make the other levels add up to it.

## Data quality checks that catch most errors

- **Units per period per SKU** plotted - a flat line that suddenly stops is a stockout or a lost channel.
- **Total units against the ledger** for the last twelve months - if they differ by more than rounding, find out
  why before forecasting.
- **SKU count over time** - a jump means new codes were created, and the old series died silently.
- **Price per unit** - an unchanged price across two years is usually a data export problem, not a pricing policy.
- **Seasonality sanity** - does the peak month match what the business remembers? If not, the data is wrong or the
  memory is.

## Minimum history

| History available | What is possible |
|---|---|
| Under 12 months | Naive or moving average; no seasonal index; say so |
| 12-24 months | One full seasonal cycle; a rough index with wide error |
| 24-36 months | A usable index, and enough to hold out a test period |
| 36 months plus | Stable indices, method comparison, per-family models |

Two years is the practical minimum for a seasonal business. A business with eleven months of history does not need
a forecaster; it needs a review date and a naive number.

## Anti-patterns

- Deleting outliers because they make the chart look tidy, then wondering why the plan misses every large order.
- Forecasting at SKU level from three units a month of history, and calling the noise a trend.
- Mixing units, packs and cases in one series.
- Using the invoice date when the dispatch date is the demand date; the lag shows up as a false seasonal shift.
- Cleaning the history without logging it, so nobody can rebuild the original series when the forecast is queried.
- Using a year in which the business was a different business (before a new outlet, before a channel) as if it were
  comparable.
