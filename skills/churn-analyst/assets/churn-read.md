# Churn read - <month YYYY>

Prepared by churn-analyst. Account IDs only; no customer names.

## 1. The number

| Metric | This month | Last month | Same month last year | Base this month |
|---|---|---|---|---|
| Logo churn % | | | | customers at start |
| Gross revenue churn % | | | | MRR at start |
| Net revenue churn % | | | | MRR at start |
| Expansion (₹) | | | | |

One line: **<what changed, in one sentence, with the number and the cause if known>.**

## 2. The cohort that moved

| Cohort | M0 | M1 | M2 | M3 | M6 | M12 |
|---|---|---|---|---|---|---|
| <YYYY-MM> | 100% | | | | | |
| <YYYY-MM> | 100% | | | | | |

Read: **<the row or column that moved, and by how much against the previous cohort>.**

## 3. The reasons, counted

| Code | Customers | Share | Revenue lost (₹) | Change vs last month |
|---|---|---|---|---|
| price-value | | | | |
| onboarding-failure | | | | |
| missing-feature | | | | |
| product-quality | | | | |
| cash-flow | | | | |
| switched-competitor | | | | |
| business-change | | | | |
| relationship | | | | |
| no-longer-needed | | | | |
| unknown | | | | |

Coded from: <form / call notes / tickets> - <n> of <n> exits had usable evidence. Unknown is not redistributed.

## 4. The early-warning list

| Score | Accounts | MRR at risk (₹) | With an owner | Oldest contact gap |
|---|---|---|---|---|
| Red | | | | |
| Amber | | | | |

Signals used: <signal 1, threshold, lead time>, <signal 2, threshold, lead time>. Last month's reds that left:
<n of n>.

## 5. The one play this month

- **Play**: <name> against reason code <code>
- **Cost**: ₹<x> per customer × <n> customers = ₹<total>
- **Expected save rate**: <x>% (source: <measured / last test / first run>)
- **Expected value**: ₹<margin protected × save rate − cost>
- **Owner**: <role>
- **How we will know**: <metric, by when>
- **Control group**: <yes / not possible, and why>

## 6. What I could not verify

- <connector not connected> - unlocks <what>
- <n> exits with no usable reason
- <definition caveat, e.g. failed payments dated at retry, not at request>
