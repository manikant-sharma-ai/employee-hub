# Programme design

The design decisions that decide whether the programme is a channel or a rebate.
Make them in this order; each one constrains the next.

## Decision 1 - what counts as incremental

| Model | Rate | Risk | Use when |
|---|---|---|---|
| New customers only | Full rate on first order, 0-5% on repeat | Partners stop promoting after the first sale | Default for most D2C |
| All customers, full rate | Highest apparent volume | Pays commission on sales you already had | Only with a strong reason |
| All customers, tiered | Full on first, 5-8% on repeat | Manageable | Subscription or consumable products |
| Full price only | Full rate, no rate on discounted | Lower volume, better margin | Products with permanent discounting |

Write the choice into the terms. Most cannibalisation arguments are really an
argument about this line, held a quarter too late.

## Decision 2 - the partner types you will admit

| Type | What they do | Typical rate | Verdict |
|---|---|---|---|
| Customer advocate | Refers people they know | 10-15% or a flat credit | Best incremental, low volume |
| Niche content site | Reviews, comparisons, tutorials | 8-15% | High quality, slow to start |
| Newsletter or community | Curated recommendations | 10-20% | Good, if the audience is real |
| Coupon or cashback site | Owns the last click at checkout | 3-8%, never on full price | Admit deliberately or not at all |
| Comparison engine | Aggregates offers | 5-10% | Volume without loyalty |
| Paid-search affiliate | Bids on your brand | 0 - banned | Pure cannibalisation |
| Sub-affiliate network | Recruits other affiliates | 2-5% override | Only with visibility into the chain |

## Decision 3 - the structure

Two or three tiers, no more. A rate card with seven tiers is a rate card nobody
reads.

```
Tier 1 - Advocate (customers, community): 12% first order, 5% repeat
Tier 2 - Content (blogs, reviewers, newsletters): 10% first order, 4% repeat
Tier 3 - Comparison and coupon (admitted): 4%, full-price orders only, no repeat
```

Bonuses: a volume bonus is fine if it is capped and paid on **new** customers
only. Uncapped volume bonuses are how a channel grows into a loss.

## Decision 4 - the rules

Publish these in the terms, before anyone joins:

1. No paid search on the brand name or its misspellings.
2. No coupon codes except those issued to you by us.
3. No self-referral, no referral of the same household or device.
4. No cookie stuffing, toolbar injection or ad hijacking.
5. No bidding on competitor terms with our brand in the ad copy.
6. Returns and cancellations are netted before payout.
7. Commission is void on orders using an unauthorised code or an employee discount.
8. Clawback within 90 days for returns, fraud or rule breaches.
9. Disclosure of the affiliate relationship wherever the link appears.
10. We may change the rate with 30 days' notice; changes are not retroactive.

## Decision 5 - the payout mechanics

| Item | Typical setting | Why |
|---|---|---|
| Cookie window | 30 days (7-14 for considered purchases) | Longer windows credit partners who did not close |
| Approval | On order, paid after the return window | Returns are the silent loss |
| Minimum payout | ₹500-1,000 | Below this, transfer cost exceeds the commission |
| Payout cycle | Monthly, fixed date | Partners plan around it |
| Payment rail | Bank transfer or UPI, invoice where registered | GST and TDS handled by `finance-ops` |

## What a launch needs, minimum

A terms page, a signup form, a dashboard, three creative assets, a welcome email
with the swipe file, and a named person to reply. Without the named person, the
programme is a form.

## Anti-patterns

- **Launching on a high rate to attract partners.** You attract the ones who only work on rate, and they leave when you correct it.
- **No new-versus-returning split.** The single most expensive omission in affiliate design.
- **Admitting coupon sites by accident.** They find you; the decision is whether to approve them.
- **A rate card with seven tiers.** Nobody reads it and everybody negotiates.
- **Rules published after the first payout.** Every partner assumes the rules are new.
