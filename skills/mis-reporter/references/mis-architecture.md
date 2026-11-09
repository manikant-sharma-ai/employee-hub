# MIS architecture

One page. If it needs scrolling on a laptop, it is a dashboard and nobody will read it
on a Monday morning.

## The page, top to bottom

| Band | Content | Job |
|---|---|---|
| Header | Period, as-of date, plan version, prepared by | Removes the first three questions |
| Row 1 - outcome | Revenue, contribution or gross margin, EBITDA | Are we winning or losing |
| Row 2 - drivers | Volume, price or realisation, conversion, utilisation | Why the outcome moved |
| Row 3 - cash and risk | Cash, receivables or DSO, stock cover, pipeline coverage | What can hurt us next |
| Variance block | The three largest gaps against plan, with rupee effect | Where the plan broke |
| Commentary | Three sentences per movement | The why, in the reader's language |
| Decision line | The one action, owner, date | The page's purpose |
| Footer | Data quality: source, as-of, provisional, missing | Whether to trust the page |

## The KPI tree

Every number on the page must sit in a tree, or it is decoration.

```
Revenue
├── Volume (units, orders, hours, seats)
├── Realisation (price per unit, net of discount and returns)
└── Mix (share of high-margin line)
Contribution = Revenue - variable cost
├── Gross margin %
└── Cost per unit
Cash
├── Collections (DSO, overdue %)
├── Inventory (cover days)
└── Committed outflows (next 60 days)
```

A driver that no one can move is not a driver. "Market demand" belongs in the
commentary, not in row 2.

## The columns

| Column | Rule |
|---|---|
| Plan | From the approved budget for that period, not a re-forecast |
| Actual | From the system, reconciled |
| Last period | Same metric, same definition, prior period |
| Run rate | Actual divided by days elapsed, times days in the period - only for the current period |
| Variance ₹ | Actual minus plan, in rupees or lakh |
| Variance % | Only where the base is not near zero |
| Signal | Red, amber, green - only where a written threshold exists |

Traffic lights without thresholds are mood. Write the threshold next to the metric in
the definitions sheet: "DSO red above 60, amber 50-60".

## Page budget

| Business size | Numbers | Commentary | Total |
|---|---|---|---|
| Under ₹5 crore revenue | 6-8 | 3 lines | 1 page |
| ₹5-50 crore | 8-12 | 6 lines | 1 page, 2 with annexure |
| Above ₹50 crore | 12-15, by function | 10 lines | 2 pages, functional annexures |

## Variants from one source

| Reader | Difference |
|---|---|
| Founder and leadership | Everything, including the number not to quote outside |
| Department heads | Their function in full, the rest as two lines |
| Board | Plan vs actual, cash, risk, three drivers; no operational detail |
| Lender | Revenue, EBITDA, debt service cover, receivables ageing, stock; monthly, fixed format |
| Investor | Revenue, growth, burn, runway, the two operating metrics agreed with them |

One workbook, one set of formulas, one definitions sheet. Variants are views of the same
cells - never a second spreadsheet, because the second spreadsheet is where the numbers
start to disagree.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| 40 metrics, no plan column | Cut to eight; add plan |
| A different layout each month | Freeze the template for a quarter |
| Percentages with no rupee figure | Rupee first, percent second |
| Commentary that restates the table | Commentary explains; it never repeats |
| The page sent on a different day each week | Fix the day; a late page is a page that stops being read |
| A second spreadsheet for the board | Variants of one workbook |
| Numbers typed in from a WhatsApp message | Every cell traced to a system or marked as an estimate |
