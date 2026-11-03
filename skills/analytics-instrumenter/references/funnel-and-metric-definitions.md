# Funnel and metric definitions

A metric without a written definition is an opinion with a chart around it. This
file is the five-line format that ends the argument.

## The five lines

For every metric:

1. **What it counts** - the numerator, in events.
2. **Over what population** - the denominator, stated precisely.
3. **Over what window** - the period and the attribution window.
4. **Excluded** - internal users, test accounts, bots, cancelled orders, duplicates.
5. **Source of truth** - which tool, and what it is reconciled against.

Worked example:

> **Activation rate.** Numerator: users with `first_key_action_completed` within 7
> days of `signup_completed`. Denominator: users with `signup_completed` in the
> period. Window: signup cohort by week, measured at day 7. Excluded: internal
> domains, accounts deleted within 24 hours, duplicate signups by the same phone.
> Source: warehouse, reconciled monthly against the CRM's created-account count.

## Funnel design

| Element | Rule |
|---|---|
| Steps | Three to six. More than six and the drop-off per step is too small to act on |
| Step event | One canonical event per step, not "any event on the screen" |
| Order | Strictly ordered within the window, not "happened eventually" |
| Window | Stated: 24 hours for checkout, 7 days for activation, 30 for purchase |
| Re-entry | Decided: does a user who returns count once or per session |
| Segmentation | Two or three cuts maximum - platform, channel, new vs returning |

## The funnel table

| Step | Event | Users | Step conversion | Drop-off | Drop-off % of start |
|---|---|---|---|---|---|
| Landing | `page_viewed` (with utm) | 10,000 | - | - | - |
| Signup start | `signup_started` | 3,100 | 31% | 6,900 | 69% |
| Signup complete | `signup_completed` | 2,050 | 66% | 1,050 | 10.5% |
| Activation | `first_key_action_completed` | 780 | 38% | 1,270 | 12.7% |

Read the last column, not the step conversion: the biggest absolute loss is the
step to fix first, and it is almost never the one with the lowest percentage.

## Definitions that are argued about most

| Metric | The argument | The decision to write down |
|---|---|---|
| Active user | Logged in, or did something? | "Did a core action in the period" - logins flatter the number |
| Churn | Logo, revenue, or user? | Pick one per dashboard and label it |
| Revenue | Booked, collected, or net of refunds? | Collected, net of refunds and gateway fees, reconciled to the gateway |
| Conversion rate | Sessions or users? | Users, deduplicated by `user_id` |
| Repeat purchase | Second order ever, or in 90 days? | 90 days, stated on the chart |
| Trial conversion | At trial end, or within 30 days after? | At trial end, with a 7-day grace window |

## Windows and attribution

- **Attribution window** - how long after a touch a conversion is credited. State it;
  7-day click and 1-day view is a defensible default for most Indian D2C.
- **Cohort vs period** - a weekly cohort measured at day 7 is not the same as "users
  active this week". Label the chart with which one it is.
- **Timezone** - IST for an Indian business; a chart in UTC shifts the day boundary
  and makes Monday look different from what the team experienced.

## Sample size, honestly

- A funnel step with 40 users in the period is not a trend; it is noise. Show the
  count next to every percentage.
- Do not compare two weeks of a low-volume funnel and call the difference a change.
  State the volume, and say "too few to conclude" when it is.

## Anti-patterns

- Two dashboards with the same metric name and different definitions.
- A conversion rate with no denominator shown.
- "Revenue" that includes cancelled orders.
- A funnel that resets on a page reload.
- Redefining a metric to make the quarter look better - the definition is the audit trail.
- Reporting a percentage on nine users.
