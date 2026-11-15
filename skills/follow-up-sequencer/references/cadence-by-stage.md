# Cadence by stage

The interval is a property of the stage, not of the salesperson's mood. This file sets the intervals and the stop
rules, and says what each stage is actually waiting for.

## The stages, defined by what the buyer is deciding

| Stage | The buyer is deciding | The next step is called | Typical interval |
|---|---|---|---|
| Enquiry received | Whether this is worth a conversation | First call | Within 1 working day |
| Conversation had | Whether the need is real and the fit is close | Needs confirmation | 2-3 days |
| Demo or sample given | Whether it does what they need | Feedback ask | 2-3 days, then 7 |
| Quote or proposal sent | Whether the price is acceptable | Decision ask | 3 days, then 7, then 14 |
| Trial or pilot running | Whether it works in their environment | Check-in with a question | Weekly, at a fixed day |
| Negotiation | Whether the terms can be agreed | Term response | 2 days, then 4 |
| Decision pending (their side) | Nothing - they are waiting on an internal step | Follow the date they gave | On the date, not before |
| Won / lost | - | Handover or reason code | Within 2 days |

If the CRM's stages cannot be filled into that table, the stages are wrong. Fix the table first; a cadence on
undefined stages just makes the wrong thing happen on time.

## The interval logic

Three inputs set the interval. Write them down per stage:

1. **How long a normal decision takes in this trade.** A ₹20,000 order in a local trade closes in days; a
   government tender in weeks; a factory equipment purchase in months. A cadence faster than the buying cycle
   reads as desperation.
2. **What the buyer said.** "Call me after Diwali", "we review vendors in March", "I will discuss with my partner
   on Saturday" - the buyer has given you the date. Use it. Following up before the date they named is the single
   most common way a warm deal cools.
3. **What the last touch promised.** If the last message said "I will send the revised pricing by Thursday", the
   next touch is Thursday, and it is yours to make, not theirs.

## Touch counts and the stop rule

| Stage | Maximum touches | Spread over | Stop rule |
|---|---|---|---|
| Post-quote, no response | 4 | 3, 7, 14, 30 days | After touch 4 with no reply, mark lost - no decision |
| Post-demo, no feedback | 3 | 2, 7, 21 days | After touch 3, ask one direct question: is this still live? |
| Post-conversation, no next step | 2 | 2, 10 days | After touch 2, park with a reason and a re-contact date |
| Trial running | Weekly until end, then 2 | Fixed weekday | At trial end plus 2 touches, decision or lost |
| Decision pending on their side | 1 per promised date | At the date they named | Two missed dates = park |
| Negotiation | 3 | 2, 4, 7 days | After touch 3, the offer lapses with a written date |

"Lost - no decision" is a real outcome and must be available in the CRM. Without it, the only way to clear a
dead deal is to delete it, and the reason disappears with it.

## Channel ladder

Escalate the channel only when the previous one has been ignored, and only within what the buyer agreed to:

| Touch | Channel | Why |
|---|---|---|
| 1 | The channel the conversation happened on | Continuity; a WhatsApp thread followed by email reads as a different company |
| 2 | Same channel | One missed message is not silence |
| 3 | A different channel, once | Email if it was WhatsApp; a call if it was email |
| 4 | A call, at a time of day they answered before | Voice is the fastest way to get a yes, a no or a date |

Never escalate to a channel the buyer has not used with you, and never to a personal number that was not given
for business contact.

## The timing that matters in India

| Situation | Adjustment |
|---|---|
| Festival weeks (Diwali, Holi, Eid, Pongal, Onam, Durga Puja) | Stop commercial follow-ups in the week itself; resume after, referencing the break |
| Financial year-end (March) | Buying committees are busy and budgets are closing - the last week of March is a real deadline, use it |
| Month-end and quarter-end | Accounts and procurement are unreachable; owners are reachable |
| Monday morning and Friday evening | Low reply rates; Tuesday-Thursday, 10am-12pm and 3pm-5pm work better |
| Monsoon, harvest, exam season, wedding season | Trade-specific; write the local pattern into `learnings.md` |
| A buyer who replies at 11pm | They are working late; a reply the next morning is fine, an automated 11pm reply is not |

## The weekly rhythm

- **Monday**: the stale list, sorted by value at risk and days since touch. Every deal past its date gets a
  decision this week - a touch, a date, or lost.
- **Daily**: the touches scheduled for today, drafted the day before so the owner can edit rather than compose.
- **Friday**: pipeline health - open, with a next step, without one, past date, lost with reason.
- **Monthly**: reply rate by touch number, by stage, by channel. If touch 3 and 4 never get a reply, the cadence
  is too long and the deals are dying at touch 2.

## Anti-patterns

- The same interval for every stage: a quote and a thank-you note are not the same decision.
- Following up the day after a quote "to check if you received it". They received it.
- A five-week cadence for a product that is decided in three days.
- Restarting a stopped sequence because a new quarter began.
- Skipping the stop rule for the big deal, so the big deal gets chased into embarrassment while the small ones
  die quietly.
- Counting an auto-responder as a reply.
