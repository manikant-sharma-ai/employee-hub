# Commission economics

A commission rate is a fraction of margin, chosen against a ceiling that already
exists. Find the ceiling first.

## The ceiling

```
Contribution margin per order  = price - COGS - shipping - payment fee - packaging
Acquisition allowance          = contribution margin x share you can spend on acquisition
Commission ceiling             = acquisition allowance - (returns x contribution margin)
```

Worked example: ₹1,200 price, ₹420 COGS, ₹90 shipping, ₹25 payment fee, ₹25
packaging gives ₹640 contribution. At 35% available for acquisition, that is
₹224. With a 12% return rate, the expected contribution per gross order is
₹563, so the ceiling sits near ₹197 - about 16% of price. A 25% commission is
above the ceiling, and no volume fixes that.

## Rate by partner type, against the ceiling

| Partner type | Rate as % of price | Why |
|---|---|---|
| Customer advocate | 10-15% | Highest conversion, lowest support cost |
| Niche content | 8-15% | Slow, durable, good for search traffic |
| Newsletter | 10-20% | Paid on a warm audience; worth the top of the range |
| Coupon and cashback | 3-8%, full price only | Mostly last-click; the rate reflects the value added |
| Paid-search affiliate | 0 | Cannibalisation, banned |

## New versus returning

| Order | Commission | Reason |
|---|---|---|
| First order | Full rate | The channel did the work of acquisition |
| Second order within 90 days | 5-8% | Retention, not acquisition |
| Repeat after 90 days | 0-5% | The brand did the work |

Paying a full rate on every repeat turns the affiliate channel into a permanent
discount with a tracking fee attached.

## The cannibalisation estimate

You cannot measure it perfectly. Estimate it, state the method, and improve it.

| Method | How | Accuracy |
|---|---|---|
| New-customer-only rate | Compare new-customer share before and after | Good, if the flag is reliable |
| Holdout by geography or cohort | Turn the programme off for one region for a month | Best, needs volume |
| Coupon-use analysis | Share of attributed orders that used no code | Directional |
| Time-to-purchase | Orders under 5 minutes after the click are usually decided already | Directional |
| Ask at checkout | Self-reported source | Weak, but fills gaps |

Report it as a range: "attributed ₹18.4 lakh, estimated 35-50% would have
happened anyway, incremental ₹9-12 lakh, commission ₹2.1 lakh". That sentence is
the whole job.

## Payback and the ceiling test

| Number | Formula | Healthy |
|---|---|---|
| Commission as % of revenue | commission / attributed revenue | Under 12% for D2C |
| Incremental revenue per ₹1 of commission | incremental revenue / commission | Above 4 |
| Cost per new customer | commission / new customers | Below blended CAC |
| Return-adjusted commission | commission on returned orders / total commission | Under 10% |

## Where the maths goes wrong

- **Returns ignored.** A 25% return rate on 15% commission means 3.75% of revenue paid for nothing.
- **Discounts stacked.** Affiliate code plus site-wide sale plus free shipping can put an order under cost.
- **Repeat orders paid at the first-order rate.** The most common quiet loss.
- **GST and TDS forgotten** in the rate model. A registered partner's invoice adds GST; TDS reduces the net paid. Ask `finance-ops` before publishing a rate.
- **Volume bonuses uncapped.** They convert a good month into a loss at exactly the moment volume rises.

## Anti-patterns

- **Setting the rate from a competitor's public page.** Their margin is not yours.
- **A single rate for every partner type.** You overpay coupon sites and underpay the advocates.
- **Raising the rate to fix a volume problem.** It buys the wrong partners at the worst price.
- **No return adjustment before payout.** The loss shows up two months later, in the books, unattributed.
