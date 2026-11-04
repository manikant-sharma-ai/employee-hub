# Payroll and statutory entries

Payroll is not one entry; it is a chain of five, and a missing link shows up as a
statutory notice three months later.

## The chain, in order

| Step | Entry | When |
|---|---|---|
| 1. Salary booked | Salaries & wages Dr / Salary payable Cr | Month end |
| 2. Deductions booked | Salary payable Dr / PF payable, ESI payable, PT payable, TDS payable Cr | Month end |
| 3. Net paid | Salary payable Dr / Bank Cr | Payday |
| 4. Statutory paid | PF payable, TDS payable Dr / Bank Cr | By the due date |
| 5. Returns filed | No entry, but the challan and the return are filed together | Monthly/quarterly |

If step 2 is skipped, the salary payable account never clears and the balance sheet
carries a phantom liability that someone will "fix" with a journal at year end.

## Accounts to keep separate

- **Salaries and wages** (expense) - never mix with director's remuneration.
- **Salary payable** (liability) - clears to zero every payday.
- **PF payable, ESI payable, PT payable, TDS payable** - one account each, so a mismatch is visible per statute.
- **Staff advances and loans** (asset) - recovered through payroll, tracked per person.
- **Reimbursements** - an expense in the right head, not part of salary.

## Documents behind each entry

Payroll register, bank statement or bank file, PF/ESI challans, TDS challan, the
professional tax receipt by state, and signed payslip acknowledgements where the
business takes them.

## Common errors

- PF computed on gross instead of the eligible wage base.
- TDS deducted but the challan booked against the wrong month.
- Reimbursements booked as salary, inflating the wage base for the next year.
- Contractor invoices booked as payroll, losing the TDS trail.
- Round-number salary entries with no register to support them.

## Reconciliation, monthly

1. Register total = sum of net pay = bank debit. Three numbers, one line.
2. Statutory payable accounts = challans paid and not yet filed.
3. TDS payable = 26AS/TRACES balance. If they differ, the difference is the finding, not a rounding.

## Anti-patterns

- One "salary" journal for the whole year.
- Deductions netted off the expense instead of booked as liabilities.
- Paying PF late and booking the penalty as bank charges.
- No per-employee ledger, so a full-and-final settlement cannot be verified.
- Suspense account used for anything payroll-related.
