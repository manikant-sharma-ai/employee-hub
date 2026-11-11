# Duplicate and anomaly detection

Most leakage in a small business is not fraud. It is the same invoice paid twice, a subscription
renewed after the team stopped using it, and a rate that was never updated in the system. All
three are found by matching, not by intuition.

## Clean before you match

| Clean-up | Why |
|---|---|
| Normalise vendor names (strip Pvt/Ltd/& Co, case, punctuation) | "ACME SUPPLIES PVT LTD" and "Acme Supplies" are one vendor |
| Extract GSTIN and match on it | The GSTIN is the vendor's real identity |
| Normalise invoice numbers (case, leading zeros, slashes) | "INV/2025/0042" and "inv-2025-42" are one invoice |
| Convert all amounts to a single sign convention | Credits entered positive create phantom duplicates |
| Standardise dates to one format | 03/04/2025 is two different days in two conventions |
| Keep the gross, the taxable value and the tax separate | A duplicate of the tax line only is a different finding |

## The tests, cheapest first

| # | Test | Rule | What it finds |
|---|---|---|---|
| 1 | Exact duplicate | Same vendor + same invoice number | The same bill entered twice |
| 2 | Same amount, date, vendor | Amount within ₹1, date within 3 days | A re-issued invoice paid again |
| 3 | Same GSTIN, different name | GSTIN match with amount and period match | Two vendor masters for one supplier |
| 4 | Two payments, one PO | PO number appears twice in payments | Advance plus final both booked as full |
| 5 | Split invoice | Two invoices just under the approval threshold, same vendor, same week | Deliberate or innocent splitting |
| 6 | Round-number clustering | Many invoices at exactly ₹9,999, ₹24,999 | Threshold avoidance |
| 7 | Bill with no PO above threshold | Amount > threshold, no PO reference | Spend outside the control |
| 8 | Payment with no bill | Payment recorded, no invoice in the ledger | Advance, or a duplicate payment |
| 9 | Credit note not applied | Return recorded, credit note never knocked off | Paying full price after a return |
| 10 | Sequential invoice numbers with a gap | A missing number in a vendor's series | A cancelled or unrecorded invoice |
| 11 | Same claimant, same receipt image | File hash or visual match | A receipt resubmitted in a later cycle |
| 12 | Weekend and holiday dates | Transaction date with no business reason | A plausible fabricated date |

## False positives, and how to clear them

| Looks like | Often is | Clear it by |
|---|---|---|
| Two identical amounts, two days apart | A part payment and the balance | Reading the payment reference |
| Same invoice number, two vendors | Vendors share a numbering format | Matching on GSTIN |
| Many invoices at ₹9,999 | A price point, not a threshold | Checking the approval matrix threshold |
| Amount just under the limit | A negotiated rate | Asking the buyer, not the vendor |
| Payment with no bill | An advance or an import remittance | The bank narration |
| Missing invoice number | A cancelled invoice | The vendor's statement |

Report each test with its false-positive count. "12 candidates, 9 cleared on the payment
reference, 3 confirmed" is an audit. "12 duplicates found" is a guess with a number attached.

## Anomaly tests that earn their keep

| Test | Why it works |
|---|---|
| Vendor spend month-on-month change above 30% | A rate change or a volume change, both worth knowing |
| A new vendor's first payment above ₹1 lakh | The highest-risk transaction in any ledger |
| Vendor bank account changed | The classic payment-diversion pattern - always verify by phone |
| A vendor with one invoice a year | A relationship with no competitive check |
| Same-day, same-amount claims from two people | A shared bill claimed twice |
| Expense category with no budget line | Spend nobody planned and nobody owns |
| Payments to a vendor whose GSTIN is inactive | Input credit at risk; also a compliance flag |
| Round-lakh payments | Quotations built backwards from a target |

## The bank side of the match

The ledger records intent; the bank records fact. Match both ways:

- **Ledger to bank**: every recorded payment cleared, on the right date, for the right amount.
- **Bank to ledger**: every debit is recorded somewhere, including charges, auto-debits and
  standing instructions. Unrecorded auto-debits are the most common invisible cost in a small
  business, because nobody ever sees the invoice.

## Evidence standard for a finding

A duplicate finding needs, in the register row or the annexure:

1. Both transaction lines with their dates, amounts and references.
2. The document for each - invoice number, payment reference.
3. The match key that proves identity (invoice number, or GSTIN + amount + period).
4. The rupee amount recoverable, and whether a credit note has been requested.

Anything short of this goes into the "to confirm" list with the question to ask.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Matching before cleaning | A vendor list of 400 is really 180 vendors |
| Reporting candidates as findings | Credibility lost on the first cleared row |
| Testing only for exact duplicates | Misses the split invoice and the re-issue |
| Ignoring the bank side | Auto-debits and charges never surface |
| No false-positive count | Nobody can judge how much to trust the sweep |
| One-off test with no re-run | The same leak returns next quarter |
