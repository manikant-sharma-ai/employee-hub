# Monthly close

The close is a checklist run in a fixed order, on a fixed date, with a cut-off. Everything else - accruals, provisions, review - exists to make that checklist honest.

## The calendar

| Day | Step | Owner |
|---|---|---|
| Day 1-2 | Freeze the period; export bank, gateway, sales and purchase data | Finance ops |
| Day 2-3 | Bank and gateway reconciliation | Finance ops |
| Day 3-4 | Purchase bills entered; expense categorisation | Finance ops |
| Day 4-5 | Payroll, statutory dues, provisions, accruals | Finance ops + HR |
| Day 5-6 | Review exceptions with the owner | Owner |
| Day 6-7 | Trial balance, P&L, balance sheet extract, pack issued | Finance ops |
| Day 10-14 | GST working papers for the CA | Finance ops |
| Day 20 | GSTR-3B due (monthly filers) - the CA files | CA |

Days-to-close is the metric to track. An SMB under 10 days is doing well; over 20 means the process, not the people, is broken.

## The checklist

| # | Check | Done when |
|---|---|---|
| 1 | Period frozen; no postings dated inside it after cut-off | A list of late items exists, dated to next month |
| 2 | Bank reconciled | Difference is zero or itemised with amounts |
| 3 | Gateway reconciled | Gross sales, fee, fee GST and refunds all posted |
| 4 | Cash counted and reconciled | Physical count matches the cash book |
| 5 | All sales invoices raised for the period | Invoice register matches the sales record |
| 6 | All purchase bills entered | Vendor ageing ties to the ledger |
| 7 | Credit notes and returns posted | They reference the original invoice |
| 8 | Expense categorisation complete | Unsure list is short and explained |
| 9 | Payroll posted | Salary, PF, ESI, TDS on salary, professional tax |
| 10 | Accruals and provisions | Rent, utilities, professional fees, bonuses, leave |
| 11 | Prepaid and depreciation | Amortisation schedule run for the month |
| 12 | TDS deducted and recorded | Section-wise working, due date noted |
| 13 | Intercompany and director accounts | Balanced, and drawings recorded as drawings |
| 14 | Suspense account reviewed | Balance is small and every item has a question |
| 15 | Trial balance reviewed | Debits equal credits; no negative balances where impossible |
| 16 | Key ratios sanity-checked | Gross margin and expense ratios in the normal band |
| 17 | Pack issued with the exception list | Sent to the owner, dated |

## Accruals and provisions worth never skipping

| Item | Basis | Why it matters |
|---|---|---|
| Rent for the last month of the quarter | Contract, monthly | Otherwise the month looks more profitable than it is |
| Electricity and utilities | Last bill, or three-month average | Bills arrive late and land in the wrong period |
| Professional fees | Contract or estimate | CA and audit fees are large and lumpy |
| Bonus and incentives | Earned in the period | Otherwise the payout month looks like a loss |
| Leave encashment | Policy | A real liability that accrues silently |
| Discounts and returns expected | Historic rate | Revenue is overstated without it |
| Interest on borrowings | Loan schedule | Easy to forget on a quarterly-reset loan |
| Freight in transit | Known shipments | Landed cost accuracy |

Every accrual is an estimate. Label it as one, with the basis, so nobody later reads it as a fact.

## The review questions before signing off

1. **Does the gross margin make sense** against the last three months, and if it moved, why?
2. **Is any expense category more than 30% away from its normal level?** Ask before explaining it away.
3. **Is any vendor balance negative?** That is a payment without a bill, or a double payment.
4. **Is any customer balance a credit?** That is an advance or an overpayment, not a sale.
5. **Did the cash balance go negative on any day?** It means something was not recorded.
6. **Are there round-number entries?** They are usually estimates someone made up.
7. **Is the suspense account growing?** The earliest signal of a process failure.

## The pack

| Page | Contents |
|---|---|
| 1 | Period, entity, basis, and days-to-close |
| 2 | P&L with comparison to last month and last year, with variance notes |
| 3 | Reconciliation bridge and the exception list |
| 4 | Ageing: receivables and payables, by bucket |
| 5 | Cash position and the next 30 days of known outflows |
| 6 | Statutory status: GST, TDS, PF/ESI, and what is due when |
| 7 | What changed and what needs a decision |

## Anti-patterns

- **Closing on a date and then posting into it for a week.** The pack becomes a draft nobody trusts.
- **Skipping accruals because they are estimates.** Omitting them is also an estimate, and a worse one.
- **Signing off with a large suspense balance.** It converts a question into a permanent error.
- **Presenting the P&L without the comparison.** A number with no baseline cannot be read.
- **Letting the close date drift a day later every month.** Track days-to-close and fix the cause.
- **Doing the close in the owner's inbox.** The pack is a document, dated, in one place.
