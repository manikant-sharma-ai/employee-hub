# Delivery exceptions: NDR, RTO, lost and damaged

The exception is where the customer relationship is won or lost, and where the money leaks. This file is the
playbook.

## The exception types

| Exception | What it means | Window to act | Cost if ignored |
|---|---|---|---|
| No scan after pickup | The shipment was not accepted, or the scan failed | 24 hours | Lost shipment with no claim |
| Stuck at a hub | No movement for 48-72 hours | 2 days | Late delivery, marketplace penalty |
| NDR - failed delivery | The carrier could not deliver: nobody home, refused, wrong address, phone unreachable | 24-48 hours | RTO, double freight, a lost sale |
| RTO in motion | Returning to origin | Immediately | Full freight both ways, stock out of the market |
| Damaged | Visible or reported damage | On delivery, with photos | Claim rejected without evidence |
| Lost | No trace after the carrier's search window | Per carrier terms | Full value, if the claim is filed in time |
| Delivered but disputed | POD exists, customer says no | 24 hours | Chargeback, review, refund without recovery |

## NDR: the highest-value 48 hours

A failed delivery attempt is not a failure yet. Most can be saved inside 48 hours, and after that the parcel
starts moving back.

| NDR reason | First action | Second action |
|---|---|---|
| Customer unreachable | WhatsApp the customer from the business number, then call | Re-attempt with a different time slot |
| Address incomplete or wrong | Confirm the address with the customer, update with the carrier | Re-attempt; if the pin code is unserviceable, offer an alternative |
| Refused - "did not order" | Check COD vs prepaid, confirm with the customer | If COD, convert to prepaid or cancel before RTO |
| Refused - "changed mind" | Offer an exchange or a partial refund before it ships back | Let it RTO and process as a return |
| Cash not available (COD) | Offer UPI or a payment link | Re-attempt next day, once |
| Premises closed | Re-attempt on a working day | Alternate address |

The rule: **every NDR gets a customer contact within 24 hours, by the channel the order came from.** A business
that does this converts a meaningful share of failures; one that does not pays the return leg on all of them.

## RTO: stopping the bleed

- **Before RTO is initiated**, decide: re-attempt, address change, convert COD to prepaid, or accept the return.
- **While in transit back**, tell the customer - a surprise return is a refund demand and a bad review.
- **On receipt**, inspect and grade, then hand to `returns-manager` for disposition. Do not restock damaged goods
  silently.
- **Count the RTO rate by reason and by carrier.** A carrier whose RTO rate is double the others is a carrier
  problem, not a customer problem.

## Damaged and lost: the claim

| Step | What to do | Evidence |
|---|---|---|
| 1 | Record the damage at delivery, before signing | Photos of the outer, the inner packing, the product, the label |
| 2 | Report to the carrier inside their window, in writing | The order ID, AWB, photos, invoice value |
| 3 | Keep the packaging until the claim closes | Carriers ask for it, and it is often discarded |
| 4 | File the claim with the value proof | Invoice, not the selling price alone |
| 5 | Follow up on a schedule, in writing | A claim without a follow-up is a closed claim |
| 6 | Decide whether to claim or absorb, by value and by relationship | Small claims cost more in time than they recover |

Insurance is worth it above a threshold the business sets. Below it, self-insure and price the loss into the
freight. Say which policy applies.

## The escalation matrix

| Situation | Escalate to | Within |
|---|---|---|
| No scan in 24h | Carrier's pickup or hub contact | Same day |
| Stuck 72h | Carrier account manager | Same day |
| NDR unresolved after 2 attempts | Account manager, with the customer contact log | 1 day |
| Lost after search window | Account manager, in writing, with the claim | Per carrier terms |
| Repeated failure on one lane | Account manager, with the numbers | Weekly review |
| Marketplace penalty risk | The marketplace's logistics support | Before the promised date |

Write the names and numbers of each of these into `notes/contacts.md` when they are first used, because the second
time is always urgent.

## Telling the customer

Hand these to `support-agent` as words, with the facts attached:

- **What happened**, in one line, without blaming the carrier by name in a way that invites the customer to
  contact them directly.
- **What is true now** - the last scan and its date, and that it is the last scan rather than the current
  location.
- **The realistic date**, and the fact that it is a promise rather than a guarantee if it is one.
- **What the business will do** if it does not arrive - the specific next step, not "we will look into it".
- **What the customer should do**, if anything - confirm the address, be available, keep the phone reachable.

## Anti-patterns

- Waiting for the carrier to resolve an NDR, when one WhatsApp message from the business would have saved the
  order.
- Letting an RTO happen to protect a COD margin, then paying freight both ways.
- Filing a damage claim without photographs, and losing it.
- Absorbing every small loss quietly, so the loss rate never appears in the report.
- Blaming the customer for a failed delivery when the address was captured badly at checkout.
- Escalating to the carrier's CEO-level email on the first stuck parcel, and losing the account manager's
  attention for the ones that matter.
- Telling a customer "it will definitely come tomorrow" on the strength of a single scan.
