# Failed payments: the cheapest revenue in the business

An expired card is not a customer decision. Treated as one, it becomes churn that gets attributed to price three
months later.

## Classify before retrying

| Failure reason | Retryable | Typical cause | Right action |
|---|---|---|---|
| Insufficient funds | Yes, on a calendar | Salary date, cash timing | Retry near month-end or the salary cycle; tell the customer the date |
| Card expired | No | Card lifecycle | Ask for a new card; pre-dun 30 days before expiry |
| Do not honour | No, not soon | Issuer block, suspected fraud | One attempt, then a different method; repeated retries damage the account |
| Authentication required | Yes, once | 3DS or mandate re-auth | Send a re-auth link; do not retry blindly |
| Mandate revoked | No | Customer or bank cancelled the NACH/UPI mandate | Re-register the mandate, with the reason explained |
| Technical decline / gateway error | Yes, in minutes | Acquirer or network | Retry within the hour; if it repeats, escalate to the gateway |
| Invalid account / UPI handle | No | Wrong details on file | Ask for correction before any retry |

Retrying a non-retryable failure four times in a week gets the merchant account flagged and recovers nothing.

## A retry calendar that respects Indian rails

| Day | Action | Channel |
|---|---|---|
| 0 | Attempt at renewal | Automatic |
| 1 | Retry (technical or soft decline only) | Automatic |
| 3 | First notice, with a payment link | Email or WhatsApp |
| 5 | Second retry, different time of day | Automatic |
| 7 | Second notice, naming the consequence and the date | Email + WhatsApp |
| 10 | Final retry | Automatic |
| 12 | Third notice: service pauses on <date> | Email + call for high value |
| 14 | Pause, not cancel | Product |

Pause before cancel. A paused account with a saved card recovers on the next successful charge; a cancelled one has
to be re-acquired, which costs the CAC again.

## Pre-dunning: the part that actually moves the number

- **Card expiry**: the gateway knows the expiry month. A message 30 days before, with a one-tap update link,
  removes a large share of failures before they happen.
- **Mandate expiry**: UPI Autopay and NACH mandates have their own end dates and per-transaction caps. Track them
  like contracts, not like settings.
- **Amount change**: a price rise above a mandate's cap fails at the bank, not at the customer. Tell them and
  re-register before the first affected cycle.
- **Low-balance timing**: for NACH and e-mandate debits, the debit date matters more than the retry count in a
  market where salary lands on the 1st or the 7th.

## Recovery rate, measured honestly

```
recovery rate = failed payments recovered within 14 days / retryable failures in the same cohort
```

Report it by failure reason. A blended rate hides that expired cards are unrecoverable and technical declines are
almost all recoverable. Report the denominator and the cohort period, always.

## When to stop

- Three attempts on a non-retryable reason, or the retry limit in `decisions.md`, whichever comes first.
- A customer who asks to stop being contacted. Honour it, keep the payment link live, and record the request.
- A customer whose account is in a genuine hardship conversation with the founder - the ladder pauses, and the
  reason is written down.

## Anti-patterns

- Emails that say "your payment failed" without the amount, the date, or a link.
- Cutting access on the failure day, which turns a ₹499 recovery into a lost customer and a bad review.
- Cancelling instead of pausing, and calling it churn.
- Retrying at the same hour every day, which fails for the same balance reason every time.
- Measuring recovery as a rupee total with no denominator.
