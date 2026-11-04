# Measurement and attribution

If the conversion event is wrong, every optimisation after it is wrong - and it
will be wrong confidently, at scale, for months.

## The verification pass, before any spend

| Check | How | Failure it prevents |
|---|---|---|
| Event fires once | Test purchase, tag assistant, platform diagnostics | Double counting, which doubles apparent ROAS |
| Value is passed | Purchase value in the event | Optimising for count when margin varies |
| Currency and tax | INR, with or without GST, stated | Revenue overstated by 18% |
| Deduplication | Platform and server events deduped by order id | Two conversions for one order |
| UTM convention | Lowercase, consistent, one source per dimension | Every report disagreeing with every other |
| Attribution window | 7-day click / 1-day view, stated | Flattering numbers that do not match the bank |
| Consent and privacy | Consent mode or the equivalent, where applicable | Legal exposure and unreliable data |

## The UTM convention

```
utm_source=meta | google | linkedin | whatsapp | partner-name
utm_medium=paid-social | cpc | email | referral
utm_campaign=<objective>-<audience>-<yyyymm>
utm_content=<creative-angle>-<variant>
```

Lowercase, hyphenated, no spaces, and one owner for the convention. Two spellings
of "Facebook" is how a channel disappears from a report.

## Reconciling the platform against reality

Monthly, one table:

| Source | Reported conversions | Reported revenue | Orders in store | Revenue in store | Gap |
|---|---|---|---|---|---|
| Meta | | | | | |
| Google | | | | | |
| Total | | | | | |

The gap is normal - view-through, cross-device, returns, cancellations, bot
traffic. What is not normal is a gap that is stable but unexplained, or a gap
that grows every month. Name the cause, and use the reconciled number in every
decision.

## Attribution, honestly

| Model | What it credits | Bias |
|---|---|---|
| Last click | The final touch | Overrates search and retargeting |
| First click | The discovery | Overrates content and social |
| Linear | Every touch equally | Ignores that touches differ |
| Data-driven | Modelled contribution | Needs volume and clean events |

For a small business, the practical answer is: use last-click for in-platform
optimisation, use reconciled total revenue for budget decisions, and never compare
a platform's ROAS to another platform's ROAS as if they were measured the same way.

## Reading the numbers without self-deception

- **Compare like windows.** A 7-day-click number against a 28-day number is not a comparison.
- **Separate new from returning.** Retargeting conversions are cheap because the work was already done.
- **Count returns and cancellations.** In Indian D2C, RTO can remove 15-30% of COD orders; a ROAS computed before RTO is fiction.
- **Watch for the stockout illusion.** A campaign that "converts worse" in a sold-out week is a stock problem.
- **Report the number the founder cares about:** verified orders or qualified leads, and cost per one.

## Anti-patterns

- **Trusting the pixel without a test purchase.** The most expensive mistake in paid media is a duplicate event nobody checked.
- **Comparing platform ROAS across platforms.** Different windows, different attribution, different definitions.
- **Ignoring GST and returns.** Both move revenue by double-digit percentages.
- **A new UTM spelling per campaign.** The report fragments and the history is lost.
- **Reporting clicks because they look good.** Clicks are the platform's currency.
