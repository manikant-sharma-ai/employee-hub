# Card update and payment methods

The customer wants to pay. Everything between them and the payment is our design, and most of it is friction we
added.

## The one-minute path

- **A direct link to the update screen**, in the first line of the message, not behind a login and a menu.
- **The card ending in <last4> shown**, so the customer knows which one is wrong.
- **One field of friction removed**: no re-entering the address, no new password, no OTP to a number that has
  changed.
- **Confirmation in the same breath**: "as soon as you save it, we will charge the pending invoice of ₹X today" -
  so the customer knows the update finishes the job.

## India-specific methods

| Method | What to tell the customer | The failure to watch for |
|---|---|---|
| Card (Visa/Mastercard/RuPay) | "Update the card ending <last4>" | Recurring card payments need an e-mandate; a new card needs a fresh one |
| UPI AutoPay | "Approve the mandate in your UPI app - it expires in 24 hours" | Mandates revoked on the bank side without notice |
| Netbanking | "Pay once now, and we will set up the automatic instruction" | Sessions time out; the customer thinks it worked |
| Bank transfer / NEFT | "Here are the account details and the reference to quote" | Payment arrives without the reference and cannot be matched |
| Wallet | Rarely recurring; treat as one-off | Balance and KYC limits |

A recurring card payment that "worked last year" is often a mandate that expired with the old card. Ask for the
mandate, not just the card.

## Mandates, plainly

- **An e-mandate is a standing instruction, not a saved card.** It can be revoked by the customer's bank without
  telling us, and the first sign is a `mandate_revoked` failure.
- **The amount ceiling matters.** A mandate registered for ₹5,000 will not collect a ₹12,000 renewal, and the
  failure looks like a decline.
- **The customer approves it in their own app.** No amount of retrying completes an unapproved mandate.

## When the customer cannot update

- **They have no access to the account** - send a payment link that does not require login, and reconcile the
  payment manually with the reference.
- **They are locked out because of the failed payment** - that is our design failing. Restore read access first,
  then ask.
- **The card belongs to a colleague who has left** - ask for the billing contact change in writing, and record it.

## What never goes in a message

Never ask for a full card number, CVV, PIN or OTP by email, chat or phone. The only place a card is entered is our
own hosted screen. If a customer offers the details, tell them not to send them and send the link instead.
