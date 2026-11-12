# Payment scheduling and prioritisation

A payment run is a queue with consequences. This file is the order of the queue and the language for
the conversation when something has to move.

## The priority ladder

| Rank | Category | Why here | Cost of being late |
|---|---|---|---|
| 1 | Statutory dues - GST, TDS, PF, ESI, PT, advance tax | Non-negotiable, and the record outlives the cash | Interest, penalty, and a compliance trail that blocks loans and tenders |
| 2 | Net payroll and salary | The one payment whose failure costs the team | Attrition, and a labour dispute that costs more than the delay saved |
| 3 | Secured debt - EMIs, vehicle, machinery loan | Security is at stake | Bounce charges, credit-bureau marks, recall risk |
| 4 | Anything that stops supply, service or a legal obligation | The business stops | Line stoppage, service cut, statutory notice |
| 5 | Rent and utilities | Escalates fast and cheaply | Eviction risk, disconnection, deposit loss |
| 6 | Vendor bills within terms | Relationship and cost of capital | Interest, credit hold, worse terms next order |
| 7 | Vendor bills past terms | Already a problem | Supply hold, legal notice, reputational |
| 8 | Discretionary, capex, subscriptions | Can wait by definition | Nothing, usually |

Two exceptions override the ladder and must be written down when used: a payment whose delay causes a
larger certain loss than a higher-ranked payment's delay (a raw-material bill that stops a line
shipping a confirmed order), and a payment whose delay is illegal under a specific contract clause.

## The weekly run

1. **Freeze the list** on a fixed day - Monday for a Friday run, or whatever the bank's cut-off is.
   Payments after the freeze go to next week unless a rule says otherwise.
2. **Reconcile the list against the ledger.** A payment run built from emails duplicates what was
   already paid and misses what was invoiced.
3. **Apply the ladder**, then check headroom against the thirteen-week minimum.
4. **Mark each line** clear, hold, or renegotiate - and for a hold, write the date it moves to.
5. **Confirm the bank cut-offs.** NEFT batches, RTGS windows, same-day limits, and bank holidays.
   A payment released at 18:40 on a Friday lands Monday.
6. **Release to a human approver** with the schedule attached. This role never releases.

## Renegotiating a payment without losing the vendor

The script has four parts, in this order: the specific date it will be paid, the reason stated
plainly but briefly, what the vendor gets for waiting, and what happens if that date is missed.

| Element | Bad | Good |
|---|---|---|
| Date | "soon", "next month" | "the 14th, by RTGS" |
| Reason | "cash flow issues" | "a large customer collection moved to the 12th" |
| Consideration | nothing | part payment now, or priority on the next order |
| Fallback | silence | "if it slips again I will call you that day" |

Rules: renegotiate before the due date, never after; put it in writing; never promise a date the
thirteen-week view does not support; and never let a renegotiation become a habit without repricing
the vendor's terms.

## Early-payment discounts

Test it as an annualised rate, never as a percentage:

```
annualised cost of NOT taking it = discount% / (100 - discount%) x 365 / (days saved)
```

2% for paying 38 days early is about 21% annualised - take it if the overdraft costs 11.5%. 1% for 10
days early is about 45% - take it if there is cash, ignore it otherwise. Compare against the real
cost of the money, not against zero.

## Anti-patterns

- **Paying the loudest vendor first.** Volume is not priority; the ladder is.
- **Paying everyone a little.** Partial payments to all suppliers create disputes with all of them.
  Pay fewer, in full, in ladder order.
- **Using statutory dues as working capital.** The cheapest-looking loan in the business and the most
  expensive one to be caught with.
- **The unrecorded promise.** A date given verbally on a call, not in the schedule, missed silently.
- **Clearing the bank balance to zero.** A zero balance is a bounced payment waiting for a charge.
- **Paying early to feel safe.** Money out three weeks early is money unavailable in the week it was
  needed.
