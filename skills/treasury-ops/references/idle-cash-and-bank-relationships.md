# Idle cash and bank relationships

Cash that is not needed this month should earn something, and cash that is needed in three weeks
should not be locked up to earn 1% more. That tension is the whole of this file.

## The layering rule

Split the balance by when it is needed, not by how much it is.

| Layer | Horizon | Where it goes | Constraint |
|---|---|---|---|
| Operating float | 0-15 days | Current account, or a sweep with same-day liquidity | Must clear payments without notice |
| Buffer | 15 days-3 months | Sweep FD / liquid fund with T+1 redemption | No lock-in, no market risk worth taking |
| Reserve | 3-12 months | FD ladder, matched to known dates | Breakable, penalty understood |
| Strategic | 12 months+ | Decided by the founder, not by this role | Not treasury's call |

The rule that keeps businesses out of trouble: never place money in an instrument whose lock-in is
longer than the horizon in which the cash is needed, even if the rate is much better. A 7.1% one-year
FD broken in month four is a 5.4% FD with paperwork.

## Reading a bank relationship

| Item | What to check | Why it matters |
|---|---|---|
| Sanctioned limit | Amount, type (CC/OD/term), renewal date | An unrenewed limit is a demand loan |
| Drawing power | Stock and debtor statement submitted? | CC drawing power falls without the monthly statement |
| All-in cost | Interest + processing + annual fee + insurance + stamp | The headline rate is rarely the cost |
| Security | Hypothecation, collateral, personal guarantee | What the founder has actually pledged |
| Charges | SMS, statement, NEFT, cash handling, minimum balance | 0.3-0.8% of turnover, invisible until added up |
| Covenants | Turnover, current ratio, stock statement, audited accounts | A breach can convert the loan to repayable-on-demand |
| Renewal | Date and documents needed | Start 60 days before, not 5 |

## The annual bank review

Once a year, price the relationship: total charges paid across all accounts, the effective rate on
each limit against two other quotes, and the balances held as a condition. Banks price on relationship
value; a business that never asks pays the first quote forever. Two quotes is a negotiation; one is a
formality.

## When to draw the line, and when not to

Draw when the alternative is a statutory default, a supply stop, or a discount whose annualised value
exceeds the line's all-in cost. Do not draw to hold a balance that "looks healthy" for the bank, to
fund a receivable that is disputed, or to pay a vendor early for a discount smaller than the interest
the drawn line costs.

## Anti-patterns

- **Parking the entire balance in a 12-month FD** because the rate looked good, then breaking it.
- **Leaving a sweep unused.** Most Indian current accounts offer an auto-sweep at the same liquidity;
  a business holding 30 lakh idle at 0% is paying for the privilege of doing nothing.
- **Drawing the OD while holding a fixed deposit.** Borrowing at 11.5% to earn 7% is a 4.5% loss with
  two sets of paperwork.
- **Ignoring the drawing-power statement.** The limit did not fall; the eligible drawing did.
- **One bank for everything.** Concentration is convenient and expensive; two banks is usually enough.
- **Never reading the charge schedule.** The relationship is priced in the annexure nobody opens.

## The quarterly treasury check

Fifteen minutes, once a quarter, and it pays for itself:

1. **Every account reconciled** to the last statement, with no unexplained debit over ₹5,000.
2. **Every limit** checked for renewal date, drawing power and any unmet covenant.
3. **Every charge** added up for the quarter and compared with the schedule the bank issued.
4. **Every rupee above the buffer** placed in a layer whose lock-in is shorter than the need.
5. **Every foreign exposure** listed with its date, its cover and its unhedged remainder.
6. **Every signatory and portal user** reviewed - who can approve, who has left, who has a token.

The output is one page, dated, in the same file as the weekly position. A treasury that only looks
weekly optimises the week and pays for the quarter.
