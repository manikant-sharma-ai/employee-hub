# Refunds: deciding the form before the amount

Most refund arguments are not about money. They are about a promise made on a call, a policy nobody read, and a
timeline that was invented.

## The decision order

1. **What did the customer agree to?** Quote the published clause. If it is silent, say it is silent.
2. **Has the service been delivered?** A refund for an undelivered period is arithmetic; a refund for a delivered
   service is a commercial decision.
3. **Is this a first request or a pattern?** The pattern matters for policy, the individual case does not get
   punished for it.
4. **Which instrument?** Refund to source, credit note, or adjustment on the next invoice.
5. **Who approves?** The threshold table, and a named approver recorded with the time.

## Instrument by situation

| Situation | Instrument | Timeline to promise |
|---|---|---|
| Paid, service not delivered, wants money back | Refund to source | 5-7 working days for cards, 2-3 for UPI, longer for NACH |
| Paid, will continue, wants the overcharge back | Credit note, adjusted next cycle | Same day, document issued |
| Paid annually, cancels at month 4 | Per the published clause; if pro-rata, refund the unused full months | Per gateway |
| Duplicate charge | Refund the duplicate immediately, no approval needed under the threshold | 5-7 working days |
| Failed delivery or a service failure with evidence | Refund or credit, plus the reason recorded | Per gateway |
| A charge the customer does not recognise | Stop: this is a dispute, not a refund | See `references/dispute-triage-and-ledger.md` |

## Partial refunds and proration

- **Prorate on days, not months**, and state the day count in the reply. "Two months unused" is arguable; "61 of
  365 days unused" is not.
- **Discounts are not refunded at list price.** A customer who paid ₹8,000 on a ₹10,000 plan gets a share of
  ₹8,000.
- **Tax follows the credit note**, not the refund. A refund of a taxed invoice needs the credit note to reverse the
  output tax in the right period.
- **Gateway fees are usually not refundable.** Say so before the customer discovers it in the settlement report.

## The record that makes it reconcilable

Every refund and credit note leaves five things on the same day: a document number, the amount, the original
invoice reference, the approver's name, and the ledger line `bookkeeper` should match. A refund promised in a
WhatsApp thread with none of these is a future reconciliation break.

## What to tell the customer

Four lines: the decision and the reason, the amount, the date it lands and where, and the reference number. If the
answer is no, the same four lines with the clause quoted and the alternative offered - a credit, a pause, a
downgrade.

## When to escalate

- Above the approval threshold, or a refund that would set a precedent for a large cohort.
- A customer citing a legal notice, a consumer forum or a payment-network complaint.
- A refund requested after a chargeback has been filed - the money is now the bank's question.
- A pattern: three refunds for the same reason in a month is a product or onboarding problem, and it goes to
  `feedback-synthesiser` and `product-manager`, not to a fourth refund.

## Anti-patterns

- Refunding to keep the peace and never recording the reason, so the cause is never fixed.
- A verbal "we will sort it out" that becomes a month-long thread.
- Promising a timeline the gateway cannot meet, then absorbing the follow-up emails.
- Refunding a charge the customer did not recognise instead of investigating it - that is how friendly fraud
  succeeds.
