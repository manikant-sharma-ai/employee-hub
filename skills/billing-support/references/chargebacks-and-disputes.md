# Chargebacks and disputes

A chargeback is a deadline with money attached. The bank gives a window - often seven to ten days - and answers with
what is in the file at that moment. Everything after the window is an appeal nobody reads.

## The first 24 hours

1. **Log it**: the dispute id, the amount, the reason code, the deadline, the transaction it refers to.
2. **Find the customer's own story**: their messages, the support thread, the cancellation attempt, the complaint.
   A dispute is often a frustrated customer whose email went unanswered, and the answer may be a refund plus an
   apology rather than a fight.
3. **Decide: contest or accept.** Contesting a genuine service failure costs the fee, the time and the customer.
   Accepting a ₹2,000 dispute to keep a ₹200,000 account is a commercial decision - escalate it, do not decide it
   alone.
4. **Pause the ladder.** No collection messages while a dispute is open.

## The evidence, by reason code

| Reason code family | What the bank wants |
|---|---|
| Fraud / "I did not authorise this" | Proof the cardholder authorised: 3DS result, IP and device at purchase, prior order history from the same card, delivery to the cardholder's address |
| Product not received | Dispatch proof, carrier tracking showing delivery, the delivery address, the signature or OTP |
| Product not as described | The listing or the specification the customer saw, the order confirmation, the usage log showing the service was consumed |
| Duplicate charge | The two transaction ids, their timestamps and statuses, the refund reference if one was issued |
| Subscription cancelled | The cancellation record, or the terms showing how cancellation works, plus the notices sent |
| Credit not processed | The refund initiation reference and the date, or the reason it was not due |

## The pack

One PDF, in the bank's order, with a one-page summary at the front: what was sold, when, to whom, that it was
delivered or consumed, and what the customer was told. Then the evidence, each item labelled with what it proves.
Then the terms, with the relevant clause highlighted.

Rules that decide these cases:

- **Delivery proof beats an argument.** A tracking number with a delivery scan is worth more than three pages of
  explanation.
- **The customer's own words are evidence**, including the ones that hurt. A thread where they say "I received it
  but it is the wrong size" changes the case from fraud to service.
- **Terms accepted at checkout**, with the timestamp and the IP, are the strongest single item for a subscription
  dispute.
- **Never submit a document that is not true.** A fabricated delivery proof is fraud, and it is discovered.

## After the outcome

- **Won**: note the reason in `learnings.md` and add the missing evidence to the standard pack.
- **Lost**: the money is gone, the fee is gone, and the finding is usually a process gap - no delivery scan, no
  cancellation record, no terms. Fix that, and write it in the journal with the value.
- **Either way**: check whether the same gap will lose the next one. A dispute is a paid audit of the checkout and
  the delivery process.

## Volume as a signal

More than a handful of disputes a month with the same reason code is not a customer problem. It is a description
problem, a delivery problem or a cancellation-flow problem, and it belongs in front of the founder with the count
and the value.
