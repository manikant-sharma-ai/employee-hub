# Pipeline hygiene: the next-step discipline

A pipeline is a set of promises with dates. This file keeps the promises visible and kills the ones that are not
real.

## The six fields that make a pipeline work

| Field | Why it exists | Bad version |
|---|---|---|
| Deal ID | The only identifier that should appear in a report | Customer name in the deal title |
| Stage | What the buyer is deciding | Nine stages with overlapping meanings |
| Value | Rupee value at stake, so work can be ranked | A number nobody has validated since creation |
| Last activity date | The clock that starts the stale list | Auto-updated by an email open |
| Next step, in words | The specific action, not "follow up" | "Follow up" |
| Next-step date | The commitment | Blank, which is the most common state |

If the CRM cannot hold the last two, a Google Sheet joined on deal ID can - but only as a stopgap, because a
sheet nobody opens is a pipeline nobody runs.

## The stale audit

Run weekly, in this order:

1. **Past their next-step date.** These are the week's work, ranked by value × days overdue.
2. **No next step at all.** These are not deals; they are records. Give each one a next step, a date, or a lost
   reason in the same session.
3. **No activity in 30 days but a future next-step date.** Check the date is real and the buyer agreed to it.
4. **Stage age.** Days in the current stage, against the normal for that stage. A deal in "negotiation" for 60
   days is not negotiating.
5. **Value with no quote attached.** A deal worth ₹15 lakh with nothing sent is a wish.

Report counts and rupees, not percentages alone: "11 deals, ₹42 lakh, past their next-step date, oldest 63 days."

## Stage definitions that survive a team

Write each stage as three lines: what the buyer has done, what has to be true to move, who decides the move.

| Stage | The buyer has | To move | Decides |
|---|---|---|---|
| Qualified | Confirmed a need and a timeline | A conversation with the decision-maker | Owner |
| Solution agreed | Agreed what the offer is | A quote sent | Owner |
| Quoted | Received a price | Their internal decision | Buyer |
| Negotiating | Made a counter or asked for terms | Terms accepted in writing | Owner + founder |
| Won | Paid or signed | - | Owner |

Any stage that a deal can enter without the buyer doing something is not a stage, it is a hope.

## Lost reasons that teach something

Use six codes, and require one on every closed-lost deal:

| Code | Meaning | What it changes |
|---|---|---|
| `no-decision` | Silence past the stop rule | The cadence, or the qualification |
| `price` | Lost on price against a named alternative | The pricing conversation, not the discount |
| `timing` | Real, but later | The re-contact date and the nurture list |
| `no-fit` | Did not actually need it | The qualification questions |
| `competitor` | Chose someone else | What the competitor offered that we did not |
| `internal` | Their budget or sponsor disappeared | Nothing - and it should not be blamed on the sales team |

`no-decision` is usually the largest code in a small business and the least examined. It is not a market problem;
it is a follow-up problem, and this role is the one that can fix it.

## Handover fields

When a deal moves to another employee, five things travel with it: the requirement in the buyer's words, the
objection, the price already discussed, the decision date, and the person who signs. Without those, the buyer
repeats themselves and the deal loses a week.

| Handoff | Goes to | What must travel |
|---|---|---|
| Technical scoping or POC | `sales-engineer` | The requirement, the environment, the timeline |
| Quote or revised quote | `quote-generator` | Configuration, price already discussed, validity needed |
| Term negotiation | `contract-negotiator` | The terms in play and what the buyer pushed back on |
| Renewal or expansion | `customer-success` | Usage, history, the last conversation |
| Won | `finance-ops` / `bookkeeper` | The agreed price, terms and delivery date |

## Weekly review, twenty minutes

1. Read the stale list aloud, deal by deal, with the owner present.
2. For each: a touch this week, a date the buyer gave, or lost with a code. No fourth option.
3. Count what changed since last week: touched, moved, lost, added.
4. Pick one cadence change for next week - an interval, a channel, a message - and write it in `learnings.md`.

## Anti-patterns

- A pipeline reviewed by scrolling, not by sorting on the next-step date.
- "Next step: follow up" - an action with no content and no date.
- Deals marked won when the PO is promised rather than received.
- Deleting dead deals to make the pipeline look clean; the reason code is the value.
- Letting the CRM auto-log email opens as activity, so nothing ever looks stale.
- A stage called "proposal sent" and another called "quote given" that mean the same thing.
- Reporting pipeline value without the age distribution: ₹2 crore of deals that are all 90 days old is not a
  pipeline, it is an archive.
