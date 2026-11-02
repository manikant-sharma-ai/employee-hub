# CRM hygiene

A pipeline nobody trusts gets ignored, and an ignored pipeline is worse than no pipeline - it produces confident forecasts from invented data.

## Stages, defined so two people log the same thing

| Stage | Definition | Exit test |
|---|---|---|
| 1. Target | On the list, not contacted | Has a named contact and a trigger |
| 2. Contacted | At least one touch sent | A send is logged with a date |
| 3. Replied | A human wrote back, any content | Reply text is stored |
| 4. Qualified | They confirmed the problem and the role in solving it | Pain, budget owner and timeline are known |
| 5. Meeting held | A conversation actually happened | Notes and next step recorded |
| 6. Proposal sent | A price and scope went out | Document attached or linked |
| 7. Won / Lost | Decision made | Reason recorded, in the buyer's words |

Rules:

- **A reply is not a lead.** "Not now" stays at Replied, not Qualified.
- **No stage moves without an artefact** - a send log, a reply, a meeting note, a document.
- **Every open deal has a next step and a date.** A deal with no next step is a Lost with better manners.
- **Stale after 30 days** with no activity = flag, then close at 60 unless the buyer gave a date.

## Required fields, and why each exists

| Field | Rule | What breaks without it |
|---|---|---|
| Company name | One spelling, canonical | Duplicates and double-touching |
| Domain | Corporate domain | Cannot dedupe by account |
| Contact name, role | As on LinkedIn, verified | You address a person who left |
| Email, phone | Verified, with date | Bounces, and DND violations |
| Source | Where the row came from + date | You cannot tell which channel produces |
| Trigger | One line, specific | Personalisation becomes generic |
| Owner | One named person | Two people email the same buyer |
| Last activity, next step | Date + action | The forecast becomes fiction |
| Lost reason | From a fixed list, plus free text | You learn nothing from the losses |

## Data standards for Indian records

- **Phone:** `+91` prefix, 10 digits, no spaces or dashes. Store the number as a string, never as a number - leading zeros disappear.
- **Company name:** strip suffixes for matching (`Pvt Ltd`, `Private Limited`, `LLP`), but keep the legal form in a separate field.
- **GSTIN and CIN:** uppercase, validated format, stored separately. Do not derive anything from a GSTIN's state code without checking it.
- **City and state:** both, because send windows and language choice depend on them.
- **Language:** note whether the buyer replies in English, Hindi or Hinglish, so the next person matches it.

## Cleanup order, when the pipeline is a mess

1. **Dedupe by domain**, then by phone, then by fuzzy name. Keep the record with the most recent activity.
2. **Kill the impossible rows** - no contact name, no email, no company.
3. **Re-stage everything by evidence.** Open a sample of 20 records and check the stage against the last activity.
4. **Close stale deals in bulk**, with reason "no response after 90 days". Do not delete them; you will want the history.
5. **Normalise the lost reasons** into six or seven options, then report on them.
6. **Add the two fields that were missing** - next step and source - and make them mandatory going forward.

## Reporting that survives scrutiny

| Metric | Definition | Common lie |
|---|---|---|
| Touches sent | Emails + calls + messages logged | Counting a sequence as one touch |
| Reply rate | Unique human replies / contacts reached | Counting auto-replies and bounces |
| Positive reply rate | Replies showing interest / contacts reached | Counting "send info" as positive |
| Meeting rate | Meetings held / positive replies | Counting booked-but-cancelled |
| Pipeline value | Sum of qualified deals only | Summing every open row |

## Anti-patterns

- **A stage called "Proposal/Meeting/Interested".** Three meanings, so nobody uses it consistently.
- **Logging the send, not the reply.** The reply is the only event that matters.
- **Personal Gmail as the CRM.** It works until the person who owns it leaves.
- **Storing full email threads with personal data in the notes.** Keep the objection, not the biography.
- **Bulk-importing a purchased list "for visibility".** It corrupts the dedupe base permanently.
- **Reporting pipeline from memory** because the CRM is not connected. Say "not measured".
