# Reverse logistics and pickup

The refund is easy. Getting the unit back is where returns actually fail, and where the money quietly
disappears.

## The reverse flow, in order

| Step | Who | Failure mode | Control |
|---|---|---|---|
| Request approved | Returns | Approved with no pickup booked | Approval and pickup booking in one action |
| Pickup scheduled | Courier | No attempt for 3 days | Attempt log checked daily, not weekly |
| Attempt 1 | Courier | Customer unavailable, address wrong | SMS with a slot, not a surprise visit |
| Attempt 2-3 | Courier | Repeated failure, then RTO | Escalate to the courier's nodal desk after attempt 2 |
| In transit | Courier | Lost or damaged in reverse leg | Insure high-value reverse legs; log the AWB |
| Received | Warehouse | Not logged on arrival | Scan-in on the same day |
| QC graded | Warehouse | Graded days later, value decayed | Grade within 48 hours of receipt |
| Disposition | Returns | Sits in a returns bin | A disposition decision with a date |

## Reverse freight, the numbers that decide the carrier

Reverse pickup is priced differently from forward: per kg, per attempt, and by pin-code serviceability.
A ₹140 reverse pickup on a ₹900 product with a 22% margin is a third of the contribution. Compare the
courier's reverse rate against its attempt success rate: a cheap carrier that fails twice costs more
than an expensive one that succeeds.

Where a return is not worth collecting - low value, high freight, unsaleable - a "refund without
return" is often cheaper than the pickup. Decide it with the arithmetic, not with a feeling, and
record it as a write-off with a reason.

## QC grading

| Grade | Condition | Disposition | Recovered value |
|---|---|---|---|
| A | Unopened or as-new, tags intact | Restock as new | 100% |
| B | Opened, unused, packaging damaged | Restock with a note, or sell as open box | 85-95% |
| C | Used, washed, minor defect | Refurbish, or sell as second | 40-70% |
| D | Materially damaged or incomplete | Return to vendor, spare parts, or scrap | 0-30% |

Grade against a written checklist, with a photo per grade. A grader's opinion without a checklist is a
dispute with the warehouse and with the customer.

## RTO is not a return, but it costs like one

A return-to-origin happens when delivery fails: refused, unavailable, wrong address, or a COD refusal.
It carries forward freight, reverse freight, two handling charges and a re-listing. The fix is upstream
- address confirmation, COD verification, a delivery slot - and the read belongs in the same weekly
number as returns, or the true cost is understated by half.

## Packaging for the reverse leg

The unit travels back in whatever the customer has. Assume the worst: a poly bag with a garment inside
will arrive damaged if the forward packaging was not reusable. Where the product is fragile or high
value, a returnable box or a pickup kit pays for itself in the first month of returns.

## Anti-patterns

- **Approving a return with no pickup date.** The ticket ages and the customer's patience does not.
- **Weekly attempt-log reviews.** Three days of silence is the difference between a pickup and an RTO.
- **Grading by memory.** "It looked fine" with no photo and no checklist.
- **Collecting a ₹300 item for ₹180.** Refund without return and write it off.
- **No AWB on the reverse leg.** A lost unit with no tracking is a refund with no recovery.
- **Ignoring RTO in the returns number.** It is the same cost with a different name.
