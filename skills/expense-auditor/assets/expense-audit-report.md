# Expense audit - <scope> - <period> - <date>

Prepared by: expense-auditor | Requested by: <name> | Data covered: <ledger export / claims sheet>
Materiality threshold: ₹<10,000> | Coverage: <all N rows / a sample of N of M>

## 1. The audit in six lines

| | Value |
|---|---|
| Period in scope | <Apr-Sep 2026> |
| Rows tested | <1,240 vendor payments, 96 claims> |
| Exceptions confirmed | <14> |
| Rupees identified | ₹<4,86,200> |
| Of which recoverable | ₹<2,14,000> |
| Of which avoidable going forward | ₹<2,72,200> |

## 2. Exceptions register

| # | Finding | Amount ₹ | Period | Vendor / claim | Evidence | Clause | Severity | Route | Owner | Due | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Same invoice paid twice | 84,000 | Aug | <vendor> | INV-2291 twice, UTRs side by side | Approval matrix, §4 | High | Credit note | Accounts | 20 Nov | Open |
| 2 | Seats paid 40, used 11 | 1,68,000/yr | FY26 | <tool> | Invoice vs console export | Policy §7 | Medium | Downgrade | Ops | Before renewal | Open |
| 3 | Hotel above city cap | 4,560 | Oct | RE-2025-0412 | Invoice vs cap | Travel §3.2 | Low | Adjusted | Claimant | 7 Nov | Closed |

Severity: High = above ₹50,000 or a control failure that repeats; Medium = ₹10,000-50,000;
Low = below the threshold, fixed in the same cycle.

## 3. The top findings, expanded

### 1. <Finding title> - ₹<amount>

- **What happened.** <Two sentences, factual.>
- **The documents.** <Invoice A and payment B, with references.>
- **The clause.** <The policy or contract line, quoted.>
- **The money.** Recoverable ₹<x>, or avoidable ₹<y> a year.
- **The route.** <Credit note / correction / downgrade / conversation.>

## 4. Vendor spend view

| Vendor | Annual spend | % of total | Rate vs contract | Action |
|---|---|---|---|---|
| | | | | |

Recurring charges: <tool, cost, seats paid vs used, owner, renewal date, overlap.>

## 5. Policy gaps

| Gap | What it allowed | Proposed change | Approver |
|---|---|---|---|
| No GRN step above ₹1 lakh | Goods billed before receipt | A receipt step in the PO flow | Founder |

## 6. Recovery tracker

| Item | Amount ₹ | Claimed on | From | Expected by | Received ₹ | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

## 7. What I could not verify

- <Data not received: bank statement side, approval trail, contracts.>
- <Sample size and how it was selected.>
- <Findings in the "to confirm" list, with the question asked.>
- <The connector that would close each gap.>

## 8. To confirm

| Candidate | Why it is not yet a finding | Question to ask | Owner |
|---|---|---|---|
| | | | |
