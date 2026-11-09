# Reorder policy - <category> - <date>

Prepared by <name> | Sales history: <period> | Service level basis: <class policy>

## The policy in one table

| SKU | Class | Avg daily demand | Demand σ | Lead time (days, P90) | Service level | Safety stock | Reorder point | Order qty | MOQ | Review |
|---|---|---|---|---|---|---|---|---|---|---|
| <SKU-1> | A / X | 40 | 14 | 21 | 98% | 131 | 971 | 1,200 | 500 | Weekly |
| <SKU-2> | B / Y | 12 | 6 | 14 | 95% | 39 | 207 | 400 | 200 | Fortnightly |
| <SKU-3> | C / Z | 1.4 | 2.1 | 30 | 90% | 14 | 56 | 60 | 60 | Monthly |

## What each class gets

| Class | Service level | Review | Count | Buffer rule |
|---|---|---|---|---|
| A | 97-98% | Weekly | Monthly | Computed per SKU |
| B | 95% | Fortnightly | Quarterly | Class default |
| C | 90% | Monthly | Half-yearly | Min-max, automated |

## This week's actions

| Action | SKU | Qty | Value ₹ | Order by | Why |
|---|---|---|---|---|---|
| Order | <SKU-1> | 1,200 | <14.4 lakh> | <date> | Cover at 11 days, below ROP |
| Stop ordering | <SKU-4> | - | - | - | 210 days cover |
| Liquidate | <SKU-7> | 340 | <1.6 lakh at cost> | <date> | Dormant 14 months, rung 3 |

## The cash effect

| Item | Now | After this policy | Change ₹ |
|---|---|---|---|
| Inventory at cost | | | |
| Inventory days (DIO) | | | |
| Cash tied up | | | |

## Service level, and its price

| SKU or class | At 95% | At 98% | Chosen | Cost of the step up |
|---|---|---|---|---|
| <A-class> | | | 98% | <₹x lakh of extra stock> |

## Open assumptions

- <Lead times are the supplier's promise, not observed; confirm with the last six POs.>
- <Sales history covers 9 months, not 12; the seasonal SKU is classified on 9 months.>
- <Cash available is from the founder, not from the bank feed.>
