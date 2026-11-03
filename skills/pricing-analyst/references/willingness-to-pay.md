# Willingness to pay

Nobody knows what a buyer will pay, including the buyer. The job is to reduce the
uncertainty with the cheapest evidence available, and to label what remains.

## The evidence ladder - cheapest first

| Method | Cost | Sample | Tells you | Cannot tell you |
|---|---|---|---|---|
| Win-loss interviews | Hours | 10-20 | Why deals closed or died, at what price | The price of a deal that never happened |
| Cost of the alternative | Hours | 3-5 buyers | The real ceiling - what they pay today, in money and effort | Their budget headroom |
| Structured conversations | Days | 12-20 | The band, the objections, the language | Precise elasticity |
| Van Westendorp | A week | 100+ | An acceptable price range, four thresholds | What they will actually pay at launch |
| Gabor-Granger | A week | 100+ | Purchase intent at fixed prices | Long-run behaviour |
| Conjoint-lite (3-5 attributes) | 2-3 weeks | 150+ | Which features carry the price | Anything with a small sample |
| Live A/B on price | Weeks | High traffic | Real behaviour | Only where traffic and ethics allow |

Most Indian SMBs should run the first three and stop. A model built on a 40-person
survey is a decoration.

## The cost-of-the-alternative question

The single most useful conversation, in this order:

1. "What do you do about this today?"
2. "What does that cost you - in money, in time, in people?"
3. "What goes wrong with it?"
4. "If something removed that, what would it be worth a month?"

The answer to (4) divided by three is usually close to a price that holds. Ask for a
number, then ask what else they would spend that money on - the second answer tells
you whether you are competing with a software budget or a hiring budget.

## Van Westendorp, used honestly

Four questions, one per respondent, about a described product:

1. At what price would it be **too cheap** to trust?
2. At what price is it a **bargain**?
3. At what price does it start to feel **expensive**?
4. At what price is it **too expensive** to consider?

Plot the four cumulative curves; the acceptable band sits between the "too cheap"
and "too expensive" crossings, and the point of marginal cheapness/expensiveness
brackets the range. Use it to **rule out** prices, not to pick one. It systematically
understates what B2B buyers will pay for a painful problem.

## Gabor-Granger, used honestly

Show one price at a time and ask "would you buy at ₹X?". Repeat across a ladder.
The curve gives purchase intent per price; multiply by your realistic close rate,
not by the intent, and treat the result as a ceiling.

## Conjoint-lite

Pick three to five attributes with two or three levels each - for example price,
support level, onboarding, and one feature - and ask respondents to choose between
packages. It tells you which attribute carries the decision, which is what packaging
needs. Below 150 responses, the output is a hint.

## Interview discipline

- **Never ask "would you pay ₹X?"** as the first question. It anchors and it invites
  politeness.
- **Ask about the past, not the future.** "What did you pay for the last thing like
  this?" beats "what would you pay?" every time.
- **Talk to the person who signs.** A user's enthusiasm is not a budget.
- **Record the segment.** A price finding from a 5-person firm does not transfer to
  a 200-person firm.
- **Write the exact words** customers use about price. Those words become the sales
  script, and the objection handling in `sales-outreach`.

## Segment before averaging

| Segment | Different because |
|---|---|
| Solo / micro | Price-sensitive, low volume, self-serve, churns fast |
| Small business (10-50) | Buys on time saved, needs a human on the phone |
| Mid-market (50-500) | Buys on process and audit trail, procurement involved |
| Enterprise | Buys on risk and integration, price is a small part of the decision |
| Government / PSU | Tender price, L1 logic, payment cycle - a different game |

An average across these segments is a number that fits none of them.

## What cannot be measured

- **Elasticity at low volume.** Under a few hundred transactions a month, a price
  change produces noise, not a curve.
- **The price of a new category.** There is no reference price; you are anchoring,
  and the first number becomes the reference for years.
- **Competitor response.** You can model it, not know it.

## Anti-patterns

- A survey of your own best customers, who are the least price-sensitive people you have.
- Asking "what would you pay" and taking the answer as data.
- Averaging across segments.
- A conjoint with 30 responses and a confident chart.
- Ignoring the cost of the alternative, which is the only real ceiling.
- Running a price test on new visitors only and calling it the market's answer.
