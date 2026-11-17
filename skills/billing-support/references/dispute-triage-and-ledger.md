# Disputes and the ledger: separating three different problems

"I have a problem with this charge" is three different sentences, and answering them as one is how a small
dispute becomes a chargeback.

## The triage

| The customer means | Signals | Route |
|---|---|---|
| "I do not recognise this charge" | Card statement, no order in the system, a family member's card | Verify, then either explain with evidence or treat as fraud |
| "I cannot pay this now" | Cash flow, salary timing, a bad month | Hardship path: pause, plan, or downgrade - never a discount reflex |
| "This amount is wrong" | A pricing, proration, tax or duplicate error | Billing correction, with the document |
| "I did not receive what I paid for" | Delivery or service failure | Service recovery, and the refund or credit follows |

Ask one question and the route is decided: *"Is the issue the amount, the timing, or that you did not expect this
charge at all?"* Three words, and the reply stops being a guess.

## Unrecognised charges

1. **Check the merchant descriptor** the customer sees on the statement - it is often not the brand name.
2. **Search the system** by amount, date, email and last four digits. A charge with no matching record is either a
   different merchant or fraud on the card.
3. **If it is genuine and they forgot**, send the invoice, the order and the login history. Evidence closes it; a
   reassurance does not.
4. **If it is not yours**, say so plainly and tell them to contact their bank. Never refund a charge that is not in
   your system - that is how friendly fraud is paid for.
5. **If it is a card-testing pattern** - several small charges, several cards, one IP - stop, do not engage
   further, and escalate to the gateway and the founder.

## Chargebacks

| Day | Action |
|---|---|
| 0 | Acknowledge internally, freeze the account, pull the evidence |
| 1-3 | Submit the response: invoice, terms accepted, login and usage logs, delivery proof, communication history |
| 7 | Confirm the response was accepted by the acquirer |
| 30-45 | Read the outcome and record the reason code |

The evidence window is short and a defence assembled on day 20 is a loss. Chargebacks above roughly 1% of
transactions put the merchant account at risk, so the count matters more than the amount.

## The daily money queue

One sheet, one row per open item, four columns that make it a queue rather than a list:

| Column | Content |
|---|---|
| Age | Days since the failure or request |
| Owner | A named person, not a team |
| Next action and date | The specific next step, not "follow up" |
| Blocked on | Customer, gateway, bank, or ledger - which decides who is chased |

Review it daily for ten minutes. Anything older than its promised window is escalated in that review, not later.

## What the ledger needs from this role

- **A document number for every money movement**, same day.
- **A reason code for every refund and write-off**, from a short fixed list.
- **The reference that ties a gateway transaction to an invoice**, so `bookkeeper` can match without a
  conversation.
- **A monthly summary of what changed** - refunded, credited, written off, recovered - that `finance-ops` can
  reconcile against the bank and the gateway settlement.

## Anti-patterns

- Refunding an unrecognised charge to close the ticket.
- Treating a hardship case with a discount, which teaches the customer that a bad month is a negotiation.
- Answering a chargeback with a screenshot of the invoice and no terms acceptance.
- A queue measured by "items closed" rather than by items closed correctly, which rewards fast wrong answers.
