# Service and cost reporting

Five numbers, one page, one decision. This file defines them so they cannot be redefined to look better.

## The five numbers

| Metric | Formula | Read it as |
|---|---|---|
| On-time delivery (OTD) | Delivered within the promise / delivered | Whether the business keeps its word |
| First-attempt delivery (FAD) | Delivered on attempt 1 / attempted | Whether the address and the customer were ready |
| Damage and loss rate | Claims raised / shipments | Whether packing and handling work |
| RTO rate | RTO received / shipped | The cost of failure, both legs |
| Cost per delivered order | Total landed freight / delivered orders | The number that decides the carrier |

Report each by carrier and by lane, because an average across carriers hides the one that is failing.

## Definitions that must not drift

Write these in `notes/decisions.md` and hold them:

- **The promise** is what the business told the customer, not the carrier's transit time. If the business promised
  4 days and the carrier promised 6, OTD is measured against 4.
- **Delivered** means the carrier's proof exists - POD, signature, OTP. A "delivered" status with a customer
  dispute is counted as disputed, not delivered.
- **Attempted** includes every failed attempt, including the ones the customer caused.
- **Landed freight** includes fuel, COD fee, ODA, RTO and insurance, not just base freight.
- **A shipment is on time or it is not**; there is no partial credit for one day late.

## The carrier scorecard

| Carrier | Shipments | OTD % | FAD % | Damage % | RTO % | Landed ₹/order | Disputes ₹ | Verdict |
|---|---|---|---|---|---|---|---|---|
| A | 520 | 94% | 88% | 0.4% | 6% | 96 | 1,200 | Keep |
| B | 240 | 81% | 74% | 1.9% | 18% | 128 | 4,600 | Fix or drop |
| C | 140 | 97% | 92% | 0.2% | 3% | 141 | 0 | Keep for premium |

The verdict column is the point of the table. A scorecard with no verdict is a report; with one, it is a decision.

## Lane analysis

Cut by lane only where the volume justifies it - 30 shipments a month in a lane is enough to read, 5 is not.

| Lane | Volume | OTD % | Landed ₹/order | Problem | Action |
|---|---|---|---|---|---|
| Metro-metro, <500g | 410 | 96% | 62 | None | Keep |
| Regional, 2-5kg | 180 | 88% | 118 | Weight disputes | Fix the box |
| North-east, any | 45 | 71% | 310 | Transit time, ODA | Change the promise, not the carrier |
| Tier-3, COD | 120 | 76% | 205 | NDR, RTO | Prepaid push, address quality |

Some lanes are not fixable by changing the carrier. A north-east lane is slow because it is far; the honest move is
a longer promise and an ODA charge, not a fourth carrier trial.

## Cost per order, decomposed

| Line | ₹ per order | Share |
|---|---|---|
| Base freight | 68 | 65% |
| Fuel surcharge | 9 | 9% |
| COD fee | 14 | 13% |
| ODA | 4 | 4% |
| RTO cost allocated | 9 | 9% |
| **Landed** | **104** | 100% |

Three levers, in order of effect:

1. **Volumetric weight** - the box, not the carrier. Usually the largest single saving available.
2. **Prepaid conversion** - removes the COD fee and most of the RTO cost.
3. **Carrier mix** - reallocating volume from the expensive lane to the right carrier for that lane.

A fourth lever - renegotiating the base rate - is usually worth less than the first three, and it is the one
everybody starts with.

## The monthly read

One page: the five numbers with the trend, the carrier scorecard with verdicts, the one lane to fix, the one
process change, and the rupees it should save. Then the assumption that would change the conclusion.

## When to change a carrier

Change when two of these are true for two consecutive months:

- OTD below 85% against a promise the business can keep
- RTO rate more than double the alternative on the same lane
- Damage rate above 1% on a fragile category
- Landed cost per delivered order more than 15% above the alternative
- Disputes unresolved past the stated window twice

One bad month is a month. Two is a pattern, and the switch has a cost - new rate cards, new pickups, new packaging
tests, a week of learning. Say what the switch costs before recommending it.

## Anti-patterns

- Reporting a blended OTD across carriers, so a failing carrier is hidden by a good one.
- Measuring OTD against the carrier's transit time after the business promised something shorter.
- A scorecard with no verdict, so the review ends with "we will monitor".
- Changing carriers to fix a problem caused by the box size or the address quality.
- Comparing landed cost without allocating the RTO leg, which flatters the carrier with the most failures.
- Reporting cost per shipped order instead of per delivered order.
- Reviewing logistics only when a customer complains loudly.
