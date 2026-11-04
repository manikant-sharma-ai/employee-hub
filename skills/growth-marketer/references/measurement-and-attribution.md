# Measurement and attribution

Every platform claims the same order. Only the gateway knows who paid.

## The reconciliation, in four steps

1. **Platform-reported conversions** - Meta, Google, marketplace: usually the
   largest number, because each platform counts a view or a click as its own.
2. **Analytics-reported conversions** - GA4 or equivalent: the middle number,
   dependent on consent, blockers and tagging.
3. **CRM or order system** - the operational truth: orders taken.
4. **Gateway or bank** - the financial truth: money collected, minus refunds and
   failed COD.

Report all four for a month, then set the ratio. In most Indian D2C accounts the
platform number is 20-60% higher than the gateway number. Once the ratio is known,
budget decisions use the gateway number and the ratio, not the platform dashboard.

## Blended versus channel CAC

$$
\text{blended CAC} = \frac{\text{total acquisition spend}}{\text{total new customers}}
$$

Blended CAC is the only number the bank recognises. Channel CAC is a management
tool. A business can be profitable on blended CAC while one channel is a pure loss;
that is a decision to make deliberately, not to discover at year end.

## Last click is a story, not a fact

The last click gets credit for everything that came before it. A buyer who saw a
reel, asked in a WhatsApp group, searched the brand, and clicked an ad is credited
to the ad. Consequences:

- **Brand search looks like the best channel** because it captures the decision.
- **Organic and word of mouth look weak** because they rarely close the last click.
- **A channel can look unprofitable while creating demand** another channel harvests.

Use two cheaper instruments:

- **A post-purchase question**: "how did you first hear about us?" One question, in
  the order confirmation. It is self-reported and biased, and it is more useful than
  last click for small businesses.
- **A geo or time holdout**: pause the channel in one city or for two weeks and
  watch total orders, not channel-attributed orders. Crude, and the closest thing to
  truth a small budget can buy.

## UTM discipline

One scheme, written down, enforced in a sheet:

```
utm_source=meta | utm_medium=paid_social | utm_campaign=diwali_reorder | utm_content=reel_hook_b
```

- Lowercase, underscores, no free text.
- `utm_source` is the platform, `utm_medium` the type, `utm_campaign` the
  initiative, `utm_content` the variant.
- Anything typed by hand will drift within a month; generate links from a sheet.

## The metrics that mislead

| Metric | Why it misleads |
|---|---|
| Impressions | Buys nothing; reach and frequency tell you more |
| CTR | A click is not intent; a curiosity click is a cost |
| Platform ROAS | Counts orders that would have happened anyway |
| "Leads" | Without a qualification definition, it is form fills |
| Average order value | Rises when the cheap SKUs go out of stock |
| Conversion rate | Falls when traffic quality rises - always read with CAC |

## What to measure weekly, in one page

- New customers and revenue collected (gateway).
- Blended CAC and payback months.
- Spend by channel and marginal CAC on the largest one.
- Refunds and COD failures as a share of orders.
- The one experiment running, its sample progress, and its end date.

## Anti-patterns

- **Reporting platform ROAS to a founder as profit.** It is a claim until it is
  reconciled.
- **Changing attribution models to make a channel look better.** Pick one, keep it
  for a year, and note its bias.
- **No baseline.** A campaign without a pre-period comparison cannot show a lift.
- **Measuring everything and deciding nothing.** Five numbers on a page, one
  decision, weekly.
- **Ignoring returns and COD.** In Indian D2C they can remove a fifth of revenue
  after the sale is counted.
