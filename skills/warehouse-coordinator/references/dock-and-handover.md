# The dock: manifest, documents, and the handover that decides a claim

The last thirty minutes decide whether a shipment is a delivery or a dispute.

## The manifest

Build it from what was physically packed, not from what the system expected:

| Check | Why |
|---|---|
| Parcel count matches the manifest | A missing parcel is found here, not at the customer's door |
| Each parcel's weight is plausible | A 4kg parcel for a 1kg order is a mis-pick or a missing item |
| Every label is scanned, not typed | Typed labels are how two orders swap addresses |
| COD parcels are separated and flagged | The courier collects the amount; a missed flag is a lost COD |
| Service level per parcel matches the paid service | An express parcel on a surface manifest is a late delivery you pay for |

## Documents a courier actually needs

| Document | When | Note |
|---|---|---|
| Manifest or pickup sheet | Every handover | Count and sign, in front of the courier |
| E-way bill | Movement of goods above the threshold, and for many B2B movements | Generated from the invoice; check the threshold before the truck arrives |
| Tax invoice | Every B2B shipment, and inside every parcel | The customer's credit depends on it |
| LR or consignment note | For surface and part-truck loads | The carrier's document, signed by both sides |
| COD remittance sheet | COD shipments | Reconciled per order, not per total |

This role prepares and checks; the tax treatment is the CA's and the rate decision is `logistics-coordinator`'s.

## The handover, in five minutes

1. **Count in front of the courier**, out loud, against the manifest.
2. **Sign both copies**, with the count written on both.
3. **Photograph the signed sheet and the stacked parcels.** It is the only evidence that survives a claim.
4. **Note exceptions on the manifest** - a damaged carton, a missing label, a parcel refused - before it leaves.
5. **Send the count and the exceptions to `logistics-coordinator` the same day**, not when the claim arrives.

## When the count disagrees

| Situation | Action |
|---|---|
| Courier counts fewer than the manifest | Do not sign the higher number; recount together; if unresolved, note the difference on both copies |
| Courier counts more | Check the staging area for tomorrow's parcels, which is the usual explanation |
| A parcel is refused at pickup | Record why, keep it, and tell the owner of the order the same day |
| The courier arrives early | Hand over what is ready, manifest it separately, and do not hold the truck for the rest |

## Parcels that must not leave

- **Unweighed.** The check exists to be used.
- **Without an address that matches the label**, or with a hand-written label.
- **With a damaged carton and fragile contents**, unless the customer has been told and agreed.
- **Against an order flagged as fraudulent or on hold.** The dock is the last place a fraud check can still work.
- **COD without the amount confirmed** on the manifest and the label.

## The 24-hour exception window

A failed attempt, a refusal, a damage or a lost parcel is cheapest to fix inside 24 hours. That is
`logistics-coordinator`'s window, and it only works if the dock hands over the exception list on the day.

## Anti-patterns

- Signing a manifest without counting, which converts a courier's error into your loss.
- Building the manifest from the order system rather than the packed parcels.
- An e-way bill generated after the truck leaves, which is a penalty waiting at a checkpost.
- COD parcels mixed into the prepaid stack, discovered at remittance.
- No photograph of the handover, so a damage claim is one person's word against another's.
