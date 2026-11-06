# Data room upkeep

A data room is not a folder of documents. It is the answer to "can this company be
diligenced in a week", and it is read by people who will notice what is missing.

## The folder schema

| # | Folder | What is in it | Refresh |
|---|---|---|---|
| 01 | Corporate | Incorporation, MOA/AOA, board and shareholder resolutions, registers | On change |
| 02 | Cap table | Fully diluted sheet, ESOP pool and grants, instrument-wise holdings | Monthly |
| 03 | Financials | Audited accounts, management accounts, monthly MIS, bank statements | Monthly |
| 04 | Tax and statutory | Returns, notices, GST registration, TDS, PF/ESI | Quarterly |
| 05 | Contracts | Customer agreements, vendor agreements, leases, loans | On change |
| 06 | IP | Trade marks, assignments, open-source register | On change |
| 07 | People | Org chart, key employment agreements, ESOP plan, policies | Quarterly |
| 08 | Product and tech | Architecture, security posture, uptime, data processing | Quarterly |
| 09 | Metrics | The workbook the update is generated from, with definitions | Monthly |
| 10 | Fundraise | Deck, model, previous round documents | On raise |
| 11 | Legal | Litigation register, material notices | On change |
| 12 | Compliance | DPDP, POSH, labour, sector licences | Quarterly |

Numbered folders, so a request can be answered with "see 03/2026-10 MIS" rather
than a search through Drive.

## The index

One sheet, every document, with five columns:

| Document | Folder | Version | Date | Owner |
|---|---|---|---|---|
| Audited accounts FY25 | 03 | v1 | 2026-09-28 | CA |

An index that is out of date is worse than none, because it promises a document
that is not there. The owner column is a person, not a team.

## Access

| Rule | Why |
|---|---|
| Named users, never a public link | A leaked link is a leaked company |
| View-only by default; download only on request | Diligence needs reading, not archiving |
| Expiry on every grant, 30-60 days | Access ends when the conversation does |
| A log of who has access and when it was granted | Answers "who has seen this" in one look |
| Separate rooms per party | Two investors must not see each other's questions |
| Revoke on request, same day | The last courtesy of a failed process |

Under the DPDP Act, personal data in the room - employee contracts, customer
records - needs a lawful basis and minimisation. Where possible, redact and provide
a summary.

## What never goes in

- **Unmasked bank details, PAN, Aadhaar or payroll files.**
- **Customer contracts with personal data, unredacted.**
- **Employee salary sheets.** A banded summary answers the question.
- **Board minutes discussing an individual.**
- **Anything from a third party under NDA** that forbids onward sharing.
- **Drafts of documents that were never signed**, unless labelled as drafts.
- **A competitor's information** received under a partnership and not licensed for this.

## The pre-diligence sweep

Before any raise, bridge or serious investor conversation, 90 minutes:

1. Every folder has a current document, or a note saying why not.
2. The cap table reconciles to the registers and the ESOP grants.
3. The MIS ties to the bank statements for the last three months.
4. Statutory filings are complete, and any notice is listed with its status.
5. The litigation register exists, even if it says "none".
6. Access is granted to nobody by default.

## The request log

| Date | Party | Document asked for | Provided | Date provided | Notes |
|---|---|---|---|---|---|

A diligence request answered in 24 hours changes the tone of the whole process. A
request that takes a week invites the question of what else is slow.

## Anti-patterns

- **A Drive folder called "Investor stuff".** It signals that nobody owns it.
- **The same document in three versions with no dates.** Diligence stops until someone decides which is real.
- **Granting access to the whole room on day one.** Least privilege, then widen.
- **A data room built in the week of the term sheet.** It is a month of work compressed into a week of errors.
- **No litigation register.** "None" is a finding; a missing file is a question.
- **Storing the room in a personal Drive account.** Ownership must sit with the company.
