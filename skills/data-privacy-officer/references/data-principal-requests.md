# Data principal requests

A request arrives by email, WhatsApp, a phone call or a form, and it has a clock on it. This file is the runbook.

## The request types

| Type | What the person wants | The work |
|---|---|---|
| Access | A summary of the data held, and who it was shared with | Gather from every system in the map, compile, redact third parties |
| Correction | Wrong data fixed | Verify, correct in every system, tell the processors |
| Erasure | Data deleted | Delete from every system, and instruct processors; check statutory retention first |
| Withdrawal of consent | Stop the processing that relied on consent | Stop marketing, stop the purpose, record the date |
| Grievance | A complaint about how data was handled | Acknowledge, investigate, respond, record |
| Nomination | Nominate someone to exercise rights on their behalf | Record the nomination and the verification |
| Any other | A question about the notice | Answer from the notice, or fix the notice |

## The runbook

| Step | Timeframe | What happens | Owner |
|---|---|---|---|
| 1. Log | Same day | Every request gets an ID, a date, a type and a channel | Privacy owner |
| 2. Acknowledge | Within 48 hours | A short reply confirming receipt and the next step | Privacy owner |
| 3. Verify identity | Before any data is disclosed or deleted | Match against known contact details, or a verification step proportional to the sensitivity | Privacy owner |
| 4. Locate | From the map | Every system and every processor holding the data | System owners |
| 5. Decide | Before acting | Any statutory retention, any third-party rights, any legal hold | Privacy owner + lawyer where needed |
| 6. Act | Inside the period the law sets | Delete, correct, compile or stop | System owners |
| 7. Confirm to processors | Same day as the action | Written instruction, and their confirmation | Privacy owner |
| 8. Reply | Inside the period the law sets | What was done, what was kept and why, and the grievance route | Privacy owner |
| 9. Record | Same day | The log entry, the decision, the evidence | Privacy owner |

The legal period and the form of the response are set by the Act and the Rules, and the position is being phased
in - check the current requirement at the time of the request and write down the date you checked.

## Verification, without creating a new risk

| Request | Verification |
|---|---|
| Access from the registered email | Reply to the registered address only, never to a new one |
| Erasure from a phone number | An OTP to the registered number, or a call-back |
| Request from a family member | Only with a documented authority, or the nomination |
| Request from an employer about an employee | Not their data to request; refuse and explain |
| Request that names an order but not the account | One additional matching fact, and a reply to the registered channel |
| Request from a lawyer | Verify the authority, then follow the same process |

Never send personal data to an address the requester supplies "because the old one is closed". That is the exact
route a data theft takes.

## Erasure, done properly

1. **Check the retention obligations first.** Tax, payroll, company law and sector rules require some records be
   kept. Erasing them is a different violation.
2. **Delete, do not hide.** A flag in the CRM that hides a record is not deletion if the record still exists in the
   database, the backup or an export.
3. **Reach the processors.** The courier, the gateway, the marketing tool, the accountant - each needs a written
   instruction.
4. **Handle the free text.** A CRM note with a phone number inside it survives a field-level delete. Notes and
   attachments are the usual failure.
5. **Backups.** State the backup cycle honestly: the record is deleted from live systems immediately, and from
   backups as they rotate, within the stated period.
6. **Anonymise where a record must be kept.** An order record kept for tax can have the personal fields removed and
   the statutory fields kept, if that satisfies the obligation - confirm the position with the CA.
7. **Confirm to the person** what was deleted, what was kept, why, and for how long.

## Access, done properly

- Compile from the map, system by system, and say which systems were searched.
- Redact other people's data - a chat log with a support agent, another customer's name in a review.
- Explain the internal codes and abbreviations; a dump of database rows is not access.
- Include who the data was shared with, in categories at minimum.
- Include the retention period and the basis.

## Grievance

- Acknowledge, investigate, and answer with what happened and what changed.
- Keep the answer factual; do not apologise for a breach that did not occur, and do not deny one that did.
- Tell the person about the next step available to them if they are not satisfied.
- Record it, and count the grievance types - three of the same kind is a process failure.

## The request log

| ID | Date | Type | Channel | Verified | Systems searched | Action | Kept (and why) | Answered on | Days taken |
|---|---|---|---|---|---|---|---|---|---|

The log is the evidence that the business has a process. Without it, every request is the first request.

## Anti-patterns

- A deletion that reaches the CRM but not the helpdesk, the inbox and the WhatsApp thread.
- Replying to a request from a new email address "for convenience".
- Deleting a tax record because someone asked, and discovering the obligation at the next filing.
- Answering an access request with a database export nobody can read.
- No acknowledgement, so the person escalates to a regulator while the team is still looking.
- Treating a request as a support ticket and closing it without an action.
- A process that depends on one person who is on leave.
