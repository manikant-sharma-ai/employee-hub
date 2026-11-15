# Carrier selection and rates

The cheapest carrier on the rate card is rarely the cheapest shipment. This file compares on landed cost.

## The rate card, decoded

| Line | What it is | Where it hides |
|---|---|---|
| Base freight | Per zone, per weight slab | The headline number everyone quotes |
| Fuel surcharge | A percentage of base, revised periodically | 8-18% of base, and it moves |
| COD fee | A percentage of the COD value, or a flat fee | ₹25-50 flat, or 1.5-3% of value |
| ODA charge | Out-of-delivery-area, by pin code | ₹100-400 per shipment, and it is not in the quote |
| Volumetric weight | (L×W×H) ÷ divisor | The divisor differs by carrier and by mode |
| RTO charge | The return leg, often the same as forward | Doubles the cost of a failed shipment |
| Insurance | Optional, per declared value | Only worth it on high-value goods |
| Appointment delivery | A scheduled slot | Rarely offered, always extra |
| Peak surcharge | Seasonal, announced by the carrier | December, festive weeks |

A comparison that uses only base freight is wrong by 20-40% in the direction of the carrier with the most
surcharges.

## Zones, and why they matter more than distance

Every carrier prices by zone, and the zone is not the distance. A 900km shipment inside a metro-adjacent state can
be a lower zone than a 300km shipment to a remote district.

| Zone | Typical definition | Price behaviour |
|---|---|---|
| Within city | Same city pin codes | Cheapest, often same-day or next-day |
| Regional | Same or adjacent state | Low |
| Metro to metro | Delhi, Mumbai, Bengaluru, Chennai, Hyderabad, Kolkata, Pune, Ahmedabad | Low-medium, best service |
| Rest of India | Other state capitals and large towns | Medium |
| Remote or ODA | North-east, islands, hill districts, small towns | High, plus ODA, plus longer transit |

Build the zone map from the carrier's own zone chart, not from a distance estimate. When two carriers disagree
about a pin code's zone, note it - it becomes a dispute later.

## Volumetric weight: the most common billing surprise

Billable weight is the higher of actual weight and volumetric weight.

**Volumetric weight (kg) = (L × W × H in cm) ÷ divisor**

The divisor is commonly 5000 for air express and 6000 or 4500 for surface, and it varies by carrier and by
contract. It is written on the rate card; if it is not, ask, because the difference between 4500 and 6000 on the
same box is a 33% swing in billable weight.

| Box | Dimensions (cm) | Volumetric at 5000 | Actual | Billed |
|---|---|---|---|---|
| Small | 20×15×10 = 3,000 | 0.6 kg | 0.5 kg | 0.6 kg |
| Medium | 30×25×15 = 11,250 | 2.25 kg | 1.8 kg | 2.25 kg |
| Oversized | 40×30×25 = 30,000 | 6.0 kg | 2.5 kg | 6.0 kg |

The oversized box bills at 6kg for 2.5kg of goods. That single line explains most "why is freight up" questions.
The fix is a box change or a packing change, which is a decision with a cost - say what it is.

## The comparison table

| Carrier | Service | Zone | Billable kg | Base | Fuel | COD | ODA | Landed | Promised days |
|---|---|---|---|---|---|---|---|---|---|
| A | Surface | Regional | 2.25 | 78 | 9 | 30 | 0 | 117 | 4-6 |
| B | Surface | Regional | 2.25 | 71 | 12 | 35 | 150 | 268 | 5-8 |
| C | Air | Regional | 2.25 | 96 | 8 | 30 | 0 | 134 | 2-3 |

Carrier B looks cheapest and is the most expensive the moment the pin code is ODA. The table exists to stop that
mistake.

## Choosing, per shipment

| Situation | Choose |
|---|---|
| Metro to metro, prepaid, low value | The cheapest surface with a 3-5 day promise |
| Customer paid for express | The fastest with a real promise, not the cheapest |
| High value, fragile | The carrier with the best damage record on that lane, insurance on |
| COD | The carrier with the shortest remittance cycle and a working COD reconciliation |
| Remote or ODA | Quote the ODA to the customer or absorb it knowingly - never discover it on the invoice |
| Bulk or B2B pallet | A transporter, not a parcel carrier; different rate logic entirely |
| Marketplace order | The platform's logistics, unless the penalty structure says otherwise |

## The monthly rate review

1. Pull the last month's freight invoices and the dispatch data.
2. Compute the **effective rate per kg and per shipment** by carrier and lane, landed.
3. Compare with the rate card. A gap above 3% is a billing problem; above 10% is a wrong rate card or a weight
   dispute pattern.
4. Compare carriers on **cost per delivered order**, not per shipped order - the return leg belongs in the number.
5. Renegotiate or reallocate volume. Most carriers will improve a rate for committed volume, and a small shipper
   gets that leverage through an aggregator rather than a direct contract.

## Anti-patterns

- Choosing a carrier by the rate someone remembers from last year.
- Comparing base freight across carriers with different divisors and surcharge structures.
- Ignoring the RTO rate when comparing: a 25% RTO carrier is expensive at any headline price.
- Using an air express service for a customer who did not pay for it.
- Sending an ODA pin code on the cheapest carrier and finding the charge on the invoice a month later.
- Renegotiating rates while the actual cost driver is the box size.
- One carrier for everything because the account manager is friendly.
