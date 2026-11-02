# Discovery and evidence

The job is not to find out what customers want - they will tell you what they want, and they are usually describing a workaround. The job is to find out what they do, what it costs them, and what they have already tried.

## Evidence hierarchy

| Rank | Evidence | What it proves | Cost |
|---|---|---|---|
| 1 | Observed behaviour in the product - funnel drop, repeat use, abandonment | What people actually do | Low, if analytics exists |
| 2 | Support tickets and WhatsApp messages, counted by theme | Where the friction is, in their words | Low |
| 3 | Five to eight customer conversations about the last time it happened | Why, and what the workaround costs | Medium |
| 4 | Sales call objections, counted | What blocks the purchase | Low |
| 5 | A survey | What people say they think | Medium, weak |
| 6 | A founder's hunch, or one loud customer | A hypothesis | Free, and expensive |

Rank 6 is where most specs start. It is not useless - it is a hypothesis, and it needs one rank-3 conversation before it becomes a plan.

## The conversation that produces evidence

Never ask "would you use a feature that does X". Ask about the past:

1. "Tell me about the last time you had to <do the thing>." (a specific instance)
2. "What did you do?" (the workaround, step by step)
3. "How long did that take, and who else was involved?" (the cost)
4. "What did you try before that?" (what has already failed)
5. "What did it cost you when it went wrong?" (the stakes)
6. "What would have to be true for you to change how you do it?" (the switching condition)

Six questions, twenty minutes, and you have a problem statement in the customer's own vocabulary. Record the quotes verbatim - paraphrase loses the words that end up in the copy.

## From feedback to decision

1. **Count themes, not requests.** "Nine of forty tickets mention the same invoice format" is a finding; a list of forty requests is noise.
2. **Separate the request from the need.** "Add a bulk delete" usually means "I have 400 test rows and no way to clean them".
3. **Name the workaround.** If customers export to Excel to do the thing, the product is missing a step, and that is the spec.
4. **Size the segment honestly.** Nine tickets from 400 customers is 2% - real, and not a reason to rebuild the product.
5. **Decide: build, fix, document, or decline.** Four outcomes, and three of them are cheaper than building.

## The four outcomes

| Outcome | When | Who does it |
|---|---|---|
| Build | Frequent, costly, and a product change is the cheapest fix | The team |
| Fix | The behaviour exists and is broken or undiscoverable | The team, faster |
| Document | The need is real but rare; a help article removes the friction | `knowledge-base-writer` |
| Decline | Rare, low cost, or against the strategy | You, with the reason recorded |

Recording a decline with its reason is the highest-value thing in this file. It stops the same request being re-litigated every quarter, and it makes the next "no" faster.

## What discovery cannot tell you

- **Whether people will pay.** Only a price conversation or a real transaction does that.
- **How big the market is.** That is `research-analyst`.
- **Whether they will switch.** Stated intent is a poor predictor; the workaround's stickiness is a better one.
- **What they will do in six months.** Behaviour changes with context.

## Anti-patterns

- **Building for the loudest customer** because they are on the phone every week. Note the revenue at stake; it is usually smaller than the noise.
- **A survey with leading questions** - "wouldn't it be useful if...".
- **Five conversations with the same type of customer**, then claiming a segment.
- **Discovery that never ends.** Two weeks and eight conversations is enough to decide; more is procrastination with travel.
- **Recording opinions instead of instances.** "They want it faster" is an opinion; "they re-enter 40 orders by hand every Monday, which takes two hours" is an instance.
