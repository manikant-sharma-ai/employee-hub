# Retention, archives and vendors

Keeping data forever is the default, and it is the exposure. This file sets the periods and the contracts.

## Retention, by category

| Category | Typical period | Reason | What happens at the end |
|---|---|---|---|
| Order and invoice records | As the tax law requires | GST and income tax | Archive the statutory fields; delete the rest |
| Payment records | Per the gateway's and tax rules | Financial audit | Delete from the business's own systems |
| Marketing consent records | The life of the consent plus the period to prove it | Proving consent | Delete with the contact |
| Support tickets | A defined period, e.g. 24 months | Service history | Delete; keep the counts and themes |
| Call recordings | A defined period, e.g. 90 days | Dispute resolution | Delete |
| CCTV footage | A short period, e.g. 30-60 days | Security | Overwrite |
| Employee payroll records | Per payroll and tax law | Statutory | Keep statutory fields; delete the rest |
| Identity documents of employees | The minimum, restricted access | Statutory verification | Return or destroy at exit |
| Job applicant data | A defined period, e.g. 6-12 months | Future roles, with consent | Delete |
| Website analytics | A defined period, or aggregate only | Measurement | Delete or anonymise |
| Children's data | The shortest defensible period | Service delivery | Delete |
| CCTV, visitor books, delivery challans | A short defined period | Security and proof of delivery | Destroy |

The exact statutory periods for tax, payroll and company records are set by those laws, not by privacy law. Confirm
each one with the CA and write the statute next to the period.

## Retention that survives an audit

- **One rule per category**, written, dated and approved by the founder.
- **An automated or calendared deletion**, not an intention. A retention rule with no deletion job is a document.
- **Backups covered**: state the rotation period, because "deleted" has to mean deleted everywhere.
- **Legal hold**: when a dispute, an investigation or a regulator's request is live, deletion pauses for the
  affected records, and the pause is recorded with a reason and an end date.
- **Anonymisation as an alternative** where a record must be kept for statistics or for tax: strip the identifiers,
  keep the transaction.
- **A quarterly check**: sample five categories, confirm the deletions happened, record the result.

## Vendors: who is a processor and who is not

| Vendor type | Relationship | What the contract needs |
|---|---|---|
| CRM, helpdesk, marketing tool | Processor - acts on your instructions | Purpose limitation, security, sub-processors, deletion on exit, breach notice |
| Cloud hosting | Processor, often a sub-processor of the above | Region, access controls, certification evidence |
| Payment gateway | Processor, with its own regulatory obligations | Data minimisation, no card data in your systems |
| Delivery partners | Processor for the address and phone | Purpose limit, retention, no reuse for their marketing |
| Accountant or payroll provider | Processor, handling sensitive data | Confidentiality, access limits, deletion on exit |
| A marketplace | Often an independent controller for its own purposes | Read their terms; you cannot contract around them |
| Analytics and advertising tools | Processor, or independent controller depending on the tool | Consent basis, IP handling, no cross-site profiling without consent |
| A consultant with a laptop of exports | Processor, and the riskiest | Written confidentiality, deletion on exit, no local copies |

## The clause, in short

Every processor agreement should cover, at minimum:

1. **Purpose** - process only on documented instructions, for the stated purpose.
2. **Confidentiality** - named people, bound, and access limited to those who need it.
3. **Security** - reasonable safeguards, and a description of them.
4. **Sub-processors** - named or categorised, with notice before a new one is added.
5. **Assistance** - help with requests from data principals, and with breach obligations.
6. **Deletion or return** - at the end of the engagement, and on instruction.
7. **Breach notice** - without undue delay, with the facts needed to notify.
8. **Audit** - a right to evidence, proportionate to the risk.
9. **Location** - where the data is stored and processed, and any transfer outside India.
10. **Liability** - whatever the commercial negotiation produces, but present.

## Cross-border transfers

- The default position is that transfers are permitted subject to the conditions in the law and any restrictions
  notified by the government. The government may specify countries to which transfers are restricted, so the
  position is a moving one - check it when a new vendor stores data abroad.
- The practical questions are: which country, which vendor, which sub-processors, and can the data be brought back.
- A vendor whose only region is outside India is a decision, not an accident. Write it down, with the reason.
- Where the business is a Significant Data Fiduciary, additional restrictions and obligations may apply - confirm
  whether that applies before assuming it does not.

## Anti-patterns

- "We keep everything for 7 years" as a policy, applied to marketing lists and support chats.
- A retention rule with no deletion, so the data is retained by inertia.
- A vendor contract with no data clause because "they are a big company, they must be fine".
- Card data or Aadhaar copies sitting in a support ticket attachment.
- A sub-processor list nobody has read since the vendor changed it.
- Assuming the cloud region is in India because the invoice is in rupees.
- Deleting records under a legal hold because a request arrived.
