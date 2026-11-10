# Cash and scenarios

A P&L budget can be profitable in every month and still kill the business in September.
This file is the check that stops that.

## The cash page

Build it from the P&L, month by month:

```
opening cash
+ collections            revenue x collection curve (not 100% in the month)
- payments to suppliers  cost of goods x creditor terms
- payroll and statutory  salaries, PF/ESI, TDS, GST paid
- rent, utilities, other fixed
- marketing spend        paid before the revenue it buys
- capex and deposits
- loan repayments and interest
- tax instalments
= closing cash
```

Then state the **lowest month** and the **headroom** - closing cash in the worst month
minus the minimum operating balance the founder is willing to hold. That single line is
the most useful number in the whole budget.

## Working capital, in one line

```
cash tied up = revenue x debtor days/30 - cost x creditor days/30 + cost x inventory days/30
```

`scripts/budget_roll.py` computes it. The point is not precision; it is that growth
consumes cash, and a 30% growth plan with 60-day debtors needs funding that a 10% plan
does not. Say the number and name the funding.

India-specific items that move cash and are routinely forgotten:

- **GST timing** - output tax is collected with the sale but paid after the return
  cycle; input credit arrives later still if the supplier files late.
- **TDS** - deducted by customers on your invoices, so cash arrives net and the credit
  comes back at assessment.
- **Advance tax instalments** - four dates a year, and they are cash out even in a loss
  year if the prior year was profitable.
- **MSME payment terms** - the buyer's deduction for a delayed payment to a registered
  micro or small supplier is a real cost; confirm the position with the CA.
- **Festival inventory build** - two months of stock bought before the quarter that
  sells it.

## The scenario ladder

Three cases, each with a trigger and a pre-agreed action list. Written in the calm
quarter, used in the bad one.

| Case | Trigger | What changes |
|---|---|---|
| Base | plan | nothing; manage to envelopes |
| Downside | revenue below plan by 10% for two consecutive months | freeze non-critical hiring, cut discretionary spend 30%, defer capex, extend creditor terms |
| Severe | revenue below plan by 25%, or closing cash under two months of fixed cost | reduce headcount in a named order, stop all non-essential spend, renegotiate rent and contracts, draw the facility, tell the lender early |

Rules for the ladder:

- **The cut order is written before the cut.** Naming people in a panic produces the
  wrong cuts and loses the people you needed.
- **Cut in this order:** discretionary spend, deferred capex, hiring freeze, contractor
  reduction, salary deferral at the top, headcount, then structural cost (sites,
  contracts). Cutting headcount first is the expensive version of the same saving.
- **Every rung names the cash effect and the date it lands.** A cut that saves money in
  April does not help in February.
- **Tell the lender before the covenant breaks, not after.** A covenant breach reported
  by the founder is a conversation; discovered by the bank, it is a default.
- **Protect the revenue engine** - the one channel or the two people who bring the
  money in. A severe case that cuts the sales team is a decision to shrink permanently.

## Sensitivity, not precision

You will be wrong. So show which three assumptions the plan is most sensitive to, and
what a 20% miss on each does to closing cash. That table converts an argument about
whether the plan is right into a conversation about what to do if it is not - which is
the only conversation worth having.
