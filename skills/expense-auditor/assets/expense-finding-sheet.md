# Expense finding sheet

The layout this employee produces. Copy the columns; the rows below are an illustration of
form, not a real audit.

## Header

| Field | Value |
|---|---|
| Period | <2026-07-01 to 2026-09-30> |
| Entity | <legal entity> |
| Rows tested | <1,842> |
| Total spend reviewed | <₹38,40,000> |
| Materiality threshold | <₹2,000> |
| Policy | <written and testable / no written policy - tested against six-month pattern> |
| Data source | <Zoho Expense export, 2026-10-02> |

## Findings

| # | Severity | Finding | Evidence | Rule | At risk | Recoverable | Owner | Action | Due |
|---|---|---|---|---|---|---|---|---|---|
| 1 | High | Duplicate claim | 4471 and 4462, same vendor, same amount, 3 days apart | Policy 4.2 | 4,999 | 4,999 | finance lead | recover in payroll; block pair 30 days | 2026-10-31 |
| 2 | High | Split invoice | 6 claims of 9,800-9,900 to one vendor in 11 days, sum 59,000 | Policy 3.1 approval threshold 10,000 | 59,000 | 0 | dept head | confirm one purchase; approval matrix fix | 2026-10-20 |
| 3 | Medium | Cap breach | 3 lodging claims above the metro cap, 5,400-6,200 | Policy 2.4 cap 4,500 | 4,900 | 0 | finance lead | exception register; cap review | 2026-11-15 |
| 4 | Medium | Missing receipt | 11 claims above 500 with no document | Policy 5.2 | 22,300 | 0 | finance lead | chase documents; block reimbursement | 2026-10-25 |
| 5 | Medium | Price drift | Courier rate up 9% from July with no change note | Vendor master rate card | 41,000/yr | 0 | ops lead | confirm with vendor; renegotiate | 2026-11-30 |
| 6 | Low | Subscription creep | 7 recurring charges, no owner, no login in 90 days | Vendor review | 2,40,000/yr | 2,40,000 | founder | cancel or assign | 2026-10-31 |

## Totals

| Measure | Value |
|---|---|
| Findings by severity | 0 critical, 2 high, 3 medium, 1 low |
| Amount at risk | <₹1,32,199> |
| Amount recoverable | <₹2,44,999> |
| Amount recovered to date | <₹0 - nothing requested yet> |

## Policy gaps and the sentence that closes each

| Gap | The sentence |
|---|---|
| No receipt rule above a threshold | "A receipt is mandatory for every claim above ₹500; no receipt, no reimbursement." |
| Self-approval possible in the tool | "The approver must not be the claimant; the tool blocks self-approval." |
| No vendor owner | "Every vendor above ₹1,00,000 a year has a named owner in the master." |

## What the tests could not see

- Work invoiced and never performed at a plausible rate.
- A personal purchase inside a plausible category with a receipt.
- Payments made outside the system: cash, personal cards reimbursed in a lump sum,
  director accounts.
