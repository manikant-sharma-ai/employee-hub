# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-15 | What this role owns, given `expense-auditor` | The forward cost base: right size, right price, right term | The auditor asks whether a past bill was allowed; this role asks what should be paid next |
| 2026-11-15 | What this role owns, given `procurement` | The review of what is already bought; procurement runs the new purchase | One is a portfolio, the other a transaction |
| 2026-11-15 | What this role owns, given `budget-planner` | The evidence and the cut list that the budget is built from | The plan sets the number; this role finds where the number can come from |
| 2026-11-15 | Where the inventory starts | The statements, reconciled to the ledger | Vendor dashboards cannot show what is paid to everyone |
| 2026-11-15 | Utilisation source | The SSO or admin log, named in the output | "Nobody uses it" without a log is an opinion, and it gets a tool cancelled that people use |
| 2026-11-15 | Savings arithmetic | Always net of switch cost, first year | Gross savings flatter the case and destroy the next one |
| 2026-11-15 | Sequencing | Waste, then price and size, then structure | The first wave funds the credibility for the third |
| 2026-11-15 | Execution | This role never cancels, downgrades or contacts a vendor | Account changes and card charges belong to a human with the credentials |
| 2026-11-15 | Do-not-cut | Backups, security, monitoring, compliance, the tools the business sells on | A saving that becomes an incident is not a saving |
