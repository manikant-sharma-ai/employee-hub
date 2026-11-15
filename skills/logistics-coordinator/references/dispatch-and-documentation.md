# Dispatch and documentation

A shipment that cannot move is not shipped. This file gets it out the door with the papers it needs.

## The dispatch day

| Time | Step | Owner |
|---|---|---|
| Before 10am | Orders picked, packed, weighed, dimensions recorded | Warehouse |
| Before 11am | Manifest built, labels printed, documents attached | Dispatch |
| Before cut-off | Pickup handed over, count verified against the manifest | Dispatch |
| Same evening | Manifest scanned against the carrier's acceptance; discrepancies raised | Coordinator |
| Next morning | Any order not accepted is rebooked or escalated | Coordinator |

The cut-off is the carrier's, not the business's, and it moves during peak weeks. Write the cut-off into the
calendar for each carrier.

## The documents

| Document | When it is needed | Who issues it |
|---|---|---|
| Tax invoice | Every taxable supply | The business, from the billing system |
| E-way bill | Movement of goods above the threshold, and for specified goods regardless of value | The business or the transporter, from the GST portal |
| Consignment note / LR | Every consignment moved by a transporter | The transporter |
| Packing list | Multi-item or B2B consignments | The business |
| Delivery challan | Goods moving without a sale (job work, approval, exhibition) | The business |
| Statutory declarations | Restricted goods, specific states, exemptions | The business, on the prescribed form |
| Insurance declaration | High-value consignments | The business, to the insurer |

**On the e-way bill**: it is generally required for consignments of goods above ₹50,000 in value, and several
states have notified lower limits for intra-state movement. Some goods require it regardless of value. The
thresholds, the state notifications and the validity rules change, so confirm the current position for the state
and the goods before a dispatch - and route the tax question to the CA, not to memory.

## E-way bill validity, in practice

- Validity is set by distance, with a day per stated kilometre slab, and it is extended only within the rules.
- A consignment that will take longer than the validity must be re-generated or extended before it expires.
- The vehicle number must match. A change of vehicle mid-route requires an update.
- A consignment held at a checkpost with an expired or mismatched document costs a day and a penalty, and it is
  always cheaper to generate the document properly than to argue at the barrier.

## Packing, priced

| Decision | Effect on freight | Effect on damage |
|---|---|---|
| Box one size down | Lower volumetric weight, direct saving | Higher damage risk - test it |
| Better void fill | No freight change | Large damage reduction |
| Fragile marking and handling | No freight change | Fewer claims, better acceptance |
| Double-wall for heavy items | Slightly higher weight | Fewer crush claims |
| Consolidating two shipments to one address | One shipment instead of two | Lower cost, longer wait for the first item |

A packing change is a cost decision with a damage consequence. Measure both for a month before adopting it, and
write the result in `learnings.md`.

## The manifest and the handover

- **Count against the manifest at handover**, in the presence of the pickup person, and get the count signed or
  acknowledged in the app.
- **Photograph the sealed bags** with the count. This is the only evidence when a shipment is "short received" at
  the hub.
- **Keep the weight slip** for every shipment. It is the evidence in a weight dispute.
- **Never hand over an unscanned shipment** - an unscanned parcel has no chain of custody and becomes "not
  received" with no way to prove otherwise.

## Multi-item and split shipments

| Case | Approach |
|---|---|
| Partial stock | Ship what is available, backorder the rest, tell the customer the two dates |
| One order, two warehouses | Two consignments, one order ID, both tracked |
| High value plus low value in one order | Consider separate shipment only if the insurance and the risk justify the extra freight |
| B2B bulk | Palletise, use a transporter, LR plus e-way bill, delivery challan where the invoice follows |

## Anti-patterns

- Printing the label with a weight nobody measured, so the carrier rebills at a higher slab.
- Shipping at 6pm against a 4pm cut-off and blaming the carrier for the delay.
- Generating an e-way bill with the wrong vehicle number, or the transporter's vehicle instead of the actual one.
- Sending goods on a delivery challan and never converting it to an invoice - a GST exposure nobody notices until
  the audit.
- Handing over 40 parcels without counting them, then arguing about 3 missing ones.
- No weight slip, then losing every weight dispute for a year.
- Using one box size for everything because buying in bulk is cheaper, when the volumetric billing costs more than
  the box saves.
