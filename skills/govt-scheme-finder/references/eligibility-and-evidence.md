# Eligibility and evidence

Every eligibility question is answered twice: against the guideline, and against the
business's own records. Both must agree, and they usually do not.

## The profile sheet

One sheet, every field with a source and a date confirmed. This is the sheet every test
runs against.

| Field | Value | Source | Confirmed on |
|---|---|---|---|
| Entity type | private limited | certificate of incorporation | |
| Registration number | CIN | MCA | |
| Incorporated | date | certificate | |
| Registered state | Maharashtra | certificate | |
| Operating states | Maharashtra, Gujarat | founder | |
| Udyam | registered, micro/small/medium | Udyam certificate | |
| GSTIN | number, active | GST portal | |
| IEC | yes/no | DGFT | |
| DPIIT startup recognition | yes/no, date | Startup India | |
| Sector | NIC code and description | Udyam or GST registration | |
| Turnover, last 3 years | as filed | audited accounts and returns | |
| Headcount | number, on payroll | payroll | |
| Investment planned | components and amounts | capex plan, quotations | |
| Prior scheme sanctions | name, amount, year | sanction letters | |
| Declared categories | only what the founder declares | founder | |

The two fields that cause the most silent ineligibility are **the NIC code** (a business
that thinks it is manufacturing and is registered as trading fails a manufacturing test
without anyone noticing) and **the entity type on the certificate versus the application**.

## The eligibility matrix

One row per scheme. Six columns, and the reason column is not optional.

| Scheme | Authority | What it gives | Status | Reason (clause and field) | Evidence |
|---|---|---|---|---|---|

Status values:

- **Eligible** - every clause satisfied on the profile sheet, with the source.
- **Needs check** - a clause cannot be tested from what is on hand, or the parameter is
  unverified. Name the field and who can confirm it.
- **Not eligible** - a clause fails. Name the clause and the gap. Say what change would
  make it eligible, if one exists.

`scripts/scheme_match.py` runs this mechanically from a rules file, so that a status
always has a reason attached. The rules file is built by hand from the guidelines; the
script does the comparing, not the reading.

## The document pack

For each scheme, four lists:

1. **Exists** - the document is in the folder and current.
2. **Exists but stale** - a certificate expired, an account is unsigned, a return is
   missing.
3. **Missing, producible** - the CA can issue it, the bank can issue it, the portal can
   generate it. Name the person and the lead time.
4. **Missing, not producible** - it does not exist and cannot be created retrospectively.
   This is the list that decides whether to apply at all.

The usual pack, in rough order of frequency: incorporation and PAN, Udyam certificate,
GST registration and returns, audited financial statements for three years, ITR
acknowledgements, project report, machinery quotations, proof of land or premises, bank
sanction letter, term loan agreement, statutory approvals (factory licence, pollution
consent, electricity connection), and a CA certificate on the investment and turnover.

## The evidence file

- **One folder per application**, named for the scheme and the window.
- **Every document named with what it proves** - "audited accounts FY24 - proves turnover
  of X", not "accounts.pdf".
- **A one-page index** at the top, because the person assessing it will not read the
  folder.
- **Read-only once submitted**, with the submission acknowledgement saved.

## Common disqualifiers

| Disqualifier | Why it happens | What to check |
|---|---|---|
| Turnover definition | the scheme uses gross turnover or excludes other income; the accounts show a different figure | the definitions clause, and the CA's computation |
| Investment definition | only plant and machinery counts; land, building, vehicles and software are excluded | the benefit clause |
| Entity mismatch | the application is in the name of a proprietorship while the asset sits in a private limited company | the certificates |
| Registration date | the scheme requires Udyam before the investment, or within a window after commencement | the certificate date against the investment date |
| Sector code | the NIC code does not match the activity the scheme funds | the Udyam and GST registrations |
| Location | a scheme is limited to specified districts, zones or categories of area | the state policy schedule |
| Prior benefit | the same asset already took a benefit under another scheme | the exclusion clause and the founder's own history |
| Litigation or default | a bank default or a pending case disqualifies in several schemes | the lender's own view |

## Anti-patterns

- **Testing eligibility against a rounded turnover** from memory rather than the filed
  figure.
- **A matrix with a status and no reason**, which cannot be defended to the founder or to
  the office.
- **Assuming a document exists** because it should. The stale list is where applications
  die.
- **Building the pack before the eligibility is settled**, which is a week spent on a
  rejection.
- **Recording a personal category the founder did not declare**, which is both wrong and
  a data problem.
