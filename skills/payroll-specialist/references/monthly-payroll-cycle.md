# The monthly payroll cycle

Payroll fails for one reason: the date is fixed and the inputs are not. This file fixes the inputs.

## The calendar

| Day | Task | Owner | If it slips |
|---|---|---|---|
| 20th (prior month) | Attendance, leave, overtime closed for the month | HR or the manager | Late inputs become an off-cycle run or a next-month correction |
| 22nd | Variable pay approved - incentives, reimbursements, commissions | Function head | Unapproved variable pay is not paid; it is held with a note |
| 24th | Joiners, exits, revisions, transfers confirmed in writing | HR | A verbal joiner is a payroll error waiting for a date |
| 25th | Register computed, reviewed, control totals checked | Payroll | |
| 26th | Register approved by the founder or finance head | Founder | |
| 27th | Bank file generated and reconciled; payslips generated | Payroll | |
| 28th-1st | Salary credited per contract | Bank, released by a human | |
| 1st-2nd | Payslips issued; queries answered | Payroll | |
| 7th | TDS deposited | Finance or CA | Interest from day one |
| 15th | PF and ESI deposited | Finance or CA | Interest and damages |
| State date | Professional tax paid | Finance or CA | State-specific penalty |
| Quarterly | 24Q filed; 26Q for contractors | CA | Late fee per return |

## The register, column by column

| Block | Columns | Rule |
|---|---|---|
| Identity | Code, name, designation, location, state, DOJ, days paid | State drives professional tax; days paid drives pro-rata |
| Earnings | Basic, DA, HRA, special allowance, conveyance, other allowances, incentive, overtime, arrears | Arrears shown separately, never merged into the month's component |
| Gross | Sum of earnings | Reconciles to the structure's gross for a full month |
| Employee deductions | PF, ESI, professional tax, TDS, loan or advance, other recovery | Each with a rule; recovery only with a written basis |
| Net | Gross minus deductions | The number the bank file must match |
| Employer contributions | PF employer, ESI employer, EDLI, admin, gratuity provision | Not a deduction; the real cost |
| Cost to company | Gross plus employer contributions | The budgeting number |

## Controls before the file leaves

1. Headcount matches the master plus joiners minus exits. A person who left last month and appears
   again is the most common payroll fraud, and it is usually an oversight.
2. No net pay is negative; a negative net is a recovery problem, not a payroll line.
3. No net pay is zero without a reason on the row (unpaid leave, full recovery).
4. Every variance against last month above the threshold (typically 10% or ₹5,000) has a cause.
5. The bank file's account numbers match the master exactly; new accounts are verified by callback.
6. Register total = bank file total = approved amount.
7. Two people have looked at it: the preparer and the approver.

## Off-cycle runs

Legitimate: a joiner after the cut-off, a missed incentive, a correction agreed with the employee, a
full-and-final settlement. Not legitimate: an input that was late because nobody chased it. An
off-cycle run costs bank charges and attention; count them monthly and fix the input, not the run.

## Anti-patterns

- **Last month plus edits.** A wrong component or a stale structure survives indefinitely.
- **Paying on a verbal instruction.** Every change in writing, dated.
- **Merging arrears into the month.** It distorts PF, TDS and the variance story all at once.
- **Rounding the control total.** A ₹1 difference hides a wrong row.
- **Payslips issued before the credit.** If the credit fails, the payslip is already a broken promise.
- **No approver.** A one-person payroll is a control gap, however honest the person.

## The first run in a business that has none

Setting up payroll from scratch is a sequence, and the sequence matters:

1. **Collect the master** - every person, their structure, identifiers and bank account, verified
   against the appointment letter, not against a chat message.
2. **Register the establishment** - PF and ESI codes, professional tax registration in each state
   where people sit, and the labour registrations that apply.
3. **Fix the cycle** - the pay date, the input cut-off, the approver, and the bank file format.
4. **Run one month manually** - a spreadsheet, checked twice, before any payroll product is trusted.
5. **Reconcile the first challans** by hand against the register; the portal and the sheet must agree
   before the second month.
6. **Write the calendar** into the team's shared calendar, so the dates are everyone's and not the
   payroll person's memory.

A business that starts with software and no cycle spends the first quarter fixing the software instead
of the process.
