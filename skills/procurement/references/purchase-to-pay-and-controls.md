# Purchase to pay and controls

The purchase is not done when the price is agreed. It is done when the goods are
received, the bill is matched, the payment is scheduled and the file can answer a
question two years later.

## The chain

| Step | Document | Control |
|---|---|---|
| 1. Need | Requisition, one line, from the person who needs it | Someone other than the buyer approves the need |
| 2. Approval | Approval note with the comparison and the TCO | Approval level by value, not by relationship |
| 3. Order | Purchase order against the approved quote | PO number on every later document |
| 4. Receipt | Goods receipt note, with quantity and condition | The person who receives is not the person who ordered |
| 5. Bill | Vendor invoice | Matched to PO and GRN before it enters the books |
| 6. Payment | Payment advice | Paid by `finance-ops` on the agreed terms |
| 7. File | PO + GRN + invoice + warranty + vendor check | One folder, retrievable by PO number |

## The three-way match

Invoice = PO = GRN. Any mismatch is an exception with a question, not a rounding.

| Mismatch | Question | Who answers |
|---|---|---|
| Quantity differs | Short delivery, or a bill for goods not received? | Stores / dispatch |
| Rate differs | Was a discount agreed and not applied? | Buyer |
| GST rate differs | Wrong HSN or a composition vendor? | Vendor, then the CA |
| Freight added | Was it in the quote or not? | Buyer |
| Extra line item | Was it approved as a scope change? | Requester |

## The approval matrix

| Value (per purchase, annualised) | Approves | Evidence required |
|---|---|---|
| Up to ₹25,000 | Department head | One quote, or a rate contract reference |
| ₹25,000 - ₹2 lakh | Founder or finance head | Three quotes, comparison table |
| ₹2 lakh - ₹10 lakh | Founder plus one other signatory | Comparison, TCO, vendor check, approval note |
| Above ₹10 lakh | Board or the delegated committee | All of the above, plus a contract review |

Set the numbers for the business, write them down, and apply them to the annual
value of a recurring purchase - not the monthly bill.

## Split purchases

Splitting one requirement into three POs to stay under a limit is the control
failure auditors test first. The rule: **if the need is one requirement, the value
is the total**, regardless of how many orders it takes.

## Vendor master and the bank-detail change

The most common successful fraud against a small business:

1. An email, apparently from the vendor, with new bank details.
2. A PDF letterhead, a signature that looks right, a plausible reason.
3. Payment goes to the new account and the real vendor is never paid.

Controls, all three, every time:

- **Call a number from the original contract or the GST record**, never from the email.
- **Require a cancelled cheque** in the vendor's legal name, and match it to the GSTIN.
- **Two-person approval** for any change to vendor master data, logged with the date
  and the name of who confirmed it by phone.

## Advance payments

| Situation | Rule |
|---|---|
| New vendor, first order | Maximum 30%, balance against GRN |
| New vendor, capital equipment | Milestone payments, 20/60/20, with a commissioning test |
| Known vendor, repeat order | Per the rate contract, typically 15-30 days after GRN |
| Any request for 100% advance | Security - a bank guarantee, a post-dated cheque, or a refusal |

## The file that survives an audit

- The requirement and who approved it.
- The quotes received, including the ones not chosen, with dates.
- The comparison and the recommendation.
- The vendor check, with the GSTIN lookup date.
- The PO, the GRN, the invoice and the payment reference.
- The warranty terms and the AMC start date.
- The renewal date and who owns the review.

## Anti-patterns

- A PO raised after the goods arrive, to tidy up.
- Receiving goods and paying the bill in the same week, with no GRN.
- One person ordering, receiving and paying.
- A vendor master change made by email with no call.
- Renewals that auto-charge because nobody owned the calendar date.
- A filing system organised by month, so the warranty for a machine bought in 2024
  is unfindable in 2026.
