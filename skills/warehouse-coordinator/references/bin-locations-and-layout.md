# Bin locations and layout

The question "where is it?" is answered by a location, or it is answered by the person who has been there longest.
The second answer is the one that leaves with them.

## The location code

A location is a short, spoken-aloud code: aisle-bay-level-bin, or zone-rack-shelf. `A-03-2` is a location;
"shelf near the packing table" is a memory. Print it, laminate it, stick it on the rack at eye height.

Rules that make a code survive:

- **Four segments at most**, and no segment longer than three characters.
- **Read left to right, in walking order**, so the code tells the picker where to walk next.
- **Never reuse a retired location code** for a different SKU without a dated note; the paper trail will lie.
- **One SKU per location.** Two SKUs in one bin is the root of most wrong-item shipments, and the second SKU always
  wins the argument.

## Zoning by velocity

Take the last ninety days of picks. Sort SKUs by lines picked, not by units or value. Then:

| Zone | Contents | Where |
|---|---|---|
| Pick face | The 20% of SKUs that produce 80% of pick lines | Closest to the pack bench, waist height |
| Reserve | Bulk of the fast movers, and everything else | Above, below, further back |
| Bulk | Full cases, slow movers, seasonal | The far end, the mezzanine, the container |
| Quarantine | Damage, returns awaiting disposition, quality holds | Separately marked, never mixed |

The pick face is refilled from reserve on a trigger (a minimum quantity, a visual mark, or a kanban card), and the
trigger is written on the bin card. Without a trigger, the pick face runs empty at the worst possible moment.

## Labelling

- **SKU label on the bin**, not only on the product. A product label is read at arm's length; a bin label at a
  glance.
- **A picture of the item on the pick face** for anything look-alike: two bottle sizes, two cable gauges, two
  shades of the same product. This single change cuts wrong-item lines more than any training.
- **Colour-code the zones** if the team is new or the warehouse is dark. Cheap, and it survives turnover.

## When to stop using a spreadsheet

A spreadsheet is enough up to a few hundred SKUs and a few hundred lines a day, if the locations are physical and
the count is disciplined. Move to a WMS or the inventory module when any of these is true: more than one person
picks at once, more than 500 SKUs, batch or expiry tracking, or a second warehouse. Until then, a good sheet beats
a bad implementation.

## The layout review

Twice a year, walk the pick path with the last quarter's pick data and ask three questions: which lines walk
furthest, which two SKUs are always picked together but sit apart, and which location is a dead end. Moving five
SKUs is usually worth more than any software purchase.
