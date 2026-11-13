# Routing and response SLA

The score decides whether to act. The SLA decides whether the action is worth anything. In inbound,
speed beats quality of first contact more often than anyone likes to admit.

## The SLA table

| Band | First touch | By whom | Channel | If missed |
|---|---|---|---|---|
| A | Same working day, within 2 hours in business hours | The owner of that segment | The channel the lead used, then a call | Escalate to the founder the next morning |
| B | Within 2 working days | The segment owner | Email, one specific question | Move to nurture, dated |
| D | Within 1 working day | Whoever can answer the one question | Same channel | Re-score and route |
| C | No contact | — | — | Decline log only |

Publish the A-band promise on the website only if the business can keep it. A "we reply within 24
hours" line that is missed on a Saturday is worse than no line.

## Routing by segment, not by turn

| Rule | Why |
|---|---|
| Route by the factor that decides the fit, usually industry or size | A round-robin ignores fit and wastes the best rep on the worst lead |
| The founder sees A-band leads above the ticket threshold, and only those | Founder time is the scarcest resource in the business |
| One owner per lead, named | Shared ownership is no ownership |
| A reassignment is recorded with a reason | Otherwise the same lead is touched twice and answered once |
| Existing customers route to customer success, not to sales | A renewal is not a lead |
| Competitors, agencies and students route to a named person, not to a queue | They will otherwise consume a rep's morning |

## The first touch, in four lines

1. **Reference the specific thing they said.** Not "thanks for your enquiry" - "you mentioned 400
   invoices a month across three branches".
2. **Answer the question they asked**, if they asked one. If the answer is a price range, give the
   range.
3. **Ask the one question that most changes the band**, from the three-question list.
4. **Propose the next step with two specific times.** Not "let me know when works".

This is where `sales-outreach` takes over for anything longer than the first touch. This role writes
the first line and the question, not the sequence.

## The handover packet

When a lead moves from qualification to a human, hand over exactly this:

| Field | Why |
|---|---|
| Score, band and the two reasons for and one against | The human can disagree with a reason, not a number |
| What the lead actually said, verbatim | Paraphrase loses the detail that matters |
| The three questions, ranked | The call starts qualified instead of cold |
| Source channel and arrival timestamp | Decides urgency and the follow-up channel |
| What is unknown | Prevents the human asking what is already known |
| The disqualifiers checked and cleared | Saves the awkward question |

## Nurture, with a date

B is not "later". B is a dated reason: "revisit on 15 January, when their new outlet opens" or
"revisit when they post a role for an operations manager". A B with no date becomes a C in three
months with nobody deciding.

## Measuring the routing

| Metric | Definition | Target |
|---|---|---|
| Time to first touch, A band | Median hours from arrival to human contact | Under 2 in business hours |
| A-band contact rate | A leads touched within SLA over A leads | 95% |
| Band override rate | Overrides over scored leads | Under 10% - above it, the rubric is wrong |
| Decline rate by source | C-band share per channel | Feeds the marketing decision |
| Reply rate on first touch | Replies over first touches | The one number that improves the message |

## Anti-patterns

- **A queue with no owner.** The lead sits in a shared inbox and everyone assumes someone replied.
- **Routing the biggest lead to the busiest person.** Fit and availability are different axes; the
  founder decides when they conflict.
- **A 24-hour SLA for a business that works six days a week.** The SLA must describe the business as
  it is.
- **Following up on a channel the lead did not use.** A WhatsApp lead answered by email reads as
  spam.
- **Banding a lead A and then booking the call for next week.** The band is a promise about speed.
