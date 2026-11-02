# Voucher entry

The entry shape for each document type a small business produces. If the document is one of these, the entry is not a matter of judgement.

## Purchase bill from a registered vendor

A bill of ₹1,00,000 plus 18% GST, with 2% TDS under 194C:

| Ledger | Debit | Credit |
|---|---|---|
| Purchases / Expense | 1,00,000 | |
| Input CGST 9% | 9,000 | |
| Input SGST 9% | 9,000 | |
| TDS payable 194C | | 2,000 |
| Creditor - vendor | | 1,16,000 |

Note: TDS is deducted on the taxable value, not on the GST-inclusive amount, unless the vendor is a specified case. Label it "confirm with CA" when the section is unclear.

## Sales invoice

A sale of ₹50,000 plus 18% GST:

| Ledger | Debit | Credit |
|---|---|---|
| Debtor | 59,000 | |
| Sales | | 50,000 |
| Output CGST 9% | | 4,500 |
| Output SGST 9% | | 4,500 |

Intra-state is CGST + SGST; inter-state is IGST at the full rate. Getting this wrong is a filing error, not a rounding error.

## Payment to a vendor

| Ledger | Debit | Credit |
|---|---|---|
| Creditor - vendor | 1,16,000 | |
| Bank | | 1,16,000 |

If the payment settles two invoices, debit the creditor once and reference both invoice numbers in the narration. If it pays an advance, debit "Advance to vendor" instead.

## Receipt from a customer

| Ledger | Debit | Credit |
|---|---|---|
| Bank | 59,000 | |
| Debtor | | 59,000 |

## Expense with no GST, paid by UPI

| Ledger | Debit | Credit |
|---|---|---|
| Expense ledger | 4,500 | |
| Bank | | 4,500 |

## Payment-gateway settlement

Gross sales ₹1,00,000, fee ₹1,900, net received ₹98,100:

| Ledger | Debit | Credit |
|---|---|---|
| Bank | 98,100 | |
| Gateway charges | 1,900 | |
| Sales (already invoiced) | | 1,00,000 |

Book the fee as an expense. Never book the net as revenue.

## Salary

Gross ₹40,000, TDS ₹2,000, employee PF ₹1,800, net ₹36,200:

| Ledger | Debit | Credit |
|---|---|---|
| Salary expense | 40,000 | |
| TDS payable | | 2,000 |
| PF payable | | 1,800 |
| Salary payable / Bank | | 36,200 |

Employer PF and ESI contributions are a separate expense, not part of the employee's gross.

## Required fields per entry

| Field | Rule |
|---|---|
| Date | The document date, not the entry date |
| Voucher number | Sequential, no gaps, never reused |
| Narration | What it was for, in words a stranger understands: "Oct rent, Hoskote godown, inv 4471" |
| Document reference | Invoice or bill number as printed on the document |
| Ledger | An existing account from the chart |
| Tax lines | Explicit, never folded into the base amount |
| Attachment | The image, named `YYYY-MM-DD_vendor_amount.pdf` |

## The five-minute pre-entry check

1. Does the invoice number already exist in the books? (duplicate)
2. Is the date inside the open period? (cut-off)
3. Does the GSTIN on the bill match the vendor's registered name? (input credit at risk)
4. Is the tax split intra-state or inter-state, and does it match the place of supply?
5. Is the total on the bill equal to the sum of the lines? (a bill that does not add up is a question for the vendor)

## Anti-patterns

- **Entering a bill as one line "₹1,18,000 purchases"** and losing the tax split. Input credit is then unclaimable without reconstructing the bill.
- **Folding freight into the purchase value** when the vendor charged it separately. It distorts stock cost and, for resale, the GST treatment.
- **Using the payment date as the bill date.** It moves the expense into the wrong month and breaks the cut-off.
- **Narrations like "as discussed" or "misc"**. Six months later nobody can act on either.
- **Entering a handwritten bill as if it were a tax invoice.** It is not, and the input credit will be disallowed.
