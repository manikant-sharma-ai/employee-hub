# Pick, pack, ship: running the day backwards from the truck

The day is not a list of orders. It is a deadline with work in front of it.

## The backwards plan

| Time | Step | Owner | If it slips |
|---|---|---|---|
| 09:00 | Order cut-off for today's dispatch | channel | Orders after this go tomorrow |
| 09:15 | Wave released, picks by zone | supervisor | Picking starts late; everything after shifts |
| 11:00 | Picking complete for wave 1 | pickers | Packing cannot start |
| 12:30 | Packing complete, weights checked | packers | Manifest cannot be closed |
| 14:00 | Manifest closed, labels printed | coordinator | Courier refuses the handover |
| 16:00 | Courier collection | courier | The truck leaves without the boxes |
| 16:15 | Handover counted, signed | coordinator | A claim becomes a dispute |

Two waves a day beats one long wave, because a single delay in the morning does not take the whole day with it.

## Sequencing picks

| Order type | Sequence | Why |
|---|---|---|
| Single line, one zone | Batch of 20-30, sorted by bin | The cheapest pick in a warehouse |
| Multi-line, several zones | Route by aisle order | Walking is 60% of pick time |
| Heavy or bulky | Own wave, own trolley, early | Fatigue and damage rise with repetition |
| Marketplace priority | First, with the label printed at pick | Their SLA penalty starts before yours |
| Pre-orders and holds | Last, or a separate day | They do not have a collection clock |

## The three checks before a box closes

1. **Scan the SKU.** Not the shelf label, the item.
2. **Count the units.** Two units of the wrong size is the same failure as the wrong SKU.
3. **Weigh the parcel.** A 1.2kg order in a 2.8kg box is a mis-pick the scanner missed, and the scale costs
   nothing per check.

## Pack station design

- **One station per 60-80 orders a day** with a person; beyond that the queue moves to the picker.
- **Consumables within arm's reach** - tape, void fill, labels, pouches - or every pack costs a walk.
- **Two zones: pack and hold.** Mixed staging is where mis-ships are born.
- **A screen or a printed sheet with the order, not a phone.** Screens are faster and both hands stay free.

## Measuring the day

| Metric | Definition | Healthy range for a small warehouse |
|---|---|---|
| Pick accuracy | Orders shipped without a pick error / orders shipped | 99%+ |
| DIFOT | Delivered in full, on time / orders due | 95%+ |
| Shipped after cut-off | Orders leaving after the channel cut-off / orders | Under 3% |
| Lines per hour | Pick lines / picker hours | Depends on layout; track the trend, not the level |
| Pack cost per order | Consumables + labour / orders | Track the trend after a packaging change |

## When the day is already lost

Say it at 11am, not at 5pm. Rank what will not make it: marketplace orders first (penalty), prepaid D2C second
(the customer is waiting and has paid), COD last (no money is at risk yet). Tell the account owner, who tells the
customer. A warehouse that announces its own failure early keeps its customers; one that goes quiet loses them.

## Anti-patterns

- Picking in order-number sequence, which walks the warehouse in the worst possible route.
- Printing labels at pack time, which means the box is closed before anyone checks the address.
- One wave a day for everything, so a single stock-out stalls the entire dispatch.
- Measuring pickers on lines per hour alone, which produces fast wrong picks.
- Packing without a weight check because the scale is at the other end of the room.
