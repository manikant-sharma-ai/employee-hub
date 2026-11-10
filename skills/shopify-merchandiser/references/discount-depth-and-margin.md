# Discount depth and margin

A discount buys volume with margin. Whether that trade is good is arithmetic, and the
arithmetic is almost never done.

## The break-even lift

```
gross profit per unit before = price - unit cost
gross profit per unit after  = price x (1 - discount) - unit cost
units multiple needed        = gp before / gp after
volume lift required         = multiple - 1
```

`scripts/merch_math.py --demo` prints the table for any price and cost. The shape is
always the same and always a surprise:

| Discount | Margin before | Margin after | Volume lift needed |
|---|---|---|---|
| 10% | 60% | 56% | 20% |
| 20% | 60% | 50% | 50% |
| 30% | 60% | 43% | 100% |
| 40% | 60% | 33% | 200% |
| 50% | 60% | 20% | 500% |

At a 60% gross margin, a 30% discount needs twice the units to stand still. At a 30% gross
margin, a 20% discount needs 200% more. Say the number out loud before the sale is
approved.

## The price reference

The customer remembers the last price they paid and the price they saw most often. A deep
sitewide discount moves both:

- **Downwards**, and it does not come back up. January's full price looks like a markup.
- **Into waiting.** A list trained by four sales a year stops buying at full price.

Protect the reference with offers that do not restate the price:

- **Value-add** - a free gift, extra units, free delivery.
- **Targeted** - a first-order code, a win-back code, a specific segment.
- **Time-boxed** - 48 hours, one collection, one price band.
- **Bundle** - a set price where no single item's price is restated.

## The ladder

Write the year's discount ladder once, with a trigger for each rung:

| Rung | Trigger | Depth | Scope |
|---|---|---|---|
| Clearance | stock cover above 120 days | 30-50% | that SKU only |
| Seasonal | the festival calendar | 15-25% | selected collections |
| New customer | first order | 10% | one use, one person |
| Win-back | no order in 180 days | 15% | targeted |
| Never | - | sitewide 40%+ | nothing |

The "never" row is the most useful line in the document, because it is the decision that
gets made in a panic otherwise.

## India-specific conventions

- **Festival sales are expected.** The shopper waits for them; plan the depth in advance
  rather than matching a competitor on the day.
- **Cash-on-delivery returns** - a discount-led order has a higher RTO rate in many
  categories. Count the return cost in the break-even, not just the unit margin.
- **Marketplace price parity** - if the same SKU is listed on a marketplace at a lower
  price, the store's discount is competing with itself. Coordinate with
  `marketplace-lister` before going deeper.
- **GST is on the discounted price**, so the tax does not cushion the discount.

## Coupon hygiene

- **One code, one purpose.** A code used for three campaigns cannot be measured.
- **Expiry on every code**, and a cap on total redemptions.
- **No code stacking** unless the maths has been run for the stack.
- **Audit the codes quarterly** - the live codes nobody remembers are the ones that get
  scraped onto a coupon site.

## Anti-patterns

- **The discount approved on the revenue it might add**, with no break-even volume.
- **A sitewide sale to hit a monthly number**, which borrows from next month at a cost.
- **Discounting the best seller** instead of the slow mover - the best seller would have
  sold anyway.
- **A permanent "sale" badge**, which is a price cut with extra steps.
- **Matching a competitor's discount** without their cost base.
