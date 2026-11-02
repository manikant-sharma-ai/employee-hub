# PRD and specs

A PRD exists to make one thing true: everyone who builds, sells and supports this feature understands the same problem and the same boundary. Anything in it that does not serve that is length.

## Size the document to the risk

| Change | Document | Length |
|---|---|---|
| Copy change, small fix, a bug with a clear cause | Ticket with acceptance criteria | 10 lines |
| Improvement to an existing flow | One-page brief | 1 page |
| New flow, new integration, new segment | Full PRD | 3-5 pages |
| Platform change, pricing change, anything touching money or data | Full PRD plus a rollback plan | 5+ pages |

A 12-page PRD for a button is a way of avoiding the decision.

## The sections that earn their place

| Section | Content | Why it exists |
|---|---|---|
| Problem | Who, what they do today, what it costs, how often | The only section that justifies the rest |
| Goal | One number, one date | Makes the release judgeable |
| Users | The one or two segments affected, and their current workaround | Prevents designing for everyone |
| Scope | What is in v1 | The contract with the team |
| Non-goals | What is explicitly out | Prevents the same rework every sprint |
| Requirements | Numbered, each with acceptance criteria | The buildable part |
| Flows and states | Happy path, empty, loading, error, permission-denied | Where most rework comes from |
| Dependencies | Other teams, vendors, approvals, data | The usual cause of slippage |
| Risks | What could make this fail, and the mitigation | Forces the honest conversation early |
| Measurement | The metric, the baseline, the read dates | Prevents an unmeasurable launch |
| Open questions | Each with an owner and a date | A PRD with no open questions is a PRD nobody read |

## Requirements that can be built

| Weak | Why | Strong |
|---|---|---|
| "Users should be able to filter orders" | No criteria, no boundary | "R-04. On the orders list, the user can filter by status (all, pending, shipped, delivered, cancelled) and by date range. Filters persist for the session. Empty result shows 'No orders match' with a clear-filters link." |
| "Make it fast" | Not measurable | "R-07. The orders list renders in under 1.5s at p95 on a 4G connection with 500 orders." |
| "Handle errors gracefully" | Unfalsifiable | "R-09. If the payment gateway times out, the user sees 'Payment not completed - no money has been deducted' with a retry button, and the order stays in pending for 30 minutes." |

Every requirement names: the actor, the action, the boundary, and what happens at the edge.

## Flows and states: the section people skip

For each screen or step, list: default, empty, loading, error, partial failure, permission denied, and the slow-network case. Then answer:

- What does the user see if there is no data at all - a new account, a new month?
- What if the action succeeds but the confirmation fails?
- What if they tap twice?
- What if they have no permission - hide the button or show a disabled one with a reason?
- What if they go back mid-flow - is the draft saved?

These six questions produce more of the actual work than the happy path does.

## Writing for three readers

The same PRD is read by an engineer, a designer and whoever supports the customer:

- **Engineer** needs: requirements, states, edge cases, dependencies, data.
- **Designer** needs: users, flows, states, what happens when it fails.
- **Support and sales** need: what changes for the customer, what to say, when it is live.

If the document only serves the first, add a short "what changes for the customer" paragraph at the top. It costs four lines and prevents three support tickets.

## Anti-patterns

- **A PRD that is a list of features** with no problem statement. It will be built and nobody will use it.
- **Screenshots of a competitor's product as the requirement.** That is a copy of a solution to a problem you have not described.
- **Acceptance criteria written after the build**, to match what was built.
- **"Phase 2" with no trigger.** Phase 2 never happens; if it matters, it is phase 1.
- **A document with 40 requirements and no non-goals.** Everything is in scope, so nothing is prioritised.
- **Open questions with no owner**, which become assumptions made by whoever is building.
