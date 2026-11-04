# Funnel diagnosis

Growth problems are almost always one step, not five. The job is to find the step
with the biggest gap between what happens and what should, and prove it with
absolute numbers rather than percentages alone.

## The table that starts every diagnosis

| Step | Definition | Volume | From previous | Benchmark | Gap |
|---|---|---|---|---|---|
| Reach | People who saw an impression | | - | | |
| Visit | Sessions that loaded the page | | | | |
| Activation | Signed up, enquired, added to cart | | | | |
| Qualified | Matched the ICP, answered, showed intent | | | | |
| Paid | First payment received | | | | |
| Retained | Still paying at day 90 | | | | |

Rules for the table: absolute numbers first, conversion rates second; one date
range; one source per row named on the sheet; and if a step is not instrumented,
say "not measured" rather than estimating it silently.

## Reading the gap

| Pattern | Likely constraint | First thing to check |
|---|---|---|
| High traffic, low activation | The promise or the page | Message match between ad and page, page speed, form length |
| High activation, low qualification | Targeting | Who is arriving, from which channel and which keyword |
| High qualification, low paid | Offer, price or follow-up | Sales response time, proposal clarity, price objection |
| High paid, low retained | Product or onboarding | Time to first value, support volume, cancellation reasons |
| All rates fine, volumes low | Reach or budget | Channel capacity, spend ceiling, market size |
| Everything fine, margin falling | Discounting or mix | Realised price, channel mix, delivery cost |

## The three questions that cut the analysis in half

1. **Is the volume big enough to trust the rate?** Under 100 events at a step, the percentage is noise.
2. **Is the drop at the step, or before it?** A 2% conversion from a cold audience and from a warm list are different problems.
3. **Is it a demand problem or a delivery problem?** If sales follow-up takes three days, no amount of traffic fixes it.

## Segment before you conclude

Cut every funnel by at least three dimensions before naming the constraint:

- **Source** - organic, paid, referral, outbound, marketplace.
- **Segment** - new versus returning, deal size, city tier, B2B versus D2C.
- **Device and channel** - mobile versus desktop still changes conversion by multiples in India.

A blended conversion rate of 3% is usually 8% on one segment and 0.4% on another,
and the answer is almost always to spend more on the first and stop the second.

## Benchmarks, honestly

- Use the business's own history first. Last quarter is a better benchmark than an industry average.
- Where no history exists, use a published range and label it: "Indian D2C checkout completion typically 45-60%; we are at 22%, so the gap is large enough to act on."
- Never present a benchmark as a target. A benchmark says what is normal, not what is right for this business.

## The one-page diagnosis

```
Constraint: <step> - <rate> vs <benchmark or history>
Proof:      <absolute numbers, date range, source>
Cause:      <the two or three plausible causes, ranked>
Test:       <the cheapest test that separates them>
Owner:      <who runs it>
```

## Anti-patterns

- **Percentage-only analysis.** "Conversion dropped 30%" hides whether it fell from 10% to 7% or from 0.3% to 0.2%.
- **Averages across segments.** The average is the story of nobody.
- **Diagnosing from the dashboard.** The dashboard shows what was instrumented, not what matters.
- **Blaming the channel first.** Most "bad traffic" is a page that does not match the promise.
- **Ignoring sales response time.** In Indian B2B, a first response after 24 hours can halve qualification.
