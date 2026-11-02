# Double entry basics

Every entry has two sides and they are equal. That is the whole system. Everything else in bookkeeping is a naming convention on top of it.

## The five account types

| Type | Increases on | Normal balance | Examples |
|---|---|---|---|
| Asset | Debit | Debit | Bank, cash, stock, debtors, equipment |
| Expense | Debit | Debit | Rent, salaries, freight, software |
| Liability | Credit | Credit | Creditors, loans, GST payable, TDS payable |
| Equity | Credit | Credit | Capital, retained earnings |
| Income | Credit | Credit | Sales, service income, interest received |

Debits on the left, credits on the right. Total debits equal total credits, in every voucher, every time.

## The nine transactions a small business actually has

| Transaction | Debit | Credit |
|---|---|---|
| Sale on credit | Debtors | Sales + Output GST |
| Sale for cash | Bank / Cash | Sales + Output GST |
| Purchase on credit | Purchases + Input GST | Creditors |
| Pay a creditor | Creditors | Bank |
| Receive from a customer | Bank | Debtors |
| Pay rent | Rent expense | Bank |
| Pay salary | Salary expense + TDS payable | Bank |
| Owner puts money in | Bank | Capital |
| Buy equipment | Equipment | Bank / Creditor |

If a transaction does not fit one of these shapes, it is usually two transactions wearing one description - a part payment against two invoices, or a purchase that includes freight.

## Reading a trial balance

- **Assets less liabilities equals equity** - if not, an entry is unbalanced somewhere, or an opening balance was typed wrong.
- **A debit balance in a creditor ledger** means you paid more than you owed, or you posted a payment to the wrong vendor.
- **A credit balance in a debtor ledger** means a customer has overpaid or a receipt went to the wrong account. Both are real and both need a person.
- **Bank balance in the books differs from the statement** by timing, by an unrecorded charge, or by an error. That is a reconciliation job, and it belongs to `finance-ops`.

## The shapes that catch people out

- **Part payment**: one payment, two invoices, and a balance. The credit is the bank for the full amount; the debits are two creditors for their parts.
- **Advance paid**: money out before the bill arrives. That is an advance to the vendor (an asset), not an expense. When the bill comes, the advance is adjusted against the creditor.
- **Credit note**: a sales return reduces income and output GST. It is not a negative sale; it is its own document with its own number.
- **Discounts**: a trade discount reduces the invoice value; a cash discount is an expense. They are not the same and they do not post the same.
- **Gateway settlement**: bank receives the net, the fee is an expense, and revenue is the gross. Booking the net understates revenue every month.
- **Owner's personal expense paid from the business account**: a drawing, not a business expense. Booking it as an expense overstates costs and understates the owner's drawings.

## Why balances drift

1. **A one-sided entry** - an amount posted to one ledger and not the other. Rare in accounting software, common in spreadsheets.
2. **A duplicate** - the same bill entered twice, usually a week apart and with a slightly different number.
3. **A wrong sign** - a credit entered as a debit in one ledger.
4. **A wrong period** - an entry in the wrong month, which breaks both months.
5. **A rounding difference** - paise dropped on many entries until they are rupees.

Each of these has a signature. Learn the signature rather than hunting line by line: duplicates cluster around month-end, sign errors cluster in one ledger, period errors cluster around a cut-off date.

## Anti-patterns

- **"It balances, so it is right."** Balancing proves the arithmetic, not the coding. A rent payment booked to repairs balances perfectly.
- **Suspense entries to close a gap.** The gap is the information.
- **Editing a posted voucher to fix a period.** Post a correcting entry with a reference instead.
- **Booking a capital purchase as an expense** because it is simpler. It distorts the P&L and the asset register.
- **Netting a receipt against an expense** because they are with the same party. Two transactions, two entries.
