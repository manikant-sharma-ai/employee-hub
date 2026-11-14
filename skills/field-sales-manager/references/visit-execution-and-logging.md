# Visit execution and logging

The visit is the unit of field cost. This file is what happens in it, and what must be true when the rep walks
out.

## The retail call, in order

| Step | What the rep does | Time | Why it is in this order |
|---|---|---|---|
| 1 | Check the shop's stock and share of shelf before speaking | 3 min | The conversation starts from what is on the shelf, not from a pitch |
| 2 | Greet the owner by name, and the counter staff too | 1 min | In India the counter staff decides whether the product is recommended |
| 3 | Report what sold since the last visit, in units | 2 min | Proof, not opinion |
| 4 | Merchandise: front-face, clean, place the POS material | 3 min | The cheapest sales intervention available |
| 5 | The order: what is short, what is new, what is the scheme | 5 min | Order booking, in the outlet's language |
| 6 | Collect: payment, cheque, or confirm the credit position | 2 min | Field collection is where the working capital is |
| 7 | Log the visit before leaving the shop | 2 min | Logged later is logged wrong |

A call under five minutes is a delivery. A call over twenty is a relationship that is not producing an order.

## The six fields of a WhatsApp log

When there is no app, this is the whole system, one message per visit, in the rep's own shorthand:

```
OUTLET-ID | ORDER-VALUE | SKU-LINES | STOCK-DAYS | SHELF-SHARE | NOTE
```

Example: `PUN-0412 | 8400 | 3 | 22 | 40% | asked for 10% scheme on 500ml, competitor at 5%`

Six fields, one line, no app to install. It is parseable into a sheet in ten minutes a day, and it gives you
coverage, drop size, stock cover, share of shelf and the objection - the five things a monthly report needs.

## What an app should capture, if there is one

| Field | Required | Why |
|---|---|---|
| Outlet ID and timestamp | Yes | Coverage and the truth of the visit |
| Geo-tag | Yes | The only defence against a proxy visit |
| Order value and lines | Yes | Drop size and mix |
| Stock on shelf (days or units) | Yes | Stock cover, and the risk of a return |
| Share of shelf | Yes | The leading indicator of secondary sales |
| Competitor activity | Optional | The market read nobody else has |
| Photo of the shelf | Optional | Evidence, and a coaching tool |
| Reason for no order | Required if zero | The only route to fixing a dead outlet |

## The no-order reasons, and what each means

| Reason | Reading | Action |
|---|---|---|
| Has stock | Frequency too high, or last order too large | Adjust the frequency, or the order size |
| Price | A real objection, or a negotiation opening | Route to `pricing-analyst`; do not discount on the beat |
| Credit not settled | The distributor's or the outlet's cash problem | Freeze new credit, escalate, do not sell more |
| Competitor scheme | A trade promotion is running | Report it; the response is a decision, not a rep's discount |
| Space | No shelf space | Merchandising and a slower-moving SKU swap |
| Owner absent | A route or timing problem | Change the beat day, not the rep's effort |
| Not interested | The outlet is the wrong fit | Reclassify to dormant or do-not-visit |

A beat with a high no-order rate and no recorded reason is a beat nobody is learning from.

## Coaching from the log, not from the number

| Signal | What it usually means | The coaching move |
|---|---|---|
| High coverage, low drop size | Calls are too short, or the order ask is weak | Role-play the order step |
| Low coverage, high drop size | Few big outlets, C outlets neglected | Rebuild the cluster |
| Good coverage, no new outlets | The rep is comfortable | Add two new outlets to the beat, with time |
| Zero orders in a cluster | A distributor stock or credit problem | Fix the supply before judging the rep |
| High shelf share, low orders | The outlet sells but does not reorder | The order conversation is missing |

## The daily ten minutes

1. Every rep sends the log by 7pm, in the six-field format.
2. The manager replies to two things only: one visit that was well done, one that needs a question.
3. The day's coverage and orders are entered in one sheet, by one person, same time every day.
4. Anything with a stock-out, a credit issue or a competitor scheme is flagged the same evening.
5. The next morning's beat is confirmed against market days and holidays.

The cadence matters more than the tool. A WhatsApp group that gets a reply every evening beats an app that
nobody opens.

## Anti-patterns

- **Logging at the end of the day from memory.** Coverage becomes approximate and drop size becomes round numbers.
- **A 25-field app form.** The rep fills the first four and taps through the rest.
- **Photo-only reporting.** A shelf photo proves presence, not an order, a stock position or a share of shelf.
- **A proxy visit.** The geo-tag and the outlet-level order history are the only defences; use both.
- **Judging a rep on orders alone when the distributor is out of stock.** The supply problem is upstream of the
  call, and the rep pays for it.
