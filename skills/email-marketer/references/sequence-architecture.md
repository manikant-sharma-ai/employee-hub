# Sequence architecture

A sequence is a decision tree with a schedule attached. The copy is the last thing written, not the first.

## Pick the sequence by the job

| Sequence | Trigger | Length | The one job |
|---|---|---|---|
| Welcome | Signup or first purchase | 3-5 emails, 10 days | Turn a signup into a first action |
| Nurture | Signed up, not bought | 4-6 emails, 3 weeks | Make the problem urgent enough to act on |
| Launch | A date | 3-4 emails, 7 days | Get the decision made by the deadline |
| Winback | No purchase in 90-180 days | 3 emails, 14 days | Find out if they are still there |
| Onboarding | Paid, not activated | 4 emails, 14 days | Get to the first real use |
| Re-permission | No opens in 180 days | 1-2 emails | Clean the list |

If the request does not fit one of these, it is a broadcast, not a sequence. A broadcast has no trigger and no exit, and it should be sent rarely.

## Timing that holds

| Gap | Works for | Fails when |
|---|---|---|
| Same day (0 + 4 hours) | Order confirmation, then a tip | Feels like two emails about nothing |
| Day 0, 2, 5, 9 | Welcome, nurture | Over 5 emails in 10 days reads as a campaign |
| Day 0, 3, 7 | Launch, three touches | A 4th touch in 7 days needs a real reason |
| Day 0, 7, 14 | Winback | Anything faster feels like harassment |

Rules:

- **Never two marketing emails in 24 hours** to the same person, from any sequence. Sequences collide, and the collision is what gets you marked as spam.
- **Suppress across sequences.** A buyer in the nurture sequence exits it. A person in winback who purchases exits it. If the platform cannot do this, do not run two at once.
- **One exit per sequence**, and it is the action, not the last email. "Buys" ends nurture; "replies" ends winback.

## The five-email welcome skeleton

| # | Day | Job | What it must contain |
|---|---|---|---|
| 1 | 0 | Deliver what was promised | The thing they signed up for, in the first screen |
| 2 | 2 | The one problem you solve | A specific situation, not a feature list |
| 3 | 5 | Proof | A real customer, a number, a before-and-after |
| 4 | 9 | The objection | Price, trust, delivery, or "will this work for me" |
| 5 | 14 | The ask | One clear next step, and an honest reason to take it now |

Email 1 is the one that decides the rest. A welcome email that says "thanks for subscribing, here is our story" wastes the highest-open email you will ever send.

## Anatomy of one email

1. **Subject and preview** - one idea between them (see `subject-lines-and-previews.md`).
2. **First line** - continues the subject. Never "Hi [First name], hope you're doing well".
3. **One idea**, in 80-150 words. Two ideas means two emails.
4. **One primary button**, above and below if the email is long. Same destination.
5. **Proof or specificity** - a number, a name, a date.
6. **Sign-off from a person**, with a reply-able address. Replies are the strongest engagement signal there is.
7. **Footer** - sender identity, physical address, unsubscribe. Non-negotiable.

## Anti-patterns

- A "drip" with no exit, running for a year.
- The same email to buyers and to people who have never heard of you.
- Four emails in five days because the launch was late.
- A welcome sequence that starts with "we are a company founded in 2019".
- Personalisation that is only the first name, used three times.
- Two sequences live at once with no suppression between them.
- A "last chance" email that is followed by another last chance.
