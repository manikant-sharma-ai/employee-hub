# Activation milestones: finding first value in the data

The milestone is the whole role. Get it wrong and every downstream number - activation rate, time to value, the
handover score - measures the wrong thing, confidently.

## Why the obvious milestone is usually wrong

| The tempting milestone | Why it fails |
|---|---|
| "Completed setup" | Setup is a prerequisite, not a value moment; a customer can finish it and still have no use for the product |
| "Logged in three times" | Measures curiosity, not value; correlates with churn as often as with retention |
| "Attended the kickoff call" | Measures the vendor's effort, not the customer's outcome |
| "Imported data" | Often the hardest step and the one that gets abandoned - it is the blocker, not the goal |
| "Created an account" | True of every customer including the ones who left the same week |

A milestone must be an action the *customer* takes that produces the outcome they bought.

## The survivor test

The only defensible way to choose one, in five steps.

1. **Take two cohorts** - customers still active at month three (or renewed), and customers who churned before it.
   Six months of history is enough; twelve is better.
2. **Take their first seven days of events** - the same event names for both cohorts, at the same grain.
3. **Compute the gap per event** - share of survivors who did it in week one, minus share of churners who did.
4. **Rank by three filters** - the biggest gap, the earliest median occurrence, and a mechanism you can explain in
   one sentence. An event with a big gap and no mechanism is a coincidence that will not replicate.
5. **State the rejected alternatives.** "We chose `sent 5 invoices` over `imported 50 contacts` because the latter
   is completed by 71% of churners too, and over `invited a colleague` because its median day is 19 and it is a
   consequence of the first, not a cause."

## Setting the threshold

A milestone with no number drifts. Specify four things:

| Element | Example | Why |
|---|---|---|
| The action | `created and sent an invoice` | Named in the product's own event vocabulary |
| The count | at least 3 | One can be a test; three is a habit |
| The window | within 21 days of first payment | Tied to the renewal cycle, not to a round number |
| The exclusion | excluding test/demo accounts and internal users | Otherwise the rate flatters itself |

Write it as one sentence a support agent could apply: *"Activated means the account sent three invoices within 21
days of payment, not counting test invoices or staff accounts."*

## When there is no event data

The common case for a small business. Three fallbacks, in order of honesty:

1. **The product's own database or export** - even a weekly CSV of activity beats nothing. Ask for the definition
   of each event, not a dashboard, because definitions drift.
2. **A proxy from systems that do exist** - the helpdesk (no setup tickets in week one), billing (first repeat
   charge), the CRM (stage moved to `live`), WhatsApp (first real question asked). Label it a proxy in every
   report.
3. **A ten-account manual audit** - read the last ten accounts' first two weeks by hand with the account owner.
   It is not a rate, it is a hypothesis, and it is labelled as one until the events exist.

Never invent the milestone from what the product *should* be used for. The gap between the intended use and the
actual value moment is the most common reason onboarding programmes fail politely.

## Keeping the milestone honest

- **Re-test it every quarter** against the newest cohort. Activation that stops predicting renewal is measuring
  enthusiasm, not value.
- **Watch for Goodhart** - once a milestone is targeted, the team will optimise the event (seed a template,
  pre-fill a record). If the event can be produced without the customer doing the work, it is the wrong event.
- **Version it.** `activated-v2` with a date, and restate the trend on both definitions rather than splicing them.
- **Keep two secondary signals** - depth (how many of the product's core objects they created) and breadth (how
  many people in the account are active). A single milestone can be hit by one enthusiast in a team of ten, and
  that account still churns.

## Anti-patterns

- Choosing the milestone in a workshop with the sales team, who describe the demo rather than the usage.
- Using a milestone that requires a human to mark it done, which makes it a measure of the vendor's calendar.
- Setting activation at "first value" and then reporting a rate computed on all signups including trials that
  never paid, which quietly redefines the denominator.
- Adding a second milestone when the first one is inconvenient, so the rate can be reported on whichever is
  higher this month.
