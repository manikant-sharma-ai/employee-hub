# The edge-case matrix

The matrix is the memory of the role. Every escaped bug belongs in it, or it will
escape again.

## Rows and columns

Rows are inputs and states. Columns are what must be true. Fill pass/fail and a
note; a matrix with no notes is a guess.

| Input / state | Valid | Empty | Boundary | Too long | Wrong type | Duplicate | No permission |
|---|---|---|---|---|---|---|---|
| Name | | required error | 1 char | 200 chars | emoji, script | - | read-only view |
| Phone | | | 10 digits, +91 | 15 digits | letters | same number twice | - |
| Amount | | 0 | 1, 99,999,99,999 | - | negative, decimal | double submit | refund path |
| Address | | | pin code only | 60-word address | - | - | - |
| File upload | | none | 1 byte, at limit | over limit | wrong format | same file twice | quota full |

## The universal list

Test these on any flow that touches data or money:

- **Empty** - first use, nothing entered.
- **Boundary** - the smallest and largest allowed value, and one either side.
- **Too long** - the longest realistic string, in the longest language.
- **Wrong type** - letters where numbers go, a file where an image goes.
- **Duplicate** - the same submit twice, a double tap, a double payment.
- **No permission** - a lower role trying a higher action, deep-linked directly.
- **Interrupted** - the connection drops mid-save, the app is backgrounded, the phone rings.
- **Stale** - the record was changed in another tab, the price changed after the cart was filled.
- **Slow** - a 3G connection, a 5-second API response, a timeout.
- **Locale** - ₹1,00,000 not ₹100,000; dd/mm/yyyy; a name with no spaces; a Devanagari name.
- **Session** - expired token mid-flow, logout in another tab, back button after logout.
- **Back button** - after success, after payment, mid-form.

## Money-specific, always

- Failure shows whether money was deducted, and what to do.
- Double submit does not double charge.
- Refund path works, and the customer sees it.
- Amounts round correctly; tax is not recomputed client-side.
- The confirmation is the source of truth, and it matches the admin panel.

## How to use it without drowning

Do not run the whole matrix every release. Run the rows that the change touches,
plus the money rows, plus whatever broke last time. Write in the plan which rows
were run and which were not - that sentence is what makes the sign-off honest.

## Anti-patterns

- A matrix that only exists in a spreadsheet nobody opens.
- Testing "empty" only on the first field.
- Ignoring the second language because the team writes in English.
- Assuming a disabled button prevents the action; deep links and APIs do not care.
- Not testing the back button, which is the most-used control in Indian mobile usage after the home button.
