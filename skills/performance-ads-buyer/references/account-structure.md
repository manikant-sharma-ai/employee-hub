# Account structure

Structure exists for one reason: so a result can be attributed to a decision. An
account nobody can read is an account nobody can improve.

## The three levels, and what each is for

| Level | Decides | Rule |
|---|---|---|
| Campaign | Objective, budget, optimisation event | One objective per campaign; one conversion event |
| Ad set / group | Audience, placement, bid strategy | One audience idea per ad set |
| Ad | Creative | Three to six ads per ad set, then refresh |

Consolidation beats fragmentation in almost every small account: fewer campaigns,
each with enough budget to exit the learning phase, will outperform ten campaigns
sharing a budget.

## The learning phase, in plain numbers

Platforms need roughly 50 optimisation events per ad set per week to leave the
learning phase. Below that, delivery is unstable and CPA is noisy. Consequences:

- **A ₹30,000 monthly budget with a ₹1,500 CPA produces about 20 events a month.**
  That cannot support five ad sets. It supports one.
- **Fewer ad sets, more budget each** is the correct response to a small budget.
- **Raising budget by more than about 20% in a day** can re-enter the learning phase
  and reset the evidence you just gathered.

## Naming that survives six months

```
<platform>_<objective>_<audience>_<geo>_<creative-concept>_<variant>_<date>
meta_purchase_broad-in_ncr_reel-ugc-unboxing_v3_2026-11
```

Rules: lowercase, hyphens inside a field, underscores between fields, no spaces, no
names of people. A naming convention that is not enforced weekly becomes free text
within a month.

## Audiences

| Type | Use for | Watch |
|---|---|---|
| Broad, no interest targeting | Most D2C with a strong creative | Needs creative variety, not audience tweaks |
| Lookalike from purchasers | Scale once there are 500+ buyers | A lookalike from 40 buyers is a random sample |
| Retargeting, site visitors | Closing, not acquiring | Frequency climbs fast; cap it |
| Customer list upload | Exclusions, and lookalikes | Consent and DPDP obligations apply |
| Interest stacks | Categories where intent is genuinely narrow | Overlap between ad sets competes against yourself |

**Exclusions are half the account.** Exclude existing customers from acquisition
campaigns, exclude purchasers from retargeting, and exclude the audience of one ad
set from another. Without exclusions, two ad sets bid against each other and the
platform reports two conversions for one order.

## The audit, ten checks

1. How many campaigns are active, and how much of the budget sits in the top two?
2. Is every campaign on one objective and one conversion event?
3. Do any two ad sets overlap by more than 30%?
4. Are existing customers excluded from acquisition?
5. Is the conversion event the one the business actually counts - purchase, or a
   lead that sales accepted?
6. Are placements left on automatic, and is that deliberate?
7. Is there a creative older than 45 days still carrying spend?
8. Does every campaign have a landing page that loads under three seconds on a phone?
9. Is the pixel or CAPI firing once per event, not twice?
10. Could a stranger tell, from the account alone, what was being tested last month?

## Common structural mistakes in Indian SMB accounts

- **One campaign, everything in it.** Cheap to set up, impossible to learn from.
- **Five campaigns for five cities with a ₹20,000 budget.** Every one stuck in
  learning.
- **Boosted posts treated as campaigns.** No optimisation event, no measurement.
- **Lead forms with no qualification question**, producing volume the sales team
  cannot use, which then reads as a "lead quality" problem.
- **Marketplace ads and own-site ads in one account**, where one steals demand from
  the other and both look good.
- **Agency-owned ad accounts.** The business must own the account and the pixel;
  access can be granted, ownership cannot be borrowed.

## Anti-patterns

- **Restructuring every month.** Each rebuild resets learning and destroys
  comparability.
- **Micro-audiences on a small budget.** Ten audiences of 5,000 people each.
- **Testing audiences when the creative is the variable that matters.**
- **Duplicating a winning campaign five times.** It competes with itself and inflates
  reported conversions.
- **No exclusions.** The single most common cause of "the platform says 60 orders,
  we shipped 38".
