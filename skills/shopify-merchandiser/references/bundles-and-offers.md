# Bundles and offers

Every offer is a trade: rupees of margin now for revenue, volume or a customer you keep. An offer
that does not name what it buys is a price cut.

## The margin floor, before any offer

```
Contribution per unit = selling price - landed cost - shipping - packaging - gateway fee
                        - marketplace fee (if any) - expected return cost
Margin floor = the contribution below which the offer stops making sense
```

| Business stage | Typical floor |
|---|---|
| Established, profitable | Contribution stays above 60-70% of the pre-offer figure |
| Growth, buying share | Above 40-50%, with a stated end date |
| Clearance | Above zero after return cost - never below |
| Loss-leader | Named, capped in units, and only to acquire a repeat buyer |

Worked example, one unit:

| Line | ₹ |
|---|---|
| Selling price | 1,200 |
| Landed cost | 420 |
| Shipping (prepaid, avg) | 78 |
| Packaging | 22 |
| Gateway 2% | 24 |
| Return provision (12% at ₹120 cost per return) | 40 |
| **Contribution** | **616 (51%)** |

A 20% discount is ₹240 off, so contribution falls to ₹376 - a 39% cut in contribution for a 20%
price cut. That ratio is the whole argument for bundles over discounts.

## Offer types, by what they buy

| Mechanic | Buys | Margin cost | Best for |
|---|---|---|---|
| **Fixed bundle** (2-3 products, one price) | Higher AOV, clearer gifting | Low - a bundle discount is smaller than the sum of parts | Sets, kits, hampers |
| **Mix and match** (pick any 3) | AOV, and it moves slow stock | Medium | Apparel, accessories |
| **Threshold gift** (free item above ₹1,500) | AOV, and it uses dead stock | Low if the gift's cost is low | Repeat categories |
| **Free shipping threshold** | AOV, and it removes the top objection | Low, and it is often the best offer available | Everything, at the right number |
| **Prepaid discount** (2-5% off for prepaid) | Removes COD cost and RTO | Very low - it usually pays for itself | India, where COD drives RTO |
| **Quantity break** (buy 2 save 10%) | Units per order | Medium | Consumables |
| **Bundle + gift** | AOV and perceived value | Medium | Festive |
| **Flat % off everything** | Revenue this week | High, and it resets the price reference | Almost never |
| **Coupon code on social** | Attribution | Medium, plus code leakage | Acquisition tests |

## The prepaid discount, sized properly

COD costs more than the fee: RTO on COD is commonly 2-4x the prepaid rate, and the return costs
shipping both ways plus handling.

| | COD | Prepaid |
|---|---|---|
| Order value | ₹1,200 | ₹1,200 |
| Gateway fee | ~0 | ~₹24 |
| COD collection fee | ₹40-60 | 0 |
| RTO rate (typical) | 25-35% | 5-10% |
| Expected RTO cost per order | ₹150-250 | ₹30-60 |

A 3-5% prepaid incentive frequently costs less than the COD it avoids. Model it on your own RTO
rates, not on this table - the table tells you where to look.

## Stacking: the leak nobody prices

Discounts combine by default unless you stop them. Write the rule down:

| Layer | Example | Stacks with |
|---|---|---|
| Automatic discount | "10% off orders above ₹2,000" | Usually everything |
| Discount code | "DIWALI15" | Check the platform's combination setting |
| Free shipping threshold | Above ₹999 | Usually everything |
| Bundle price | Fixed price for a set | Should be excluded from % codes |
| Loyalty or referral credit | ₹100 off | Should be capped |

Three tests before launch: **(1)** put the worst-case basket through checkout and read the total;
**(2)** check the combination settings on each discount; **(3)** cap the total discount as a
percentage of order value, and put the cap in `notes/decisions.md`.

## Code hygiene

| Rule | Why |
|---|---|
| One code per channel, and a naming convention (`IG-DIWALI-15`) | Attribution without a spreadsheet argument |
| Expiry date on every code | A forgotten code is a permanent price cut |
| Usage limit per customer | Stops a code circulating beyond its audience |
| Minimum order value on every % code | Protects the small basket |
| Deactivate, never delete | History and attribution |
| Review live codes monthly | The most common source of margin leakage |

## The offer sheet

One table, agreed before launch:

| Field | Example |
|---|---|
| Offer | Festive bundle - 3 kurtas |
| Mechanic | Fixed price ₹2,499 (list ₹3,600) |
| Margin floor | Contribution ≥ ₹700 |
| Actual contribution | ₹812 |
| Stacking | Excluded from all % codes; free shipping applies |
| Cap | 400 units, or 31 Oct |
| Stock dependency | 180 sets available at launch |
| Success metric | AOV ₹1,850 vs ₹1,410 baseline |
| Kill condition | Contribution below ₹700 for three days |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| A percentage off everything | The price reference resets and never comes back |
| Bundling two slow movers | The bundle inherits both problems |
| A bundle priced below the sum of contributions | Volume rises, profit falls |
| Codes that stack with an automatic discount | A 10% offer becomes 25% silently |
| No end date | A campaign becomes the price |
| Free shipping with no threshold | Shipping cost moves to every order |
| A gift nobody wants | Costs margin and reads as clutter |
| Offer launched without a stock check | Sold out in a day, and the traffic is wasted |
