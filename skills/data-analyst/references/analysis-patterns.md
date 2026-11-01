# Analysis patterns

Most business questions are one of eight shapes. Recognise the shape, and the analysis is mechanical - which is exactly what you want, because it leaves your judgement for the interpretation.

## 1. Decomposition - "why did this move?"

The workhorse. Never explain a change as one cause when you can split it.

**Multiplicative split:**
```
Revenue = Orders x Average order value
        = Customers x Orders per customer x AOV
        = Traffic x Conversion x AOV
```

**Additive split (contribution):**
```
Δ Revenue = Δ Volume effect + Δ Price effect + Δ Mix effect

Volume effect = (V1 - V0) x P0
Price effect  = (P1 - P0) x V0
Mix effect    = the remainder
```

Rules:

- **The parts must sum to the whole.** If they do not, you have a residual - name it.
- **Report the residual.** It is usually mix or an error, and both matter.
- **Say which factor is doing the work.** "70% of the drop is one SKU losing volume, not price."
- **Stop when the next split is not actionable.** Splitting below the level someone can change is decoration.

## 2. Segmentation - "which one is the problem?"

- **Cut by one dimension at a time** first: product, city, channel, customer, month. Then combine two.
- **Compare against a base rate, not against zero.** "This city is bad" only means something against the average.
- **Watch for small-n segments.** A city with 3 orders can be -80% and mean nothing. Show n next to every rate.
- **Pareto / ABC analysis** - the top 20% usually carry 60-80%. Useful for stock and focus decisions, and almost always worth running once.
- **Do not stop at the worst segment.** Ask why it is worst: price, stock, delivery, or simply the wrong customer mix.

## 3. Cohort - "is this getting better or worse over time?"

The right tool for retention, repeat purchase and product quality. Group by the month of first purchase, then track each group forward.

| Cohort | M0 | M1 | M2 | M3 |
|---|---|---|---|---|
| Jan | 100% | 42% | 28% | 21% |
| Feb | 100% | 39% | 25% | 19% |
| Mar | 100% | 46% | 33% | 26% |

Read down a column to compare cohorts; read across a row to see decay. A flat column means the product has not improved, whatever the headline revenue says.

## 4. Funnel - "where do people drop?"

- **Define each step precisely.** "Visit" is not a step; "product page viewed with a variant selected" is.
- **Steps must be nested** - everyone in step 3 was in step 2.
- **Report the rate between steps**, not just the counts.
- **A funnel with no time window is meaningless.** 30 days, not "ever".
- **The biggest drop is not always the biggest opportunity.** A 40% drop at a step you cannot change is less valuable than a 5% drop you can.

## 5. Variance vs plan - "why are we off target?"

| Variance | Cause | Who can act |
|---|---|---|
| Volume | Fewer units sold | Sales, marketing, stock |
| Price / discount | Discounting to hit volume | Pricing |
| Mix | Selling more of the cheap thing | Merchandising, sales |
| Cost | Input, freight, wastage | Operations, procurement |

Report variance as a table with the four lines and a total that ties. Then say which line is fixable this quarter.

## 6. Time series - "what is the trend?"

- **Always compare year on year for anything seasonal.** Indian retail has Diwali, monsoon, exam season, wedding season. A month-on-month comparison across a festival is noise.
- **Use a 3-month rolling average** to see direction, and the raw line to see the shocks.
- **Distinguish trend, seasonality and one-off.** A spike is a one-off until it repeats.
- **Never fit a straight line through 8 points and call it a forecast.** See `references/statistical-honesty.md`.

## 7. Concentration and dependency - "how fragile are we?"

- **Top-5 customer share of revenue and of margin.** A business where one customer is 40% of revenue is one renewal away from a crisis.
- **Top-5 SKU share**, and the share of stock value in the slowest 30%.
- **Channel concentration**, and single-supplier dependency for any input.
- Report as a percentage with the names, not just the number.

## 8. Unit economics - "does any of this make money?"

The one analysis that overrides all the others.

```
Contribution per order = Revenue - COGS - shipping - payment fee - packaging - returns provision
CAC                    = total acquisition spend / new customers
Payback                = CAC / contribution per order per month
```

Do this per segment - product, channel, city - because the average hides the business. A blended positive margin with three loss-making channels is the most common shape of a failing D2C business, and the average will not show it.

## Choosing the right pattern

| Question | Pattern |
|---|---|
| "Why did X change?" | Decomposition (1) |
| "Who is the problem?" | Segmentation (2) |
| "Are we getting better?" | Cohort (3) |
| "Where do we lose people?" | Funnel (4) |
| "Why are we off plan?" | Variance (5) |
| "What is the trend?" | Time series (6) |
| "How risky is this?" | Concentration (7) |
| "Is this profitable?" | Unit economics (8) |

## Anti-patterns

- Answering a decomposition question with a segmentation table. The most common mismatch.
- Explaining a movement with a single cause and no arithmetic.
- Reporting a rate with no denominator.
- Comparing a festival month to a normal month without adjustment.
- Building a dashboard when the question was one number.
- Analysing at the level of the total when the decision is at the level of the segment.
- Letting the available data choose the question, rather than the decision choosing the data.
