# Promise to pay, and the forecast

A cash forecast built on due dates is fiction. A forecast built on promises is a
forecast, provided every promise is logged, dated and scored.

## The promise log

| Field | Why |
|---|---|
| Invoice and amount | What the promise covers |
| Promised date | The only field that makes it a promise |
| Promised amount | Part payments are the norm |
| Who said it, and their role | A promise from someone without authority is a rumour |
| How it was made - email, WhatsApp, call | The evidence, if it slips |
| Status - open, kept, slipped, broken | Scored weekly |

A promise with no date is a polite no. Write the date down in the reply: "Noted -
₹3,91,000 by 30 November."

## Scoring promises

| Outcome | Definition | What it teaches |
|---|---|---|
| Kept | Paid on or before the date | The customer's word is usable |
| Slipped | Paid, but after the date, within 14 days | Discount their next promise by 7-14 days |
| Broken | Not paid 14 days after the date | The next promise needs a plan, not a date |
| Silent | No payment, no answer | Stage 4 |

Two broken promises from the same customer and the ladder jumps a stage. That rule
is the whole value of the log.

## The weekly forecast

```
expected this week = promises due this week × kept-rate for that customer
                  + non-promised current invoices × historical on-time rate
                  + part payments confirmed
```

Worked example: three promises due this week, ₹6.4 lakh total; this customer has
kept two of three, so ₹4.3 lakh expected. Twelve invoices due, ₹9 lakh, at an 80%
on-time rate, so ₹7.2 lakh. Forecast ₹11.5 lakh against ₹15.4 lakh invoiced - and
say which of the two numbers you would defend.

## Forecast accuracy, scored monthly

| Metric | Formula | Target |
|---|---|---|
| Forecast accuracy | collected ÷ forecast, for the month | 85-110% |
| Promise kept rate | kept ÷ promises made | Above 70% |
| Average slip | mean days late on slipped promises | Falling |
| Ageing drift | 90+ bucket this month vs last | Falling |

A forecast that is consistently 60% of actual is not a forecast; it is a number
that makes the founder feel safe. Publish the miss and the reason.

## The monthly collections report, one page

1. **Collected** this month, against forecast.
2. **Outstanding** by bucket, with the movement since last month.
3. **Top five by money-days**, with the next action and the owner.
4. **Promises** - kept, slipped, broken, and the value.
5. **Escalations** - what moved to hold, notice or recovery.
6. **DSO**, and the one reason it moved.

Six lines. A founder reads six lines and asks one question; nobody reads a
14-column export.

## Cash planning with the forecast

| Week | Committed out | Expected in (forecast) | Gap |
|---|---|---|---|
| W1 | | | |
| W2 | | | |
| W3 | | | |
| W4 | | | |

The gap is what `finance-ops` needs for the runway view. Send it weekly, on the
same day, so the two roles are looking at one number.

## Anti-patterns

- **Forecasting on due dates alone.** It is the most optimistic possible model.
- **Counting a promise twice.** Once logged against an invoice, it is not also in the on-time pool.
- **A promise log nobody updates.** Stale statuses are worse than no log.
- **Hiding the miss.** A forecast that is always met is a forecast that was never real.
- **A monthly report of 14 columns.** Nobody reads it, so the escalation list never gets acted on.
- **One forecast for all customers.** Segment by behaviour: the two biggest accounts decide the month.
