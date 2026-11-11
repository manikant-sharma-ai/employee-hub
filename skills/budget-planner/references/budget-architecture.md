# Budget architecture

The structure decides whether the budget is arguable. Get this wrong and every later number
is decoration.

## Step 1 - fix the base case first

Restate last year's actuals into the heads this plan will use, before projecting anything.

| Move | Why |
|---|---|
| Re-cut the ledger into plan heads | The chart of accounts is built for the accountant, not for decisions |
| Mark every one-off | A spike inherited as a baseline inflates the whole year |
| Split direct cost from overhead | Gross margin must be visible monthly, not annually |
| Reconcile to the bank | If the books and the bank disagree, the base is the bank |
| Note the unrecorded liabilities | A vendor bill not yet entered is a cost the plan must carry |

Twelve months of actuals is the minimum. Eighteen is better: it shows one full cycle and the
seasonality.

## Step 2 - choose the build method, honestly

| Method | Use when | Cost |
|---|---|---|
| **Driver-based** | Anything with a volume you can name: orders, kg, hours, seats, visits | Needs one good volume number and a rate |
| **Incremental** | Stable overhead lines: rent, insurance, compliance | Inherits last year's inefficiency forever |
| **Zero-based** | A line nobody has questioned in two years, or a new function | Slow; use it on 10% of the lines, not all |
| **Committed / contractual** | Leases, loans, AMCs, subscriptions | Not a choice - read the contract |
| **Benchmark** | A line with no internal history | The benchmark's business is not yours |

Most small-business budgets should be 60-70% driver-based, 20% committed, 10% zero-based
review, and near-zero benchmark. Say which method each head uses in the assumptions register.

## Step 3 - the line structure

A workable structure for a trading, manufacturing or services business:

```
REVENUE
  Product / service line A        <- units x price, net of returns and discounts
  Product / service line B
  Other income                    <- interest, scrap, incentives - separate, never blended

DIRECT COST
  Material / COGS
  Direct labour
  Freight outward
  Marketplace or channel fees
  Payment gateway charges
GROSS MARGIN

PEOPLE
  Salaries and wages              <- headcount plan, by role and month
  Statutory contributions         <- PF, ESI, gratuity provision, bonus
  Contract staff and consultants
  Recruitment and training

PREMISES AND UTILITIES
  Rent and common area            <- with the escalation clause dated
  Electricity, water, internet
  Repairs and maintenance

SELLING AND DISTRIBUTION
  Advertising and performance media
  Travel and conveyance
  Packaging and consumables

ADMINISTRATION
  Professional fees (CA, legal, consultant)
  Software and subscriptions
  Insurance
  Compliance and licences
  Bank charges and interest
  Depreciation and amortisation   <- non-cash, keep it out of the cash budget
EBITDA / PBT
```

Rules: revenue is always net of returns, discounts and GST. Direct cost is only what moves
with volume. Depreciation, provisions and interest sit below EBITDA so the operating plan is
readable on its own.

## Step 4 - the summary page

One page, and it is the page the founder actually uses:

| Line | Plan YTD | Actual YTD | Var ₹ | Var % | Cause |
|---|---|---|---|---|---|
| Revenue | | | | | |
| Gross margin % | | | | | |
| People cost | | | | | |
| Selling cost | | | | | |
| Admin cost | | | | | |
| EBITDA | | | | | |
| Cash closing | | | | | |

Everything else is an annexure. If the summary needs a second page, the plan has too many
heads.

## Step 5 - how much detail is enough

A rule that holds: a line earns its own row only if a person can change it and someone would
notice. "Printing and stationery ₹4,000 a month" does not need a row; "Marketplace fees" at
₹3.8 lakh does.

| Symptom | Fix |
|---|---|
| 300 rows, 8 people use it | Collapse to 25 heads, keep the detail in a separate tab |
| One "miscellaneous" line at 12% of cost | Split it; something is hiding there |
| Every line identical to last year | The budget is a copy, not a plan |
| No volume anywhere | Rebuild driver-based; you cannot manage a rupee you cannot move |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Annual total ÷ 12 | The festive quarter looks funded and the lean quarter looks failed |
| GST included in revenue | Every margin in the plan is 5-18% wrong |
| Depreciation inside direct cost | Gross margin is meaningless |
| One "salaries" line, no headcount | The largest cost is the least controllable |
| Budget approved with no assumptions register | Nobody can say why it was wrong |
| Two versions in circulation | Every review argues about which plan is the plan |
| A new outlet costed as a monthly average | The lumpy capex and hiring never get funded |
