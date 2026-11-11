# Cost and headcount planning

People are usually the largest controllable cost and the worst-planned one. One salary line
with no headcount behind it is the reason the plan misses by 15%.

## Cost behaviour, before cost heads

| Type | Behaviour | Planning rule |
|---|---|---|
| **Fixed** | Unchanged with volume: rent, insurance, core salaries | Read the contract; date the escalation |
| **Variable** | Moves with units: material, freight, packaging, gateway | A rate per unit, never a total |
| **Step** | Jumps at a threshold: a second shift, a third accountant, a bigger godown | Date the step and the trigger |
| **Semi-variable** | Electricity, phone, courier | Split into a base plus a per-unit element |

Every head is tagged with one of these. The tag is what lets you answer "what happens to cost
if we sell 20% more" in one minute instead of one week.

## The headcount plan

One row per role, not per person where the team is large:

| Role | CTC band | Current | Apr | May | Jun | ... | Annual cost | Trigger for the hire |
|---|---|---|---|---|---|---|---|---|
| Sales exec | ₹4.8L | 3 | 4 | 4 | 5 | | ₹28.6L | 2 closures/month per exec |
| Warehouse asst | ₹2.6L | 2 | 2 | 3 | 3 | | ₹8.1L | >400 orders/week |

Then load the statutory on-costs - they are not optional and they are routinely forgotten:

| Head | Basis | Note |
|---|---|---|
| PF (employer) | 12% of basic, on eligible employees | Plus 0.5% EDLI and admin charges |
| ESI (employer) | 3.25%, where wage is within the ESI ceiling | Ceiling changes; verify current limit |
| Gratuity | 4.81% of basic, for eligible service | Provision it even if unpaid |
| Bonus | 8.33% of basic, within the wage ceiling | Statutory, not discretionary |
| Leave provision | Earned leave encashment | A real liability at exit |
| Recruitment | 8-15% of CTC for a specialist; near zero for a referral | Charge it to the month it is paid |

Rule of thumb for planning: **CTC × 1.15-1.20** is the real monthly cost for a small Indian
team. Put that multiplier in the assumptions register with the arithmetic, not as a belief.

## Step costs, dated

| Threshold | Step that arrives | Typical lead time |
|---|---|---|
| Orders per day cross the packer's capacity | Extra packer, second shift | 1-2 weeks |
| SKUs cross ~500-1,000 | WMS or a real inventory system | 4-8 weeks |
| Revenue crosses the GST audit threshold | CA retainer increases | Immediate |
| Headcount crosses 20 | PF/ESI coverage, POSH compliance, registers | 1 month |
| Headcount crosses 50 | Statutory officer roles, standing orders | 1 quarter |
| A second state | Local registration, agent, stock point | 1-2 quarters |

A plan that grows volume 40% with no step cost in it has a cost base that cannot deliver the
volume.

## Contracts and escalation clauses

Read the contract, do not recall it. Extract:

| Item | What to pull | Where it bites |
|---|---|---|
| Rent | Lock-in, escalation %, escalation date | A 15% jump in month 13, unplanned |
| AMC / maintenance | Annual value, escalation, scope | Repairs land in a lump |
| Software | Seats, per-seat price, annual uplift, renewal date | Silent 10-20% creep |
| Loan | EMI, moratorium, floating rate, reset date | A rate reset changes the whole year |
| Insurance | Premium, sum insured, renewal date | Renewal is often 10%+ up |
| Logistics rate card | Per-kg slab, fuel surcharge, zone | Volume discounts never applied |
| Professional retainer | Monthly fee, scope, out-of-scope rates | Every extra filing is a new bill |

## Vendor and overhead review, once a year

For every line above ₹50,000 a year, three questions:

1. **Is it still needed?** Subscriptions outlive the person who asked for them.
2. **Is the rate still competitive?** One alternate quote is enough to find a 20% gap.
3. **Is the quantity right?** Seats, licences, sq ft, litres, kg - over-provisioning is quiet.

Anything found here goes to `expense-auditor` for the spend review; this role prices the
saving into the plan once it is agreed.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| One salary line, no headcount | The biggest cost is uncontrollable and unexplained |
| CTC used as cost | Understates by 15-20% before the first payslip |
| Step costs omitted | The plan cannot physically deliver its volume |
| Escalation clauses forgotten | A 15% rent jump appears as a variance, not a plan |
| Contract staff treated as fixed | Flexing down is assumed and does not happen |
| Every hire planned in April | Cash leaves 9 months before the revenue arrives |
| Attrition assumed at zero | Replacement cost, notice-period overlap and rehiring are real |
