# Risk in money: turning clauses into rupees

A founder cannot weigh "unfavourable" against "acceptable". They can weigh ₹18 lakh against ₹2 lakh.

## The five exposures to price

| Exposure | How to compute it | What to compare it to |
|---|---|---|
| Liability cap | Cap amount, or 12 months of fees if uncapped | The contract value and the worst realistic claim |
| Indemnity | The claim the clause covers × the probability of it arising | The margin on the deal |
| Committed spend | Monthly fee × committed months, including auto-renewal | The cash the business will have in that period |
| Payment terms | Invoice value × days beyond your cash cycle × cost of borrowing | The margin on the deal |
| SLA credits | Maximum credit % × monthly fee × likely breach months | The fee, since credits are a refund of the same money |

## Worked examples

**Uncapped liability.** A ₹12 lakh annual SaaS contract, unlimited liability for data loss. The realistic worst
case is a breach affecting the client's customers. If that is ₹40 lakh, the contract is a ₹40 lakh bet for a ₹12
lakh fee. Ask for a cap at 12 months of fees; if refused, price the difference into the fee or decline.

**90-day payment terms.** ₹8 lakh a month invoiced, paid at 90 days. That is ₹24 lakh permanently financed at
whatever the business's working capital costs - at 12% a year, ₹2.9 lakh of annual cost, straight off the margin.

**Auto-renewal with a 60-day window.** A three-year ₹5 lakh a year contract that renews unless notice is given 60
days before. Missing the window commits ₹15 lakh. The clause is worth nothing to read and everything to diarise.

**Termination for convenience, one-sided.** The client can leave in 30 days; the business cannot. The exposure is
the mobilisation cost - hiring, tooling, dedicated staff - amortised over a contract that may end in month two.
Price it as a recovery period: "fees for 60 days after notice" is the standard ask.

**SLA credits capped at 10% of monthly fees.** On ₹4 lakh a month, the maximum compensation for a month of
downtime is ₹40,000. If the client's own loss from an outage is ₹10 lakh, the clause is a rounding error and the
real question is the liability cap, not the SLA.

## Ranking, and the one number that matters

Rank deviations by rupee exposure, then report:

- **Total quantified exposure** - the sum, which is usually dominated by one clause.
- **The largest single exposure** - the clause to argue about.
- **Exposure as a share of contract value** - anything above 100% needs the founder's decision, not a redline.
- **Exposure as a share of a year's gross margin** - the number that decides whether the deal is worth having.

## When it cannot be priced

Some clauses resist arithmetic: a non-compete, an exclusivity, an audit right, a most-favoured-customer clause.
Price them as **optionality lost** - "exclusivity for 12 months in this segment costs us the two other
conversations we are in, worth ₹x of pipeline". State the assumption; a stated assumption is a decision aid, an
unstated one is a guess.

## Anti-patterns

- Ranking by clause importance rather than by exposure, so the liability cap is buried under an NDA term.
- Pricing the cap but not the indemnity that sits beside it and does the same job.
- Ignoring the committed spend because "we will probably renegotiate" - the contract is the default, not the
  intention.
- A risk total with no denominator, which sounds alarming and decides nothing.

## Presenting it so the decision gets made

Three numbers, one table, one sentence. A founder who has to read a paragraph to find the exposure will sign the
document and hope.

| What to show | Why it is the one that matters |
|---|---|
| The largest single exposure, in rupees | It is usually 80% of the total and it is the only clause worth arguing |
| Total quantified exposure against contract value | Says whether the deal is a bet or a trade |
| The cost of the terms the other side will not move | Turns "non-negotiable paper" into a price, which is a decision |

Then the sentence: *"On a ₹12 lakh contract we would be accepting ₹40 lakh of unbounded exposure for a ₹3 lakh
margin; I recommend we ask for the 12-month cap and walk if it is refused."* That is a decision aid. A clause
list is not.

## The exposures people forget to price

- **The notice period on the business's own exit**, which is the cost of staying in a deal that has stopped working.
- **The audit right**, which is unbilled staff time twice a year and a discovery risk in the hands of a competitor.
- **The most-favoured-customer clause**, which caps every future price to the lowest one ever given.
- **The reference and case-study obligation**, which spends a customer relationship the sales team was saving.
- **The data deletion obligation on exit**, which is real engineering time if the data sits in six systems.
