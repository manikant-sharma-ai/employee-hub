# Margin and unit economics

Every pricing argument ends in one table: what comes in, what goes out, and what is left per unit. Build it bottom-up or the answer is a guess with a decimal point.

## The table, per unit or per order

| Line | What it is | Common error |
|---|---|---|
| Gross price | What the customer is quoted | Quoting inclusive and modelling as if it were revenue |
| Discount | Trade, coupon, scheme | Forgetting that the discount also reduces the GST you collect |
| Net price | Gross less discount | |
| GST | 5/12/18% depending on the item - a pass-through | Treating collected GST as revenue |
| Net revenue | Net price / (1 + GST rate) | Using the inclusive number |
| COGS | Materials, bought-in components | Using the last purchase price when it has moved |
| Packaging | Box, filler, label, insert | Ignored because it is small - it is 3-8% in D2C |
| Freight out | Forward shipping | Ignored, or modelled as free because the customer paid |
| Freight back | Returns, at the return rate | The single most under-modelled cost in D2C |
| Payment fee | 1.5-3% gateway, UPI often lower | Applied to net revenue instead of gross |
| Marketplace commission | 8-25% plus fulfilment | Ignored when the same SKU also sells D2C |
| Returns allowance | Rate × (COGS + freight both ways + refurb) | Modelled as a percentage of revenue |
| Contribution | Net revenue less all variable cost | Confused with gross margin |
| Fixed cost | Rent, salaries, tools | Wrongly allocated per unit at low volume |
| Break-even units | Fixed cost / contribution per unit | Computed with a contribution that includes fixed cost |

## The arithmetic worth memorising

- **Contribution per unit** = net revenue − all variable cost.
- **Contribution margin %** = contribution / net revenue. Above 40% is healthy for D2C; below 25% leaves nothing for acquisition.
- **Break-even units** = fixed cost / contribution per unit.
- **Break-even revenue** = break-even units × net price.
- **Price floor** = the price at which contribution is zero. Below it, every extra sale increases the loss.
- **CAC payback** = CAC / contribution per order, in months for a subscription, in orders for a one-off.
- **Discount break-even uplift** = 1/(1 − d) − 1. A 10% discount needs 11.1% more volume to stand still, and more once variable cost is in the model.

## Why discounts hurt more than they look

On a product with 30% contribution margin, a 10% discount removes a third of the contribution. The volume needed to recover it:

| Discount | Contribution before | Contribution after | Volume uplift needed |
|---|---|---|---|
| 5% | 30% | 25% | +20% |
| 10% | 30% | 20% | +50% |
| 15% | 30% | 15% | +100% |
| 20% | 30% | 10% | +200% |

That table is the whole argument against discounting to win a deal, and it is arithmetic, not opinion.

## Fixed versus variable, honestly

At low volume, spreading fixed cost per unit produces a scary number that stops a good decision. At high volume it produces a comfortable number that hides a bad one. Show both: contribution per unit, and the fixed cost that has to be covered each month.

## Channels change the margin

The same product at the same price has three different margins:

| Channel | Fee load | Net contribution |
|---|---|---|
| Own site, prepaid | 2% gateway + freight | Highest |
| Own site, COD | 2% + RTO risk 8-20% | Lower than it looks |
| Marketplace | 15-25% + fulfilment + ads | Often below the floor |
| Distributor | 20-35% trade margin | Volume, but a different business |

Model each separately. A blended margin hides the channel that is losing money.

## Anti-patterns

- Gross margin quoted as "60%" when it is markup on cost.
- Ignoring returns and RTO in a COD-heavy Indian business.
- Allocating fixed cost per unit at the current volume and calling it unit economics.
- Comparing a D2C price to a marketplace price without the fee load.
- Modelling GST as revenue.
- A break-even computed once and never updated when costs moved.
