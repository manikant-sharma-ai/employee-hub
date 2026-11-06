# Health scoring

A health score exists to make one decision: which account gets attention this
week. If it does not change what you do, it is a dashboard, not a score.

## The five inputs

| Input | What it measures | Where it comes from | Weight |
|---|---|---|---|
| Usage trend | Are they getting value? | Product analytics, admin panel | 35% |
| Ticket severity | Is something broken or blocking? | Helpdesk | 20% |
| Champion strength | Is there a person who wants this to work? | CRM, call notes | 20% |
| Payment behaviour | Is the commercial relationship clean? | Billing, books | 10% |
| Days to renewal | How much time is left to fix anything? | Contract register | 15% |

Usage carries the most weight because it is the only input the customer cannot
be polite about.

## Scoring each input

| Input | 0 (red) | 1 (amber) | 2 (green) |
|---|---|---|---|
| Usage | Down >30% in 60 days, or zero in 30 | Flat or down 10-30% | Up >10%, or at capacity |
| Tickets | A P1 open over 7 days, or 3+ in 30 days | One open, resolved slowly | None open, fast resolution |
| Champion | Left, silent 45+ days, or never identified | Responsive but junior, or shared | Active, senior, advocates internally |
| Payment | Overdue 30+ days, or a disputed invoice | Late once, now clear | On time, or advance |
| Renewal | Under 60 days with no conversation | 60-120 days | Over 120 days, or already renewed |

Weighted total out of 10. Write the raw values beside the score - "usage 0
(1,240 → 610 sessions), tickets 1 (one open, 9 days), champion 2, payment 2,
renewal 0 (48 days)" - because the score is for ranking and the raw values are
for the conversation.

## Bands and what each one obliges

| Score | Band | What you owe the account this month |
|---|---|---|
| 8.5-10 | Strong | Expansion conversation, a reference ask, a case study |
| 6.5-8.4 | Stable | One value check-in with a number in it, and the renewal calendar entry |
| 4.5-6.4 | Watch | A real call within two weeks, a written success plan, the risk named to the founder |
| Under 4.5 | Critical | A save plan, an executive contact, and a decision date |

The band is a work queue, not a label. An account in "strong" that nobody has
spoken to in 90 days is not strong; add "days since last human contact" as a
watch flag even though it is not in the weighted score.

## The one number per product

Find the action that separates accounts that renew from accounts that cancel, and
use it as the anchor. It is rarely logins.

| Business | The number that predicts renewal |
|---|---|
| SaaS tool | Weekly active users as a share of licensed seats |
| E-commerce enabler | Orders processed per month |
| Agency retainer | Deliverables shipped and approved per month |
| Marketplace seller tool | Listings live and enquiries answered |
| B2B distribution | Reorder frequency and basket size |
| Accounting or compliance service | Filings completed on time, zero notices |
| Training or edtech | Sessions attended per learner |

Compute it for the accounts that renewed and the accounts that left. The gap
between the two distributions is your threshold, not a benchmark from a blog.

## Reading the trend, not the level

- **A flat score at a falling usage is a falling account.** Score the trend in the usage input, not the absolute level.
- **Three months of data is the minimum for a trend.** Before that, mark the account "insufficient history" rather than inventing a direction.
- **Seasonality is real.** A wedding-season retailer in July and a school in May will look dead and are not. Note the season per account type.
- **A spike is not health.** One big month after a complaint is often a catch-up, not a recovery.

## The monthly ritual

1. Refresh every input from the system, not from memory. A score built from last quarter's numbers is a story about the past.
2. Re-rank by value at risk: score band crossed with ARR. The ₹40 lakh account in "watch" comes before the ₹40 thousand account in "critical".
3. Write one line per account that moved a band: what changed and what you will do.
4. Pick the three accounts for this month's attention. Three, not thirteen.
5. Record the score history. The number that matters is the direction over three months.

## Anti-patterns

- **Scoring on sentiment from the last call.** The most cheerful call is often the last one before a cancellation.
- **A 40-field scorecard nobody fills in.** Five inputs, refreshed monthly, beats twenty, refreshed never.
- **Equal weights.** Usage and champion strength decide renewals; a payment delay is often an accounts-payable process, not a signal.
- **Using the score as a customer-facing number.** It is an internal queue; shown to a customer it reads as a threat.
- **No owner per account.** A score without a named owner is a report, not a plan.
- **Scoring only the big accounts.** The ten mid-size accounts that renew quietly are where expansion lives.
