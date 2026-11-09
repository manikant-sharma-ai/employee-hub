# Working capital and the purchase plan

Inventory is the largest controllable use of cash in most product businesses. This file
turns a stock policy into a monthly plan the business can actually fund.

## The three numbers

```
Inventory days (DIO)   = average inventory at cost / COGS × 365
Cash conversion cycle  = DIO + DSO - DPO
Inventory turnover     = COGS / average inventory
```

| Metric | Good | Watch | Act |
|---|---|---|---|
| DIO (trading) | 30-45 | 45-60 | above 60 |
| DIO (manufacturing) | 60-90 | 90-120 | above 120 |
| CCC | 20-40 days | 40-60 | above 60 |
| Turns per year | 8-12 (FMCG), 3-6 (durables) | - | Falling two quarters running |

DIO is calculated at cost, never at MRP. At MRP every business looks efficient and none
of them are.

## The cash effect of a stock decision

```
Cash released = units reduced × unit cost
Cash tied up  = units added × unit cost
```

A worked example: cutting cover from 75 to 50 days on a ₹1.2 crore annual COGS line:

```
Daily COGS       = 1,20,00,000 / 365 = ₹32,877
25 days of cover = ₹8.2 lakh released
```

That is the sentence to put in front of a founder who is short of cash: not "reduce
inventory", but "₹8.2 lakh, this quarter, without losing a sale you would have made".

## The purchase plan, by month

| Column | Meaning |
|---|---|
| Opening stock (units and ₹) | From the system, reconciled |
| Forecast sales (units) | Baseline, with the season adjustment stated |
| Target closing stock (units) | From the cover policy per class |
| Gross requirement | Sales + target closing - opening |
| Open orders | Already committed, arriving this month |
| **To order** | Gross requirement - open orders |
| Order value (₹) | Units × landed cost |
| Payment date | Terms applied, not the invoice date |
| Cash available | Bank + collections - committed outflows |
| Gap or surplus | Order value vs cash available |

A plan without the last three rows is a shopping list.

## When the plan exceeds the cash

In this order:

1. **Stage the order** against the supplier's delivery schedule, if they allow it.
2. **Move the class-C tail** to a longer review cycle and a lower service level - it is
   usually 30-50% of the SKU count and under 10% of the value.
3. **Release dead stock first** - the cheapest funding available is the stock already
   paid for.
4. **Negotiate terms, not price** - 45 days instead of 30 is often worth more than a 2%
   discount, and it costs the supplier less than the discount does.
5. **Use the credit line for a working-capital cycle**, not for permanent overstock. A
   line that funds dead stock becomes a term loan with interest.
6. **Cut the buy to the hero SKUs only** and accept the tail stock-out, in writing.

## Terms and the real landed cost

| Term | Effect on cash | Note |
|---|---|---|
| 30 days | Standard | Compare against 45 and 60 |
| Advance 30% | Ties up cash before goods move | Price it into the landed cost |
| LC or BG | Bank cost plus margin | Add the bank charge to the unit cost |
| Consignment | Supplier holds the stock | Best cash position, worst availability |
| MOQ discount | Cheaper unit, more cash, more ageing | The trade is usually a loss |

Landed cost = invoice + freight + duty + clearing + inward freight + bank charges +
insurance. Comparing suppliers on invoice price is how a 6% "saving" becomes a 3% loss.

## The working-capital review, monthly

Four lines, in this order: DIO, DSO, DPO, CCC. Then the two decisions: what stock to
release this month, and what terms to ask for this month. Anything else is commentary.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Cover measured at MRP | The real cash tied up is invisible |
| Purchase plan with no payment dates | The plan and the cash never meet |
| Funding permanent stock with a credit line | Interest on dead stock, forever |
| Chasing the MOQ discount | Cash goes into stock that ages past the saving |
| Cutting inventory by cutting the hero SKU | Sales fall faster than cash is freed |
| DIO reported once a year | By the time it is seen, the season is over |
