# Driver-based budgeting

A budget built from drivers answers "what happens if we sell 20% fewer units" in a
minute. A budget built from last year's totals answers it in a week, and wrongly.

## The build order

1. **Frame** - entity, financial year and start month, currency, scope, approver, date.
2. **Drivers** - the two to six things that actually move revenue, and the three to six
   that actually move cost.
3. **Revenue** - bottom-up per driver, monthly, with seasonality from last year.
4. **Cost by behaviour** - fixed, variable, step. Never a single "expenses" block.
5. **Envelopes** - cost blocks grouped under one named owner.
6. **Cash** - the P&L translated into when money arrives and leaves.
7. **Scenarios** - base, downside, severe, with triggers.

## Choosing revenue drivers

| Business | Usual driver set | Watch out for |
|---|---|---|
| D2C product | sessions x conversion x AOV, repeat rate | returns and RTO as a deduction, not a footnote |
| B2B services | billable people x utilisation x day rate | bench time, and the pipeline lag between sell and start |
| SaaS | new logos, seats per logo, ARPU, churn | annual prepay inflating cash and hiding churn |
| Marketplace | GMV x take rate, active sellers | discount-funded GMV that never repeats |
| Retail store | footfall x conversion x basket | seasonality and the festival calendar |
| Manufacturing | capacity x utilisation x realisation | rejection rate, and power and freight as variable cost |

If the founder cannot name the drivers, build the driver list from the last twelve
months of actuals - which line moved when revenue moved - and confirm it in one
paragraph before going further.

## Cost behaviour, not cost category

- **Fixed** - rent, salaries of existing staff, insurance, subscriptions. Does not move
  with volume inside the year; moves in steps when you add a person or a site.
- **Variable** - raw material, packaging, payment gateway fees, shipping, commissions.
  Moves with units, so it is a rate per unit and must be modelled as one.
- **Step** - the hire in October, the second warehouse at 8,000 orders a month, the
  agency retainer that starts with the ad budget. These break plans, because a straight
  line hides them and the cash arrives before the revenue does.

Rule: any cost above 5% of total spend gets its own driver and its own month shape. A
line that is 0.4% of spend can be a flat monthly number and nobody will be misled.

## Seasonality

Take the last twelve months of revenue by month, divide each by the average month, and
you have an index. Apply the index to the driver-based total. Do not invent a shape from
memory - last year's actual shape, adjusted for a known change (a new store, a lost
account), is the only defensible version.

State the index in the workbook. A founder looking at a flat revenue line in a business
with a 3x festival quarter is looking at a plan that will be "behind" for eight months
and "ahead" for one.

## The assumptions register

One sheet, one row per assumption: the assumption, its value, who believes it, the
evidence, the date, and the sensitivity - what it costs if it is 20% wrong. The
sensitivity column is the point: it tells the founder which three arguments are worth
having.

## Anti-patterns

- **Last year plus a percentage.** Fast, plausible, and blind to every driver change.
- **Annual divided by twelve.** Hides seasonality, hire months and campaign timing.
- **Zero-based theatre.** Rebuilding every line from scratch each year costs a month and
  usually lands where the increment would have, because the drivers did not change.
  Zero-base the new lines and the step costs; increment the stable ones.
- **One revenue line called "sales".** It cannot be variance-analysed later.
- **Growth applied to last year's total** without asking whether the capacity, the
  people or the cash to deliver it exist.
- **The budget owned by finance alone.** A plan the sales head did not agree to is a
  plan the sales head will beat or miss without consequence.
