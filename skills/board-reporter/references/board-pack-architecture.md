# Board pack architecture

A board pack is a decision instrument with appendices, not a report with a cover. The
test: a director who reads only pages one to six can still decide everything on the
agenda.

## The page order

| Page | Content | Length | Job |
|---|---|---|---|
| 1 | Decision list - item, ask, owner, disposition | 1 page | Tells the board what it is there to do |
| 2 | Open actions from the last meeting | 1 page | Proves the last meeting mattered |
| 3 | Performance against plan | 1 page | The four to six numbers, plan vs actual |
| 4 | Cash, runway, and the next 90 days | 1 page | The only section that can end a company |
| 5-12 | Decision papers, one page each | 1 page each | The actual decisions |
| 13 | People and organisation | 1 page | Hires, exits, key-person risk |
| 14 | Compliance, risk and legal | 1 page | What could stop the business |
| 15 | Regulatory items and resolutions | 1 page | What the statute requires this meeting |
| Annexures | Accounts, contracts, term sheets, models | As needed | Evidence, referenced not repeated |

Total for a quarterly board of a 50-person company: 15 to 20 pages plus annexures.
Ninety pages is a sign that nobody edited.

## The decision list

```
| # | Item | Ask | Owner | Disposition |
|---|------|-----|-------|-------------|
| 1 | Capex - second packing line | Approve Rs 42 lakh, 18-month payback | COO | Decide |
| 2 | Bank facility renewal | Approve sanction terms, authorise signatories | CFO | Decide |
| 3 | Q2 performance | Note | CEO | Note |
| 4 | Auditor's management letter | Note, approve management response | CFO | Decide |
```

Four columns, no prose. A director reads this page in ninety seconds and knows whether
the meeting is worth attending.

## The one-page decision paper

Fixed order, one page, no annexure in the body.

1. **The ask.** One sentence, with the number: "Approve Rs 42 lakh for a second
   packing line, funded from the SBI working-capital enhancement."
2. **Why now.** Three sentences. What changed, what breaks if this waits a quarter.
3. **The options.** Three, one of them "do nothing". Each with cost, time and the
   constraint it relieves.
4. **The recommendation.** Which option, and the one number that decides it.
5. **The money.** Capex, opex, payback, IRR or simple break-even, and the effect on
   runway. State the assumption that carries the case.
6. **The risk.** The two ways this goes wrong, the mitigation, and the early warning
   signal the board should ask about next quarter.
7. **The cost of deferring.** A number and a date. "Deferring to February costs about
   Rs 6 lakh in outsourced packing and risks the March dispatch peak."
8. **The resolution wording.** Exactly what the board is asked to pass.

## The performance page

| Metric | Plan | Actual | Last quarter | Variance | Comment |
|---|---|---|---|---|---|

Four to six rows. Revenue, gross margin, EBITDA or contribution, cash, and the one
operating metric the business runs on. Anything more belongs in the MIS, not here.

## What does not belong in the pack

- A slide of the same number the table already shows.
- A strategy essay. Strategy goes to an offsite, not to a quarterly pack.
- The full management accounts in the body. Annexure, with the summary page in front.
- Anything a director cannot act on. "Market conditions remain challenging" has never
  changed a decision.
- A decision paper with no recommendation. Management recommends; the board decides.
  A paper that presents options neutrally is a paper that has not done its job.

## Circulation and access

- One folder per meeting, read-only, named `YYYY-MM-DD board`.
- A single PDF in the order above, plus the source documents in a subfolder.
- A circulation log: who received it, at what time, on which address. This is the
  evidence for the five-day rule.
- Late papers go in a `late` subfolder with the reason recorded. Two late papers from
  the same owner in a year is a conversation with the chair.

## Pre-read discipline

The chair gets a fifteen-minute call three days out: what is contested, what is thin,
which director will push back and on what. A director who raises an objection for the
first time in the room has usually not been read in - that is a failure of this role,
not of theirs.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Pack is a monthly report with a board cover | Rebuild from the decision list down |
| Decision paper is four pages of background | Move background to an annexure, keep one page |
| No recommendation, "for the board's consideration" | Management recommends, in one line, with the number |
| Numbers with no plan column | Always plan, actual, last period, variance |
| Everything marked "for approval" | Separate decide, note, inform - and cut what is neither |
| Pack circulated the night before | Move the item; do not train the board to decide blind |
