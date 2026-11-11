# GST and TDS on expenses

This file exists so the auditor can spot a tax defect on an invoice and route it to the CA with
the document in hand. It is a checklist, not an opinion. The CA decides; the founder signs.

## Invoice validity, the five fields that void a credit

| Field | Requirement | What goes wrong |
|---|---|---|
| GSTIN of the supplier | Valid and active at the invoice date | Cancelled GSTIN, credit at risk |
| GSTIN of the recipient | Must be the business's registered GSTIN | Billed to a personal name |
| Invoice number and date | A consecutive series, dated | No series, or a date outside the return period |
| Taxable value, rate and tax | Rate correct for the HSN/SAC | Wrong rate, or a composite rate |
| Place of supply | Determines CGST+SGST vs IGST | Intra-state billed as inter-state |

A tax invoice without these is a payment problem even when the expense is genuine.

## Blocked and restricted credits, flagged not decided

| Category | Usual position | Action |
|---|---|---|
| Employee personal expenses | Not a business credit | Do not book as a credit |
| Motor vehicles and fuel, small fleets | Restricted in many cases | Flag for the CA |
| Food and beverages, outdoor catering | Restricted | Flag |
| Club membership and health | Restricted | Flag |
| Works contract for immovable property | Restricted in part | Flag |
| Free samples and gifts | Distinct treatment | Flag |
| Insurance, where exempt | No credit | Do not claim |

The list changes with notifications and circulars. The rule for this role: **flag the category
and the amount, name the CA, never assert the answer.**

## TDS, where it commonly bites a small business

| Payment | Section to ask about | Trigger to check |
|---|---|---|
| Professional and technical fees | 194J | Any CA, lawyer, consultant, designer invoice |
| Contract labour and job work | 194C | A contractor with a bill above the threshold |
| Rent of premises or machinery | 194I | A landlord invoice, including a co-working bill |
| Commission and brokerage | 194H | Marketplace or agent commission |
| Interest other than bank | 194A | A loan from a director or a relative |
| Purchase of goods, larger entities | 194Q | Above the turnover threshold, and a large seller |
| E-commerce operator payments | 194O | Marketplace settlements |

Two checks that catch most of it: **is there a TDS line against every vendor invoice that needs
one**, and **does the vendor's PAN exist and match the name**. A missing TDS is a disallowance
and interest, not a rounding error. Thresholds and rates change - the CA confirms the current
position, and the auditor records what was asked.

## What a missing TDS or GST defect costs

| Defect | Consequence |
|---|---|
| TDS not deducted | 30% of the expense disallowed, plus interest |
| TDS deducted late | Interest for the delay, per month or part |
| GSTIN inactive at invoice date | Input credit reversed, with interest |
| Credit claimed on a blocked category | Reversal, interest and a penalty exposure |
| Invoice without a valid GSTIN | No credit, and a supplier quality question |
| Expense booked to a personal GSTIN | The business cannot claim; the individual may be liable |

## The audit rows that carry this

Add to the exceptions register:

| Finding | Evidence | Route |
|---|---|---|
| Vendor invoice with an inactive GSTIN | GST portal status, invoice | Stop payment of the tax component; ask for a revised invoice |
| Expense with no TDS line | Vendor invoice, payment record | CA to compute the shortfall; deduct and remit |
| Billed to a personal GSTIN | The invoice | Revised invoice; credit cannot be taken |
| Tax rate wrong for the HSN | Invoice vs the schedule | Revised invoice from the vendor |
| Credit claimed on a blocked head | Ledger, invoice | CA to reverse in the next return |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Giving a tax opinion | Wrong, and relied upon |
| Ignoring the tax defect because the expense is genuine | Credit lost or reversed with interest |
| Chasing the vendor's GSTIN after the return is filed | Too late for that period |
| Assuming no TDS because the vendor said so | Disallowance falls on the payer |
| Booking a personal invoice as a company expense | Two exposures, one of them the individual's |
| Treating a marketplace settlement as net revenue | Commission and TDS both disappear |
