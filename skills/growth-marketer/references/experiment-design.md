# Experiment design

A test is a decision with a price and a date. Written before it runs, or it is an
opinion with spend attached.

## The brief, seven fields

| Field | Rule |
|---|---|
| Hypothesis | "If we <change>, then <metric> will move by <amount>, because <reason>" |
| The one variable | Exactly one. Two changes and one result is a story |
| Primary metric | Chosen before the test; the one that decides |
| Guardrail metrics | The ones that must not get worse: refund rate, lead quality, page speed |
| Sample and duration | Per variant, from the power calculation, and the days it takes to reach it |
| Kill rule | The result that ends it early, and the safety threshold that ends it immediately |
| Decision | What happens if it wins, and if it does not |

A hypothesis without a "because" is a preference. The "because" is what makes the
result generalisable to the next test.

## Sizing it

Per variant, for a two-variant test at 95% confidence and 80% power:

$$
n \approx \frac{16 \cdot p(1-p)}{\delta^2}
$$

where $$p$$ is the baseline rate and $$\delta$$ the absolute lift you want to
detect. Run `scripts/experiment_power.py` rather than doing this by hand.

Two consequences worth internalising:

- **Small effects need enormous samples.** Detecting a move from 2.0% to 2.4%
  (a 20% relative lift) needs about 19,600 users per variant. Most SMBs do not have
  that traffic, which means most small tests cannot detect small effects.
- **Test big changes.** If the traffic only supports detecting a doubling, then
  test a new offer, not a new button colour. This single rule raises the value of
  every small business's testing programme.

## Duration rules

- **Whole weeks.** Day-of-week effects are large in B2C; a Tuesday-to-Thursday test
  measures Tuesdays.
- **At least two business cycles.** A B2B test over one week measures one mood.
- **Long enough to include a payday and a non-payday week** in consumer categories.
- **Stop at the pre-registered point**, not when the chart looks good.

## The peeking problem

Checking a running test and stopping when it looks significant inflates false
positives dramatically. Two workable options:

1. **Fix the end date and do not look at the primary metric until then.** Look at
   guardrails only.
2. **Pre-register a single interim look** at the halfway point, with a stricter
   threshold, and accept the small power loss.

What is not workable is checking daily and stopping on the first green reading.

## Reading the result

| Result | Reading |
|---|---|
| Clears the bar, guardrails fine | Ship it, and write down what it taught |
| No difference, sample was adequate | A real finding: this change does not matter. Move on |
| No difference, sample was too small | Not a finding. Say so plainly and do not ship on it |
| Better on the metric, worse on a guardrail | A trade-off, not a win; decide with the margin |
| Worse | Usually the most informative result; write down why it might have failed |

## Experiments worth running in a small business

- A new offer or bundle versus the current one.
- Price displayed above the fold versus below.
- Form with 3 fields versus 6.
- WhatsApp follow-up within 2 hours versus 24.
- Landing page in English versus the buyer's language.
- COD versus prepaid incentive.
- Lead form versus site form, measured on qualified leads, not leads.

## Anti-patterns

- **The A/B test on 400 visitors.** It cannot detect anything; run a bigger change
  or a sequential test instead.
- **The metric switch.** "Conversions did not move, but time on page did" is how a
  failed test becomes a slide.
- **Testing the trivial.** Button colour is a rounding error next to offer and price.
- **The permanently running test.** Without a decision date, it is a dashboard.
- **No experiment log.** The team re-runs the same failed test every year.
- **Personalisation by guess.** Segment-specific tests need segment-specific
  sample sizes, which most SMBs do not have; use qualitative evidence there instead.
