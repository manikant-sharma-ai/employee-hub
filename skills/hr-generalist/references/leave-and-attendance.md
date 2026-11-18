# Leave and Attendance

Leave is where trust in HR is won or lost, because it is the one policy every employee checks against their own memory every month.

## The ledger, and why it must be one

Keep a single ledger per employee per leave type, with these columns and no others:

| Column | Meaning |
|---|---|
| Opening | Balance carried in, as at the period start |
| Accrued | Credited this period, with the rule applied |
| Availed | Taken, with the date and the approval reference |
| Encashed / lapsed | Removed, with the rule that removed it |
| Closing | Opening + accrued - availed - encashed - lapsed |

If opening + movement does not equal closing, the line is wrong and must be shown as wrong. Never plug a difference into "adjustment" - that is how a ledger stops being evidence.

## Reconciliation between two sources

The common real case: the HRMS says one thing, employees say another, and the spreadsheet in between is the truth nobody trusts. Method:

1. Take both exports as at the same date. If the dates differ, the comparison is invalid - say so.
2. Match on employee ID, never on name. Report unmatched records on both sides separately.
3. For each employee, compare closing balance per type. Sort by absolute difference, largest first.
4. For the top differences, trace one transaction at a time until the first divergence: a missed accrual, a double approval, a leave type mapped wrongly, or a manual edit.
5. Classify every difference into one of those four causes. The classification is the deliverable, because it tells the business which process is broken.
6. Produce the corrected ledger and a one-page note: total employees, matched, unmatched, total days in dispute, and the causes with counts.

## Attendance

- **Pick one source of truth** - biometric, an app, or a signed register. Two sources produce an argument every payroll cycle.
- **Define the exceptions before the month starts**: late, half-day, missed punch, work-from-home, on-site travel, comp-off. Each needs a rule and an approver.
- **Regularisation is an approval, not a correction.** It carries the name of who approved it and why. An unexplained regularisation is an audit finding.
- **Overtime and comp-off** need a trigger, a rate and an expiry. Comp-off with no expiry accumulates into a liability nobody has budgeted.

## Encashment and carry-forward

Both are money. State three things: the cap, the basis of calculation (basic, gross, or a defined wage), and the event at which it is paid (annual, on exit, or at the employer's option). A carry-forward cap with no lapse rule means the balance grows forever, and the day the employee leaves it becomes a settlement dispute.

## Common defects worth naming

- Leave year differs from financial year, and nobody wrote down which one the accrual follows.
- Probationers accruing leave they are not yet entitled to take.
- Sick leave requiring a medical certificate at a threshold that was never stated.
- A leave type that exists in the HRMS, is used by employees, and appears in no policy.
- Maternity benefit handled as ordinary leave rather than under the statutory scheme.

## What to hand over

The reconciled ledger, the cause classification with counts, the corrected rule set, and the one change that would prevent the same divergence next month.
