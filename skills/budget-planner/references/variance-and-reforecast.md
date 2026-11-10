# Variance and reforecast

A variance is a question, not an answer. The job is to turn "12% over" into a cause, an
owner and an action.

## The decomposition

For revenue, split the gap three ways before anyone speaks:

```
total gap    = actual revenue - plan revenue
price effect = (actual price - plan price) x actual volume
volume effect= (actual volume - plan volume) x plan price
residual     = total gap - price effect - volume effect   (mix, discount, returns)
```

A negative price effect with a positive volume effect is a discount-led quarter: the
business bought revenue. That is a decision, and it should be named as one. Run the
arithmetic with `scripts/budget_roll.py --demo` rather than by hand; the residual is the
part nobody explains, and it is usually mix.

For cost, classify the gap before you explain it:

| Cause | Test | What it means |
|---|---|---|
| Volume | the cost moves with units at the planned rate | not a problem, if the revenue came too |
| Price or rate | the rate per unit or per hour rose | renegotiate, or re-base |
| Mix | the cheap product sold less than planned | a margin conversation, not a cost one |
| Step | a hire, a site or a contract started | planned or unplanned - say which |
| Timing | the invoice landed a month later | not a saving; it will arrive |
| One-off | a legal fee, a repair, a settlement | do not annualise it |
| Error | a mis-coding, a duplicate, a wrong period | fix the books, then re-read |

## The monthly variance pack

One page, fixed shape, out by the 7th:

1. Plan, actual and variance for revenue, gross margin, each cost block and EBITDA.
2. The three largest variances, each with cause, owner and action.
3. Anything that changes the full-year landing point, with the new number.
4. The one line that is favourable for a bad reason - a deferred hire, a slipped
   campaign - because that is where next quarter's surprise is hiding.

Rule: no variance goes in the pack without a named cause. "Unclear, investigating" is
allowed once, with an owner and a date; twice means nobody is looking.

## Reforecast discipline

- **Cadence** - quarterly, on a fixed date, plus any month with a variance above 10% on
  revenue or EBITDA.
- **Method** - year-to-date actual, plus the remaining months re-driven from today's
  drivers, not from the original assumption. Anything else is arithmetic on a hope.
- **Label both numbers** - "original budget ₹4.2 crore, reforecast ₹3.6 crore, variance
  ₹60 lakh, cause: two enterprise deals slipped to Q3". The original stays visible; it
  is the benchmark, not the plan.
- **Re-base only on a structural change** - a lost anchor customer, a new funding round,
  a price change, a regulatory shift. Re-basing every quarter because the number is
  embarrassing destroys the benchmark and the discipline with it.

## The five questions to ask a variance

1. Is it timing or permanent?
2. Is it volume, rate or mix?
3. Did we choose it (a discount, a hire, a campaign) or did it happen to us?
4. Does it repeat next month?
5. What is the full-year effect if it does?

If the answer to 3 is "we chose it", the conversation is about the decision, not the
number. Most variance meetings argue about arithmetic when the decision was taken weeks
earlier by someone who is not in the room.

## Anti-patterns

- **Variance as a percentage only.** "12% over" on a ₹40,000 line and on a ₹40 lakh line
  are different problems.
- **Favourable variances left unexamined.** Under-spend is usually under-delivery.
- **Annualising a one-off**, in either direction.
- **The reforecast that only moves the revenue line.** If revenue falls and cost does
  not, the plan is not a reforecast, it is a wish.
- **Blaming the plan.** The plan was wrong; the business is the truth. Fix the plan.
