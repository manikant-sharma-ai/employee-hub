# FX and cross-border collections

A foreign invoice is two transactions: a sale, and a currency position. Most small businesses price
the first and ignore the second until the rate moves.

## What to establish before anything else

| Fact | Why |
|---|---|
| Currency and amount | The exposure itself |
| Expected receipt date | The exposure's duration |
| Incoterms | Who pays freight and insurance, and therefore what the invoice actually is |
| Payment terms | 30/60/90 days from dispatch or from acceptance |
| Whether a forward is booked | Determines whether the rate is a risk or a fact |
| Purpose code and FIRC | Whether the money can be credited at all, and the export evidence |
| LUT or IGST paid | Whether the invoice should carry GST |

## The exposure, stated simply

Rupee exposure = foreign amount x (rate today - rate you will actually get). A 40,000 USD receivable
at 88 moves ₹1.6 lakh for every rupee the rate moves. That is the number to show, not "currency risk".

Cover the exposure when the amount is material against the month's cash (rule of thumb: more than 5%
of monthly inflow), the date is reasonably certain, and the business cannot absorb the move. Do not
cover a receivable that is disputed, unscheduled or likely to be cancelled - a cancelled forward is
its own loss.

## Forward cover, in one paragraph of plain language

A forward contract fixes the rate for a future receipt or payment, at a cost embedded in the forward
rate rather than a fee. Book it for the amount you are confident of, at a tenor matching the expected
receipt, with the bank that holds the account. Understand the cancellation and rollover charges before
signing, and never book cover for the full order book when only half of it is certain.

## Collection mechanics in India

| Step | Detail | Failure it prevents |
|---|---|---|
| Invoice in the contracted currency | Currency, Incoterms, payment terms on the face | Disputes about what was agreed |
| Purpose code on the inward remittance | Correct code per the export's nature | Credit held by the bank |
| FIRC / eBRC | Obtain and file per remittance | Export incentives and GST refunds blocked later |
| AD bank code on invoices | Required for realisation tracking | EDPMS mismatch |
| Realisation within the period | Track the Softex/EDPMS status | Caution-listing on future exports |
| LUT filed, if exporting services or goods without IGST | Filed annually | IGST charged on an export invoice |
| Withholding tax in the buyer's country | Check the treaty rate and the TRC | Paying tax twice on the same income |

## The rate moved - what to do, in order

1. **Quantify, in rupees, on the actual amount.** Not "the rupee weakened" but "this receipt is worth
   ₹1.4 lakh less than at the rate we quoted".
2. **Check whether the quote or contract carries a rate clause.** If it does, the answer is in the
   document, not in a hedging decision.
3. **Check the cover.** A booked forward means the move is not the business's problem this month.
4. **Decide only on the uncovered remainder**, and only where the amount is material and the date is
   known.
5. **Record the realised rate** on every foreign receipt, so next quarter's pricing conversation
   starts from what actually landed rather than what was quoted.

## Anti-patterns

- **Pricing in dollars and thinking in rupees.** The margin is computed at the rate on the invoice
  date and delivered at the rate on the receipt date.
- **Forward cover on uncertain receivables.** A cancelled forward is a speculative loss wearing a
  hedging label.
- **Chasing the rate.** Holding a receivable for a better rate is a currency trade, not treasury.
- **Ignoring the bank's inward-remittance queries.** Money held for a purpose code is not cash.
- **No FIRC trail.** It is the document every export benefit and refund asks for, and it is hardest
  to reconstruct a year later.
- **Assuming GST is never payable on exports.** It is zero-rated with an LUT; without one, the
  invoice carries IGST and the refund becomes a working-capital problem.
