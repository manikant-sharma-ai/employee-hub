# Tracking and attribution

An affiliate programme is a tracking system with a payment attached. If the
tracking is loose, the payment is wrong, and the argument arrives with the invoice.

## The four settings that decide everything

| Setting | Options | Recommended default |
|---|---|---|
| Cookie window | 7 / 30 / 60 / 90 days | 30 days; 7-14 for considered purchases |
| Attribution | Last click / first click / linear | Last click, published |
| Coupon ownership | Partner-owned / brand-owned / none | Brand-owned; partners get issued codes only |
| Cross-device | Platform-dependent | Accept the gap; report it |

## Last click, and why it must be published

Last click credits the partner holding the cookie at checkout. On a two-week
consideration cycle, that is often a coupon site, not the reviewer who did the
work. Publishing the rule does not fix it, but it stops the argument and tells
content partners what they are being paid for.

If content partners are the strategy, consider a first-click or a two-part
split (40% first click, 60% last click) - but only if the platform supports it.
A rule you cannot enforce is worse than last click.

## Coupon ownership

| Model | Who gets the code | Effect |
|---|---|---|
| Brand-issued only | You create a code per partner | Clean attribution, some leakage to code-sharing sites |
| Partner-issued | Partner makes their own code | Convenient, unverifiable, easy to abuse |
| Coupon aggregation | Sites scrape any live code | Highest volume, lowest incrementality |

Brand-issued codes, one per partner, with a naming convention -
`PRIYA12`, `KITCHENCO10` - is the only model that survives an audit.

## Reconciling the platform against the orders

Do this monthly, before payout. Three checks:

1. **Order count**: platform-reported orders against the order system, filtered to the same dates.
2. **Value**: attributed revenue against order value net of discounts, shipping and returns.
3. **Duplicates**: the same order credited to two partners, which happens with multi-touch and coupon stacking.

A variance above 2% is a tracking problem, not a rounding error. Find it before
you pay it.

## What to track beyond revenue

| Metric | Why |
|---|---|
| New customers per partner | The incrementality proxy that matters |
| Return rate per partner | Some audiences return far more |
| Average order value | Coupon partners lower it; reviewers raise it |
| Time from click to order | Under 5 minutes suggests a decided purchase |
| Direct traffic on brand terms after a coupon post | The leakage signal |
| Clawbacks applied | If this is zero every month, the rules are not being checked |

## Tools, and what they are good at

| Tool | Strength | Limitation |
|---|---|---|
| Refersion | Shopify-native, simple payouts | Limited multi-touch |
| Tapfiliate | Flexible commissions, good API | Setup effort |
| FirstPromoter | SaaS subscriptions, MRR tracking | Weak for physical goods |
| UpPromote / GoAffPro | Cheap, Shopify app, quick start | Basic fraud controls |
| Platform-native (Shopify Collabs, WooCommerce) | No extra cost | Fewer rules and reports |

## Anti-patterns

- **A 90-day cookie because a partner asked.** Every extension pays someone for a decision already made.
- **Paying from the platform's report without reconciling.** The platform is an interested party.
- **No code naming convention.** You cannot tell which partner a redemption came from.
- **Tracking coupons you did not issue.** The commonest source of unexplained commission.
- **Ignoring returns until the quarter closes.** By then the partner has been paid and the argument is unwinnable.
