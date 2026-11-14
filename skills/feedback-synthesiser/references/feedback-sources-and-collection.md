# Feedback sources and collection

Where the voice of the customer actually lives, what each channel is worth, and what each one lies about.

## The channel map

| Channel | Typical volume | What it is good for | Its bias |
|---|---|---|---|
| Helpdesk tickets | High | The broken things, in detail, with a timeline | Skews to the articulate and the persistent |
| App store / Play reviews | Medium | Emotional, public, unedited | Extremes only; the middle rarely writes |
| Google Business reviews | Low-medium | Local and service businesses, walk-in experience | Skews to anger and to staff-prompted praise |
| Marketplace reviews (Amazon, Flipkart) | High | Product, packaging, delivery, size | Skews to delivery and to the first week |
| WhatsApp Business | High in India | The real complaint, in the customer's own register | Skews to the paying, the older, the relationship-led |
| NPS verbatims | Medium | A reason attached to a score | Skews to promoters and detractors; passives are silent |
| Cancellation / churn forms | Low | The most honest sentence in the business | Skews to the polite; the real reason is often "price" |
| Sales-call notes | Low | Objections that kill deals before they are customers | Only what the rep wrote down |
| Community / social comments | Medium | Emerging issues, competitor mentions | Skews to the loud and the young |
| Returns reasons | Medium | Product truth: fit, quality, description mismatch | Only for physical goods |
| Support agent's own memory | Unmeasured | The pattern nobody recorded | Unverifiable; a hypothesis, not evidence |
| The founder's inbox | Low | Enterprise and high-value relationships | One customer, enormous weight |

A read built on one channel is a read of that channel. State which channels are in and which are out, every
time, in the first three lines.

## What to collect, in what format

| Field | Why |
|---|---|
| Date | Trend, and whether the period was representative |
| Channel | The bias, and the weight |
| Customer ID (hashed or internal) | Counting customers, not mentions |
| Segment: plan, tenure, monthly value, city tier | The segment read is the actual insight |
| The text, unedited | The coding depends on the customer's words |
| Reason code from the system, if any | To compare the system's taxonomy with the real one |
| Outcome: resolved, refunded, churned, ignored | Severity |

An export missing the segment fields is still useful; it just cannot answer "who". Say so.

## Sampling when the corpus is large

| Corpus size | What to do |
|---|---|
| Under 500 | Code everything |
| 500-3,000 | Code a random 300-400 plus every cancellation and every 1-2 star review |
| Over 3,000 | Stratified sample by channel and rating, 400 minimum, plus a keyword sweep for known issues |

A sample is fine. An unstated sample is not. Write the sample size, the method and the confidence caveat in one
line.

## The channels people forget, and they are usually the best ones

1. **Sales-call objections.** The deal that never closed has the clearest statement of what is wrong with the
   product, and nobody files it.
2. **Cancellation free-text.** One sentence, written by someone with nothing to gain.
3. **The first reply in a WhatsApp thread.** The customer's opening message is the complaint; the rest is
   negotiation.
4. **Refund and return reasons.** Product truth, at the SKU level.
5. **The support agent's shortcuts.** If the team has a canned reply for something, it is a theme with a count
   nobody has taken.
6. **The questions in the pre-sales chat.** What people ask before buying is what the listing fails to say.

## Consent, privacy and the honest limit

- Feedback given in a support conversation may be read for improvement; it may not be republished with
  identity. Redaction is not optional.
- Under India's DPDP Act, feedback text tied to an identifiable person is personal data. Keep it in the system
  it arrived in, work from a de-identified extract, and put nothing raw in the repo.
- Never quote a customer in a public document, a deck or a listing without written permission.
- Never combine details - city, plan, product, date - in a way that identifies one person to their own team.

## Anti-patterns

- **Reading only the last two weeks.** Recency is the strongest bias in feedback and the least useful.
- **Reading only the loud channel.** Twitter is 0.5% of customers and 30% of the emotional volume.
- **Asking the team what customers say.** It produces the team's theory, which is what you were trying to test.
- **A survey to answer a question the tickets already answer.** Send the survey when the corpus is silent on a
  specific thing, not as a substitute for reading.
- **Collecting without a period.** A corpus with no start and end date cannot be compared to anything later.
