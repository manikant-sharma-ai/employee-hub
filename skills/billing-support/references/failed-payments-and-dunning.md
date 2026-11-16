# Failed payments and dunning

A failed payment is a message from a bank, written in a code nobody reads. Reading the code is the whole job: it
decides whether to retry, to ask for a new card, or to call the customer.

## The codes that matter

| Code (typical) | What it means | What to do | What to tell the customer |
|---|---|---|---|
| `insufficient_funds` | The account was short at that moment | Retry on a sensible schedule - salary dates, not random | "Your bank declined for insufficient funds on <date>. We will try again on <date>, or you can pay now here: <link>" |
| `card_expired` | The card on file is dead | Ask for a new card, do not retry | "The card ending <last4> expired in <month>. Update it here and the renewal completes immediately." |
| `do_not_honor` | The issuer declined without a reason it will share | One retry, then a new card request, then a call | "Your bank declined the payment. This is usually a card limit or a block on recurring payments - your bank can confirm in one call." |
| `authentication_required` | The bank wants the customer to approve (3DS, OTP) | Send a fresh payment link, not a retry | "Your bank needs you to approve this payment once. It takes a minute: <link>" |
| `invalid_account` / `processing_error` | Usually ours, or the gateway's | Check the gateway status and our configuration before blaming anyone | "This was our error, not yours. It is fixed and we have retried; no action needed." |
| `mandate_revoked` | The customer cancelled the standing instruction (UPI AutoPay, e-mandate) | Ask for a fresh mandate | "The automatic payment instruction was cancelled on <date>. Here is how to set it up again: <link>" |

## The ladder

Five rungs, each with a date, a channel and a purpose. The dates are a policy decision recorded in `decisions.md`,
not a per-ticket improvisation.

| Rung | Day | Channel | Purpose | Access |
|---|---|---|---|---|
| 0 | 0 | Email, from a person | Tell them it failed and why, with the link | Full |
| 1 | 3 | Email + SMS or WhatsApp | One retry has happened; ask again with the reason | Full |
| 2 | 7 | Email, copy the account owner | The payment is now overdue; name the consequence and the date | Full, grace stated |
| 3 | 14 | Phone call by the owner | Understand the blocker - cash, a lost card, a cancelled project | Downgraded or limited |
| 4 | 21 | Final notice | Suspend at a stated date, and say exactly what suspending means | Suspended after the date |

## Rules that keep a ladder honest

- **Retry on a schedule that matches money arriving.** Retrying at 2am on the 28th, three times, is a way to
  collect three decline fees and no money. Retry after a salary date, and never more than four times in a cycle.
- **Never retry a dead card.** It produces a decline, a fee and a worse relationship, and it delays the one thing
  that would work: asking for a new card.
- **Check delivery of the dunning email.** An email in spam is not a dunning email. Look at bounces and opens per
  rung, and send the critical rung on a second channel.
- **State the suspension date and what it stops.** A customer who is told "access ends on the 21st" either pays or
  tells you why not; one who is told "your account is at risk" ignores it.
- **The grace period is a decision, not a favour.** Written down, applied to everyone, with the exception path
  named.
- **Disputes pause the ladder.** Collection messages during a chargeback is how a dispute becomes a complaint to
  the regulator.

## Measuring

`recovered value by rung / failed value` per month. A ladder where rung 0 recovers 60% is a good ladder; one where
rung 4 recovers everything is a ladder that is only collecting at the point of pain, and it is losing the customers
it keeps.
