# The cash position and the thirteen-week view

The monthly P&L answers a question nobody asked. This file builds the view that answers the one that
gets asked: what do we have, what is coming, what leaves, and which week breaks.

## Why thirteen weeks

Thirteen weeks is a quarter, which is as far ahead as a small business's dated commitments are real.
Beyond that, inflows become a forecast of a forecast. Inside it, almost everything has a date: a
payroll run, a challan, an EMI, a rent cheque, a purchase order's credit period.

| Horizon | What it is good for | What it hides |
|---|---|---|
| Balance today | Whether a payment can clear now | Everything about next week |
| Weekly, 13 weeks | The actual management view | Nothing important at this scale |
| Monthly, 12 months | Board and bank conversations | The week where payroll and GST collide |
| Annual | Planning | Every cash hole inside it |

## The build, line by line

| Line | Source | Rule |
|---|---|---|
| Opening cash | Bank statements, dated | Include only cleared balances; note uncleared cheques |
| Collections - confirmed | Signed POs, dispatched invoices | Book in the week the credit period ends |
| Collections - promised | Customer emails, WhatsApp | Book at the customer's historical delay, not the promise |
| Other inflows | Refunds, claims, subsidy, loan drawdown | Book only if the sanction exists and the date is known |
| Payroll | Payroll register, pay date | Net pay plus statutory, in the week it debits |
| Statutory | GST, TDS, advance tax, PF, ESI, PT | On the due date, never the filing date |
| Debt service | EMI schedule, interest | On the debit date; include the quarter's interest on OD |
| Vendors | Payables ageing with due dates | Due date, not invoice date |
| Rent, utilities, subscriptions | Contracts and mandates | On the debit date |
| Capex and one-offs | Approved POs | Only if committed; label planned separately |
| Founder drawings | The house rule | Never omit it; it is a real outflow |
| Closing cash | Arithmetic | Opening + inflows - outflows |

## Reading the result

1. **Mark the minimum point.** The lowest closing balance and the week it occurs. That number and
   date are the headline of every position.
2. **Test the minimum against the floor.** The floor is not zero. It is the buffer that absorbs a
   bounced inflow: typically two weeks of unavoidable outflows for a trading business.
3. **Separate the structural from the timing hole.** A week that is short because a customer paid
   late is a timing problem with a phone call as the fix. A quarter that trends down every week is
   structural, and no scheduling fixes it.
4. **Show the "without promises" case.** Rebuild the view with every promised inflow removed. If that
   case is negative, the business is running on hope with a spreadsheet attached.

## Worked example (illustrative figures)

| Week | Opening | Inflows | Outflows | Closing | Note |
|---|---|---|---|---|---|
| W1 | 4.20 | 1.80 | 2.10 | 3.90 | |
| W2 | 3.90 | 0.60 | 3.40 | 1.10 | Payroll 1.9, PF 0.2 |
| W3 | 1.10 | 2.40 | 1.20 | 2.30 | Confirmed PO collection |
| W4 | 2.30 | 0.30 | 2.60 | **0.00** | **Minimum** - GST 1.1, vendor 1.2 |
| W5 | 0.00 | 1.50 | 1.30 | 0.20 | Promised receipt only |

The answer is not "we are fine on average". It is: W4 is at zero and only works if the W5 promise
lands early, so the action this week is to move the W4 vendor payment to W6 in writing, before the
GST challan date, and to confirm the W3 collection is not itself late.

## Anti-patterns

- **The monthly average.** "We have about 3 lakh a month spare" while W4 is at zero.
- **The promised receipt at face value.** Booking a payment on the date the customer said, in a
  business where that customer has never once paid on the date they said.
- **Statutory dues on the filing date.** The challan debits before the return is filed.
- **Ignoring the card settlement cycle.** Two to three days is enough to bounce a payment scheduled
  against the sale date.
- **The single account.** Three accounts, one read. The position is the sum or it is wrong.
- **No founder drawings.** A business that looks solvent because the owner has not been paid is not.
- **Rebuilding from memory each week.** Keep one sheet, roll it forward; the history is the accuracy
  measure.
