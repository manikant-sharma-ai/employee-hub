# QA and data quality

An event that has not been seen firing is a hope. This is the pass that turns a
tracking plan into a measurement system.

## The QA pass, per event

| Check | How | Fail looks like |
|---|---|---|
| Fires once | Debug view, act once, count | Two rows for one action (re-render, retry) |
| Fires at the right moment | Act, watch the timestamp against the screen | Fires on page load, before the action |
| Properties present | Inspect the payload | `undefined`, `null`, `""`, or a string where a number belongs |
| Property values valid | Check against the enum | `plan_tier: "Growth "` with a space |
| Platform coverage | Web, Android, iOS, server as planned | Web only, because that is where the developer tested |
| User identified | Check `user_id` present | Events land anonymous, funnel step missing |
| No personal data | Read every property value | An email in a search event |
| Consent respected | Block consent, act, check nothing marketing fires | Events fire before consent |

## The warehouse reconciliation

The number that matters is the one that ties to money.

| Source | Compare | Tolerance | If it fails |
|---|---|---|---|
| `order_paid` count | Payment gateway successful payments | ±2% | Missing server-side event, or a failed client event |
| `order_paid` value | Gateway settlement, net of refunds | ±2% | Currency, GST, or a duplicate |
| `signup_completed` | CRM or user table created rows | ±5% | Anonymous events, or a bot filter |
| `subscription_cancelled` | Billing system cancellations | ±2% | Cancellation event fired client-side only |

Run it for one full day before the release is called done, and monthly afterwards.
Name the difference rather than averaging it.

## The five data-quality failures, in order of frequency

1. **Duplicates.** Mobile retries, double taps, re-renders. Fix with an `event_id`
   and dedupe in the warehouse; never with a `distinct` in the chart only.
2. **Missing properties on one platform.** iOS ships a version later and the
   property is absent, so the segment silently disappears.
3. **Free-text values.** A plan name typed by the user becomes 300 values. Enum it.
4. **Time zone and date boundary.** A chart in UTC against an IST business day
   shows a different "yesterday".
5. **Bot and internal traffic.** Office IPs, monitoring, and preview deployments
   inflate the top of the funnel. Exclude them in the definition, not in the reading.

## The debug checklist, in order

1. Open the debug view or the realtime report.
2. Clear the session; act once; confirm exactly one event.
3. Inspect properties against the plan, one by one.
4. Repeat on the second platform if there is one.
5. Test the failure path - payment declined, OTP wrong, network off.
6. Test after consent is declined.
7. Paste the evidence into the release ticket.

## Data quality monitoring

| Monitor | Cadence | Action |
|---|---|---|
| Event volume vs 7-day median, per event | daily, automated | Alert on a 50% drop or a zero |
| Null rate per required property | weekly | Fix in code, not in the chart |
| Distinct values per enum property | monthly | Add to the enum or fix the source |
| Reconciliation to gateway and CRM | monthly | Name the gap in the readout |
| Events with no dashboard using them | quarterly | Retire or justify |

## Anti-patterns

- Testing only the happy path, so `payment_failed` is never verified.
- Testing in a development build with a different analytics property.
- A QA pass that checks the event name and not the properties.
- Fixing a duplicate in the chart with a `distinct` and leaving it in the data.
- Reconciling once, at launch, and never again.
- Recording QA as "looks fine" instead of pasting the payload.
