# Budget, pacing and bidding

Pacing is arithmetic. It is the difference between a month that ends on target and a
month that ends with a panic cut in the last week.

## The four numbers

| Number | Meaning |
|---|---|
| Budget for the period | What the business allocated, and whether it is fixed |
| Target CPA | What the margin can afford at the volume wanted |
| Spend to date and days elapsed | Where the period actually is |
| Conversions to date | What the spend has bought so far |

From these: projected spend, projected conversions, and the **allowable CPA for the
remaining days**:

$$
\text{allowable CPA} = \frac{\text{remaining budget}}{\text{remaining conversions needed}}
$$

If the allowable CPA is below what the account has ever achieved, the target is not
reachable at this budget, and the decision is to change the target, change the
budget, or change the offer - not to "optimise harder". Run
`scripts/pacing_calculator.py` rather than estimating.

## Pacing patterns, and what they mean

| Pattern | Reading | Action |
|---|---|---|
| Underspending with a healthy CPA | Bid too low, audience too small, or delivery constrained | Raise budget or bid, widen the audience |
| Underspending with a poor CPA | The account is being throttled by performance | Fix creative or page before adding budget |
| Overspending ahead of plan | Daily budget over-delivery or a lifetime budget mis-set | Cap the daily, or shift to lifetime |
| On pace, CPA drifting up | Saturation or creative fatigue | Refresh creative before touching budget |

## Scaling

- **Steps of 20%**, held three days, watching CPA and frequency.
- **Scale the winner, not the account.** Moving budget to a campaign still in
  learning wastes it.
- **Duplicate for scale only when the budget is large enough** to keep both copies
  out of learning; otherwise raise the budget on the original.
- **Cap the ceiling before you start.** At some spend, the marginal CPA exceeds the
  affordable number; the ceiling is where scaling stops.

## Bidding, in one page

| Strategy | Use when |
|---|---|
| Lowest cost, no cap | You trust the creative and want volume; watch CPA daily |
| Cost cap | You have a stable CPA and want to hold it; expect less volume |
| Bid cap | Auction control in a competitive category; risky on small budgets |
| ROAS target | Only with reliable revenue values and enough conversions to learn |

Small budgets and tight caps are a bad combination: the platform cannot find enough
volume under a low cap, delivery stalls, and the account looks broken when the cap
was the problem.

## Seasonality, India

| Period | What happens | Plan |
|---|---|---|
| Diwali fortnight | CPMs climb sharply; intent is high but so is competition | Book budget early, expect a higher CPA, do not judge creative in this window |
| IPL and major cricket | Evening CPMs spike, especially video | Shift to daytime or non-sports placements if the audience allows |
| End of financial year (March) | B2B budgets release; B2C discount noise | Segment B2B campaigns separately |
| Exam and admission season | Education categories spike | Category-specific |
| Monsoon and regional festivals | Demand shifts by category and state | Plan per state, not nationally |

Judge creative and structure outside these windows. A test run during Diwali tells
you about Diwali.

## The daily discipline, ten minutes

1. Spend against plan.
2. Conversions and CPA, per campaign.
3. Frequency on the largest cold audience.
4. Any campaign with zero delivery.
5. Any landing page that failed a check.
6. The one change you will make today, and the rule it follows.

One change a day, maximum. Three changes at once and tomorrow's number means
nothing.

## Anti-patterns

- **Cutting budget in the last week to hit a monthly number.** It destroys the
  learning and the month after.
- **Chasing a daily CPA target with daily edits.** The auction rewards stability.
- **Lifetime budgets on evergreen campaigns.** They hide the daily pacing.
- **Judging a campaign on day one.** Every campaign starts badly.
- **Setting a cost cap below the historical CPA.** Delivery stalls and everyone
  blames the creative.
- **No ceiling.** The campaign that scales beautifully at ₹50,000 can be a loss at
  ₹3 lakh, and nothing in the dashboard says so.
