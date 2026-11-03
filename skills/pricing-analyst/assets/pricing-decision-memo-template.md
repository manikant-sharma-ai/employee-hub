# Pricing decision memo - <product / plan>

Date: <date> | Owner: <name> | Decision owner: <name> | Decision by: <date>

## 1. The decision

**Recommendation:** <one number, one structure, one sentence>

**In one paragraph:** what changes, from what to what, why now, and what it is expected to do.

## 2. Unit economics

Inputs as given, so someone else can reproduce the model:

| Input | Value | Source |
|---|---|---|
| Price (incl GST) | | current / proposed |
| GST rate | | CA-confirmed |
| Discount / trade margin | | policy |
| COGS | | books |
| Packaging | | books |
| Freight out | | rate card |
| Return rate | | last 90 days |
| Freight back | | rate card |
| Payment fee % | | statement |
| Marketplace fee % | | settlement |
| Fixed cost / month | | books |
| Units / month | | books |

| Per unit | ₹ | % of net revenue |
|---|---|---|
| Gross price | | |
| Discount | | |
| GST component | | |
| Net revenue (ex-GST) | | |
| Variable cost | | |
| **Contribution** | | |
| Returns allowance | | |

Model output:

```
$ python3 scripts/margin_model.py model.json
<the output>
```

## 3. The floor and the band

| | ₹ |
|---|---|
| Price floor (contribution = 0) | |
| Current price | |
| Headroom over floor | |
| Band the evidence supports | |
| Break-even units / month | |

## 4. The evidence

| Rank | Evidence | Sample | What it says |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

The one assumption that would change this recommendation:

## 5. Structure or policy

<three tiers with the middle one named as the target, or the discount ladder with rupee costs and approval levels>

| Level | Discount | Who grants | Contribution cost | Condition |
|---|---|---|---|---|
| | | | | |

## 6. Effect on existing customers

- Who is affected, how they are told, and from when:
- Contract or marketplace constraints:
- What happens to renewals already quoted:

## 7. Test and read date

| Metric | Baseline | Target | Read on |
|---|---|---|---|
| | | | |

Decision rule written before the change: if <metric> is <x> by <date>, then <keep / revert / adjust>.

## 8. What I could not verify

- Actual fee load / returns rate: <unknown, modelled at>
- Win-loss reasons: <not available>
- Elasticity: <no test run>
- Statutory rates: <routed to CA>
