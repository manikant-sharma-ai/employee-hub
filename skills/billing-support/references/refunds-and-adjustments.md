# Refunds and adjustments

A refund is two things: money moving back, and a customer being told the truth about when. Most refund complaints
are about the second.

## The states, and the words for them

| State | What is true | What to tell the customer |
|---|---|---|
| Requested | The customer asked; nothing has been decided | "We have your request and will confirm within <n> working days" |
| Approved | Someone with authority said yes | "Approved on <date> for ₹X" |
| Initiated | The gateway has the instruction | "Initiated on <date>, reference <id>. It reaches your account in <n> working days" |
| Settled | The gateway confirms completion | "Completed on <date>. If it is not visible, your bank can trace it with this reference" |
| Rejected | Not due, per policy | "Not eligible because <reason>, and here is what is possible instead" |

Never use "processed", "done" or "reflected" without one of the five states behind it.

## The trail the customer needs

1. **The refund id** from the gateway, not our internal ticket number.
2. **The date it was initiated**, and the amount in the original currency.
3. **The method it goes back to** - the same card, the same UPI handle, the bank account.
4. **The realistic arrival window** for that method, in this country, at this bank.
5. **Who to chase** if it does not arrive: the bank's dispute line with the reference, or us.

## Policy questions this role does not answer

- **Whether the refund is due** - the returns policy belongs to `returns-manager`, the contract to the founder.
- **Whether to refund as goodwill** - a commercial decision with a threshold, recorded in `decisions.md`.
- **How it is posted** - `bookkeeper` decides credit note against payment reversal.

## Partial refunds and adjustments

- **A partial refund needs a reason code** - a service credit, a short shipment, a price correction. The reason
  goes in the note, because the same customer asking twice with two different reasons is a signal.
- **A credit note is not a refund.** It reduces what is owed next time; the customer expecting money in the bank
  will not be satisfied by it. Say which one it is.
- **Waiving a late fee** is an adjustment, not a refund, and it needs the same approval trail.

## Failure modes

- **The refund was initiated to a closed card.** The money comes back to us in a few days and the customer is told
  it is on its way. Check the card status before initiating.
- **The refund was initiated twice.** Two references, one customer, one angry bank conversation. One case, one
  owner.
- **The refund was never actually initiated**, only noted in a ticket. The gateway is the only proof; the ticket is
  a promise.

## Closing a refund case

Close it only when the state is `settled` or the customer confirms receipt. Then write the journal line with the
amount and the days taken, because the median days-to-refund is the number that predicts the next complaint.
