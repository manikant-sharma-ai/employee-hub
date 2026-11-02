# Invoicing and billing

An invoice is a legal document, a payment request and a data record at once. Getting one field wrong costs a correction, a delayed payment, or an input-credit problem for the customer.

## The fields that must be right, every time

| Field | Rule | Consequence if wrong |
|---|---|---|
| Supplier legal name and address | Exactly as on the GST registration | Customer cannot claim input credit |
| GSTIN | 15 characters, validated checksum | Invoice is invalid for ITC |
| Invoice number | Sequential per financial year, no gaps | Audit query; some systems reject it |
| Invoice date | The date of supply or the date raised, per policy | Wrong tax period |
| Customer legal name, address, GSTIN | As given, not as remembered | ITC denial for the customer |
| Place of supply | State of the recipient for services, state of delivery for goods | Wrong IGST vs CGST/SGST split |
| HSN or SAC code | Correct code for the goods or service | Classification risk on review |
| Description and quantity | Specific enough to identify the supply | Disputes, and a weak audit trail |
| Taxable value | Before tax, with any discount shown separately | Wrong tax |
| Rate and tax amount | Split CGST+SGST or IGST, per place of supply | Wrong tax, wrong ledger |
| Total in words | Matches the figure | Common rejection in B2B and government |
| Bank details and terms | Correct account, due date stated | Payment to a wrong or closed account |
| Reverse charge flag | Stated where applicable | Both parties' returns disagree |

## The place-of-supply decision

This is the field most often wrong, and it decides the whole tax treatment.

| Supply | Place of supply | Tax |
|---|---|---|
| Goods, moved | Where the goods are delivered | Intra-state: CGST+SGST. Inter-state: IGST |
| Goods, not moved (installed) | Where installed | As per that state |
| Services, B2B | Recipient's registered address | Intra or inter, by state comparison |
| Services, B2C | Supplier's location (generally) | CGST+SGST |
| Immovable property services | Where the property is | That state |
| Event services | Where the event is held | That state |
| Transport of goods | Destination (generally) | That state's treatment |

If the case is genuinely ambiguous - a cross-border SaaS subscription, a mixed goods-and-service contract - present the two readings and the amount at stake, and say the CA decides.

## Invoice types and when each is used

| Type | When | Note |
|---|---|---|
| Tax invoice | A taxable supply | The default |
| Bill of supply | Exempt or composition supply | No tax charged, so no ITC for the buyer |
| Credit note | Value or quantity reduced after invoicing | Must reference the original invoice |
| Debit note | Value increased, or a purchase return to a vendor | Mirror of the credit note |
| Proforma | Before supply, for approval or advance | Not a tax document |
| Export invoice | Supply outside India, with LUT or with IGST | Needs the declaration and the shipping bill reference |
| E-invoice | Above the notified turnover threshold | IRN and QR are mandatory once applicable |

## Numbering

- One series per entity per financial year, e.g. `ACM/25-26/0001`.
- No gaps. If an invoice is cancelled, cancel it in the system with a reason rather than deleting it.
- Never renumber to make a report look tidy.
- Never use the same number for a credit note series - it needs its own prefix.

## Sending and follow-through

1. **Send to the billing contact and the AP contact** - they are usually different people.
2. **Attach the invoice as a PDF and put the key facts in the body**: invoice number, amount, due date, PO reference. Accounts teams process from the email body more often than from the attachment.
3. **State the PO number** if the customer requires one; an invoice without it sits in a queue.
4. **Log the send date** - the due date runs from the invoice date, not from when they opened the email.
5. **Do not resend the same invoice daily.** One reminder at due date minus three days is more effective than five after.

## Anti-patterns

- **Raising an invoice before the PO or the approval exists.** It gets rejected and the payment clock restarts.
- **Bundling four months into one invoice.** It is harder for the customer to approve and harder for you to attribute.
- **Rounding the total to a round number.** It breaks the tax computation and looks improvised.
- **Sending from a personal email address.** It reads as unverifiable, and the record leaves the business.
- **Correcting an invoice by editing it.** Issue a credit note and a fresh invoice; an edited tax document is not a document.
- **Assuming a customer's GSTIN from their state code.** Validate it.
