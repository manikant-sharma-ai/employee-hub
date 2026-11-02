# Scope and saying no

Scope does not creep by itself. It creeps because someone says yes to a small thing without naming what it displaces. This file is how to say yes, no, or later, in a way that keeps the relationship and the date.

## The cut list, written before the build

Every plan gets three columns:

| In v1 | Deferred, with a trigger | Not doing, with a reason |
|---|---|---|
| The smallest thing that changes behaviour | "If more than 30% of orders need it, build in v2" | "Against the strategy: we are not building a CRM" |

The third column is the most valuable and the least written. It is what stops the same conversation in eight weeks.

## The five ways scope arrives

| Arrival | The move |
|---|---|
| "While we're in there..." | "That is a separate story; it is not in this release." |
| A stakeholder's must-have the day before launch | "Adding it moves the date by X days. Do you want that trade?" |
| A customer's request routed through sales | Route it to the tracker with a score, not into the sprint |
| An engineer's good idea mid-build | Park it; the release is not the place for a new idea |
| Your own good idea | The most dangerous one. Write it down and score it next cycle |

## The scripts

**The trade, not the refusal:**
> "Yes, and it moves the date by four days or displaces the export. Which would you rather have on the 20th?"

**The trigger:**
> "Not in v1. If more than a third of users hit it in the first month, we build it in the next cycle - I'll bring you the number."

**The strategy no:**
> "This is a good idea and it is not what we are doing this year. We are the fastest way to invoice, not a full accounting suite. If that changes, this is the first thing I'd revisit."

**The evidence ask:**
> "Before I size it - can you get me three customers who hit this in the last month? If it is real, it will outscore two things on the list."

**The honest no on capacity:**
> "Two engineers, six weeks. Three of these fit. Here are the three, and here is what falls out."

## Protecting the date

- **A scope freeze at 80% of the time**, not at the end. The last 20% is for the things that always appear: permissions, migration, content, edge cases.
- **The date moves or the scope moves, never both silently.** Say which one, to whom, on the day it is known.
- **Buffer in the estimate, not in the promise.** Estimate with the buffer; promise the date you believe.
- **One owner per dependency.** "The payment gateway sandbox is being arranged" with no name is a dependency that will slip.

## When to kill a thing

Kill it, rather than defend it, when:

- The metric it was meant to move has not been defined.
- It has been "in progress" for two cycles with nothing shipped.
- The users it was for have stopped asking, or stopped existing.
- The cost of finishing exceeds the value of the outcome, and saying so is cheaper than finishing it.

Killing work is a decision with a note, not a quiet abandonment. Write what was learned; that is the return on the spend.

## Anti-patterns

- **"We'll see how it goes"** on a scope change. That is a yes with no trade.
- **Absorbing the extra work and telling the team to "just make it work"**. It produces a late release and a tired team.
- **Saying no to the person rather than to the item.**
- **A date promised to a customer before the team has estimated.** It converts an estimate into a commitment made by someone else.
- **Silent de-scoping.** Shipping less than promised without saying so is worse than shipping late.
- **A backlog that grows faster than it is closed**, treated as a plan rather than a symptom.
