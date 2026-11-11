# Revenue and the driver build

A revenue number is not a plan. Units, price, mix and capacity are.

## The identity

```
Revenue = SUM over products ( units x net price )
units   = addressable demand x win rate x repeat rate
capacity = the binding constraint (machines, hours, stock, cash, people)
```

Write the identity for the business in front of you, then fill each term with a source.
If a term has no source, it is an assumption - and it goes in the register with a name.

## Where each driver comes from

| Driver | Best source | Fallback |
|---|---|---|
| Units sold | Last year's actuals by month and SKU | Order data from the marketplace |
| Price | Current price list, net of trade discount | Invoice average realisation |
| Mix | Share of revenue by product or channel | The last three months' skew |
| Win rate | CRM: won ÷ qualified | Quotations sent vs POs received |
| Repeat rate | Customers with 2+ orders ÷ customers | Order history in the sheet |
| Capacity | Machine hours, sq ft, headcount, stock | Ask the person who runs the floor |
| Seasonality | Two years of monthly actuals | Category norm, labelled as such |

## Seasonality, written down

Do not assume flat. Build a monthly index from actuals:

| Month | Last year ₹L | This year ₹L | Index |
|---|---|---|---|
| Apr | 18 | 22 | 1.00 |
| May | 24 | 29 | 1.32 |
| Jun | 14 | 17 | 0.77 |
| ... | | | |
| Sep-Oct (festive) | 41 | 52 | 2.36 |

Index = month ÷ average month. Apply the index to the annual driver build, then check that the
indexed year still adds up. If the business is growing, index the *shape* and grow the
*level* - never multiply a growth rate into a festive month and call it seasonality.

## Ramp curves for anything new

A new outlet, product, channel or geography does not deliver its run rate in month one.

| Month after launch | Typical share of steady-state | Why |
|---|---|---|
| 1 | 20-30% | Stock, listing, first customers |
| 2 | 45-60% | Repeat and referral start |
| 3 | 70-80% | Awareness |
| 4-6 | 90-100% | Full run rate |

Write the curve you used and why. A new store planned at 100% from month one is the single
most common way a plan overstates the year.

## Capacity is the check on ambition

| Constraint | Test |
|---|---|
| Production | Units planned ÷ (shift hours × efficiency) ≤ available hours |
| Stock | Units planned ÷ turns ≤ storage and working capital |
| People | Orders planned ÷ orders per person ≤ headcount in the plan |
| Cash | Growth × working-capital days ≤ the limit |
| Channel | Listing count, account health, ad budget |

If the plan breaks a constraint, one of two things must be in the plan: the investment that
removes it, with a date, or a lower revenue number. A revenue target that breaks capacity with
no capex behind it is a wish.

## Mix moves margin more than volume

| Scenario | Units | Price | Mix | Revenue | Gross margin |
|---|---|---|---|---|---|
| Base | 10,000 | ₹500 | 40% premium | ₹50.0L | 38% |
| Volume push | 11,500 | ₹480 | 30% premium | ₹55.2L | 34% |
| Mix push | 10,000 | ₹520 | 50% premium | ₹52.0L | 42% |

Same revenue story, three different businesses. Always show the mix assumption explicitly,
because a discount-led plan and a mix-led plan have different cash needs and different
operations.

## Discounts, returns and channel fees

Plan revenue **net**. Each of these is a real deduction, and each is forgotten:

| Deduction | Typical size | Where it hides |
|---|---|---|
| Trade or volume discount | 2-15% of list | In the invoice, not in the price list |
| Returns and RTO | 3-25% depending on channel | A cost line, or nowhere |
| Marketplace commission | 5-25% by category | "Other expenses" |
| Payment gateway | 1.5-3% | Bank charges |
| Coupons and offers | 2-10% | A marketing line, understated |

Model each as a percentage of gross sales, then show gross-to-net in one bridge row. A budget
that plans gross sales as revenue is overstating by the sum of these.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| "20% growth" with no driver | Nobody can act on it, and nobody can explain the miss |
| Revenue ÷ 12 | Seasonal months starve and lean months look like failures |
| New line at full run rate | Overstates the year by the ramp, usually 10-20% |
| Gross sales as revenue | Margin and cash both overstated |
| Capacity never checked | The plan is unachievable and everyone knows it by June |
| One blended price | A mix shift toward the cheap SKU is invisible until margin collapses |
| No downside case | The first bad month becomes a crisis instead of a scenario |
