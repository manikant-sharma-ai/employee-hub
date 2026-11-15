# Early-warning signals: who is about to leave

A churn model that cannot be acted on is a dashboard. This file finds the two or three behaviours that precede
an exit, states their lead time, and puts a threshold on them.

## The rule of three

Keep three signals, not thirty. Each must pass all four tests:

| Test | Question | Fail looks like |
|---|---|---|
| Lead time | Does it fire at least 30 days before the exit, on most leavers? | A signal that fires in the last week |
| Separation | Does it separate leavers from stayers clearly? | A drop in logins that half the healthy base also shows |
| Actionability | Can the account owner do something when it fires? | "The customer's business is slowing" |
| Cost | Is the data available without new instrumentation? | A signal that needs an event nobody logs |

## The signal families

| Family | Example signal | Typical lead time | What it usually means |
|---|---|---|---|
| Usage decay | Weekly active days down 50% against the customer's own 90-day average | 45-90 days | Value stopped being delivered |
| Breadth collapse | Seats, modules or locations in use falling | 30-60 days | The champion left or the rollout stalled |
| Support sentiment | Two or more tickets in 30 days, or one escalation | 30-60 days | Something is broken and unresolved |
| Payment friction | A failed payment, a card retry, a request to change terms | 7-30 days | `cash-flow`, sometimes a decision already made |
| Contact silence | No reply to two consecutive check-ins | 30-90 days | Disengagement; often the earliest and cheapest signal |
| Champion departure | The named contact's email starts bouncing | 30-90 days | The internal sponsor is gone |
| Price-shock event | A usage overage bill, a renewal quote, a plan change | 14-45 days | The value conversation is about to be reopened |
| Seasonal | Same month last year's exits | 12 months | Real but not actionable alone; use as a weighting |

## Building the score from your own data

1. Take the last 100 exits and a matched group of 200 customers who stayed, over the same period.
2. For each signal, compute **hit rate** (share of leavers who showed it) and **false-positive rate** (share of
   stayers who showed it).
3. Keep a signal only if hit rate is at least twice the false-positive rate. Anything closer is a mood.
4. Combine two or three signals with simple weights - two signals present is amber, three is red. Do not use a
   model nobody can explain to the account owner who has to make the call.
5. Set the threshold on the account owner's capacity: if the list has 80 names and the team can work 15, the
   threshold is wrong.

## The warning table

| Account ID | MRR | Tenure | Signals fired | Score | Owner | Days since contact |
|---|---|---|---|---|---|---|
| ACC-1042 | ₹48,000 | 14 mo | usage -60%, 2 tickets | Red | A | 21 |
| ACC-2210 | ₹12,500 | 3 mo | no reply ×2 | Amber | B | 34 |
| ACC-0871 | ₹1,20,000 | 26 mo | payment failed, silence | Red | A | 9 |

Account IDs only. The owner maps them to names; the report never carries a customer name.

## What to do with the list

| Score | Action | Who |
|---|---|---|
| Red | A call this week, with the reason and the last conversation in hand | Account owner |
| Amber | A specific, useful check-in - not "just checking in" | Account owner or success |
| New, first 30 days | Activation review, regardless of signals | Onboarding owner |
| Red + price shock | Route to `pricing-analyst` for a policy answer before any offer | Founder |

## Calibrating and keeping it honest

- **Backtest monthly.** Run the score against last month and count how many reds actually left. A score that
  flags 40% of the base is a churn prediction of "everyone".
- **Track the false positives as a cost.** Every red that was going to stay costs an account owner an hour and
  possibly a discount. That is the price of the model and it belongs in the read.
- **Retire a signal when the product changes.** A signal built on a dashboard that no longer exists is noise.
- **Never present a score as a certainty about a person's intentions.** It is a probability from behaviour, and
  the read says so.

## Anti-patterns

- A machine-learning model on 60 exits: it will fit the noise and nobody will trust it.
- Flagging on a single login gap, when half the base is seasonal (festivals, harvest, exam season, financial
  year-end).
- Using support tickets as a negative signal only: a customer who writes in is engaged. Silence is the danger.
- Emailing the customer automatically because a score turned red - that is how a save becomes the reason they
  leave.
- Reporting the list to the founder without an owner: an unowned red is a number, not a task.
