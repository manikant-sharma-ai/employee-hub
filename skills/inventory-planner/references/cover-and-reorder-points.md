# Cover and reorder points

The whole method is five lines of arithmetic. Written down, it ends the argument;
left implicit, it produces a different answer from every person who touches it.

## The definitions

```
position         = on_hand + on_order
cover_days       = position / avg_daily_sales
reorder_point    = avg_daily_sales * (lead_time_days + safety_days)
order_up_to      = avg_daily_sales * (lead_time_days + safety_days + review_days)
order_quantity   = max(0, ceil(order_up_to - position))    when position <= reorder_point
```

`scripts/reorder_plan.py` implements exactly this. Change the formula in one place,
not in the spreadsheet, and re-baseline the plan when you do.

## Reading cover

| Cover in days | Meaning | Action |
|---|---|---|
| Under lead time | Will stock out before a new order can arrive | Order today, expedite if the SKU is A |
| Under lead time + safety | At risk in a normal month | Order now, at the reorder point |
| Lead time + safety to 2x that | Healthy | Hold |
| 2x to 4x | Overstocked for the velocity | Stop ordering, watch the promotion calendar |
| Over 4x, or no sales at all | Capital tied up | Dead-stock decision |

Cover is a ratio, so it is only meaningful with a velocity. A SKU selling 0.2 a day
and one selling 20 a day can both show 60 days cover, and only one of them is a
problem in cash terms.

## The review cycle matters as much as the reorder point

A reorder point with a weekly review means the order is placed up to seven days
after the point is crossed. The order quantity must cover that review window, which
is why `order_up_to` includes `review_days`. Monthly review on a fast-moving SKU is
how a business stocks out with a correct reorder point.

## ABC planning

Rank SKUs by revenue over the period, cumulatively:

- **A items** - the first ~80% of revenue, usually 15-25% of SKUs. Plan tightly: weekly review, per-SKU reorder points, safety stock sized to protect revenue.
- **B items** - the next ~15%. Monthly review, per-SKU or by family.
- **C items** - the last ~5%, usually more than half the catalogue. Fixed-cycle ordering, generous safety days, and a standing decision on whether to keep them at all.

The C tail is where the working capital hides. Half the SKUs, 5% of revenue, and
often a third of the stock value.

## Worked example

SKU A-100: on hand 60, on order 0, selling 6 a day, lead time 10 days, safety 7
days, review 7 days.

```
position       = 60
cover_days     = 60 / 6 = 10 days          -> under lead time + safety (17) -> act
reorder_point  = 6 * (10 + 7) = 102        -> position is below it
order_up_to    = 6 * (10 + 7 + 7) = 144
order_quantity = 144 - 60 = 84             -> round up to MOQ / pack size
```

If the MOQ is 100 and the pack size is 20, the answer is 100. Saying "84" and
leaving the buyer to discover the MOQ is not a plan.
