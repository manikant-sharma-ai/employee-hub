# Discrepancies: four causes, one investigation

"Shrinkage" is not a cause. It is the word a warehouse uses when it has stopped investigating.

## The four causes

| Cause | What it looks like | Where the evidence is |
|---|---|---|
| Pick error | Wrong item, wrong quantity, wrong bin picked | Scanner log, packing sheet, the customer's photo |
| Receipt error | Vendor short-shipped, carton counted as a unit, a GRN posted twice | The inward record, the vendor's invoice, the gate entry |
| Unrecorded movement | Damage, return, sample, warranty replacement, staff purchase | The damage bin, the returns register, WhatsApp approvals |
| System error | Unit-of-measure mismatch, a bundle deducting components, a cancelled order still deducted | The item master, the last change to it, the integration log |

Every variance resolves into one of these four, or it stays open. "Unknown" is allowed for a week, then it is
escalated, not written off.

## The 24-hour investigation

1. **Pull the last movement** for that SKU and location - receipt, pick, transfer, return.
2. **Check the item master** for unit of measure, pack size and bundle rules. A "case" counted as a "piece" explains
   more variances than theft ever does.
3. **Look at the bin physically**: neighbouring bins, the overflow, the damage corner, the returns trolley.
4. **Ask the two people who touched it**, without accusation, and write down what they say.
5. **Decide the cause and the fix.** A cause with no fix is a note; a fix with no owner is a wish.

## Short picks

A short pick is a pick against a system quantity that the shelf cannot fill. It is always a symptom.

| Sequence | Meaning |
|---|---|
| Short pick, then the count is also short | The stock never existed - a receipt or system error |
| Short pick, but the count is correct | The picker looked in the wrong place, or the item is in overflow |
| Short pick repeats on one SKU | The location is wrong, or the item is in two places without a record |

Repeated short picks on one SKU are the cheapest early warning in a warehouse. Track them weekly by SKU.

## Damages and the damage bin

- **A physical damage bin with a register**, one line per unit: SKU, quantity, cause, date, who recorded it, photo.
- **Grade on receipt** for anything returned: sellable, refurbishable, scrap. Unrecorded returns are the largest
  hidden source of "missing" stock in a D2C business.
- **Write off monthly**, with a cause code and an approver, not quarterly in a panic.

## Mis-ships and wrong addresses

Two failures that look the same and are not:

| Failure | Cause | Fix |
|---|---|---|
| Right customer, wrong item | Pick or pack error | Scan at pick, count at pack, weight check |
| Right item, wrong customer | Label swapped at pack, or two orders staged together | One order per staging slot, label printed after the check |
| Right item and customer, wrong address | Address changed after label print | Re-print on change; never hand-write a label |

The cost is never just the reverse pickup. It is the second shipment, the review, and the customer who now checks
the box on camera.

## The variance log

One sheet, one row per variance: date, SKU, location, system quantity, counted quantity, difference, class, cause
code, investigation owner, fix, date closed, approver. Sorted by rupee value, reviewed weekly for ten minutes.

That log is the warehouse's memory. Without it, the same cause is discovered every quarter by a different person.

## Anti-patterns

- Writing off at month end to close the books, with no cause.
- Blaming the picker before checking the item master.
- Investigating a variance that is inside the threshold, while three outside it wait.
- A damage bin with no register, which is a pile with a name.
- Fixing the count instead of the process, so next month's count finds the same gap.
