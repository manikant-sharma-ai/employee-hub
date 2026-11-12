# Refunds and policy application

A refund is a money movement with a rule attached. This file is the rule and the mechanics.

## Decide the disposition, then the money

| Disposition | When | The money |
|---|---|---|
| Full refund | Not as described, damaged, defective, wrong item, within the window | Full amount including forward freight where charged |
| Refund less return freight | Changed mind, where the policy discloses it | Price minus disclosed return freight |
| Exchange | Size or fit, where stock exists | No money; a replacement order and a reverse pickup |
| Store credit | Changed mind, where the policy offers it and the customer accepts | Credit note, with the GST treatment correct |
| Partial refund | Used or incomplete item, or a goodwill settlement | Agreed amount, documented, once |
| Refuse | Outside the window, excluded category, or evidence contradicts | Nil, with the clause and the evidence cited |
| Hold pending evidence | Integrity flag, or the unit has not been received | Nil until resolved, with the date of the next action |

## The mechanics, by payment method

| Paid by | Refund route | Typical time | Watch |
|---|---|---|---|
| Card | Gateway refund to the same card | 5-7 working days after initiation | The gateway fee is usually not returned |
| UPI | Gateway or a direct UPI collect to the payer | 3-5 working days | Name and VPA must match the payer |
| Net banking | Gateway | 5-7 working days | |
| Wallet | Gateway | 1-3 working days | |
| COD | Bank transfer to an account in the customer's name | 3-7 working days | Never refund to a third party's account |
| EMI | Gateway, and the EMI continues | 7-10 working days | The customer still pays interest to the issuer - say so |
| Marketplace prepaid | Marketplace refund flow | Their timeline | You cannot refund directly; you can only approve |
| Credit note | Your own document | Immediate | GST treatment differs from a cash refund |

Two rules that prevent most refund disputes: the refund goes back to the original payer, and the date
the customer will see it is stated with the reference number.

## The policy, written to be defensible

A publishable policy has seven parts and fits on one screen:

1. **Window** - how many days from delivery, and whether that differs by category.
2. **Condition** - unused, tags, accessories, original packaging.
3. **Exclusions** - innerwear, personal care, customised, perishable, digital - each with the reason.
4. **Who pays return freight** - stated per reason, not as "as applicable".
5. **Refund method and timeline** - by payment method, with the gateway's real timeline.
6. **Exchange and credit note** - offered, and on what terms.
7. **How to raise it** - one route, with the information needed.

What must never appear: a deduction nobody explained, a discretionary "management decision", or a
window that differs between the website and the marketplace listing.

## Lawful deductions

| Deduction | Lawful when | Not lawful when |
|---|---|---|
| Return freight | Disclosed in the policy in force, for the reasons it applies to | Applied to damaged or wrong-item returns |
| Restocking or handling fee | Disclosed before purchase, reasonable, and not a penalty | Invented at refund time |
| Forward freight | Disclosed, and the item was delivered as described | The item was defective |
| Value reduction for use | The item is materially used, and the reduction is evidenced | The item is unused |

## GST and the credit note

A sales return reduces taxable value. Issue a credit note under the GST law, referencing the original
invoice, within the prescribed time limit, and report it in the return for the period. Where the
customer is unregistered, the credit note is issued to the same person and the refund follows. An
e-invoice already reported needs its own handling - the IRN cannot simply be edited. This is the
mechanical part most businesses get wrong and it surfaces at the annual reconciliation.

## Anti-patterns

- **Refunding before the unit is graded** on a high-value item, then finding it unsaleable.
- **Refunding to a different account** because the customer asked. It is a fraud vector and breaks the
  audit trail.
- **Silent deductions.** The refund arrives ₹150 short with no explanation, and the ticket reopens.
- **Promising "3-5 days" when the gateway takes seven.** The gap is the complaint.
- **No credit note for a B2B return.** The customer's input credit and your output liability both go
  wrong.
- **A policy that differs by channel.** It is the first thing a marketplace dispute examines.
