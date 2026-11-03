# Testing and rollout

A price change is a live experiment on the business. This file is how to run one
without losing the customers you already have.

## Can you test at all?

| Traffic / volume | What is possible |
|---|---|
| Under 200 transactions a month | No A/B. Use a sequenced rollout with a before-after comparison and say the evidence is weak |
| 200-2,000 | A pilot on one segment, one city or one channel, for 4-6 weeks |
| Over 2,000 | A proper A/B on new visitors, with the same creative and channel mix |
| B2B with a sales team | No A/B; test on new quotes only, and compare win rate at matched deal sizes |

Never A/B price on existing customers renewing, without notice. It is a trust
problem and, in some cases, a legal one.

## The sequenced rollout

1. **New customers first.** Always. The old price stays for the base until the new
   one is proven.
2. **One segment, one channel, one city.** Enough to read, small enough to reverse.
3. **Run for a full cycle.** For a monthly product, six weeks; for a seasonal
   business, the same weeks as last year.
4. **Compare like with like.** Same channel mix, same creative, same season. A price
   test that runs during Diwali is a test of Diwali.
5. **Decide on the pre-agreed metric**, not on the feeling in the room.

## Grandfathering

| Option | Use when | Cost |
|---|---|---|
| Forever at the old price | Loyal, long-tenured, small share | Grows into a permanent discount base |
| 12 months, then the new price with notice | Default for most businesses | Needs a communication plan |
| At the next renewal, with 60 days' notice | Contractual customers | Churn risk at the renewal |
| Immediately, no exception | The old price was an error, or a compliance issue | Relationship damage; use only with a reason |

Rule: **existing customers get notice, not a surprise.** The notice period is written
in the change plan, and the message says what changes, when, and what stays.

## Communication

- **Say what changes, the date, and the reason in one sentence each.** "From 1
  December, Growth moves to ₹4,999 a month. It now includes the reporting module and
  five users. Your price stays at ₹3,999 until your renewal in March."
- **Give the sales team the script before the customers hear it.** A salesperson
  learning the price from a customer is a churn event.
- **Prepare the objection answers** for the three that will come: why now, why not
  for me, and what do I get.

## Measurement

| Metric | Compare | Window |
|---|---|---|
| Conversion or win rate | Same segment, same channel, prior period | 4-6 weeks |
| Realised price | Before and after, from invoices not the list | Monthly |
| Churn and downgrade rate | Cohort, not aggregate | 90 days |
| Support contacts about price | Before and after | 4 weeks |
| Revenue and contribution | Against the model's scenario | Monthly for a quarter |

## The reversal trigger

Written before the change, in one line:

> "If win rate falls more than 8 points against the matched segment for two
> consecutive months, or contribution revenue falls below ₹X, the price returns to
> ₹Y on the first of the following month."

A change without a reversal trigger becomes permanent by default, whatever the
evidence says.

## The memo the founder signs

One page: current state, evidence, recommendation, scenarios, the discount policy,
the rollout dates, the metric, the reversal trigger, and what is not known. Signed
and dated, filed in `notes/decisions.md`. Six months later, this is the only document
that explains why the price is what it is.

## Anti-patterns

- Testing a price on everyone at once and calling the revenue change the result.
- A/B testing on a sample too small to detect anything but a large effect.
- Announcing a rise with no notice period.
- No grandfathering, and a churn spike explained as "the market".
- A test that changes price, packaging and the sales script in the same week.
- No reversal trigger, so a bad change is only discovered at the annual review.
- Deciding the result by looking at a chart rather than the pre-agreed metric.
