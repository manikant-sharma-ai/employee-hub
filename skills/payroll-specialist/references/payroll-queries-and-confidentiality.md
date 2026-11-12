# Payroll queries and confidentiality

Half of payroll work is answering "why is my salary less this month" in a way that ends the question
rather than the relationship.

## The query, answered in four lines

1. **The number**: gross this month, gross last month, and the difference.
2. **The cause**, named by component: two days of unpaid leave, a professional tax instalment, the
   March TDS catch-up, a loan instalment that started.
3. **The rule**, in one sentence a non-accountant can check.
4. **What happens next**: the correction date, or the reason there is none.

Never answer a pay query with "as per policy" or "system generated". Both are true and neither is an
answer.

## The recurring queries and the honest answer

| Query | The real cause, usually | The fix that prevents it |
|---|---|---|
| "My salary is less this month" | Unpaid leave, TDS catch-up, a new deduction, a revision applied late | A pre-run note when net moves more than the threshold |
| "My PF is deducted but not showing" | Challan paid late, or the UAN not linked to the establishment | Monthly challan discipline and UAN verification at joining |
| "Why is my TDS so high" | Projection before declarations, or a regime change | Collect declarations in April, recalculate in January |
| "I did not get my payslip" | Distribution list, or a bounced email | Issue payslips on a fixed date with a fallback channel |
| "My friend with the same CTC takes home more" | Structure differs, not CTC | Explain the structure at offer, in writing |
| "My full and final is short" | A recovery the employee did not know about | Show the computation before the last day |

## Confidentiality, operationally

- Salary data lives in the register and the payslip system. Not in a shared drive folder, not in a
  group email, not in a chat thread, not in `notes/`.
- Payslips go to the person, one at a time. Never a single PDF with everyone's page.
- Any file that leaves the business for the CA carries only the rows it needs.
- A manager asking for a team member's salary gets "the person can share it", not the number.
- An employee asking about another employee's salary gets the same answer, warmly.
- The repo is public. Nothing in `notes/` names a person's pay, a bank account or an ID number.

## When salary will be late

Say it before the date, not after: the date it will be paid, the reason in one line, and what is being
done. Silence on payday is the single fastest way to lose a team's trust, and it costs more than the
delay. If the delay is more than a few days, the founder says it, not payroll.

## Anti-patterns

- **The screenshot reply.** Pasting the register row into a chat exposes the structure of the whole
  sheet.
- **Explaining TDS with a section number** and no rupee figure.
- **Promising a correction date you cannot hold.**
- **A shared payroll mailbox** with no named owner, so queries go unanswered for a week.
- **Burying a deduction in "other".** Name it or do not deduct it.
- **Discussing one person's pay in a leadership group.** It travels, and the damage is permanent.

## The reply that closes a query

Four lines, in this order, in plain language:

```
Your gross this month is ₹42,000, the same as last month. The ₹2,400 difference in net is
professional tax of ₹200 for the half-yearly instalment, and TDS of ₹2,200 because the
January recalculation moved your projected annual income into the next slab.
Both are recoverable against your actual tax liability when you file. Payslip attached.
```

Then: name the component, give the rule, give the number, say what happens next. If the answer is
"this is an error", say so before the employee has to argue for it - a correction offered is worth more
than a correction conceded.
