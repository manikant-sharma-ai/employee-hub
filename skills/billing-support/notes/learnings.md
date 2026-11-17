# Learnings - billing-support

1. **Classify the failure before retrying.** A do-not-honour card retried four times recovers nothing and gets the
   merchant account flagged.
2. **Pre-dunning beats dunning.** A card-expiry message 30 days early removes the failure instead of chasing it.
3. **Pause before cancel.** A paused account with a saved card comes back; a cancelled one costs the acquisition
   cost again.
4. **The consequence is stated in the first message, not at the suspension.** Surprise is what makes a customer
   leave with a story.
5. **Refund, credit note and adjustment are three different instruments** with three different accounting
   consequences. Choosing the amount first is how the books break.
6. **Never reissue an invoice to hide an error.** A duplicate number is a GST problem, not a formatting one.
7. **Place of supply decides IGST versus CGST+SGST.** It is the commonest invoice error and the customer's
   accountant always finds it.
8. **A refund without a document number on the same day is a reconciliation break waiting to happen.**
9. **Triage with one question** - is it the amount, the timing, or that they did not expect the charge at all -
   because the three routes have nothing in common.
10. **Never refund an unrecognised charge to close a ticket.** That is how friendly fraud gets paid for.
11. **Recovery needs a denominator.** A rupee total with no cohort is an anecdote.
