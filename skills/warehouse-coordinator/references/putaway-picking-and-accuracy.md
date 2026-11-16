# Putaway, picking and accuracy

Accuracy is designed, not asked for. A picker who has to remember is a picker who will be wrong at 5pm on a
Friday.

## Putaway

- **Every arrival goes to a location, the same day.** Stock on the floor is stock that is not in the system and
  not findable.
- **The rule is written**: same SKU to its own location; a new SKU to a location chosen by velocity; anything
  damaged to quarantine. Nobody chooses a location by convenience.
- **The putaway is recorded** - SKU, quantity, location, date, who. If it is not recorded, the count will find it
  in three months as a variance.

## Picking

The four controls, in the order they pay back:

1. **Location** - the pick list is sorted by walking order, not by order number. This alone halves pick time in
   most small warehouses.
2. **Verification** - a scan, a check digit, or a quantity call-out. Scanning is best; a check digit on the label
   is nearly free and catches most transpositions.
3. **The pack bench check** - a second pair of eyes on the item and the quantity against the order, at packing.
   This is where a wrong pick becomes a wrong shipment, and it is the cheapest place to stop it.
4. **The feedback loop** - every wrong-item report is traced back to the pick, the location or the label, and the
   fix is a change to one of the three. "Be more careful" is not a fix.

## Wrong-item rate

`wrong-item lines / total lines picked`, weekly. A rate above 1% is a process problem; above 3% it is a
customer-experience problem that costs more than the labour saved by going faster. Track it per picker only to
find training needs, never to rank people publicly - the data is noisy at small volumes and public ranking
destroys the reporting.

## Packing

- **One order, one tote.** Mixing orders on a bench is how item A ships in box B.
- **A photo of the packed box** for high-value or dispute-prone orders. It settles arguments for a rupee a photo.
- **The label is applied after the check, not before.** A labelled box is a shipped box in everyone's mind.

## Speed against accuracy

Measure both, and never one alone. Picks per hour rising while the wrong-item rate also rises is not an
improvement - it is the same errors, arriving sooner. The target is lines per hour at a wrong-item rate under the
threshold; if the team must choose, choose accuracy, because a return costs the pick, the pack, the shipping both
ways and the customer.

## Handover to shipping

The packed order, the manifest and the exception list go to `logistics-coordinator` at a fixed time. Anything
picked but not manifested by that time is stated, not silently left for tomorrow.
