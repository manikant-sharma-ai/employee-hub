# ABC-XYZ classification

Classification is what makes 4,000 SKUs manageable. Policy by class, attention by
exception.

## ABC - by annual consumption value

Annual consumption value = units sold in 12 months × unit cost.

| Class | Share of value | Typical share of SKUs | What it means |
|---|---|---|---|
| A | 70-80% | 10-20% | The business. Every decision is individual |
| B | 15-20% | 20-30% | Managed by policy, watched monthly |
| C | 5-10% | 50-70% | Cheap to hold, expensive to manage. Automate |

Sort descending, cumulate, and cut where the cumulative curve flattens. Do not force
70/20 - a distribution business with a narrow range can be 85/10.

## XYZ - by demand variability

Coefficient of variation over the lookback: CV = σ / mean.

| Class | CV | Behaviour | Policy |
|---|---|---|---|
| X | below 0.3 | Steady, predictable | Lean stock, tight ROP, low safety |
| Y | 0.3 to 0.7 | Seasonal or trending | Buffer, seasonal build, watch the trend |
| Z | above 0.7 | Lumpy, project-driven | Order to order, or hold spares; never carry deep |

CV on monthly data understates variability. Use weekly or daily buckets where the data
allows.

## The 3×3 policy matrix

| | X (steady) | Y (seasonal) | Z (lumpy) |
|---|---|---|---|
| **A** (high value) | Weekly review, 98%, tight ROP, monthly count | Seasonal build with a written buffer, 97%, pre-season order date | Make or buy to order; hold components, not finished stock |
| **B** (mid) | Fortnightly, 95%, standard ROP | Seasonal build, 95%, review the trend line monthly | Order on signal only, 90%, cap the holding |
| **C** (low value) | Monthly, 90%, two-bin or min-max, automate | Seasonal bulk buy once, 90% | Stock only against a named order |

Nine policies, nine sentences. Anything more granular is a policy nobody remembers.

## What each class gets

| Element | A | B | C |
|---|---|---|---|
| Review | Weekly | Fortnightly | Monthly |
| Service level | 97-98% | 95% | 90% |
| Count | Monthly | Quarterly | Half-yearly |
| Forecast attention | Individual | By family | None |
| Buffer | Computed per SKU | Class default | Min-max only |
| Dead-stock review | Monthly | Quarterly | Half-yearly |

## Reclassify, don't set and forget

- Re-run the classification every quarter.
- A SKU that moves from C to A has usually just become a bestseller - that is the single
  most valuable output of this exercise, and it is missed if the class is never refreshed.
- A SKU that moves from A to C is dying. It gets a dead-stock action, not a bigger buffer.
- Log every class change in the policy sheet with the date. A silent reclassification is
  indistinguishable from a mistake.

## Reading the matrix as a story

| Pattern | What it says | What to do |
|---|---|---|
| Many A-Z SKUs | The business sells projects, not products | Move to order-based supply, hold components |
| Many C-Z SKUs | Catalogue bloat | Delist or make to order; the tail costs more than it earns |
| A-X dominance | Healthy, predictable core | Tighten the ROP, release the excess safety stock to cash |
| B-Y cluster | Seasonal business | Build a season calendar and a written buffer |
| Everything is A | The cut was never made | Re-run on 12 months of value, not on gut |

## The tail

The C class is where cash hides. It is 60% of the SKUs and 8% of the value, and it
consumes most of the counting, the storage and the attention. The correct treatment is
brutal and cheap: min-max, one reorder rule, an annual delist review, and no individual
conversation.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Classification by unit price, not consumption value | The cheap high-volume SKU is under-managed |
| Never re-running the ABC | The bestseller of this year is still managed as a C |
| Treating C as unimportant | It is unimportant financially and critical operationally - automate it, don't ignore it |
| Same service level for every cell | Either too much cash or too many stock-outs, always |
| Classifying on 3 months of data | Seasonality is invisible; the classes are wrong |
