# Bundles, add-ons and basket size

Average order value is the cheapest growth there is: the traffic is already paid for. But
every AOV lever is also a margin lever, and only one of them can be pulled without cost.

## The AOV arithmetic

```
AOV = units per order x average price per unit
```

Two levers, two very different economics:

- **More units per order** - bundles, add-ons, quantity breaks, threshold shipping. Cost
  is real (the extra unit's cost) but usually small relative to price.
- **Higher price per unit** - premium placement, larger pack sizes, a better-margin
  variant shown first. Cost is often the same as the cheap variant.

`scripts/merch_math.py` computes the gross profit of each option; use it before you
recommend one.

## Bundle types, in order of reliability

| Type | What it is | Best for | Watch out for |
|---|---|---|---|
| Curated set | three or four products chosen as a gift or a routine | gifting, starter kits, routines | stock mismatch kills it |
| Mix and match | pick any two, get a set price | categories with real variety | the shopper picks the two cheapest |
| Quantity break | buy 3, save 10% | consumables, basics | trains bulk buying at a discount |
| Gift with purchase | free item above a threshold | lifting AOV without cutting price | the gift's cost is real; count it |
| Threshold shipping | free delivery above ₹X | almost every Indian D2C store | set X from the cost of delivery, not a round number |
| Post-purchase add-on | one more item at checkout | impulse categories | must not delay the order |

## Pricing a bundle: up from cost

```
floor price   = total cost / (1 - margin floor)
list value    = sum of the component list prices
max discount  = 1 - floor / list value
```

If the floor price is above what the shopper would pay, the bundle is wrong - not the
price. Fix the assortment (cheaper components, fewer items), do not drop below the floor
to make the offer "work".

A bundle that shows "save ₹450" while running at 12% margin is a revenue story with a
margin problem, and the founder will find out at the year end.

## Threshold shipping, set properly

- Take the delivery cost per order, including RTO and packaging.
- Set the threshold at roughly 1.4 to 1.8 times the current AOV - close enough to reach,
  far enough to add an item.
- Show the gap: "₹240 away from free delivery" converts better than a static banner.
- Recompute quarterly; a threshold set two years ago is a subsidy.

## The attachment rate

The metric that tells you whether the offer works:

```
attachment rate = orders containing the add-on / total orders
```

A bundle with a 2% attachment rate is decoration. Aim for 8-15% on a well-placed add-on;
anything above 20% is usually cannibalising the item it sits beside.

## Placement

- **Product page** - the add-on that completes the purchase, priced and one click.
- **Cart drawer** - the threshold message plus one recommendation, never a carousel.
- **Post-purchase** - one item, one click, no discount.
- **Collection page** - the set, presented as a set, with the saving shown.

Every additional recommendation costs attention. Two is the maximum that helps; five is a
shop that looks like it does not know what it sells.

## Anti-patterns

- **A bundle priced as a discount rather than a set.** "Buy 3 at 30% off" is a sale with
  extra steps.
- **A gift with purchase that costs more than the margin it protects.**
- **Threshold shipping set at a round number** nobody calculated.
- **An add-on that is out of stock** - the commonest cause of a dead bundle.
- **Recommending the cheapest item to every shopper**, which lowers AOV while looking
  like personalisation.
