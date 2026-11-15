# Save plays and win-back: what is worth paying to keep

A save is a trade: margin now for revenue later. This file makes the trade explicit, and keeps the discount
where it belongs - as one play among several, never the first one.

## The play library, by reason code

| Reason code | First play | Second play | Do not offer |
|---|---|---|---|
| `price-value` | A right-sized plan or a usage review that lowers the bill honestly | A time-boxed discount against a commitment | A permanent discount with no commitment |
| `cash-flow` | A payment plan or a pause, with the term written | A downgrade to the entry plan | A refund you cannot afford |
| `missing-feature` | A workaround, a manual service, a date on the roadmap | A credit while they wait | A promise with no owner and no date |
| `product-quality` | An escalation with a named engineer and a fix date | A service credit | A discount, which reads as an admission with a bribe |
| `onboarding-failure` | A guided re-onboarding with a named person | A concierge setup of the first workflow | Anything, until they have seen value once |
| `switched-competitor` | Nothing, usually - ask what would bring them back in six months | A win-back in 90 days | A price war you cannot win |
| `business-change` | A pause or a downgrade, warmly offered | A referral ask | A save attempt that ignores their reality |
| `relationship` | A call from the founder or the most senior person | A change of account owner | A credit; the problem was not money |
| `no-longer-needed` | An exit that is easy and gracious | A referral and a testimonial ask | Retention theatre |

## The economics of a save

Compute this before offering anything. It is four numbers and it settles most arguments.

| Input | Example |
|---|---|
| MRR at risk | ₹48,000 |
| Gross margin % | 62% |
| Expected remaining life if saved | 11 months |
| Margin protected | 48,000 × 0.62 × 11 = ₹3,27,360 |
| Cost of the play (discount × months + hours × cost) | 48,000 × 0.25 × 3 + 4h = ₹36,000 + ₹6,000 |
| Save rate of this play, measured | 35% |
| Expected value | 0.35 × 3,27,360 − 36,000 = ₹78,576 |

If the expected value is negative, the play is a refund with extra steps. Say so.

Three rules that follow:

- **A save is only a save with a control group.** Compare the customers offered the play against a matched group
  that was not. The difference is the effect; the raw retention is the market.
- **Discount depth should be the smallest that changes the decision.** Test 10% before 30%. A customer who
  accepts 10% was worth 10%.
- **Never discount without a commitment.** A discount against a 12-month term buys revenue; a discount against
  nothing buys a month and teaches the customer to ask again.

## Win-back, with a memory

| Window | Offer | Expected rate | Note |
|---|---|---|---|
| 0-30 days | A specific fix for the stated reason, no discount | Highest | They remember why they left |
| 30-90 days | A re-onboarding plus a new feature they asked for | Moderate | Cheapest window before they settle elsewhere |
| 90-365 days | A return offer at the old price, capped | Low | Only where the reason was `business-change` or `cash-flow` |
| Over a year | Nothing proactive | Very low | They have replaced you; a list is enough |

Win-back is outbound, so the list goes to `sales-outreach`; this role supplies the reason code, the window and
the offer ceiling. The customer must not be contacted twice by two employees in the same month.

## Consent, dignity and the DPDP line

- Marketing to a lapsed customer is marketing. It needs a lawful basis, an opt-out that works, and honouring a
  prior do-not-contact.
- A customer who asked to be erased from the system is erased, not moved to a win-back list.
- A save call to a customer who said "stop contacting me" is a compliance problem, not a retention tactic.
- The repo and the notes carry reason codes and account IDs, never names, phone numbers or emails.

## Measuring the plays

| Metric | How | Why it matters |
|---|---|---|
| Save rate by play | Saved / offered, with a control group | The only number that says whether to keep running it |
| Cost per save | Total play cost / saves | Compare with the margin protected, not with the MRR |
| Downstream survival | Share of saved customers still active at 6 months | A save that buys 60 days is a delay, not a save |
| Discount leakage | Rupees of discount given / customers offered | Detects the play becoming policy |
| Contamination | Customers who ask for the offer before cancelling | The play has become a price list |

If downstream survival at six months is under half the normal cohort, the play is renting time. Stop it or
re-price it.

## Anti-patterns

- Offering a discount before the reason is coded: the offer is then a guess with a budget.
- Saving the loudest customers and ignoring the quiet ones, who are the majority of churn.
- Making the save play a permanent tier in the price list.
- Letting whoever takes the cancellation call decide the offer: the incentive is to save at any price.
- Counting a customer who stayed for one discounted month as retained in the board pack.
- Win-back campaigns to everyone who ever left, with no reason and no window.
