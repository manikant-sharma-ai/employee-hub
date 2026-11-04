# Measurement and incrementality

Paid media measurement has one job: to tell you what would not have happened without
the spend.

## The stack, in order of trust

| Layer | What it says | Trust |
|---|---|---|
| Gateway or bank | Money collected, minus refunds and failed COD | Highest |
| Order system or CRM | Orders taken, leads accepted by sales | High |
| Analytics (GA4, warehouse) | Sessions, events, attributed conversions | Medium |
| Ad platform | Conversions it claims, with its own attribution window | Lowest, and the largest |

Report the top three next to the fourth, and state the ratio. A platform claiming
1.6x the gateway is normal; 3x means something is broken or double-counted.

## The tracking that has to be right before scaling

- **One pixel or CAPI per property**, firing once per event. Duplicate firing is the
  most common cause of inflated conversions.
- **Server-side events where possible** (CAPI or equivalent), because browser
  tracking loses a large share of events on mobile.
- **Value and currency on every purchase event**, so ROAS targets mean something.
- **Lead events only after qualification** where sales qualifies; otherwise optimise
  for volume and complain about quality forever.
- **Consent handling** that does not silently drop the events the business is paying
  to optimise.
- **A test event in the platform's own debug view** before any campaign launches.

## Attribution windows, and what they hide

| Window | What it captures | The trap |
|---|---|---|
| 7-day click, 1-day view | Most considered purchases | Over-credits the platform for demand created elsewhere |
| 1-day click | Impulse purchases | Under-credits longer consideration |
| View-through | Brand impressions | Generous; almost always inflates |

Pick one, write it in the read-out, and keep it for at least a quarter. Changing the
window to improve a campaign's number is a reporting decision dressed as an
optimisation.

## The cheap incrementality tests

1. **Geo holdout.** Pause the channel in two comparable cities for two weeks and
   compare total orders, not attributed orders. Crude, and usually decisive.
2. **Time-based pause.** Stop spend for a week in a low-season window and watch the
   organic baseline.
3. **Brand vs non-brand split.** Brand search usually harvests demand created
   elsewhere; measuring it separately stops it flattering the account.
4. **Post-purchase survey.** One question in the order confirmation: how did you
   first hear about us. Biased, self-reported, and the best cheap signal most SMBs
   have.

## Lead quality, the Indian SMB version

A lead is not a lead. Compare, for each source:

| Field | Why |
|---|---|
| Cost per lead | What the platform reports |
| Share that answered a call | The first real filter |
| Share that qualified | The number sales cares about |
| Cost per qualified lead | The number to optimise |
| Cost per closed deal | The number the founder should see |

Meta lead-form leads in many categories qualify at a fraction of site-form leads.
Optimising for lead volume while reporting cost per qualified lead is how a channel
gets blamed for a form design problem.

## Reconciliation, monthly

One table, four columns, no commentary:

| Month | Platform conversions | Analytics conversions | Orders | Collected revenue |
|---|---|---|---|---|
| | | | | |

Compute the ratio and keep it. When the ratio moves sharply, something in tracking
changed, and every CPA in the account just became incomparable to last month's.

## Anti-patterns

- **Optimising for a proxy event** (add-to-cart, page view) and reporting purchase
  CPA from it.
- **Trusting the platform's ROAS as profit.** It ignores returns, COD failures, GST
  and cost of goods.
- **Changing attribution windows mid-quarter.**
- **No baseline.** A campaign with no pre-period cannot show a lift.
- **Double-firing pixels after a site migration**, discovered a month later.
- **Ignoring COD returns in D2C.** A fifth of "conversions" can come back.
