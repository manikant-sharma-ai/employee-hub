# Nudges: behaviour triggers, not a calendar

The difference between a nudge and a newsletter is whether the trigger is the customer's behaviour. A calendar
sequence sends the same message to someone who has already finished and someone who has not started.

## Trigger design

| Trigger | Fires when | Message job |
|---|---|---|
| `paid` | payment captured | Confirm, set expectation, ask for the one thing needed |
| `stalled:setup` | 72h since paid, setup incomplete | Name the specific blocker, offer the shortest unblock |
| `stalled:no-first-object` | setup done, no real object created | Offer to do the first one with them, or a template |
| `first-object` | first real object created | Reinforce, show the next step, ask for nothing else |
| `single-user` | 10 days in, one active user | Make the invite the ask, with the reason it helps them |
| `silent` | 14 days, no event | A short human question, not a feature list |
| `at-risk` | 21 days, milestone not reached | Escalate to the owner with the blocker named |

Every trigger is checked at send time, not at schedule time. That single engineering detail is the difference
between a sequence that works and one that insults the customer who already did the thing.

## Message shape

Four lines, in this order: the specific thing they have not done, why it matters to the job they bought, the one
link, and the way out.

```
You have not connected your bank feed yet, so the first reconciliation will be manual.
Connecting it takes about four minutes and then every payment matches itself.
[Connect the bank feed]
If you would rather do this on a call, reply "call" and I will set one up.
```

## Channel choice

| Channel | Use it for | Do not use it for |
|---|---|---|
| Email | Anything with a link or a document; the record of what was said | Anything urgent in a WhatsApp-first market |
| WhatsApp | Indian SMB and D2C customers, reminders, confirmations | Long explanations, anything needing a document trail |
| In-app | The step itself, the empty state, the next action | Anything that must survive the session |
| Call | High value, high complexity, a stalled decision | Self-serve plans, or as a substitute for a product fix |
| Nothing | When the customer is progressing | Filling a gap in the sequence |

One channel per step. The same message on three channels reads as panic.

## Stop rules, and telling the customer

The sequence ends on the first of: activation, a reply, an opt-out, or day 30. Say so in the first message -
*"three short notes over the next month, then I will leave you alone unless you ask"* - because a stated stop rule
raises response rates and a hidden one destroys trust when it fires anyway.

## Measuring a nudge

- **Sent, delivered, opened** are not outcomes. Report them, do not celebrate them.
- **Step completion within 48h of the nudge**, against a matched group who did not receive it, is the outcome.
- **Incrementality needs a holdout.** With fewer than a few hundred accounts a month, hold out a fifth and accept
  the noise; without a holdout, label the result *unattributed*.
- **Watch for the annoyed.** Replies, unsubscribes and support tickets mentioning the messages. A nudge that lifts
  activation by two points and generates ten angry replies is a net loss in a small business.

## Anti-patterns

- Sending "getting started?" to an account that sent its fifth invoice this morning.
- A discount in message three, which teaches every future customer to stall for a month.
- Personalisation that names the wrong person - "Hi there" is better than the previous owner's name.
- A sequence longer than the journey. Four good triggers beat eleven scheduled emails.
