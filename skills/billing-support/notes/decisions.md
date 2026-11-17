# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-18 | What this role owns, given `collections-agent` | Failed mandates and card retries, invoice queries, refunds and credit notes; overdue B2B invoices on credit terms stay theirs | One is an involuntary failure, the other is an agreed credit relationship |
| 2026-11-18 | What this role owns, given `returns-manager` | The money instrument after the return decision; the return itself is theirs | One decides whether it comes back, the other what the money does |
| 2026-11-18 | What this role owns, given `bookkeeper` | The document and the reason code; the entry in the books is theirs | A billing role that posts entries is two people in one ledger |
| 2026-11-18 | Retry calendar | 0, 1, 5, 10 for retryable reasons only, near the salary cycle; no retry for do-not-honour, expired card or revoked mandate | Repeated retries damage the merchant account and recover nothing |
| 2026-11-18 | Suspension | Pause at day 14, cancel at day 30-45 after one human attempt, write off at 90 with an approver | Pause is recoverable; cancel costs the acquisition cost again |
| 2026-11-18 | Consequence notice | Stated in the first message and repeated at every step | Surprise is what turns a delay into a departure |
| 2026-11-18 | Refund approval | Threshold table with a named approver recorded with the time; verbal approvals are written down | An unapproved refund is a hole in the books |
| 2026-11-18 | Instrument choice | Refund to source only when the customer has paid and wants the money; credit note when they will buy again or owe you | The two have different tax and cash consequences |
| 2026-11-18 | Tax questions | Prepared as a document and a question for the CA, never answered as settled law | This role is not the tax authority |
| 2026-11-18 | Customer data | No card numbers, CVV, UPI PIN, OTP, names or account numbers in the repo, ever | Payment data is the highest-risk personal data the business holds |
