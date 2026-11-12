# Treasury controls and fraud

Treasury is where money leaves, which makes it the one function where a control gap is not an
inefficiency but a loss. The controls here are cheap; the losses are not.

## The five controls that stop most losses

| Control | How it works | What it stops |
|---|---|---|
| Maker-checker | One person prepares the payment, another approves it | A single person's mistake or intent |
| Payee change callback | Any new bank detail verified by phone on a number already on file | Vendor-email fraud, the most common attack |
| Duplicate check | Match invoice number, amount and date against the last 90 days | Paying the same bill twice |
| Bank reconciliation to the day | Every debit matched to an approved payment | Unauthorised or unexplained debits |
| Access hygiene | No shared OTP device, no credentials in email or chat, limits per user | Account takeover |

## The vendor bank-detail change, in detail

This is the fraud that costs Indian SMEs the most per incident, and it is always the same shape: a
message from a known supplier's email, a new account number, urgency, and a request for secrecy.

1. Never act on the message, however correct the letterhead or the email thread.
2. Call the number in the vendor master, not any number in the message.
3. Ask a question only the real vendor can answer - the last invoice amount, the contact's name.
4. Confirm in writing to the address on file, and get a signed letter on letterhead with the GSTIN.
5. Change the master record only after all four, and record who verified and when.
6. Pay a small test amount first on any change above the approval threshold.

## Red flags in a payment request

- Urgency plus secrecy, or an instruction to bypass the normal approver.
- A round-number "advance" to a new vendor with no PO.
- A payee name that differs from the invoice's supplier name by a word.
- An invoice number that already exists with a different amount.
- A bank account in a state where the vendor has no operation.
- A request to pay a personal account for a company invoice.

## Segregation of duties in a small team

A five-person business cannot separate everything, so separate the one thing that matters: the person
who creates a payee cannot also approve and release. If the founder is the approver, the founder sees
the bank-detail change and the callback result before approving, every time. Where even that is
impossible, a second signature on the bank mandate and a monthly independent statement review is the
minimum.

## Anti-patterns

- **The founder's phone as the OTP device for every payment.** Convenient, and the single point of
  failure for the entire treasury.
- **Approving from a screenshot.** Approval needs the schedule and the payee, not a picture of a bill.
- **"We know the vendor."** The fraud arrives through the vendor's own compromised mailbox.
- **Reconciling monthly.** A month is long enough for a wrong debit to become a rounding difference.
- **Shared portal credentials.** No audit trail, and no way to say who did what.

## The monthly control test

Run these five in twenty minutes on the first working day of the month, and record the result even
when it is clean:

| Test | Method | Pass condition |
|---|---|---|
| Payee master changes | List changes in the month, match to callbacks | Every change has a name, a date and a callback |
| Duplicate payments | Match amount and invoice number across 90 days | Zero, or a recovery in progress |
| Unexplained debits | Bank statement lines with no matching approval | Zero over the threshold |
| Approver coverage | Payments released while the approver was away | Every one has a documented delegate |
| Access review | Portal users and OTP devices | No leaver, no shared device, no shared password |

Write the result into the journal as one line: month, tests run, exceptions, action. A control that is
not tested monthly is a control that exists in a document.
