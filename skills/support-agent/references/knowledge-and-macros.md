# Knowledge and macros

Every repeat question is a design failure somewhere upstream - a confusing page, a missing article, an unclear policy. This file is how support stops answering the same thing five hundred times and starts removing the cause.

## The three uses of a macro

| Use | Good macro | Bad macro |
|---|---|---|
| Speed | The skeleton of a reply with the facts filled in | The whole reply, sent unchanged |
| Consistency | The same policy stated the same way by everyone | The same words to a customer who described a different problem |
| Training | Shows a new agent what a good answer looks like | Becomes the only thing anyone can write |

A macro is a skeleton. The first line must always be written fresh, from the customer's own words.

## The macro library worth building

Build these twelve before anything else. Each is a paragraph, not a page.

| Macro | Covers |
|---|---|
| Order status - on time | Confirms the date, gives tracking |
| Order status - delayed | Last scan, trace raised, next check date |
| Wrong item shipped | Owns the error, replacement date |
| Damaged in transit | Photo request (only if needed), replacement or refund |
| Refund initiated | Amount, method, timeline by method |
| Refund not received | Gateway reference, chase commitment |
| Payment failed, money held | Reversal raised, timeline, no double payment |
| Return how-to | Steps, pickup booking, what to keep in the box |
| Out of policy, exception offered | What is not possible, what is, how to ask |
| Warranty claim | Period, cover, service point, turnaround |
| Pre-sale product question | Answer, honest limitation, next step |
| Escalation acknowledgement | Named role, what happens, when they hear |

## Writing a macro that survives

1. **Lead with the variable.** `Your order #{{order_id}} was due on {{due_date}}...` - if the first sentence has no variable, it will be sent wrong.
2. **Name the placeholders explicitly** so nobody forgets one: `{{amount}}`, `{{date}}`, `{{courier}}`, `{{agent_name}}`.
3. **No policy number without the sentence explaining it.** "Per clause 4.2" helps nobody.
4. **State the timeline in the customer's units** - "5-7 working days for cards", not "T+5".
5. **Include the next step, always.** A macro without a next step is a holding message.
6. **Date-stamp the macro.** Policies change; a stale macro states a policy the business no longer honours.

## Turning repeats into fixes

The loop, run weekly:

```
Count the repeats  →  find the cause  →  fix the cause  →  measure the drop
```

| Repeat question | Usual cause | Fix |
|---|---|---|
| "Where is my order?" | No proactive tracking message | Send a dispatch message with tracking, unprompted |
| "What is your return policy?" | Policy is on page 4 of the footer | Put the three-line policy on the product page |
| "Do you deliver to <city>?" | Pincode check is hidden | Show it on the product page |
| "How do I use this?" | No instructions in the box | One card in the box, one article |
| "Why was I charged this?" | Invoice unclear | Itemise the invoice |
| "Is this the right size?" | No size chart, or a bad one | Size chart with measurements, not S/M/L |

**A help article that removes ten tickets a month is worth more than any macro.** Write it, link it in the reply, and measure whether the question comes back.

## What a good help article looks like

- **Title in the customer's words**, not the internal name. "Why was I charged twice?" not "Duplicate authorisation handling".
- **The answer in the first two lines.** No preamble.
- **Steps numbered**, one action each, with what they will see.
- **A screenshot** where the interface is the confusion.
- **What to do if it still does not work** - the escalation, with a link.
- **Updated date.** A stale article generates tickets of its own.

## Handing over knowledge

- **The decision log is the memory.** Every exception granted, with the reason, so the answer is consistent next month. See `notes/decisions.md`.
- **The product team should hear the top three complaints monthly.** Support sees the failure first; that is the most valuable thing it can give away.
- **Record the vocabulary customers use.** If they call it a "cover" and the site calls it a "sleeve", the search fails and the ticket is created. Feed that back to whoever writes the site.

## Anti-patterns

- A macro library of 200 entries that nobody can find.
- Macros that begin with "Thank you for reaching out to us" and end with "your satisfaction is important to us", with nothing in between.
- Sending a macro whose placeholder was left in, or filled with the wrong order.
- Writing the article and never linking it from the reply that generated it.
- Fixing the article but not the page that caused the confusion.
- Measuring macro usage instead of repeat-contact rate. Usage is not the goal; fewer questions is.
