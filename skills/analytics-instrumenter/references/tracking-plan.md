# The tracking plan

The tracking plan is the contract between the person who wants the number and the
person who writes the code. It lives in the repo or the tracker, versioned, not in
a chat thread.

## The row

| Column | Content | Example |
|---|---|---|
| Event name | Canonical, snake_case | `checkout_started` |
| Description | What it means, in one line | User reached the payment screen with at least one item |
| Trigger | The exact moment it fires | On screen mount, after cart validation passes |
| Platforms | Web / iOS / Android / server | web, android, ios |
| Properties | Name, type, required, allowed values | `cart_value_inr` number required; `coupon_applied` boolean optional |
| Owner | The person accountable for it working | <name> |
| Question served | Which question in the questions table | Q2: where checkout loses people |
| Status | Planned / in build / live / QA-passed / retired | live |
| Notes | Dedup rule, edge case | Fires once per session, not per re-render |

## The questions table comes first

| # | Question | Who asks | How often | Decision it changes |
|---|---|---|---|---|
| Q1 | Where do we lose signups? | Founder | weekly | Which screen to fix next |
| Q2 | Which channel brings paying customers? | Marketing | monthly | Where the budget goes |
| Q3 | Does the new pricing page convert better? | Product | at launch | Keep or revert |

Every event in the plan names a Q number. An event with no Q is deleted in review.

## Implementation notes that prevent the usual bugs

- **Fire on the event, not the render.** A React re-render or a back-navigation
  fires the event again; specify once-per-action.
- **Server-side for money.** `order_paid` and `refund_issued` come from the backend,
  keyed to the order ID, so ad blockers and iOS limits cannot delete revenue.
- **Identify before events.** Set the user ID at login; anonymous events before
  identification produce a funnel with a step missing.
- **UTM on every campaign link**, captured at landing and persisted to signup, or
  attribution stops at the session.
- **Deduplicate by a key.** Send an `event_id` or an order ID and dedupe in the
  warehouse; mobile retries and network flakiness produce duplicates.
- **One place for consent.** The tag manager should not fire marketing events before
  consent, and the check should be in one component, not twelve.

## The release gate

Write this into the ticket, not into a conversation:

> This release is not done until: every planned event fires once in the debug view,
> the required properties are present, `order_paid` reconciles to the gateway within
> 2% for a day, and the funnel chart renders. QA evidence pasted in the ticket.

## Versioning the plan

| Field | Rule |
|---|---|
| Version | `v1`, `v2` at the top, with the date |
| Changelog | One line per change: added, renamed, retired, and the date |
| Migration | Any rename states the dual-fire window and the retirement date |
| Owner | One named owner for the whole plan; per-event owners beneath |

## Handing it to the builder

Deliver three things, not one:

1. **The plan** as a sheet or a CSV, one row per event.
2. **The acceptance criteria** as a checklist the developer can close.
3. **A 20-minute walkthrough**, recorded, because the trigger column is where the
   misunderstanding always is.

## Anti-patterns

- A plan in a PDF, so the implementation drifts the day after it is shared.
- Events with no owner, so nobody notices the day they stop firing.
- A trigger described as "when the user clicks pay" without saying which pay button
  on which screen.
- Properties marked "required" that the code cannot always supply.
- A plan delivered after the sprint started.
- No changelog, so a renamed event silently breaks last quarter's comparison.
