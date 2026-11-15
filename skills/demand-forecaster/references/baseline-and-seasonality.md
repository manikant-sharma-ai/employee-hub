# Baseline, trend and seasonality

The baseline is what would sell in an average month. Seasonality is how each month differs from it. Both are
measured from this business's own data.

## Decomposing the series

| Component | What it is | How it is read |
|---|---|---|
| Level | The current average | The anchor for the forecast |
| Trend | The direction and rate of change | Growth, decline, or flat - and whether it is real |
| Seasonality | The repeating shape within the year | The index that moves the plan |
| Residual | What none of the above explains | Where the promos, one-offs and errors live |

A simple decomposition is enough for most businesses: a centred 12-month moving average for the trend, the ratio
of actual to trend for the seasonal index, and the residual examined for known events. State the method used and
the years covered.

## The seasonal index

1. For each period, divide actual by the centred moving average of the same period. That ratio is the raw index.
2. Average the ratios for the same calendar month across years. With two years, that is an average of two
   numbers and the error is wide - say so.
3. Normalise so the index averages 1.0 across the year. A month at 1.35 sells 35% above the average month.
4. Check the index against the business's memory. A peak in a month nobody remembers being busy means the data or
   the mapping is wrong.

| Month | Year 1 ratio | Year 2 ratio | Index | Trust |
|---|---|---|---|---|
| Jan | 0.82 | 0.79 | 0.80 | High - consistent |
| Feb | 0.74 | 0.81 | 0.78 | Medium |
| Sep | 1.41 | 2.10 | 1.75 | Low - the festival moved |
| Oct | 2.20 | 1.52 | 1.86 | Low - same cause |
| Nov | 1.15 | 1.90 | 1.52 | Low - same cause |

The Sep-Nov row is the most important line in this file: **a festival that moves between years destroys a
calendar-month index** unless the history is aligned to the festival, not to the month.

## Aligning the festival calendar

Diwali, Eid, Pongal, Onam, Durga Puja, Ganesh Chaturthi, Rath Yatra and most of the retail calendar follow lunar or
regional calendars and move each year - by up to a fortnight or more, and occasionally into a different month.

| Step | Do this |
|---|---|
| 1 | Get the actual date for each year in the history from a panchang or the official holiday list, and write the source |
| 2 | Mark each year's festival week and the two weeks before it (the stocking window) |
| 3 | Build the index on **weeks relative to the festival**, not on calendar months: week -4, -3, -2, -1, festival, +1 |
| 4 | For the forecast year, take that year's date and convert the relative index back into calendar weeks |
| 5 | Where the festival falls near a month boundary, split the demand across the two months in the ratio the history shows |

A business that sells through distributors stocks earlier than one that sells direct - the distributor's order
lands three to six weeks before the retail peak. Two peaks, one cause. Model both.

## The Indian seasonal shape, by trade

Use this to sanity-check the index, never to replace it.

| Trade | Typical peak | Typical trough | Watch out for |
|---|---|---|---|
| Apparel and gifting | Sep-Nov (festive), Jan-Feb (weddings) | Jun-Aug | Festival shift; wedding dates vary by region and year |
| Consumer electronics | Sep-Nov (festive sales), Mar (year-end offers) | Jun-Jul | Marketplace sale events are announced, not seasonal |
| Building material and hardware | Oct-Mar (construction season), post-monsoon | Jul-Sep (monsoon) | Regional monsoon differences |
| Agri inputs | Kharif (Jun-Jul) and Rabi (Oct-Nov) sowing | Between seasons | Rainfall and mandi prices dominate |
| Food and staples | Steady, with festive spikes | - | Perishable SKUs need weekly grain, not monthly |
| B2B industrial | Jan-Mar (budget flush), Oct-Nov | Apr-Jun | Buyer's financial year drives it, not yours |
| Education | Apr-Jun (admissions) | Nov-Dec | State board calendars differ |

## Trend: real or artefact

| Pattern | Likely cause | Check |
|---|---|---|
| Steady growth | More customers, more outlets, price rises | Compare units and value separately; a price rise is not volume growth |
| Growth that stops | Channel saturation, stockouts, a lost account | Split by channel before concluding |
| Decline | Losing a channel, a competitor, a product ageing | Check the biggest accounts and the stockout record |
| Step change | A new outlet, a new channel, a lost distributor | Find the date and forecast from it |
| Flat with rising value | Price increases | Forecast units, report rupees |

Do not extrapolate a trend beyond the horizon where the cause is understood. A 12% annual growth trend from a
single new outlet is not a growth trend; it is a step.

## New products and no history

| Situation | Method | Error to expect |
|---|---|---|
| New SKU in an existing family | Family forecast × expected share, then adjust | Wide - state the range |
| New SKU in a new category | An analogue: a similar product launched before | Wider - one scenario plus a range |
| A relaunch | The pre-discontinuation series, discounted for the gap | Medium |
| A seasonal first year | The category index applied to a conservative base | Very wide - order in two tranches |

## Anti-patterns

- A "Diwali is 2.5x" rule in a spreadsheet cell, unchanged for four years, in a business where the festival moved.
- Building the index from one year, then reporting it to two decimal places.
- Using calendar months for a business that plans in weeks during the festive quarter.
- Ignoring the distributor's earlier stocking peak, and being out of stock in the retail peak.
- Applying a national festive index to a regional trade where the local festival dominates.
- Reporting the trend from a period that includes a one-off order.
