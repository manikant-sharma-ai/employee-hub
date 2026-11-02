# Controls and fraud checks

Most money lost in a small business is lost to boring, repeatable patterns: the same bill paid twice, a vendor's bank details changed by email, a refund to a new account. Ten minutes a month catches most of it.

## The monthly control pass

| Check | How | Threshold to act |
|---|---|---|
| Duplicate payment | Same amount + same vendor within 30 days, or same invoice number twice | Any duplicate |
| Duplicate bill | Same bill image hash, or same invoice number from one vendor | Any duplicate |
| Round numbers | Payments ending in 000, 5000, 00000 | Over ₹10,000 |
| New vendor | First payment to a vendor in the period | Any new vendor above ₹25,000 |
| Changed bank details | Any change to a vendor's account in the master | Every change, always |
| Refund to a different account | Refund requested to a new account or UPI ID | Every case |
| Payment before bill | Money out with no purchase order or bill | Any case |
| Off-hours entry | Entries posted outside working hours in the accounting system | Repeated pattern |
| Vendor with no GSTIN | Registered vendor missing a GSTIN | Any vendor above threshold |
| Expense just under an approval limit | Multiple entries at ₹9,900 against a ₹10,000 limit | Repeated pattern |
| Same person raises and approves | Payment approved by the person who created it | Any case |
| Cash withdrawals | Frequency and round amounts | Weekly or round |

## Vendor bank-detail change: the highest-risk event

This is the most common successful fraud against Indian SMBs, and it usually arrives as an email that looks like the vendor's.

1. **Never action a change from an email alone.** Call the number on the original contract or invoice - not a number in the email.
2. **Verify the account name matches the legal entity name.** A mismatch is a stop.
3. **Ask for a cancelled cheque or a bank statement header**, on letterhead.
4. **Two-person approval** for any change above the business's threshold.
5. **Log the change**, with who verified it, when, and how.
6. **Hold the next payment one cycle** if anything is unclear. A delayed payment is recoverable; a wrong transfer usually is not.

## Refund and return fraud patterns

| Pattern | Signal | Action |
|---|---|---|
| Refund to a new UPI ID or account | Different from the original payment method | Refund only to the source |
| Multiple refund requests for one order | Same order ID, different contacts | Freeze and check |
| High-value return after the window | Pressure to make an exception | Policy applies; escalate, do not decide |
| COD return with an empty box | Weight discrepancy in the logistics record | Claim with the carrier, do not refund blind |
| Staff-initiated discount then return | Same staff ID on both | Review the pattern |

## Segregation of duties, for a business small enough to say it cannot afford it

Minimum viable version:

| Step | Who | Never the same person as |
|---|---|---|
| Create the vendor | Ops | The person who pays |
| Raise the bill | Whoever received the goods | The person who pays |
| Approve the payment | Owner or a director | The person who created it |
| Execute the payment | Finance | The person who approved it |
| Reconcile the bank | Finance | The person who executed the payment, where headcount allows |

If headcount makes this impossible, name the compensating control: a monthly independent review of the bank statement by the owner, dated and signed.

## Red flags worth escalating immediately

- A vendor email asking to change bank details, especially with urgency or a new domain that looks similar.
- An employee asking to be the sole point of contact for a vendor's payments.
- Invoices from a vendor whose address is a residential flat, at a value above the normal range.
- A customer asking for a refund to an account that is not the payer's.
- Bank statements that do not match the system and nobody can explain why.
- Cheques or transfers to a "consultant" with no contract and no deliverable.

## How to raise it

Report the facts, the amount, the date and the documents - and no accusation. Then hand it to a named human. You never confront a person, and you never write the word "fraud" in a note unless a human has confirmed it.

## Anti-patterns

- **Reconciling the difference away.** Every unexplained gap is a control failure, whether or not fraud is involved.
- **Trusting a changed bank detail because the email looked right.** The email looking right is the attack.
- **Approving an exception because the amount is small.** Small is how the test starts.
- **Leaving a duplicate-payment recovery to "next month".** Recovery gets harder every week.
- **Burying a red flag in the middle of a close pack.** Escalate it separately, before the pack.
- **Accusing someone.** Report the pattern and the documents; let the owner decide what it means.
