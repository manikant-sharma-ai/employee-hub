# Locations and layout: making the work shorter

Most warehouse speed is decided by where things are, not by how fast people move.

## Bin naming that a temp can follow

A four-part code, in the order a person walks:

```
A-03-B-02      aisle A, rack 03, level B, position 02
```

Rules: aisles numbered from the packing bench outwards, levels lettered bottom to top, positions left to right as
you face the rack. Print the code on the bin, on the shelf edge, and on the pick sheet, in the same order. If two
people can read the same code and walk to different places, the naming has failed.

## Slotting by velocity

| Class | Where it goes | Why |
|---|---|---|
| A (top 20% of picks) | Golden zone: waist to shoulder height, nearest the bench | Saves a bend and a walk on every pick |
| B | Middle aisles, mid levels | The working middle |
| C | Top and bottom levels, far aisles | Rarely picked, cheap to reach slowly |
| Bulky | Floor level, near the dock | Handling cost dominates |
| Fragile | Mid level, away from traffic | Damage is a return and a review |

Re-slot quarterly from the pick-frequency report. One hour of moving bins can cut a fifth off the walk, and it is
the highest-return hour in the building.

## The layout in five zones

| Zone | Purpose | Common error |
|---|---|---|
| Receiving and staging | Inward, GRN, put-away | Stock sits here for days and gets picked from, uncounted |
| Reserve | Bulk, overflow, backstock | Not recorded, so it does not exist until it is found |
| Pick face | What the picker can reach | Overfilled, so the reserve becomes the pick face |
| Pack and hold | Packing, per-order staging | Mixed orders, which is how mis-ships happen |
| Dispatch | Manifest, handover, courier | Used as storage when the day is busy |

## Replenishment

- **Trigger on a minimum, not on emptiness.** A pick face that empties during a wave costs a picker a trip and
  produces a short pick.
- **Replenish between waves**, never during one, unless the SKU is the wave.
- **Replenishment is a recorded movement**, not a physical act. An unrecorded top-up is a variance in waiting.
- **Set the min by the wave size**: enough for the largest single wave plus a day.

## Space maths

```
pallets needed = (units on hand / units per pallet) × (1 + growth for the season)
```

Then check the ceiling, not just the floor: racking height, the fork lift's reach, and the fire clearance. A
seasonal build that cannot be stored is a purchase order that becomes a corridor problem.

## The walk

Measure it once. Count the steps for a typical 20-line pick before and after a slotting change. It is the only
layout number that matters and the only one nobody records. Ten seconds a line, 200 lines a day, is half an hour of
one person's shift.

## Anti-patterns

- Bins named after the product, so a rename orphans the location.
- Overflow stock stored without a location record, which becomes "missing" at the next count.
- Reorganising the warehouse during peak season, when nobody can afford the relearning.
- A layout designed for the truck rather than for the picker.
- Storing the returns pile in the pick face because it is convenient.
