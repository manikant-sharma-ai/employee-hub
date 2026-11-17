# The dunning ladder: asking before cutting

Dunning fails for two reasons: it is rude too early, or it is silent until the account is suspended. Both lose a
customer who would have paid.

## The ladder

| Step | Day | Channel | Message job | Consequence stated |
|---|---|---|---|---|
| 1 | 0 | Automatic retry | Nothing said yet | — |
| 2 | 1-3 | Email | The amount, the date, the link, one line on why it failed | "Your plan renews as normal once this clears" |
| 3 | 5 | WhatsApp or SMS | Shorter, same link, the date | — |
| 4 | 7 | Email | Name the pause date, and what pauses | "Access pauses on the 14th" |
| 5 | 10 | Email + call (high value) | Ask if something has changed, offer a pause or a downgrade | Repeats the date |
| 6 | 12 | Email | Final notice, the exact date and time | "Access pauses tomorrow" |
| 7 | 14 | System | Pause the account, keep the data, keep the link | "Your data is kept for 30 days" |

Every message carries: the amount, the date it failed, the payment link, the date of the consequence, and a way to
reply to a human. Five facts, four lines.

## Tone, by step

- **Steps 2-3: assume a mistake.** Most failures are a card or a balance, not a decision. "Your payment of ₹4,999
  did not go through" is the whole first line.
- **Steps 4-5: assume nothing, ask.** "If something has changed on your side, reply and we will work out a
  different arrangement" recovers more than any urgency.
- **Steps 6-7: state, do not threaten.** The date and the consequence, no adjectives.

Never use "final notice" before it is final, and never use a threat the business will not carry out.

## What pauses and what does not

| Pauses | Does not pause |
|---|---|
| Access to the paid product | The customer's data |
| New orders or shipments | The ability to pay and reactivate |
| Support entitlement | The invoice and its tax treatment |
| API access | The legal obligation to keep records |

Say which, exactly. "Your account will be suspended" with no detail produces a support ticket and a bad review.

## Pause, then cancel, then write off

1. **Pause at day 14.** Keep the data for a stated period. Keep the payment link live.
2. **Cancel at day 30-45** only after one human attempt, and record the reason in the cancellation field.
3. **Write off at 90 days** with a named approver, a reason code, and a line in the monthly read. A written-off
   receivable that nobody approved is a hole in the books.

## Segmenting the ladder

| Segment | Ladder | Why |
|---|---|---|
| Self-serve, under ₹2,000 a month | Fully automated, 4 steps | A call costs more than the recovery |
| SMB, ₹2,000-25,000 a month | Automated plus one call at day 10 | The call is the recovery |
| Enterprise or annual | Account owner owns it from day 1; this role supplies the facts | The relationship outranks the ladder |
| Distributor or channel | Ladder to the channel, not the end customer | One relationship, many invoices |

## Measuring the ladder

- **Recovery by step**: which message actually produces the payment. If step 4 recovers nothing, it is noise.
- **Time to recovery**: median days from failure to cleared.
- **Pause-to-reactivation rate**: of accounts paused, how many come back. This is the number that says whether the
  ladder is a delay or a loss.
- **Complaints per 100 messages**: a ladder that recovers 20% and annoys 5% is a net negative in a small business.

## Anti-patterns

- A dunning email with no amount and no link, which generates a support ticket instead of a payment.
- Cutting access on the failure day.
- Escalating tone with each message, when the customer simply has a card problem.
- Sending from `noreply@`, which guarantees the reply never arrives.
- Letting the ladder run on a customer who is mid-conversation with the founder about a payment plan.
