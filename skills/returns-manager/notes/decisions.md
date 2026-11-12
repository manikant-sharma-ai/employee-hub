# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-13 | What this role owns, given `support-agent` | The decision, the money, the reverse movement, the read | Support writes the reply to one customer; the disposition and the cost of returns is a different job |
| 2026-11-13 | Policy basis | The policy in force on the order date, with the channel rule overriding | Anything else is a retroactive change and a guaranteed complaint |
| 2026-11-13 | Sequence | Grade, then refund, where the amount is material | Refunding first and finding an unsaleable unit is a double loss |
| 2026-11-13 | Deductions | Only those disclosed at purchase, stated before the refund | Undisclosed deductions are disputes with a statutory basis |
| 2026-11-13 | Integrity flags | Flag and hold, never accuse; a human decides the account | A wrong accusation is unrecoverable and penalised by the channel |
| 2026-11-13 | Low-value returns | Refund without return when reverse cost exceeds recovered value | The arithmetic decides, and it is recorded as a write-off |
| 2026-11-13 | Execution | This role never posts the refund, credit note or stock adjustment | Money and stock move through `bookkeeper` and a human with panel access |
| 2026-11-13 | Notes | No customer name, address, phone or payment detail in the repo | The repo is public; the log carries order IDs, not people |
