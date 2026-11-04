# API and integration testing

Screens lie politely; APIs fail loudly. Most money bugs live in the layer between
two systems, where nobody is looking.

## What to test on every endpoint

| Case | What to assert |
|---|---|
| Happy path | 200, correct shape, correct values, no extra fields leaking |
| Validation | 400 with a field-level message, not a generic failure |
| Auth | 401 without a token, 403 with the wrong role |
| Not found | 404 for a missing id, not 500 |
| Duplicate | Idempotency key honoured; the second call does not create a second record |
| Boundary | Max length, zero, negative, huge numbers, unicode and emoji |
| Partial failure | A dependent service down returns a defined error, not a hang |
| Rate limit | 429 with a retry hint, and the client backs off |

## The integration checks that catch real incidents

- **Webhooks**: signature verified, retried on failure, idempotent on replay, and the same event twice produces one effect.
- **Third-party timeouts**: payment gateway, SMS, email. Force a timeout and confirm the user sees a defined state, not a spinner.
- **Partial success**: order created but payment confirmation missing - what does the user see, and what fixes it?
- **Currency and rounding**: ₹ rounding at the paise, GST split correct, total equals the sum of lines.
- **Timezone**: an event at 23:59 IST belongs to the right day in the report.
- **Pagination**: no duplicates or gaps across pages when rows are inserted mid-scroll.
- **Order of operations**: cancel after ship, refund after refund, retry after success.

## How to run it without a test suite

1. Postman or a curl script, saved, with environment variables per environment.
2. One file per flow, named after the business flow, not the endpoint.
3. Assertions on the response body, not just the status code.
4. A seed step and a cleanup step, so the run is repeatable.

If the team has CI, these become a Playwright or pytest suite that runs on every
push - but a saved curl collection that a person runs beats no test at all.

## Contract drift

When two teams own the ends of an integration, the schema is the contract. Record
the expected shape, and fail the build when it changes. The alternative is
discovering it from a customer.

## Evidence to capture

Request, response, headers (redacted), timestamp, trace or request id. That is
what makes a report actionable for a developer who was not there.

## Anti-patterns

- Testing only the happy path because the API "works".
- Trusting the frontend's validation as the API's validation.
- Testing on production data with real cards.
- No idempotency test, then a double charge in week one.
- A green suite that asserts only `status == 200`.
