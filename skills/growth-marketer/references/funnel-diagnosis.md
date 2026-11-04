# Funnel diagnosis

Growth is a rate problem before it is an idea problem. Find the rate that costs the
most money, and fix that one.

## The arithmetic

| Stage | Count | Rate from previous | Revenue value of +20% on this rate |
|---|---|---|---|
| Reach / impressions | | - | |
| Clicks / sessions | | CTR | |
| Enquiry or signup | | conversion | |
| Qualified or activated | | qualification | |
| First order | | purchase | |
| Repeat within 90 days | | repeat | |

Fill every cell from a named source. A funnel with an assumed stage is a funnel
with an assumed conclusion.

The last column is the point of the exercise. A stage converting at 2% looks worse
than one at 40%, but if a 20% improvement on the 40% stage is worth ten times more
rupees, that is the constraint.

## Finding the constraint, not the ugliest number

Three tests, in order:

1. **Money.** Improvement × volume × contribution per unit. Compute it, do not eyeball it.
2. **Controllability.** Can this business move that rate this quarter, with the tools it has? A 3% site conversion is movable; a market-wide CPM is not.
3. **Compounding.** Does fixing it improve the next stage too? Activation lifts repeat purchase, which lifts lifetime value, which raises the CAC you can afford.

The constraint is the stage that passes all three. Usually exactly one does.

## Rates worth knowing, and why benchmarks mislead

Benchmarks from another market, another price point or another category are a way
of feeling informed. Use them only as a sanity band, and prefer your own history:

- **Your own last twelve weeks** is the only benchmark that controls for your
  offer, your price and your audience.
- **Cohorts beat periods.** Comparing this month's signups to last month's tells
  you about mix; comparing each month's cohort at day 30 tells you about the
  product.
- **Segment before concluding.** One segment converting at 0.5% can hide another at
  6%. Split by source, device, city tier and language before you call the rate.

## The common leaks, in the order they usually appear

| Leak | Symptom | First check |
|---|---|---|
| Reach to click | High impressions, low CTR | Is the creative saying the thing the audience wants, in their language |
| Click to enquiry | Sessions bounce under 10 seconds | Does the first screen answer "what is it, for whom, how much" |
| Enquiry to qualified | Sales says the leads are junk | Is the form qualifying, or is the incentive attracting the wrong person |
| Qualified to first order | Long gap, high drop | Price clarity, delivery promise, payment options, trust signals |
| First order to repeat | One purchase, never two | The product experience, the post-purchase contact, the reorder trigger |
| Paid to retained | Good CAC, bad 90-day value | Retention is a product problem wearing a marketing costume |

## Reading a funnel that "does not add up"

- **Definitions differ between systems.** A "lead" in the CRM is a form fill; a
  "lead" in the ad platform is a click on a button. Write both definitions down.
- **Attribution windows differ.** Seven-day click versus one-day view produces
  different numbers from the same week.
- **Bots and internal traffic.** Filter your own IPs and staff devices before
  concluding anything about a landing page.
- **The gateway is the truth.** Orders, refunds and COD failures live there, not in
  the analytics tool.
- **A stage that is missing entirely** is usually the most valuable finding: many
  Indian SMB funnels have no qualification step, so the sales team does the
  qualifying by hand and calls it a lead-quality problem.

## Diagnosing with almost no data

If the business has never instrumented anything, do not start with a dashboard.
Start with what exists:

1. The order book or the books, by month and by source if the source was ever asked.
2. The WhatsApp or call log - who enquired, who bought, what they asked.
3. The top twenty customers, asked directly: "how did you first hear about us".
4. The sales team's last fifty conversations, read in order.

Three hours of that produces a better constraint than a month of a half-installed
analytics tool.

## Anti-patterns

- **Optimising the top of the funnel when the leak is at the bottom.** More traffic
  into a broken checkout is a faster way to lose money.
- **Fixing the rate that is easiest to measure** rather than the one that costs most.
- **A funnel with no repeat stage.** Acquisition-only thinking caps the business at
  its first purchase.
- **Comparing this month to last month without cohorts.**
- **Calling a product problem a marketing problem.** If 60% of buyers never return,
  no channel fixes it.
