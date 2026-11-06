# Data-room upkeep

A data room is not for the raise. It is the company's record, kept current so that
diligence is a link rather than a month of work.

## The structure

| Folder | Contents | Refresh |
|---|---|---|
| 01 Corporate | COI, MOA, AOA, PAN, GST, board and shareholder resolutions | On change |
| 02 Cap table | Cap table, ESOP plan and grants, convertibles, register of members | Monthly |
| 03 Financials | Audited accounts, management accounts, bank statements, MIS | Monthly |
| 04 Tax and statutory | ITR, GST returns, TDS, PF, ESI, notices | Monthly or on filing |
| 05 Contracts | Key customers, vendors, leases, loans | On signature |
| 06 People | Employment agreements, IP assignments, consultants, vesting | On hire |
| 07 IP and tech | Trademarks, patents, licences, architecture, security policy | Quarterly |
| 08 Compliance | Privacy policy, DPDP records, sector licences, insurance | Quarterly |
| 09 Litigation | Notices, cases, disputes | On event |
| 10 Fundraise | Model, deck, prior round documents, SHA, investor updates | Per round, updates monthly |

## The monthly ten minutes

1. Add last month's management accounts and bank statements.
2. Update the cap table if anything moved - a grant, an exercise, a conversion.
3. Add the investor update, in the folder, in order.
4. Check the two documents most likely to be stale: the ESOP schedule and the insurance policy.
5. Check the access log. Remove anyone who has left, add anyone who has joined.

A data room maintained monthly takes ten minutes. Rebuilt for diligence, it takes
three weeks and it is always missing the same two documents.

## Access

| Investor type | Access | Notes |
|---|---|---|
| Existing shareholder | Financials, cap table (own holding), updates | Read-only, watermarked where the tool allows |
| Prospective investor, first meeting | Deck, model summary, no data room | The data room follows the term sheet, not the coffee |
| Prospective investor, diligence | Full, time-limited, named individuals | Revoke on close or on pass |
| Board member | Full | - |
| Advisor or CA | As needed, named | Never a shared generic login |

Keep the access log. Who has seen what, when, and who granted it. A leaked
document is traced by the log, and a fund's compliance team will ask.

## What never goes in

- Unredacted customer contracts with pricing that would damage a negotiation.
- Employee salaries and personal documents, beyond the aggregate cost.
- Another investor's terms, side letters or questions.
- Anything with a password, a bank credential or a personal ID number.
- Draft documents that have not been signed, unless labelled as drafts.

## Watermarking and naming

- Name files with a date: `2026-10-management-accounts.pdf`, not `final_v3(2).pdf`.
- Watermark PDFs per recipient when the tool allows it.
- One folder per round in `10 Fundraise`, so the history stays legible.

## The diligence answer sheet

For each of the twenty questions a fund will ask, one line and the document that
answers it. That sheet is what turns a diligence call from an interrogation into a
confirmation.

| # | Question | Our answer | Document |
|---|---|---|---|
| 1 | Revenue by month, recognised | | 03 |
| 2 | Cohort retention | | 03 |
| 3 | Gross margin, fully loaded | | 03 |
| 4 | Top five customers and share | | 05 |
| 5 | Contract terms and termination | | 05 |
| 6 | Statutory dues outstanding | | 04 |
| 7 | Cap table and unallocated pool | | 02 |
| 8 | IP assignments signed | | 06 |
| 9 | Related-party transactions | | 03 |
| 10 | Data privacy position | | 08 |
| 11 | Open litigation | | 09 |
| 12 | Key-person dependency | | 06 |
| 13 | Loan covenants | | 05 |
| 14 | Employee disputes | | 06 |
| 15 | Third-party licences | | 07 |
| 16 | Insurance cover | | 08 |
| 17 | Related entities | | 01 |
| 18 | Use of prior round funds | | 03 |
| 19 | Board composition and approvals | | 01 |
| 20 | The three risks we would flag | | A note |

Question 20 is the one that wins trust. Write it yourself, honestly, before they
ask it.

## Anti-patterns

- **Building the data room when a fund asks.** The documents were always needed; the deadline is the only thing that changed.
- **A generic login shared with three people.** Nobody knows who leaked, and the fund's compliance team will object.
- **A folder of 400 files with no index.** Diligence time is the investor's cost, and they price it.
- **Leaving access open after a pass.** It signals inattention, and it is a live confidentiality risk.
- **Uploading the cap table as a screenshot.** It will be outdated in a month and unreadable in a spreadsheet.
- **No version dates.** Two files called "final" is a diligence finding.
