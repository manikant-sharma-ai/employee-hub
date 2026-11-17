# Time to value and the drop-off read

Onboarding fails at a step, not in general. This file turns "onboarding is bad" into a step, a count and a rupee
figure.

## The funnel

| Step | Count | % of paid | Median day | Owner |
|---|---|---|---|---|
| Paid | 100 | 100% | 0 | billing |
| Account opened | 94 | 94% | 0 | product |
| Setup complete | 71 | 71% | 3 | customer |
| First real object | 52 | 52% | 8 | customer + onboarding |
| Second user | 33 | 33% | 17 | account owner |
| Milestone (activated) | 41 | 41% | 14 | — |
| Still active at day 90 | 34 | 34% | — | customer-success |

Two things to notice. Activation is 41% while setup completion is 71% - the leak is between setup and first real
object, not at signup, which is where everyone looks. And the second-user step sits *after* activation, so the
handover has to carry it.

## Time to value, reported properly

| Statistic | Why it is reported |
|---|---|
| Median days to milestone | The typical customer's experience |
| p90 days | The tail - where churn actually accumulates |
| Share activated within the target window | The only figure the journey is judged on |
| Median days for the *unactivated* | How long the business takes to give up |

The mean is not reported. One enterprise account that took 140 days distorts it and hides the tail that matters.

## Cutting the funnel

Cut by **signup week** to see whether a change landed (a journey edit shows as a step change in the weeks after
it). Cut by **plan** to see whether a tier needs a different path. Cut by **channel** to see whether referral
customers activate faster and whether paid-acquisition customers need more. Cut by **whether they had a kickoff
call**, which is the single most informative cut in most businesses and the one nobody runs.

Never cut by anything personal - name, language, region, gender. Plan, channel, size and industry are business
attributes; the rest is profiling.

## Converting the drop into rupees

```
customers stalled at step n   × contract value   × (activation→renewal lift)
```

If 19 customers a month stall between setup and first object, at ₹6,000 a month with an annual retention
difference of 30 points between activated and not, the step is worth roughly ₹41,000 of monthly recurring revenue
a year. That number is what gets the fix prioritised; a percentage does not.

## Instrumenting when there is no data team

1. **Name ten events, no more** - paid, account opened, setup complete, first object, fifth object, second user,
   milestone, support ticket, silent 14 days, cancelled. A small business can instrument ten.
2. **Get the definitions in writing** from whoever owns the product, and date them. Event definitions drift, and a
   drifted definition reads as a result.
3. **Build the funnel in a spreadsheet first.** One row per account, one column per event date, computed
   counts above. It is slower and it is trusted, and it settles the arguments a dashboard starts.
4. **Reconcile to billing monthly.** The number of paid accounts in the funnel must equal the number of payments
   in the ledger, or the base is wrong and every rate above it is wrong.

## Anti-patterns

- A funnel that starts at "visited the website", mixing marketing with onboarding and hiding the paid cohort.
- Reporting activation as a share of signups when the journey starts at payment - two different denominators.
- Deleting the drop-off step because it is the product's fault. Report it, route it to `product-manager`, keep it
  in the funnel.
- A dashboard built before the milestone is agreed, which is a very expensive way to measure the wrong thing.
