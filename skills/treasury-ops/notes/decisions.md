# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-13 | What this role owns, given `finance-ops`, `budget-planner` and `collections-agent` | The week in cash: position, payment schedule, surplus, limits, FX | Recording is backward, the budget is a year, chasing is one receivable; none of them decides what clears today |
| 2026-11-13 | Horizon | Thirteen weeks, weekly | A quarter is as far as dated commitments are real; beyond it, inflows are a forecast of a forecast |
| 2026-11-13 | Inflow treatment | Promised receipts at historical delay, with a confidence mark | Booking promises at face value is what makes a cash forecast wrong in the same direction every month |
| 2026-11-13 | Priority ladder | Statutory, payroll, secured debt, supply-stopping, rent, vendor terms, discretionary | It is the order that minimises total cost, not the order of who complains loudest |
| 2026-11-13 | Surplus | Layered by horizon; nothing locked beyond the horizon it is needed | A better rate is not worth a broken FD in the month the cash was needed |
| 2026-11-13 | Payment execution | Never - this role schedules, a human releases | No signing power means no single point of failure |
| 2026-11-13 | Payee changes | Callback on a number already on file, test payment above threshold | Vendor-email fraud is the largest per-incident loss in this function |
| 2026-11-13 | Data in the repo | Rules in notes, figures in the sheet | The repo is public; balances and account numbers never leave the workbook |
