# COD remittance and freight reconciliation

Two flows of money move through this role: cash the carrier collected for you, and freight you owe the carrier.
Both leak silently.

## COD remittance: what to check

| Check | What goes wrong | How to catch it |
|---|---|---|
| Order count | Remittance covers fewer orders than delivered | Match AWB to order ID, order by order |
| Amount | Collected amount differs from the order value | Compare against the order, not against the remittance total |
| Fee | COD fee charged at a different rate than agreed | Recompute at the contracted rate |
| Cycle | Remitted later than the agreed cycle | Count days from delivery to remittance |
| Deductions | Freight, RTO, weight disputes netted off without notice | Ask for the deduction statement, line by line |
| Missing AWBs | Delivered but never remitted | Aged list, escalated weekly |

Reconciliation is per order, not per total. A total that matches can hide two orders swapped and one missing.

## The reconciliation sheet

| AWB | Order ID | Delivered on | COD value | Fee | Expected net | Remitted | Cycle days | Status |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Status values: `matched`, `short`, `missing`, `fee-mismatch`, `in-dispute`. Anything not `matched` after the cycle
plus three days is escalated.

## Freight invoice audit

| Line | Check | Common error |
|---|---|---|
| Billable weight | Against the weight slip and the volumetric calculation | Billed on a higher slab than measured |
| Zone | Against the carrier's zone chart for the pin code | Wrong zone for a border district |
| Service | Against what was booked | Charged air for a surface booking |
| Fuel surcharge | Against the rate in force that month | Old rate, or a rate not in the contract |
| COD fee | Against the contract | Percentage applied where a flat fee was agreed |
| ODA | Against the pin code list | Charged for a serviceable pin code |
| RTO | Against the exception log | Charged twice for the same return |
| Duplicates | Same AWB invoiced twice | Happens in monthly consolidated invoices |

A 5-10% error rate on freight invoices is common in a business that has never audited them. That is margin, and it
is recoverable if the dispute window is respected.

## The dispute process

1. **Identify** the lines that differ, with the evidence: the weight slip, the manifest, the rate card, the
   booking confirmation.
2. **Quantify** - rupees, per line, with a total. A dispute without a number is an email.
3. **File** inside the carrier's window, in writing, referencing the AWBs. Most carriers have a stated window;
   missing it loses the money.
4. **Track** the dispute in the same sheet, with the date filed and the date resolved.
5. **Escalate** through the account manager when a dispute passes its stated resolution time.
6. **Adjust** the process if the same error repeats - a repeated weight dispute is a packing or a data problem.

| Dispute | Evidence required | Typical outcome |
|---|---|---|
| Weight | Weight slip, photos of the parcel on the scale | Rebill at the measured weight |
| Zone | The carrier's own zone chart | Credit note |
| Service | Booking confirmation | Credit note |
| Duplicate | Two invoice references for one AWB | Full credit |
| ODA | The pin code's serviceability status | Credit note |
| Damage | Photos, claim filed in window | Partial to full value |

## Cash flow discipline

- **COD is a working-capital trap.** Money collected by the carrier is not money in the bank until it is remitted,
  and the cycle is typically days to weeks. A business scaling COD without watching the cycle can run out of cash
  while its sales grow.
- **Prepaid conversion is a logistics lever.** Every order converted from COD to prepaid removes a remittance
  cycle, a fee, a refusal risk and a cash gap. Offer a small incentive, measure the effect, and report it.
- **The unremitted balance is a number on the monthly read**, aged by carrier, because it is a receivable with a
  weak counterparty.

## The monthly close

| Step | Output |
|---|---|
| COD reconciliation for the month | Matched, short, missing, disputed, with rupees |
| Freight audit for the month | Invoiced, expected, disputed, recovered |
| Ageing of unremitted COD | By carrier, by days |
| The rate actually paid | Effective rate per kg and per shipment, by carrier and lane |
| The two actions | One process fix, one escalation |

Hand the closed numbers to `bookkeeper` and `finance-ops` so the freight expense and the COD receivable in the
books match the operations reality. A freight number that only exists in a spreadsheet is not a number the
business can manage.

## Anti-patterns

- Reconciling COD by total, so a short remittance hides inside a big month.
- Paying a freight invoice because it is due, and auditing it never.
- Missing the dispute window because the audit happened after month-end.
- Treating COD fees as a rounding error when they are a visible share of margin on low-value orders.
- Letting one carrier hold an unremitted balance for months because the account manager is responsive on other
  things.
- Booking freight as a single expense line, so nobody can see which carrier or lane is expensive.
- Auditing only the biggest invoices, where the errors are proportionally the smallest.
