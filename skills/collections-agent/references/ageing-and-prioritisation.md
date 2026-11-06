# Ageing and prioritisation

The ageing report is not a statement of what is owed. It is a work queue, and a
queue without an order is a list.

## The buckets

| Bucket | Days past due | What it means | Default action |
|---|---|---|---|
| Current | Not yet due | Normal | Nothing. A reminder before the due date is an insult |
| 1-30 | 1-30 | Usually admin, sometimes cash | Reminder, then a call |
| 31-60 | 31-60 | A real delay or an undiscovered dispute | Firm follow-up, owner involved |
| 61-90 | 61-90 | Cash problem or a lost contact | Founder informed, hold decision |
| 90+ | 90+ | Recovery, or a decision to stop | Escalation ladder end, legal or write-off |

Buckets are calculated from the **due date**, not the invoice date. A 45-day term
invoice at 40 days old is current; a 7-day term invoice at 40 days is deep in the
second bucket.

## Ranking: value × days

Sort by `amount × days past due`, descending. That number is money-days: it
combines how much is stuck with how long it has been stuck.

| Invoice | Amount | Days | Money-days | Rank |
|---|---|---|---|---|
| A | ₹8,00,000 | 22 | 1,76,00,000 | 1 |
| B | ₹2,40,000 | 61 | 1,46,40,000 | 2 |
| C | ₹45,000 | 95 | 42,75,000 | 3 |
| D | ₹12,00,000 | 3 | 36,00,000 | 4 |
| E | ₹18,000 | 120 | 21,60,000 | 5 |

Note what the ranking does: D, the largest invoice, is fourth because it is barely
late - and it still gets a courteous day-3 note. E is the oldest and still last,
because a ₹18,000 invoice does not deserve a founder's morning.

Two overrides on top of the ranking:

- **A 90+ invoice at any size gets one personal call**, because silence at that age is a decision.
- **A top-5 customer by revenue outranks the maths.** Losing a ₹40 lakh account to collect ₹2 lakh is a bad trade; route it to the account owner, not the ladder.

## DSO, and why it moves

```
DSO = (average receivables ÷ revenue) × days in the period
```

| What moved DSO | Where to look |
|---|---|
| Terms got longer | Sales promised net 60 to close deals |
| One large customer stopped paying | The top-five list, not the average |
| Invoices went out late | Billing ran after month end, so the clock started late |
| Disputes rose | Product or delivery issue, not collections |
| A seasonal customer's cash cycle | Same month last year |

DSO that rises two months in a row is a board-level fact, not a collections
metric. Say so plainly.

## The weekly routine

| Day | Job | Time |
|---|---|---|
| Monday | Refresh the ageing, rank, assign owners | 30 min |
| Monday | Send stage-appropriate messages for the week | 45 min |
| Wednesday | Call the top five by money-days | 30 min |
| Thursday | Chase promises due this week | 20 min |
| Friday | Update the forecast, log slips, escalate | 30 min |

Two and a half hours a week keeps a small business's receivables moving. The
failure mode is a heroic four-hour session once a month, which is always too late
for the oldest invoices.

## What the ageing view must show

- Invoice number, customer, amount, invoice date, due date, days past due, bucket.
- Amount received, and the balance.
- Disputed flag and the disputed amount, separately.
- Promised date and promised amount, if any.
- Owner and next action with a date.

## Anti-patterns

- **Sorting by customer name.** It is alphabetical, not actionable.
- **Sorting by amount only.** The biggest invoice is often the newest.
- **Chasing the oldest first.** Age matters, but ₹18,000 at 120 days is not the priority.
- **A bucket with no action attached.** Every bucket must imply a next step.
- **Excluding disputed invoices from the total.** The money is still owed; it is just argued about.
- **One DSO number for the whole business.** Split by customer segment or the average hides both the good and the bad.
