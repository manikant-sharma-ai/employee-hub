# Findings, severity and recovery

An audit is judged by whether the findings get acted on. That depends almost entirely on
how they are written.

## The finding format

One block per finding, seven fields, no prose:

```
Finding:        Duplicate claim - vendor and amount match across two claims
Evidence:       Claim 4471 (2026-09-14, Amazon, 4,999) and claim 4462 (2026-09-11,
                Amazon, 4,999). Both approved by the same approver, both reimbursed.
Rule:           Expense policy 4.2 - a duplicate claim is recoverable in full
Amount at risk: 4,999
Recoverable:    4,999
Owner:          <finance lead>
Action:         Recover in the October payroll cycle; block the vendor-person pair in
                the tool for 30 days
Due:            2026-10-31
```

Anything longer than that is a report. Anything shorter than that is an opinion.

## Severity

| Severity | Test | Who sees it |
|---|---|---|
| Critical | fraud indicator, ghost vendor, altered document | founder only, separate note |
| High | duplicate, split invoice, recoverable amount above the materiality line | owner plus founder |
| Medium | cap breach, missing receipt, price drift | owner, batched |
| Low | pattern, heuristic, policy gap with no money attached | in the appendix |

Severity is amount x recurrence x intent. A ₹900 duplicate repeated 40 times a year is a
high finding; a one-off ₹4,000 cap breach by a first-time claimant is medium at most.

## Amount at risk versus recoverable

- **At risk** - everything the test flagged, including the money you cannot get back.
- **Recoverable** - only what a policy, a contract or a person's agreement supports.
- **Recovered** - only what has actually come back, with a date.

Report all three, in that order, and never let the third be assumed from the second. The
gap between at-risk and recoverable is itself a finding: it is the cost of not having had
a testable policy.

## The conversation

- **Batch by owner.** One mail per owner with their lines, not one per finding.
- **Ask a question, not for a confession.** "Was this one purchase split across two
  claims?" gets an answer. "You split this invoice" gets a defence.
- **Give the fix, not just the fault.** "From next month this category needs a receipt
  above ₹500" is actionable; "ensure compliance" is not.
- **Set a date and put it in the register.** An open finding with no date becomes the
  finding you report again next quarter.

## Escalation

Escalate beyond the owner when: the amount is above the founder's threshold, the same
finding is open for two cycles, the finding involves the owner themselves, or the pattern
suggests intent. In the last case: stop the audit, secure the evidence, hand it to the
founder and the statutory auditor, and write nothing else about it.

## The evidence pack

For the statutory auditor or a diligence request, in this order:

1. Scope, period, materiality threshold, and the data source with its row count.
2. The tests run and the result of each.
3. Findings, in the fixed format, with the evidence attached.
4. The open findings from the previous period and their status.
5. Policy gaps and the fixes proposed.
6. What the tests cannot see.

Keep it read-only once issued, dated, and versioned. An evidence pack that changes after
issue is worse than none.

## Anti-patterns

- **"Irregularities observed"** - a phrase that has never recovered a rupee.
- **A finding with no owner**, which is a finding nobody has.
- **Recovery reported as achieved before the money lands.**
- **The same finding re-reported for three quarters** instead of being escalated.
- **A person's name in the headline** when the finding is a transaction.
