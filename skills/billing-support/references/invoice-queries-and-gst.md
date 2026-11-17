# Invoice queries: getting the document right

A billing reply that fixes the relationship but leaves the document wrong creates an accountant problem that
outlives the customer's goodwill.

## The four query types

| The customer says | What it usually is | Instrument |
|---|---|---|
| "The GSTIN is wrong" | A data error at onboarding | Amend the invoice (or cancel and reissue within the same return period) |
| "The amount is wrong" | A pricing, proration or discount error | Credit note for the difference, plus a correct invoice if the original stands |
| "I never received it" | Delivery, or a wrong email | Resend from the system, never a PDF from a personal inbox |
| "I need it in a different name or address" | Billing entity or place of supply | Amendment, and the place of supply decides the tax treatment |

## What an Indian tax invoice must carry

Check these before sending anything, every time. A missing field is a rejection at the customer's accountant and a
mismatch in their GSTR-2B.

| Field | Why it matters |
|---|---|
| Supplier name, address, GSTIN | The credit depends on it |
| A consecutive serial number, unique for the year | Duplicates and gaps both attract questions |
| Date of issue | Decides the return period |
| Recipient name, address, GSTIN (if registered) | A B2B credit needs a valid GSTIN |
| HSN or SAC code | Wrong code, wrong rate, wrong credit |
| Description, quantity, value | The line the auditor reads |
| Taxable value, rate and amount, split by CGST/SGST or IGST | The split follows the place of supply |
| Place of supply | Decides IGST versus CGST+SGST, and it is the commonest error |
| Reverse charge flag where applicable | Silence here is read as "no" |
| Signature or digital signature | Required form |

Inter-state supply is IGST; intra-state is CGST plus SGST. A wrong place of supply is not a formatting error, it is
a wrong tax collected from the customer.

## Amend, credit or reissue

- **Same return period, error in a field**: cancel and reissue with a fresh number is often simplest, and the
  original is reported as cancelled.
- **A later period, or a value change**: a credit note (or debit note) referencing the original invoice number and
  date. Never delete the original.
- **A missing invoice entirely**: issue it now, with the correct date of supply, and say so.
- **A duplicate**: the second one is cancelled, and the customer is told which number stands.

The CA decides the return treatment. This role prepares the document, the reference and the question.

## Credit note versus refund, in one table

| | Credit note | Refund |
|---|---|---|
| Money moves | No | Yes |
| Reduces the customer's payable | Yes | No |
| Tax treatment | Reduces output tax in the period of issue | Original invoice stands; refund is a payment |
| Use when | The customer will buy again, or owes you | The customer has paid and wants the money back |
| Ledger effect | Adjustment | Cash out |

## Answering in one reply

The reply has five lines and no more: what was wrong, what the correct document is, the number and date, when it
reaches them, and who to ask if their accountant disagrees. Attach the document; never describe it.

## Anti-patterns

- Sending a corrected PDF with the same invoice number and a different amount.
- A credit note with no reference to the original invoice.
- Agreeing a place of supply from the customer's shipping address without checking the registered address.
- Promising a "fresh invoice" for a period already filed, which creates a mismatch the customer discovers at
  year-end.
- Letting a salesperson issue a document from their own email. Every document comes from the system.
