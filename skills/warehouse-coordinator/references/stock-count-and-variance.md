# Stock count and variance

A stock count is not an audit of people. It is a measurement of a process, and its output is a list of differences
with a cause and a rupee value - not a number that goes to the accountant and a shrug that goes to the owner.

## Before the count

- **Freeze the movement.** No receipts, no issues, no transfers during the count window, or a cut-off time written
  down and applied to both the system export and the count sheet. A count against a moving system reconciles to
  nothing.
- **Export the system stock the same day.** Not last week's report. The export carries the timestamp.
- **Fix the unit of measure** for every SKU before counting: piece, box, case, strip, kilogram, metre. Write the
  conversion factor beside the SKU, and count in the unit the system uses.
- **Count blind where you can.** The counter should not see the system quantity; a counter who knows the expected
  answer finds it.

## The variance arithmetic

For each SKU: `variance units = physical - system`, `variance value = variance units x unit cost`. Report negative
variances (short) and positive (excess) separately - excess is usually a paperwork error, not a gift, and it hides
a short somewhere else.

Then classify by value, not by count. A hundred missing bolts is not the same finding as one missing motor, and a
report ordered by unit variance will bury the motor.

## Tolerance, by class

| Class | Rule of thumb | Tolerance | Count frequency |
|---|---|---|---|
| A | top 70-80% of value | 0-1% by value | monthly, or continuous |
| B | next 15% | 2-5% | quarterly |
| C | the long tail | 5-10% | twice a year |

The tolerance decides the action, not the honesty of the counter: inside tolerance, `clear`; just outside,
`recount`; well outside, `investigate`.

## Recount before adjustment

1. **A second person**, blind, on a different day, on the same unit of measure.
2. **Same result twice** - the variance is real. **Different result** - the counting process is the problem, and
   that is the finding.
3. **Only then** propose the adjustment, with the reason code, the evidence and the approver's name.

## The four causes, in order

| Cause | Test | Typical evidence |
|---|---|---|
| Paperwork | Does the movement history explain it? | A receipt entered twice, an issue never recorded, a return booked to the wrong SKU |
| Misplacement | Is it in another bin? | Found during the recount in the neighbouring location |
| Damage | Is it in the damage or scrap bin, unrecorded? | A physical unit, broken, never written off |
| Unexplained | None of the above | Recorded as shrinkage, with a value and a date |

The first three are process failures with cheap fixes. The fourth is the only one worth a security conversation,
and it should be small if the first three are done properly.

## The count pack

The variance table, the recount list, the causes, the adjustment proposal and one process change - one page, in
that order. The adjustment proposal is a proposal: `bookkeeper` posts it after the owner approves, and the approval
is recorded in `decisions.md` with the date.
