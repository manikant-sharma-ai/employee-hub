# Pricing and rejection

A marketplace price is not the price on the sheet. It is the price after the
channel's share, the shipping, the returns and the tax.

## The price working, per unit

```
selling price (incl. GST)          ₹999
- GST component (18%)              ₹152
= net revenue ex-GST               ₹847
- marketplace commission (say 15%) ₹127   (usually on the ex-GST or incl-GST value - check the channel)
- closing fee                       ₹25
- shipping (if seller pays)         ₹70
- returns provision (return rate x cost of a return)
= net realisation                   ₹...
- product cost                      ₹...
= contribution per unit             ₹...
```

Show this table for every price decision. A listing priced at a 40% gross margin
often lands at 20-25% net after a marketplace, and the owner should see that
before the first order, not after the first settlement report.

## The returns provision

Use the category's actual return rate, not the optimistic one. Apparel in India
runs high; electronics lower but costlier per return. Provision as
`return_rate * (forward shipping + reverse shipping + refurbishment or write-off)`.
A price that ignores returns is a price that loses money on 15% of orders.

## Discount discipline

- **MRP is a legal declaration**, not a marketing number. A permanent "70% off" on an inflated MRP is a legal metrology problem and a trust problem.
- **One discount reason at a time.** End of line, festive, bundle, or clearance - not all four.
- **Marketplace-funded discounts are not your margin.** Track them separately so a channel-led promotion does not look like a price cut you made.
- **Price parity across channels is a decision, not a default.** Some categories need it, some do not; write it down.

## The rejection log

Every rejection is a rule you did not know. Record it the same day:

| Date | Channel | SKU | Rejection code / reason | Rule learned | Fix applied to template |
|---|---|---|---|---|---|
| | | | | | |

The point is not the individual fix, it is the template change, so the next bulk
upload of 200 SKUs does not reproduce the same failure 200 times.

## The five commonest rejections, and the fix

1. **Invalid HSN** - wrong digit count or a code that does not match the product. Fix: confirm with the CA, apply to the whole category at once.
2. **Missing mandatory attribute** - often a filter field nobody noticed. Fix: add the column to the sheet, not the individual row.
3. **Image below the minimum or a non-white main image** - fix the image set, not the listing.
4. **Prohibited claim in the title or bullets** - remove it, and add it to the banned list in `scripts/listing_qa.py` if it is a pattern.
5. **Brand gating or approval not cleared** - a process blocker, not a listing blocker; escalate to the category manager with the brand authorisation letter.
