# Reorder points and safety stock

Two numbers per SKU decide whether you are out of stock or overstocked: when to order,
and how much to hold against the uncertainty while you wait.

## The two formulas

```
Average daily demand        d  = units sold in the period / days in the period
Lead time (days)            L  = order date to shelf-ready date, observed
Safety stock                SS = z × σd × √L
Reorder point               ROP = d × L + SS
Order quantity              Q  = economic or MOQ-constrained (see below)
```

Where σd is the standard deviation of daily demand over the lookback, and z comes from
the service level:

| Service level | z | Meaning |
|---|---|---|
| 90% | 1.28 | One cycle in ten runs short |
| 95% | 1.65 | One in twenty |
| 97.5% | 1.96 | One in forty |
| 98% | 2.05 | One in fifty |
| 99% | 2.33 | One in a hundred - usually 25-40% more stock than 95% |

Use σ over the same lookback as the demand average, and use *daily* variability, not
monthly - monthly smoothing hides the spikes that cause the stock-out.

## Worked example

A ₹1,200-cost SKU, 21-day lead time, selling 40 units a day on average.

| Input | Value |
|---|---|
| d | 40 units/day |
| σd (daily) | 14 units |
| L | 21 days, observed 18-29 |
| Service level (A-class) | 98% → z = 2.05 |

```
SS  = 2.05 × 14 × √21 = 2.05 × 14 × 4.58 = 131 units
ROP = 40 × 21 + 131 = 971 units
```

At ₹1,200 cost, the safety stock is ₹1.57 lakh of working capital. That is the price of
98% service on this SKU - say it in the output, because someone will ask whether 95% is
enough, and at 95% it is 106 units and ₹1.27 lakh.

## When lead time varies

If the supplier's lead time moves more than demand does, use the combined formula:

```
SS = z × √( L × σd²  +  d² × σL² )
```

σL is the standard deviation of lead time in days. For imports, this term usually
dominates - a 12-day swing on a 40-unit day is 480 units of exposure that demand
variability never predicts.

## Lead time, measured honestly

| Component | Ask for | Plan with |
|---|---|---|
| Supplier order-to-dispatch | Their promise | Their last six actual dispatches |
| Transit | The forwarder's estimate | The observed range, P90 not average |
| Inward QC and put-away | Your own record | Your worst month |
| Payment or credit hold | Finance | Add it if a PO waits for funds |

A supplier who says 21 days and delivers in 21 to 45 is a 45-day supplier for planning.
Using 21 is how a business runs out every quarter and blames the supplier.

## Order quantity, with the real constraints

Economic order quantity is a starting point, not an answer:

```
EOQ = √( 2 × annual demand × order cost / holding cost per unit per year )
```

Then apply, in this order:

1. **MOQ** - if EOQ is below the minimum, either order the MOQ (and accept the cover) or
   find a second supplier who breaks the pack.
2. **Pack size** - round up to the case, never down.
3. **Price breaks** - a 4% discount on double the quantity is a 4% margin gain and a 100%
   increase in inventory days. Show both numbers; do not decide it silently.
4. **Shelf life and obsolescence** - never order more than 60-70% of the remaining shelf
   life at expected sell-through.
5. **Cash** - if the order exceeds the available cash or the credit line, the plan is
   staged, not abandoned.

## Review cycle by class

| Class | Review | Count | Why |
|---|---|---|---|
| A | Weekly | Monthly cycle count | The money is here |
| B | Fortnightly | Quarterly | Stable enough to watch |
| C | Monthly | Half-yearly | Policy, not attention |

## The stock-out you cannot afford

Name two or three SKUs in writing where a stock-out is unacceptable - the hero product,
the one that anchors the bundle, the one a key account orders monthly. For those, hold
the next service level up and say what it costs. Everything else buys the class policy.

## Anti-patterns

| Anti-pattern | Consequence |
|---|---|
| Reorder point below MOQ | The system orders every week and never reaches the point |
| Safety stock on monthly averages | Spikes are smoothed away and the stock-out is a surprise |
| 99% service on every SKU | 30% more inventory for a fraction of the sales |
| One lead time for all suppliers | The slow supplier's SKU is always short |
| Ordering to the price break | Cash goes into stock that will age |
| Never reviewing the policy | Demand doubled and the ROP did not move |
