# Pack architecture

The pack is a stack of answers, not a stack of documents. This is the order and
the page budget that survives contact with a real board.

## The default shape - twelve to sixteen pages

| Page | Section | Owner | What it must contain |
|---|---|---|---|
| 1 | Chair's summary | board-reporter, signed by the chair | Three decisions, three movements, note-to-board |
| 2 | Decisions required | the executive who owns each | Ask, options, recommendation, number, resolution wording |
| 3-5 | Financial pack | finance-ops | P&L against budget, cash and runway, balance-sheet movements, one variance note |
| 6-8 | Trading and operations | mis-reporter | The five to eight metrics that run the business, with the flag and the reason |
| 9 | People and organisation | hiring-manager | Headcount against plan, two or three named risks, attrition |
| 10 | Risk and compliance | compliance-watch | Register movements, filings due, any regulatory change with a date |
| 11 | Strategy progress | chief-of-staff | The three commitments made last time, and the honest status |
| 12 | Actions and governance | board-reporter | Action register, aged; resolutions passed since last meeting |
| Appendix | Everything else | as commissioned | Detail the board asked for, and nothing it did not |

For a company under ₹25 crore revenue with an advisory board rather than a
statutory one, six to eight pages is right. The shape holds; the depth does not.

## Rules that decide what gets cut

1. **If it does not answer a question the board has already asked, it is an appendix.**
2. **If two pages answer one question, they become one page.** The board's time is the constraint, not the paper.
3. **The page budget is fixed before the sections are commissioned**, and it is allocated by `scripts/pack_planner.py` so nobody negotiates a page count in the week the pack is due.
4. **A late section does not push the pack.** It arrives as a one-page addendum with the date it arrived, and the pack circulates on time.
5. **Nothing goes in because it exists.** An existing monthly report is not a reason to include it.

## The chair's summary - the only page everybody reads

Write it last, in this order, in under 400 words:

1. **The ask.** "The board is asked to approve three things: ..." - numbered, with the resolution wording attached.
2. **The three numbers that moved.** Actual, movement, and one clause of explanation each.
3. **The note-to-board paragraph.** What happened that the board should know but is not being asked to decide.
4. **The bad news.** In the first half of the page, never in a footnote.
5. **What the board is not being asked about**, if a director has raised something that is deliberately deferred.

A director who reads only page one should be able to vote correctly.

## The appendix rule

An appendix is for detail the board asked for, referenced from a page, with a
page number in the text. An appendix is not a place to hide a section that did
not fit, and it is not a dumping ground for a management report. If nobody has
asked for it and no page references it, it is not in the pack.
