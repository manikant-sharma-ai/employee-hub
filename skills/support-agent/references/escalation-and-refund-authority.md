# Escalation and refund authority

Support fails in two directions: a person who cannot decide keeps the customer waiting, and a person who decides too freely gives away money the business did not plan to. This file sets the line.

## Authority ladder

Fill these numbers in with the business. Until they are filled in, treat every monetary commitment as needing approval.

| Action | Who may decide | Limit |
|---|---|---|
| Replacement for damaged or wrong item | Support agent | Cost of goods, no approval |
| Free return pickup | Support agent | Standard pickup rate |
| Partial refund | Support agent | Up to ₹<X> or <Y>% |
| Full refund within policy window | Support agent | Any amount within the window |
| Full refund outside the window | <owner> | Case by case, in writing |
| Goodwill credit or coupon | Support agent | Up to ₹<X> |
| Waiving shipping on a future order | Support agent | Yes |
| Any refund after 60 days | <owner> | Rarely |
| Anything above ₹<X> total | <owner> | Always in writing |

**The default when the ladder is empty:** you may offer the remedy the written policy already promises. Everything else is a question to the owner, and the customer gets a straight answer about when they will hear.

## Escalate immediately - no attempt to resolve first

| Trigger | Why | To whom |
|---|---|---|
| Words "lawyer", "legal notice", "consumer court", "suo motu" | Legal exposure; anything you write can be evidence | Founder, today |
| Product injury, allergic reaction, electric shock, fire | Safety and liability | Founder, within the hour |
| Data breach, someone seeing another customer's data | Regulatory (DPDP) and reputational | Founder and technical owner, within the hour |
| Threat of self-harm or harm to others | Human safety outranks the commercial issue | Founder or manager, immediately |
| Journalist, influencer with reach, regulator, or a marketplace's own dispute team | Escalation is asymmetric | Founder, today |
| Chargeback or bank dispute raised | Timelines are legal, not commercial | Accounts owner, today |
| Abuse or threat directed at staff | Duty of care to the team | Manager, immediately |
| A demand you suspect is fraud (new account, high value, urgent) | Money at risk | Accounts owner, before any action |

## Escalating well

A handoff is not "please look into this". It has to make the next person's first action obvious.

```
ESCALATION - S1/S2
Customer:      <name, contact, channel>
Order/account: <id, date, amount>
Issue:         <one sentence>
What I checked: <systems and facts, with timestamps>
What I already told them: <verbatim>
What they want: <their words>
What I need from you: <the specific decision>
Their deadline: <when they expect to hear>
Risk if we miss it: <public post, legal, churn, none>
```

Rule: **the customer is told it has been escalated, by name of the role, with a time they will hear.** An escalation the customer does not know about is a ticket that has disappeared.

## Refunds: the four questions before you offer one

1. **Is it in policy?** If yes, do it now and do not make them argue.
2. **Is it fair even if out of policy?** A customer who received a broken product on day 32 should get a refund. Say so to the owner with the reason.
3. **What is the cost of refusing?** A ₹2,000 refund against a public complaint, a chargeback fee and a lost customer is usually the cheaper option - but that is the owner's call, not yours.
4. **Can I state it without inventing a number?** If the amount or method is unclear, ask before you promise.

## Things that are never a support decision

- Changing the refund or returns policy.
- Admitting legal liability, or saying "we are responsible for the damage".
- Agreeing to pay medical costs, compensation or damages.
- Confirming whether a product is safe for a specific medical condition.
- Deleting or editing a customer's review.
- Issuing a refund to a different account than the one that paid, without the owner's written approval - this is the standard fraud pattern.

## Escalation hygiene

- **One owner at a time.** Reassign explicitly; do not add a second name.
- **The escalation note lives in the ticket**, not in a DM. If it is only in chat, it will be lost.
- **Close the loop with the customer even when the answer is no.** "The answer is no, and here is why, and here is what I can still do" ends more tickets than a delay does.
- **Write the outcome into `notes/decisions.md`** when an exception is granted. Next month the same case arrives, and the answer should be consistent.

## Anti-patterns

- Escalating without having checked the record. The owner re-does your work and the customer waits twice.
- Escalating everything. If the owner receives half the inbox, nobody triages.
- Promising the customer an outcome you are escalating for. "I am sure we can refund you" is a commitment you just made on someone else's behalf.
- Sitting on an S1 overnight because it arrived at 7pm.
- Quietly granting an exception and not recording it, so the next agent refuses the same request.
- Telling a customer "my manager said no" without a reason.
