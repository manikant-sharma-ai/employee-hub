# Vendor and payment tracking

The question a business asks most often is not "what did we spend" but "what do we owe, to whom, and by when". That is a tracker, and it is the bookkeeper's daily product.

## The tracker columns

| Column | Why |
|---|---|
| Vendor | Legal name, not the brand |
| Invoice number | The vendor's number, exactly as printed |
| Invoice date | For the ageing bucket |
| Due date | From the terms, not from a habit |
| Amount | Gross, and the taxable value separately where GST applies |
| TDS deducted | So the payment equals the invoice minus TDS |
| Amount paid | Cumulative, not the last payment |
| Balance | Amount minus paid |
| Status | Open / part-paid / paid / disputed / on hold |
| Days overdue | Today minus due date, only when unpaid |
| Payment reference | UTR or cheque number, so a query can be answered |

## Ageing buckets

| Bucket | Meaning | Action |
|---|---|---|
| Not yet due | Within terms | Nothing |
| 1-15 days overdue | Normal slippage | Pay in the next run |
| 16-45 days | A pattern | Find out why before paying; usually a missing bill or an approval |
| 46-90 days | A dispute or a cash problem | Escalate with the facts |
| 90+ days | Neither party is treating it as a live debt | Confirm it is still owed before paying it |

## Matching a payment to invoices

The commonest hard question: one payment, three invoices, one of which was partly paid.

1. **Oldest first**, unless the vendor's own statement says otherwise.
2. **Reference the invoice numbers in the narration** - "paid inv 4471, 4488, part 4492".
3. **If the amount does not match exactly**, check TDS first, then a discount, then a credit note, then a rate difference. In that order - it is almost always TDS.
4. **If a vendor statement disagrees**, reconcile it line by line before paying the difference. Vendors make mistakes too, and paying the difference quietly is how double payments start.
5. **Never leave a payment unmatched in a suspense ledger.** An unmatched payment is an open question, and it becomes an argument at year end.

## Controls worth keeping, even in a small business

- **One person raises the bill, another approves the payment.** In a two-person business, the founder approves; the bookkeeper prepares. Never the same hand for both.
- **Bank details are changed only on a phone call to a number from the original contract** - never on the strength of an email. This is the single most common successful fraud against an Indian SMB: a vendor email with new account details, an urgent tone, and a payment that cannot be recovered.
- **A payment run on a fixed day**, once or twice a week. Ad-hoc payments are how urgency becomes a control.
- **Advance payments need a PO and a name.** An advance with neither is a loan to a stranger.
- **Cash payments above the statutory threshold are disallowed as an expense** - the exact limit is a question for the CA, and it changes.

## What to hand over weekly

One page:

1. **Due in the next seven days** - vendor, invoice, amount, and whether the bill is in hand.
2. **Overdue** - with the reason, not just the age.
3. **Disputed** - the amount, the issue, who is resolving it.
4. **Paid this week** - with the UTR, so the bank reconciliation later is trivial.
5. **Cash position** - bank balances as of the statement date, and what is committed in the next fortnight.

## Anti-patterns

- **A tracker with no due dates**, only invoice dates. Then everything looks equally urgent.
- **Marking an invoice paid because a payment of a similar amount went out.** This is how a vendor gets paid twice and a real creditor sits unpaid for a year.
- **Ignoring credit notes.** They reduce the payable and are usually forgotten, then paid in full.
- **Paying a disputed invoice to keep the peace** without recording the dispute. The dispute then reappears as a margin surprise.
- **Changing a vendor's bank details on email instruction**, however convincing. Call the number on the original contract.
