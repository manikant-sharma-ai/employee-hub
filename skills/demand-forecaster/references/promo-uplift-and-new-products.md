# Promotions, price changes and new products

Most "uplift" in a small business is measured wrongly, in the flattering direction. This file measures the part
that is real.

## The three effects of a promotion

| Effect | What it is | Where it goes |
|---|---|---|
| Increment | Sales that would not have happened | Real uplift |
| Pull-forward | Sales brought earlier from the following weeks | Not uplift - a timing shift |
| Cannibalisation | Sales taken from another SKU of yours | Not uplift - a mix shift |
| Post-promo dip | The trough after the pull-forward | The cost of the promotion |

The honest read subtracts all three. A promotion that lifts 40% for a week and leaves a 25% hole the following
fortnight has lifted very little.

## Measuring it, step by step

1. **Define the baseline** for the promo period: the same weeks last year adjusted for trend, or the surrounding
   weeks with the seasonal index applied. Write which, and why.
2. **Take the observed units** in the promo window, including the days the discount was live but the ad was not.
3. **Compute incremental units** = observed − baseline.
4. **Measure the dip**: the same calculation for the two to four weeks after.
5. **Net increment** = incremental in the window − the dip.
6. **Check cannibalisation** on the closest substitute SKUs in the same window.
7. **Compute the margin**, not the revenue: incremental units × unit margin after the discount, minus the promo
   cost (media, extra freight, marketplace fees).

| Line | Example |
|---|---|
| Baseline units (2 weeks) | 400 |
| Observed units | 640 |
| Incremental | 240 |
| Post-promo dip | −110 |
| Net increment | 130 |
| Margin per unit after 20% discount | ₹180 |
| Net margin gain | 130 × 180 = ₹23,400 |
| Promo cost (ads, fees, freight) | ₹18,000 |
| Net | ₹5,400 |

A ₹5,400 result on ₹18,000 of spend is not a success, and it is the number most businesses never compute.

## The uplift factor for planning

For forecasting, the useful output is a multiplier with a stated condition:

| Field | Value |
|---|---|
| SKU or family | |
| Promo type | Discount / bundle / BOGO / free shipping / marketplace event |
| Discount depth | 20% |
| Channel | Marketplace / own store / retail |
| Measured uplift | 1.6x the baseline over the window |
| Net of pull-forward | 1.25x |
| Confidence | High (3 comparable runs) / Low (1 run) |
| Applies to | Discounts of 15-25% on this family, not to a 40% clearance |

Never carry a multiplier from one family to another. A 1.6x on fast-moving staples says nothing about a
high-ticket item.

## Marketplace sale events

Amazon, Flipkart and similar platforms announce event dates, run their own discounts, and change their
visibility algorithms during the event. For forecasting:

- Treat the event as a **calendar event with a date you know in advance**, not as seasonality.
- Baseline from the same event last year if it existed, adjusted for the SKU's trend.
- Expect a **larger pull-forward** than a self-run promo, because the platform markets the event to everyone.
- Model **return rates higher** on event sales; net them out of demand.
- Plan stock to arrive **before the inbound cut-off**, which is the real deadline, not the event date.

## Price changes

A price change is a demand change and needs the same discipline.

| Change | What to expect | What to measure |
|---|---|---|
| Price up 5-10% | Small volume loss, margin gain | Units, and the revenue, over 8 weeks |
| Price up 15%+ | Visible volume loss, some to a substitute | Units, and the switch to the cheaper SKU |
| Price down | Volume gain, often less than hoped | Units and margin; a price cut rarely pays back on volume alone |
| Pack size change | Confusion in the history | Convert to a per-unit basis before comparing |

Without enough price history, use a stated elasticity assumption, label it as an assumption, and set the review
date when there will be data. Never present an assumed elasticity as measured.

## New products

| Data available | Approach | Honest range |
|---|---|---|
| A similar SKU in the same family | Family forecast × expected share | ±40% |
| A comparable launch elsewhere | Its first 12 weeks, scaled by market size | ±60% |
| Nothing | A conservative base, ordered in two tranches | State that the number is a guess with a review date |

For a new product, the forecast's real job is the **reorder date**, not the first order quantity: order small,
set a review at week 4 and week 8, and let the actual rate drive the second order. Say that in the output.

## Anti-patterns

- Comparing promo week to the annual average and calling the difference uplift.
- Counting the post-promo dip as new demand, so the next plan is built on a peak that was borrowed.
- Measuring revenue instead of margin: a 30% discount that doubles units usually loses money.
- Applying last Diwali's uplift to this Diwali without checking the dates moved.
- Treating a marketplace event as seasonality, then being surprised when the date changes.
- Forecasting a launch with the same confidence as a mature SKU, and putting the whole number in one purchase
  order.
- Ignoring cannibalisation, so the family looks up while the flagship SKU quietly dies.
