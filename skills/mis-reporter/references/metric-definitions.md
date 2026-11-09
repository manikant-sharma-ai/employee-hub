# Metric definitions

A metric without a written definition is a different metric every time someone new
calculates it. This sheet is the contract.

## The definition record

For every metric on the page:

| Field | Example |
|---|---|
| Name | Revenue (recognised) |
| Formula | Invoiced and delivered in the period, net of returns and discounts, excluding GST |
| Source | Zoho Books, sales register, as of 23:59 on the period end |
| Owner | Finance lead |
| Period | Calendar month, 1st to last day |
| Inclusion | Domestic and export; excludes inter-branch transfers |
| Exclusions | Advance received but not delivered; cancelled orders |
| Known gap | Marketplace settlements lag 7 days; provisional until the settlement report |
| Threshold | Red below 90% of plan, amber 90-97% |

## The traps, by metric

| Metric | The trap | The rule |
|---|---|---|
| Revenue | Booked vs invoiced vs collected vs recognised | State which one; the page uses recognised, the cash line uses collected |
| GMV | Marketplace GMV is not your revenue | Net revenue = GMV minus returns minus platform fee |
| Gross margin | Excludes or includes freight and packaging | Fixed rule: contribution after all variable cost, before overheads |
| GST | Inclusive figures inflate revenue by 18% | Always exclusive; say so once in the definitions sheet |
| Returns | Booked in the month of the order, or the month of the return | Month of the return, so the margin line tells the truth |
| Headcount | Heads vs FTE vs billable | FTE for cost per head, heads for payroll, billable for utilisation |
| DSO | Average receivables or closing | Closing receivables ÷ revenue × days in period; state it |
| Stock cover | Value or units | Units for cover days, value for working capital; both, labelled |
| CAC | Blended or paid-only | Paid-only for channel decisions, blended for the board |
| Churn | Logo or revenue | Revenue churn for the P&L, logo churn for the sales conversation |
| Pipeline | Created or weighted | Weighted by stage probability, with the weights written down |
| Utilisation | Billable hours over total, or over available | Available hours, excluding leave, stated in the definition |
| Burn | Gross or net | Net: cash out minus cash in, excluding fundraise |

## Reconciliation rules

1. **Revenue reconciles to the books**, every period. A gap over 1% is investigated, not
   explained.
2. **Cash reconciles to the bank statement**, not to a cash-flow model.
3. **Volume reconciles to the ops or billing system.** If the sales sheet and the
   warehouse disagree, the warehouse is the physical truth.
4. **The gap is written down.** "Sales sheet ₹18.4 lakh, books ₹17.1 lakh; ₹1.3 lakh is
   two invoices dated the 1st and booked in the next period." That sentence is worth
   more than the reconciliation.
5. **Provisional is a status, not a guess.** Mark the cell, name the date the final
   figure arrives.

## When a definition changes

| Situation | Do |
|---|---|
| A genuine error was found | Restate prior periods, note it, tell the readers in one line |
| The business changed (new channel, new cost) | Change from the start of a month, keep both series for a quarter |
| A reader wants their own definition | Keep the page's definition; add their variant as a labelled column |
| Two departments use different definitions | One owner decides; the definitions sheet names them |

Never restate silently. A silent restatement is found by an auditor and it discredits
every other number in the file.

## The definitions argument

When two people disagree about a number, the disagreement is almost never arithmetic.
It is one of four things: a different period, a different inclusion, a different source,
or a different moment of recognition. Ask those four questions in that order and the
argument ends in two minutes.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Definition lives in someone's head | Every new joiner produces a different number |
| "Revenue" used for four different things in one meeting | The meeting argues about words, not the business |
| A metric improved by changing its formula | Discovered at diligence; the round gets harder |
| Percentages on a near-zero base | 300% growth on ₹40,000 of revenue |
| One metric, two owners | Neither reconciles it |
