# GST and statutory readiness

You prepare working papers. The CA decides positions and files returns. Nothing here is tax advice, and every ambiguous case is presented as options with the amount at stake.

## The monthly GST cycle

| Document | What it is | Who does what |
|---|---|---|
| GSTR-1 | Outward supplies - sales | You assemble from the invoice register; CA files |
| GSTR-3B | Summary return and tax payment | You prepare the summary; CA computes and files |
| GSTR-2B | Auto-drafted inward supplies | You reconcile purchases against it; CA reviews |
| ITC register | Input tax credit claimed | You maintain the register with 2B match status |
| E-invoice (IRN) | Mandatory above the notified turnover threshold | Generated in the accounting system or portal |
| E-way bill | Movement of goods above the notified value | Generated at dispatch, per consignment |

Thresholds and due dates change with notifications. State the threshold you are assuming, and tell the person to confirm the current one before a filing. Do not present a remembered threshold as current fact.

## The 2B reconciliation

This is where money is lost. For every purchase:

| Case | Treatment | Action |
|---|---|---|
| Bill in books, in 2B, values match | Claim ITC | Nothing |
| Bill in books, in 2B, values differ | Claim the lower, or query | Ask the vendor; do not claim the higher |
| Bill in books, not in 2B | Do not claim yet | Vendor has not filed; follow up and hold |
| In 2B, not in books | Missing bill | Find the bill before claiming; an unmatched credit is a future demand |
| In 2B from a vendor you do not recognise | Risk | Investigate; fraudulent credits are the taxpayer's liability |
| Bill for a blocked credit (e.g. certain categories) | Not claimable | Track separately, with the reason |

The general rule for the working paper: **claim only what is both in the books and in 2B, and list the rest with the reason.**

## TDS working

| Item | Detail |
|---|---|
| Sections used | 194C (contractors), 194J (professional), 194I (rent), 194H (commission), 192 (salary) - per the actual payments |
| Rate and threshold | Confirm the current rate and threshold per section; they change |
| Lower-deduction certificate | If a vendor has one, record the number and the rate |
| Challan and due date | TDS deposited by the 7th of the following month (except March) |
| Quarterly return | 24Q (salary), 26Q (others), with the certificate due to the vendor |
| Record | Section-wise ledger with vendor PAN, amount, rate, deducted, deposited, return quarter |

A payment to a vendor without a PAN, above the threshold, attracts the higher rate. Flag those rows explicitly - they are the ones that cost money later.

## The filing calendar, as a shape not a promise

| Due | What | Frequency |
|---|---|---|
| 7th | TDS deposit for the previous month | Monthly |
| 11th | GSTR-1 | Monthly (or quarterly under QRMP) |
| 13th | IFF for QRMP filers | Monthly |
| 20th | GSTR-3B and tax payment | Monthly |
| 25th | PMT-06 for QRMP | Monthly |
| 15th of the month after the quarter | PF and ESI | Monthly (15th) |
| 31 July / 31 Oct / 31 Jan / 31 May | Advance tax instalments | Quarterly |
| 30 September | ITR for most non-audit cases | Annual |
| 31 October | Tax audit report, where applicable | Annual |
| 31 December | GSTR-9 / 9C | Annual |

Dates move. Put the business's actual dates in `notes/decisions.md` after the CA confirms them, and remind rather than assert.

## Evidence to keep, per month

- Sales invoice register, with the GST summary and the GSTR-1 export.
- Purchase register with the 2B match status column.
- Bank statements and gateway settlement reports.
- TDS workings, challans, and the return acknowledgement.
- Payroll summary, PF and ESI challans.
- Stock statement, if the business holds inventory.
- A signed copy of the close pack.

## Anti-patterns

- **Presenting a tax position as settled.** Say "the CA decides" and give the two readings with the amount at stake.
- **Claiming ITC on a bill not in 2B.** It comes back as a demand with interest, months later.
- **Ignoring a small mismatch.** Small mismatches are how a large one hides.
- **Filing late and paying the fee quietly.** Late filing costs interest and blocks future credits; report the pattern to the owner.
- **Using last year's threshold or due date.** Confirm the current notification.
- **Keeping the working papers only in an email thread.** They belong in a folder, dated, per month.
