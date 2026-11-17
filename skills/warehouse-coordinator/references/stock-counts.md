# Counting stock: cycle counts, the physical count, and what a variance means

The count is not an audit of the stock. It is an audit of the process that produced the number.

## Why full counts alone fail

A yearly physical count finds a variance twelve months after the cause, when nothing can be traced and everyone
agrees to write it off. A cycle-count programme finds the same variance in week three, while the pick that caused
it is still in the scanner history.

## The ABC cycle-count calendar

| Class | Share of SKUs | Share of value | Count frequency |
|---|---|---|---|
| A | 10-20% | 70-80% | Weekly, or every two weeks |
| B | 20-30% | 15-20% | Monthly |
| C | 50-70% | 5-10% | Quarterly |
| Slow or dead | Whatever is left | Near zero | Once, then by exception |

Classify on consumption value (units moved × unit cost), not on unit price alone. A ₹40 fastener that ships 4,000
times a month matters more than a ₹40,000 machine that ships once a quarter.

## Running a count that produces evidence

1. **Freeze the bin, not the warehouse.** Count one zone while picking continues elsewhere.
2. **Print blind sheets** - SKU, location, and a blank quantity. A sheet with the expected number is a
   confirmation exercise.
3. **Count in the same unit the system uses.** A case counted as units is the commonest self-inflicted variance.
4. **Recount any line outside the threshold before recording it.** One counter's error is not a discrepancy.
5. **Record who counted and when**, on the sheet. A variance with no counter cannot be investigated.
6. **Post the variance the same day**, with a cause code, not at month end when memory is gone.

## The threshold

Set it before the count, in writing, per class:

| Class | Variance threshold | Action at or above |
|---|---|---|
| A | 1% of units, or 2 units, whichever is greater | Investigate within 24 hours |
| B | 2% or 3 units | Investigate within 48 hours |
| C | 5% | Adjust with a cause code, review monthly |

A threshold that moves after the count is not a threshold, it is a negotiation.

## The full physical count

Do it once or twice a year, for three reasons only: a statutory or audit requirement, a system migration, or a
suspicion that the cycle programme itself has drifted.

- **Plan the shutdown**, or count over a weekend, and say which.
- **Count in two passes**: a first count, then a recount of every variance by a different person.
- **Reconcile to the books, not just the WMS.** Three numbers exist - physical, system and ledger - and they are
  rarely the same.
- **Publish the result**: variance by class, by cause, and the rupee value. A count nobody reads is a stocktake
  for the auditor's file.

## What a variance actually means

| Pattern | Likely cause |
|---|---|
| One SKU, one bin, small, repeated | A pick error, a similar-looking item nearby, or a mislabelled bin |
| One SKU, large, one-off | A receipt error: a carton counted as a unit, or a short delivery from the vendor |
| Many SKUs, small, in one zone | A receiving or put-away error in that zone |
| Many SKUs, growing, across zones | Theft, or unrecorded damages and returns |
| System high, physical low, on fast movers | Unrecorded sales, a channel not integrated, or a bundle consumed as components |
| System low, physical high | Unrecorded returns, or a cancelled order still deducted |

The pattern names the cause. The count only produces the pattern if the sheet records location and class.

## Anti-patterns

- Counting everything once a year and calling it inventory control.
- Adjusting to match the system, which makes the system the truth and the shelf the error.
- Counting during a dispatch peak, when the floor is a moving target.
- Recording a variance without a location, which makes the pattern invisible.
- A count that stops the warehouse for two days a year, twice, and finds the same causes each time.
