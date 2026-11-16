# Billing queries and invoice mismatch

Half of billing support is arithmetic and the other half is the story the salesperson told. Both are answerable,
and neither is answered by "as per our records".

## The four questions behind every billing query

1. **What did they agree to?** The quote, the order form, the email where the price was confirmed. Not the price
   list, not what the CRM says if it disagrees with the document.
2. **What did we invoice?** Plan, quantity, period, tax, discount, proration.
3. **What did they pay?** Amount, currency, date, reference, and whether it settled or is still pending.
4. **What is the difference, exactly?** A number, a currency and a reason. "There is a mismatch" is not a finding.

## The usual causes, in order of frequency

| Cause | Tell | Fix |
|---|---|---|
| Proration on a mid-cycle change | Two part-months on one invoice | Show the two lines with dates and rates |
| Tax rate or place of supply | GST differs from the quote | Recheck the GSTIN and the state code; issue a revised invoice |
| Discount not applied, or expired | The invoice is at list price | Apply the agreed discount and credit the difference |
| Quantity or seats drift | Usage-based or per-seat billing | Show the count, its date and the source |
| Currency or exchange rate | A USD contract invoiced in INR | State the rate and the date, per the contract |
| A promise made in sales | The customer quotes an email | Honour it or escalate; never argue with the document |

## The duplicate charge, explained properly

The most common "you charged me twice" is not a double charge:

1. **An authorisation hold** and a **capture** - the customer's bank shows both for a few days.
2. **A failed attempt and a successful retry** - the failure shows as pending, then drops.
3. **Two invoices in one month** because of a plan change or a proration.
4. **An actual double charge** - two settled transactions with different ids.

The reply shows the transaction ids, the statuses and the dates. If it is a hold, say so and say when it drops. If
it is a real double charge, it is ours: refund the duplicate immediately, with the reference, and say it was our
error in the first line.

## Revised invoices and credit notes

- **A revised invoice must reference the original** and state what changed. A fresh invoice with no reference
  leaves the customer with two documents and no story.
- **A credit note needs a reason and a reference**, and it must be posted by `bookkeeper` before it is quoted to
  the customer as done.
- **Never tell a customer an invoice has been corrected** until the corrected document exists.

## Handing over

- **Pricing disputes** go to `pricing-analyst` or the founder, with the quote and the invoice attached.
- **Contract terms** go to `contract-negotiator` if the question is what the clause means, and to `legal-drafter`
  if a document must be produced.
- **The books** are `bookkeeper`'s and `finance-ops`'s; this role supplies the trail, not the entry.
