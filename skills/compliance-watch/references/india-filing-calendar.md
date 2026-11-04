# The India filing calendar, as a working model

Dates here are the commonly published statutory dates for recurring obligations.
They move with notifications, extensions and amnesties, and state-level items vary
by state. Check every date at source before it goes into a client calendar - this
page is the shape of the year, not the authority for it.

## Monthly

| Obligation | Due | Note |
|---|---|---|
| TDS and TCS deposit | 7th of the following month | April to February; March has its own rule, verify |
| PF contribution | 15th of the following month | ECR generation precedes the payment |
| ESI contribution | 15th of the following month | |
| GSTR-1, monthly filer | 11th of the following month | Invoice-wise outward supplies |
| GSTR-3B, monthly filer | 20th of the following month | Summary return and payment |
| Professional tax | State-specific, often monthly | Maharashtra and Karnataka differ; check the state |
| GST for QRMP filers | Quarterly return with monthly payment | Invoice furnishing and payment have separate dates - verify both |

## Quarterly

| Obligation | Due | Note |
|---|---|---|
| TDS statement 24Q (salary) | 31st of the month after the quarter ends | Q4 has a different date, verify |
| TDS statement 26Q (non-salary) | 31st of the month after the quarter ends | |
| Advance tax instalments | 15 June, 15 September, 15 December, 15 March | Cumulative percentages of the year's liability |
| Board meeting (private limited) | At least once a quarter under the applicable rules | Gap between meetings is capped |
| POSH internal committee review | Quarterly, as good practice | The annual report is the inspectable artefact |

## Annual

| Obligation | Due | Note |
|---|---|---|
| GSTR-9 annual return | 31 December of the following financial year, as notified | Applicability by turnover |
| Income tax return, non-audit | 31 July | Extensions are common; verify |
| Income tax return, audit case | 31 October | Follows the audit report date |
| Tax audit report | 30 September | Where the audit applies |
| ROC AOC-4 (financial statements) | 30 days from the AGM | Private limited and LLP variants differ |
| ROC MGT-7 or LLP Form 11 | 60 days from the AGM | |
| DIR-3 KYC | 30 September | Per director with a DIN |
| FSSAI annual return | 31 May, for the previous financial year | Category-specific |
| Shops and Establishments renewal | State-specific | Often annual or multi-year |
| POSH annual report | To the district officer, as prescribed | Composition and training evidence too |

## Event-based, which no calendar catches

| Event | Obligation |
|---|---|
| New employee in a new state | Professional tax and shops registration may trigger in that state |
| Turnover crossing a threshold | E-invoicing, GST scheme change, audit, CSR, internal committee |
| New warehouse or branch | GST registration in that state, and often a licence |
| Director change, capital change, charge | ROC filing within the prescribed days |
| Notice or demand | The reply deadline on the notice itself, which is never the statutory calendar |
| Contract with a foreign party | FEMA reporting, withholding, and possibly a permanent-establishment question |

## How to use this page

1. Confirm the entity profile - monthly or QRMP, states, sector.
2. Generate the dates with `scripts/filing_calendar.py`.
3. Open the source for each obligation once, note the date and the URL, and put
   that date in the calendar.
4. Put the obligation in the register with an owner and the evidence location.
5. Re-verify quarterly, and immediately after any budget or council announcement.

## Anti-patterns

- **A calendar built once and trusted for three years.** Two or three dates move every year.
- **National dates applied to state obligations.** Professional tax and shops registration are the commonest error.
- **The March crunch.** Half the annual obligations cluster in September to December; a calendar that starts in January is already late.
- **No reminder before the reminder.** T-3 is too late for anything requiring the CA, a signature or a payment approval.
- **The date without the source.** When it is challenged, the source is the answer.
