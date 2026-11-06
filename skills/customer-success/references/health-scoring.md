# Health scoring

A health score exists to answer one question at a glance: **which account needs a
person this week**. It is a ranking device, not a grade, and it is only useful if
every number in it can be traced to a signal.

## The six signals

| Signal | What it measures | Weight | Data source | Fails when |
|---|---|---|---|---|
| Core-action trend | Is the product doing its job, this month vs last | 30% | Product analytics | The product has no event for the core action |
| Seat utilisation | Active users ÷ paid seats | 20% | Product analytics | Licences are pooled across a team |
| Support load | Tickets per month, weighted by severity, plus repeats | 15% | Support desk | Support is handled on WhatsApp and never logged |
| Payment behaviour | Days late on the last two invoices | 15% | Invoice system | The customer prepaid a year |
| Champion presence | Is the person who bought it still there and engaged | 10% | CRM + last contact date | Nobody wrote it down |
| Outcome progress | Movement on the outcome they bought | 10% | QBR notes | It was never defined at signature |

Weight the top three higher in transactional products (usage dominates) and the
bottom three higher in enterprise accounts (relationship dominates). Write the
weights into `notes/decisions.md` once chosen, and do not change them mid-quarter.

## Scoring each signal 0-4

| Score | Core-action trend | Seat use | Support | Payment | Champion | Outcome |
|---|---|---|---|---|---|---|
| 4 | Growing >10% | >80% | 0-1 low tickets | On time | Active, engaged <30 days | Exceeded |
| 3 | Flat to +10% | 60-80% | 2-3 low | <15 days late | Active, quiet | On track |
| 2 | Down 5-15% | 40-60% | 1 high or 4-6 low | 15-30 days | Unclear | Partial |
| 1 | Down >15% | 20-40% | 2 high or repeat issue | 30-60 days | Left or leaving | Behind |
| 0 | No activity | <20% | Escalated, unresolved | >60 days or disputed | No contact | Not defined |

Total = Σ(score × weight) × 25, giving 0-100.

## Bands and what each one obliges

| Band | Score | Meaning | Action | Owner | Deadline |
|---|---|---|---|---|---|
| Green | 75-100 | Value is landing | Expansion conversation at the next QBR | Account owner | Next QBR |
| Amber | 50-74 | Drifting, recoverable | Value check-in with the champion, agenda in writing | Account owner | 14 days |
| Red | 25-49 | At risk | Save play chosen by cause, founder informed | Founder + owner | 5 working days |
| Critical | 0-24 | Leaving | Exit-safe conversation, retention only if cause is fixable | Founder | 48 hours |

Never let a score sit in Amber for two months. Amber is a decision point, not a
waiting room, and the accounts that churn quietly are the ones that were Amber in
the month nobody looked.

## The two numbers that outrank the score

1. **Renewal date.** A Red account renewing in 18 months is a project. An Amber
   account renewing in 30 days is the emergency.
2. **Revenue at risk.** Rank by score × contract value, not by score. A 30-score
   account at ₹40 lakh outranks a 10-score account at ₹40,000.

Sort the monthly list by revenue at risk, then by days to renewal. That ordering
is the whole prioritisation.

## Signals that predict churn earlier than the score

- **The champion's replacement never takes the meeting.** The most reliable early
  signal in B2B, and it appears 3-6 months before the renewal conversation.
- **Login drop that coincides with a hiring freeze at the customer.** Their budget
  problem becomes your churn problem a quarter later.
- **A new decision-maker asking for the contract.** They are building a case.
- **Support tickets that shift from "how do I" to "why does".** Frustration, not learning.
- **Invoice paid late for the first time, after two years on time.** Cash stress at the customer, and your invoice is not the priority.

## Anti-patterns

- **Scoring with missing data as if it were zero.** A missing usage feed scores the
  account Red and sends a founder to a healthy customer. Score only the signals you
  have, re-weight, and say what is missing.
- **One composite number with no inputs shown.** It becomes an argument about the
  number instead of the account.
- **Changing weights to make the picture look better.** The score is a
  thermometer; you do not fix a fever by moving the line.
- **Scoring once a quarter.** Monthly, on the same day, from the same source.
- **Treating NPS as the health score.** It measures sentiment at a moment and
  arrives too late to act on.
