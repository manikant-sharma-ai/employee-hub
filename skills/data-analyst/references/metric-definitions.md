# Metric definitions

Two people in the same company can produce three different churn rates. Not because either is wrong, but because neither wrote the definition down. This file is how you end that.

## The definition template

Every metric gets five lines. No exceptions, no "it's obvious".

```
Name:        Monthly active customer
Numerator:   distinct customer_id with >=1 completed, non-cancelled order in the calendar month
Denominator: distinct customer_id with >=1 completed order in the prior 12 months
Window:      calendar month, IST
Excludes:    cancelled orders, returns after 30 days, internal/test accounts, B2B GST orders
```

If any of those five is missing, the metric is not defined yet.

## The metrics that cause the most argument

| Metric | The usual fight | The honest resolution |
|---|---|---|
| **Revenue** | Gross vs net, GST in or out, freight included | State one. Most businesses should report net of GST, net of returns, excluding freight, and say so |
| **Active customer** | 30/60/90 days? One order or one login? | Pick the window that matches the repurchase cycle. For a 6-month cycle, 30 days is meaningless |
| **Churn** | Logo vs revenue vs customer; logo churn of 5% with 40% revenue churn | Report both. They tell different stories and both are true |
| **MRR** | New + expansion - contraction - churn; is a 10-month prepaid deal 1/10 per month? | Write the amortisation rule down |
| **CAC** | Sales salaries in or out? Blended or paid-only? | Total go-to-market cost / new customers, and state whether salaries are included |
| **AOV** | Orders or invoices? Returns netted? | Orders, net of returns, and the window |
| **Margin** | Gross of what? Freight? Payment fee? Returns provision? | Define the cost lines included, and call it contribution margin if freight and fees are in |
| **Lead** | Form fill vs qualified | Use two words: lead and qualified lead. Never one |
| **Conversion** | Of visits, sessions, users or leads? | Name the denominator in the metric name |
| **Retention** | Day-30, month-3, or cohort-based? | Cohort-based, and show the curve |

## Denominators: where numbers go wrong

- **Every rate needs its denominator in the name.** "Churn 8%" is meaningless. "Monthly logo churn, 8% of accounts active at month start" is a fact.
- **Decide the population before the event.** Churn's denominator is who existed at the start, not who was there at the end.
- **Do not average percentages.** Weighted average from the underlying counts, always.
- **Do not sum percentages.** Obvious, and it happens in every deck.

## The metric tree

Before defining anything, draw the tree. It shows which metric is a lever and which is a symptom.

```
Revenue
├── Customers
│   ├── New            <- acquisition spend, channels, conversion
│   ├── Retained       <- product, support, pricing
│   └── Reactivated    <- win-back, offers
└── Revenue per customer
    ├── Frequency      <- assortment, reminders, availability
    └── AOV
        ├── Price      <- pricing, discount depth
        └── Units/order<- bundling, cross-sell
```

Then: **which node does the decision move?** If the answer is "none of them", the decision is not a data decision.

## Time windows and periods

- **Calendar month vs 30-day rolling vs 4-4-5.** Pick one and never mix within a report.
- **Financial year in India is April-March.** FY26 is April 2025 to March 2026. State it in the first line of any report that uses it.
- **A partial month is not a month.** If the data ends on the 24th, say so, or compare like-for-like days.
- **Cut-off time.** A sale at 23:50 IST on the 31st belongs to that month. If the system cuts at UTC, it does not - check.

## Metric hygiene

| Rule | Why |
|---|---|
| One owner per metric | Two owners means two numbers |
| One definition, one place | A definitions file in the repo, dated |
| Version the definition | A change in definition is a break in the series - annotate the chart |
| Report the n alongside the rate | 100% of 3 is not a finding |
| Show the trend, not the point | A single month is noise in most businesses |
| Never change a definition mid-quarter silently | Someone's target depends on it |

## When two numbers disagree

1. **Do not average them.** That is the one thing that is certainly wrong.
2. **Compare definitions first**, line by line. Nine times in ten the difference is one of: GST, returns, a partial period, a different denominator, or a cancelled-order filter.
3. **Reconcile to the source of record** - the accounting system for money, the order system for orders. The source of record wins, and the other number gets an explanation.
4. **Write the resolution into `notes/decisions.md`** with the date, so it is not re-argued next month.

## Anti-patterns

- A metrics dictionary that lives in someone's head.
- Defining the metric after seeing which definition gives the better number. This is the most common form of analytical dishonesty and it is usually unconscious - guard against it by writing the definition first, and dating it.
- Reporting a rate without n.
- Changing the definition to make a target.
- Using "active" to mean anything other than a written, dated rule.
- Copying a SaaS metric definition into a business with a different repurchase cycle.
