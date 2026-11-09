# Listing economics and pricing

A marketplace price is a landed cost plus a fee stack plus a returns provision plus a
margin. Set it in that order and the listing makes money; set it from a competitor's
sticker and the margin is someone else's decision.

## The build-up

```
Landed cost
  + Platform referral or commission (% of selling price)
  + Closing fee (price slab)
  + Shipping or fulfilment fee (weight and zone)
  + Storage or inbound (where applicable)
  + Returns provision (return rate × reverse logistics + damaged stock)
  + GST (on the selling price, collected and remitted)
  + Payment or collection fee
  + Advertising allowance (% of revenue, where ads run)
  = Total cost
Selling price - total cost = contribution
Contribution / selling price = contribution margin
```

Note the circularity: commission is a percentage of the price you are setting. Solve for
price, do not guess:

```
Price = (Landed cost + fixed fees + returns provision + target contribution) / (1 - % fees - GST%)
```

## A worked example

A ₹400 landed-cost product on Amazon.in, 15% referral, ₹25 closing fee, ₹70 shipping,
12% return rate with ₹90 reverse logistics, 18% GST, target 20% contribution:

| Line | ₹ |
|---|---|
| Landed cost | 400 |
| Referral (15% of 899) | 135 |
| Closing fee | 25 |
| Shipping | 70 |
| Returns provision (12% × (90 + 400 × 0.3)) | 25 |
| GST (18% of 899, collected) | 162 |
| **Total cost** | **817** |
| Selling price | 899 |
| Contribution | 82 (9%) |

At ₹899 the margin is 9%, not the 20% the founder assumed. To reach 20% contribution the
price needs to be about ₹1,050 - and the question becomes whether the market bears it,
which is a pricing decision, not a listing one.

## The fee types to model

| Fee | Behaviour | Where it hurts |
|---|---|---|
| Referral or commission | % of price, category-specific | High-ASP, low-margin goods |
| Closing fee | Fixed slab by price | Cheap items - can exceed the margin |
| Shipping | Weight and zone | Bulky, light, or long-zone shipments |
| Storage | Per cubic foot per month | Slow-moving stock |
| Returns and RTO | Per return, plus damaged stock | COD-heavy categories, fashion |
| Collection or payment fee | % of settlement | Everything |
| Advertising | Bid-based, per click | New listings without reviews |

## The break-even price

The price at which contribution is zero. Every listing sheet carries it, because it is the
number that stops a discount from becoming a loss:

```
Break-even price = (Landed cost + fixed fees + returns provision) / (1 - % fees - GST%)
```

A salesperson who does not know the break-even price will find it during a negotiation.

## MRP, selling price and the discount game

- **MRP is a legal declaration**, printed on the pack, inclusive of taxes. It is not a
  marketing number, and inflating it to show a bigger discount is a legal metrology issue.
- **The selling price is the MRP minus the discount**, and the platform shows the discount
  prominently. A permanent 60% discount teaches the buyer to wait for 70%.
- **Price ladder discipline**: decide the floor (break-even plus the minimum contribution),
  the list price, and the maximum discount, in writing, before the first promotion.

## Returns and RTO, modelled honestly

| Category | Typical return or RTO range | Provision |
|---|---|---|
| Fashion and apparel | 20-40% | Highest in the model |
| Footwear | 15-30% | Size mismatch dominates |
| Electronics and appliances | 5-12% | Installation and DOA |
| Beauty and personal care | 3-8% | Leakage and expectation |
| Home and kitchen | 5-10% | Damage in transit |
| Industrial and B2B (IndiaMART) | under 3% | Negotiated, not returned |

Use the category range, not the company average, and revise it quarterly from actual
settlement data. An RTO on COD costs the forward and the reverse freight, and the product
comes back used.

## Multi-platform pricing

| Approach | When it works |
|---|---|
| Same price everywhere | Strong brand, low price sensitivity |
| Different price per platform, from each fee stack | The default, and the honest one |
| Lowest on your own site | Only if the site converts as well; otherwise it cannibalises nothing and costs margin |
| Price-matching a competitor | Only after the break-even is known |

Never let a marketplace undercut your own channel by accident - a D2C customer who finds
the product 20% cheaper on Amazon does not come back.

## The quarterly review

Four numbers per SKU: selling price, contribution, return rate, and the fee change the
platform announced. Platforms change fee slabs; a listing priced last year is priced for
last year's rules.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Price set from a competitor's listing | Margin decided by someone else's cost base |
| Commission ignored in the price | A 15% hole in every sale |
| Returns not provisioned | A profitable-looking listing that loses money in March |
| Inflated MRP to show a discount | Legal metrology exposure |
| Permanent deep discount | The buyer learns to wait, and the full price never sells again |
| Break-even price unknown | Discounts that are losses, approved by someone who did not know |
