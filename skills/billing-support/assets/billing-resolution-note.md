# Billing resolution - <reference / customer ref>

Prepared by billing-support. Customer reference only; no names, no card details, no account numbers.

## 1. What the customer asked

- **Channel and date**: <email / WhatsApp / call>, <date>
- **Their words, in one line**: "<verbatim, short>"
- **Triage**: <unrecognised charge / cannot pay now / amount is wrong / service not delivered>

## 2. What the system says

| Fact | Value | Source |
|---|---|---|
| Amount | ₹ | gateway |
| Date of charge | | gateway |
| Invoice number and date | | invoice register |
| Plan and period | | billing system |
| Payment method state | <active / expired / mandate revoked> | gateway |
| Previous failures | <n, with reasons> | gateway |

## 3. The answer to the customer

> <Four lines: what happened, what it means, what happens next and by when, the reference number. Ready to send.>

## 4. The instrument

| Field | Value |
|---|---|
| Instrument | <correction / credit note / refund to source / retry / pause / none> |
| Reason | <the rule or clause that decides it> |
| Amount | ₹ |
| Document number | <CN-xxxx / amended invoice no.> |
| Approver | <name, time> |
| Ledger line for bookkeeper | <reference, amount, match to> |
| Timeline promised | <n working days, held by <gateway / bank>> |

## 5. The queue position

- **Closed today**: <what>
- **Waiting on the customer**: <what, and the date they were told>
- **Waiting on the gateway or bank**: <what, and the escalation date>
- **Reopened from a previous close**: <yes/no, why>

## 6. The pattern

<n instances of this failure reason this month. If three or more, the named cause and the owner.>

## 7. What I could not verify

- <gateway logs at attempt level not visible> - so the retry count is inferred
- <ledger not connected> - so the booking is unconfirmed
- <mandate status not visible> - so the failure reason is a hypothesis
- <CA has not confirmed the return treatment for this correction>
