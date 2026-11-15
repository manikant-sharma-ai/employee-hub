# The data map

Every privacy answer depends on this document. It is built from the systems, not from the policy.

## The record of processing, one row per purpose

| Field | What goes in it | Example |
|---|---|---|
| ID | A stable reference | `C-01` |
| Data category | Customer / employee / vendor contact / applicant / child | Customer |
| Purpose | The specific thing it is used for | Delivering an order |
| Fields | The actual fields, not "customer info" | Name, phone, address, order history |
| System | Where it lives | Shopify, Zoho Books, the delivery partner |
| Basis | Consent, or the specific legitimate use relied on | Consent at checkout |
| Retention | The period and the reason | 8 years - tax record |
| Access | Which roles can see it | Ops, accounts |
| Processors | Vendors who see it | Payment gateway, courier, accountant |
| Location | Where stored, and whether it leaves India | Cloud region; check the vendor |
| Notes | Known gaps | No consent captured before 2024 |

## Finding the data - where it hides

| Place | Usually forgotten | Why it matters |
|---|---|---|
| The CRM | Free-text notes with phone numbers and addresses | Cannot be deleted by a field-level erase |
| The helpdesk | Attachments - screenshots with card details, prescriptions, ID copies | The most sensitive data in the business |
| Email inboxes | Order confirmations, ID proofs sent by customers | Never covered by a system-level deletion |
| WhatsApp Business | Addresses, photos, payment screenshots | Not exportable in most small businesses; a real gap |
| Shared drives | Old spreadsheets, exports, "backup final v3" | The commonest source of a leak |
| The website's analytics | IP addresses, device identifiers, session recordings | Session replay can capture form fields |
| The payment gateway | Card and UPI data | Held by the gateway, not you - say so |
| Payroll and HR | Aadhaar, PAN, bank details, health and leave records | High sensitivity, statutory retention |
| Recruiting | Resumes, interview notes, offer letters of people not hired | Kept forever with no purpose |
| Physical | Registers, visitor books, delivery challans, KYC photocopies | Still personal data |

## The three buckets, and what to do with each

| Bucket | Test | Action |
|---|---|---|
| Needed and used | There is a live purpose and a basis | Map it, retain it, protect it |
| Held with no purpose | Nobody can name why it is kept | Delete it, and stop the collection |
| Held for a legal reason | A statute requires the record | Keep for that period, restrict access, delete at the end |

The third bucket is where founders get into trouble in both directions: deleting records that tax or company law
requires, and keeping records for a decade after the requirement ended. Both are answered by writing the statute
next to the period.

## The map's own discipline

- **Reviewed quarterly**, and whenever a new tool is bought. A new SaaS signup is a new data processor, and it
  happens without anyone telling the privacy owner.
- **Verified, not assumed.** "The CRM holds customer data" is an assumption; "the CRM contact record has 14 fields,
  three of which are free text" is a map.
- **Counts, not records.** The map records fields and volumes, never a sample record. Copying real data into the
  map is the mistake that creates the leak the map was meant to prevent.
- **Named owner per system.** A system with no named owner is a system nobody will delete from.

## What a first map looks like in one hour

1. List every tool on the credit card statement and the bank statement - this finds the subscriptions nobody
   mentioned.
2. For each, open the settings or a sample export header and write the field names.
3. Ask one question per field: why do we have this? If nobody knows, mark it `no purpose`.
4. Write the retention as it is today, even if it is "forever". The honest baseline is what makes the fix visible.
5. Mark every field that is free text - those are where the unmapped data lives.

## Anti-patterns

- A data map built from the privacy policy, which describes an aspiration rather than the systems.
- Listing systems but not the free-text fields inside them.
- Treating the cloud vendor's compliance as the business's compliance. The vendor's certification is not the
  fiduciary's obligation.
- A map with no retention column, so every field is kept forever by default.
- A map that only covers customers, while payroll and recruiting hold the most sensitive data in the business.
- A map nobody updates, which becomes wrong within one quarter and dangerous within two.
