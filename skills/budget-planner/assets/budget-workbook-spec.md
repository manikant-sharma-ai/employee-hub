# Budget workbook spec

The sheet layout this employee builds. Copy the structure, not the numbers.

## Sheet 1 - Frame

| Field | Value |
|---|---|
| Entity | <legal entity> |
| Financial year | <FY27, April 2026 to March 2027> |
| Currency | INR, lakh |
| Scope | P&L and cash |
| Approver | <founder / board> |
| Approval date | <date> |
| Version | <draft 1 / approved 2026-03-28> |

## Sheet 2 - Drivers

| Driver | Last year actual | This year | Change | Reason | Owner | Sensitivity if 20% wrong |
|---|---|---|---|---|---|---|
| Sessions per month | 210,000 | 260,000 | +24% | two new collections plus 15% ad spend | growth | revenue +/- 8% |
| Conversion | 1.9% | 2.1% | +0.2pp | PDP rebuild in Q1 | growth | revenue +/- 10% |
| AOV | 1,850 | 1,900 | +3% | bundle launch | merch | revenue +/- 3% |
| Return rate | 11% | 9% | -2pp | size guide | ops | margin +/- 2pp |
| Headcount | 24 | 31 | +7 | hiring plan, months 3, 5, 8, 10 | founder | cost + 12% |
| Ad spend per month | 6.0 | 8.5 | +42% | paid search expansion | growth | revenue +/- 6% |

## Sheet 3 - Monthly build

| Line | Apr | May | ... | Mar | FY total |
|---|---|---|---|---|---|
| Revenue - D2C | | | | | |
| Revenue - marketplace | | | | | |
| Less returns and RTO | | | | | |
| Net revenue | | | | | |
| COGS (variable, per unit) | | | | | |
| Gross margin | | | | | |
| Payroll (step, by hire month) | | | | | |
| Marketing (envelope, seasonal) | | | | | |
| Fulfilment (variable per order) | | | | | |
| Rent and utilities (fixed, escalated) | | | | | |
| Software (fixed) | | | | | |
| Other (envelope) | | | | | |
| EBITDA | | | | | |

Every row carries its driver and its behaviour in the row label. A row nobody can
explain is deleted.

## Sheet 4 - Envelopes

| Envelope | Owner | Annual | Monthly shape | What the number buys | Confirmed |
|---|---|---|---|---|---|
| Marketing | <growth lead> | 102.0 | seasonal, 3x in Oct-Dec | 8.5 lakh/month baseline plus festival | yes, 2026-03-24 |
| Payroll | <founder> | 214.0 | step at months 3, 5, 8, 10 | 31 heads, bands as per plan | yes |
| Fulfilment | <ops lead> | 58.0 | per order, 0.62 lakh/1,000 orders | courier plus packaging | yes |
| Premises | <founder> | 36.0 | flat plus 8% from month 7 | rent, CAM, power | committed |

## Sheet 5 - Cash

| Line | Apr | May | ... | Mar |
|---|---|---|---|---|
| Opening cash | | | | |
| Collections (revenue x 82% in month, 18% next) | | | | |
| Supplier payments (creditor days 30) | | | | |
| Payroll and statutory | | | | |
| GST and TDS paid | | | | |
| Capex and deposits | | | | |
| Loan repayment | | | | |
| Closing cash | | | | |
| Headroom over minimum balance | | | | |

## Sheet 6 - Scenarios

| Case | Trigger | Revenue | EBITDA | Lowest cash | Actions |
|---|---|---|---|---|---|
| Base | plan | | | | manage to envelopes |
| Downside | 10% under for two months | | | | freeze hiring, cut discretionary 30% |
| Severe | 25% under, or cash under 2 months fixed cost | | | | cut order as written |

## Sheet 7 - Variance (in-cycle)

| Line | Plan | Actual | Variance | Cause | Owner | Action | Date |
|---|---|---|---|---|---|---|---|
| | | | | volume / rate / mix / step / timing / one-off | | | |
