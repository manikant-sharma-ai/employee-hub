# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-07 | What this role owns, given `support-agent` and `collections-agent` exist | The relationship, the health score, the QBR, the renewal, the expansion and the save | Tickets are transactions; a renewal is a relationship with a date on it |
| 2026-11-07 | Who answers a customer's complaint | `support-agent` for the reply; this role owns the account consequence | A reply closes a ticket, not a renewal |
| 2026-11-07 | Who chases an overdue invoice | `collections-agent`, with the account owner informed | Cash chasing and relationship management need separate voices |
| 2026-11-07 | Health score design | Five weighted inputs with raw values shown, usage carrying the most weight | Sentiment is the input that lies; usage is the one that does not |
| 2026-11-07 | Renewal timing | The conversation starts at 90 days, with the notice period and PO process confirmed at 120 | Late discovery of paperwork is the most common lost renewal |
| 2026-11-07 | Discounting | Last rung of the concession ladder, and only with a term or scope change | The first concession sets the anchor for every renewal after it |
| 2026-11-07 | QBR format | Nine pages, their goal quoted, one ask, decisions with owners | A feature review produces no decision |
| 2026-11-07 | Cohort churn analysis | Out of scope - `churn-analyst` (#49, not shipped) | Per-account work is this role; the pattern across accounts is analysis |
