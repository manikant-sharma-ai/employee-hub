# Field data and coverage analytics

Six numbers explain a field team. This file is how to compute them, what they look like when healthy, and what to
do when they are not.

## The six numbers

| Metric | Formula | Healthy shape |
|---|---|---|
| Coverage | Outlets billed this month ÷ outlets in the beat universe | 85-95% of the planned beat |
| Productive calls per day | Visits with an order ÷ rep-days worked | 8-14 depending on density |
| Strike rate | Visits with an order ÷ total visits | 55-75% in a mature beat |
| Drop size | Order value ÷ orders | Rising slowly, with the range |
| Cost per productive call | (Salary + fuel + incentive + app) ÷ productive calls | The number that decides a beat |
| Secondary per outlet per month | Secondary sales ÷ active outlets | The demand truth |

Anything not measurable from the log is stated as "not measured". Six honest numbers beat twenty invented ones.

## Coverage, done properly

| Denominator | What it means | When to use it |
|---|---|---|
| Outlets in the beat | Are we running the plan | Weekly |
| Outlets in the territory | Are we covering the market | Monthly |
| Outlets billed | Are we selling to the market | Monthly |
| Active outlets (billed in 90 days) | Is the base alive | Quarterly |

A business that reports only the first one looks 95% covered and is 60% covered in reality, because the beat was
designed on the outlets it already served.

## The coverage map, which always surprises

Plot the outlets as a scatter on a map with the pin codes, coloured by billed or not billed in the last 30 days.
Three patterns appear in almost every territory:

1. **The dense core is over-covered** - an outlet visited four times a month that buys once.
2. **A ring of unvisited outlets around the core** - physically close, never on a beat.
3. **A long tail of dormant outlets** that were billed once, eighteen months ago.

The fix is usually to move calls, not to add reps: reduce the core frequency by one, add the ring.

## Strike rate and drop size together

| Strike rate | Drop size | Reading | Action |
|---|---|---|---|
| High | High | A healthy beat | Protect it, and add new outlets |
| High | Low | Right outlets, wrong range | Range selling; the order ask is too narrow |
| Low | High | A few big buyers, many dead calls | Reclassify; the beat carries too many non-buyers |
| Low | Low | Wrong outlets, or a supply or price problem | Fix supply and price before the beat |

Never report one without the other. A strike rate of 80% with a ₹1,800 drop is a different business from 80% with
₹14,000.

## Cost per productive call, the number that decides a beat

```
annual field cost for a rep = salary + incentive + fuel + phone + app + manager share
cost per productive call      = annual field cost / productive calls in the year
```

Worked shape: ₹3.6 lakh salary, ₹60,000 incentive, ₹72,000 fuel, ₹18,000 phone and app, ₹90,000 manager share =
₹6.0 lakh. At 11 productive calls a day × 25 days × 12 = 3,300 calls, that is **₹182 per productive call**.

Compare it to the gross margin per order. A ₹8,000 drop at 22% margin is ₹1,760 of gross margin; ₹182 is a tenth
of it, which is workable. A ₹1,500 drop at 12% is ₹180, which means the call costs more than it earns - and that
beat should be served by the distributor's salesman instead.

## The territory scorecard

| Territory | Outlets | Coverage | Prod. calls/day | Strike | Drop ₹ | Secondary ₹ | Cost/call ₹ | Verdict |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | Keep / fix / drop |

"Drop" rarely means abandon. It usually means: move to the distributor's own beat, serve monthly instead of
weekly, or merge into an adjacent cluster.

## Leading against lagging indicators

| Type | Metric | Why |
|---|---|---|
| Leading | Coverage, calls per day, share of shelf, new outlets added | Movable this week |
| Lagging | Primary, secondary, drop size | The result |
| Diagnostic | Strike rate, no-order reasons, stock-outs | Explains the gap |

A review that looks only at lagging numbers is a post-mortem. The weekly review runs on the leading ones.

## When the data is missing

| Missing | What you can still say | What you cannot |
|---|---|---|
| No visit logs | Beat design, target split, outlet potential | Coverage, calls per day, strike rate |
| No secondary data | Primary movement, distributor stock if reported | Real demand, stuffing, the true growth rate |
| No outlet universe | Nothing about coverage | Everything that depends on a denominator |
| No geo-tag | Orders and visits as logged | Whether the visit happened |

Say which column is empty and what it would change. A read that names its missing data is trusted; one that
papers over it is not.

## Anti-patterns

- **Reporting primary as sales.** It is stock movement, and the difference is a warehouse.
- **A coverage number with no denominator stated.** The denominator is the whole claim.
- **Judging reps on a metric the supply chain controls.** Stock-outs and credit stops are not the rep's failure.
- **A dashboard nobody opens.** Six numbers on one page, reviewed weekly, beats a BI tool.
- **Comparing two territories on drop size alone.** A metro A-outlet beat and a rural C-outlet beat are different
  businesses.
