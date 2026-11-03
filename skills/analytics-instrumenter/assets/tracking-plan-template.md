# Tracking plan - <product> <release> - v1 - <YYYY-MM-DD>

**Owner:** <name>  **Implementer:** <name>  **Tools:** <GA4 / Mixpanel / warehouse>
**Release date:** <date>  **QA gate:** no release until every row below is QA-passed
**Consent basis:** <analytics consent / legitimate use, as advised by the privacy owner>

## 1. The questions this plan answers

| # | Question | Who asks | How often | Decision it changes |
|---|---|---|---|---|
| Q1 | | | | |
| Q2 | | | | |
| Q3 | | | | |

## 2. Journeys and failure points

| Journey | Step | Event that marks it | Failure path event |
|---|---|---|---|
| Signup | Landing → form → OTP → dashboard | `signup_started`, `signup_completed` | `verification_failed` |
| Checkout | Cart → address → payment → confirmation | `checkout_started`, `order_paid` | `payment_failed` |
| Activation | First session → first key action | `first_key_action_completed` | - |

## 3. Events

| Event | Description | Trigger | Platforms | Properties (type, required) | Owner | Q | Status |
|---|---|---|---|---|---|---|---|
| `page_viewed` | Page rendered | on route change, once per path | web | `path` string req; `utm_source` string opt; `utm_campaign` string opt | | Q1 | planned |
| `signup_started` | Signup form opened | on form mount | web, android, ios | `method` enum req (email, google, otp) | | Q1 | planned |
| `signup_completed` | Account created | server, after DB commit | server | `method` enum req; `user_id` string req | | Q1 | planned |
| `first_key_action_completed` | First core action | server, first occurrence only | server | `action_name` enum req | | Q1 | planned |
| `checkout_started` | Payment screen reached | after cart validation | web, android | `cart_value_inr` number req; `item_count` number req | | Q2 | planned |
| `order_paid` | Payment captured | gateway webhook, verified | server | `order_id` string req; `amount_inr` number req; `payment_method` enum req | | Q2 | planned |
| `payment_failed` | Payment attempt failed | gateway failure callback | server | `order_id` string req; `failure_code` string req | | Q2 | planned |

**Naming:** `object_action`, snake_case, past tense. **Never** in properties: email,
phone, name, address, PAN, Aadhaar, free-text input.

## 4. Metric and funnel definitions

| Metric | Numerator | Denominator | Window | Excluded | Source |
|---|---|---|---|---|---|
| Signup completion | `signup_completed` users | `signup_started` users | same session | internal IPs, bots | warehouse |
| Activation | `first_key_action_completed` within 7 days | `signup_completed` cohort | 7 days | deleted accounts | warehouse |
| Paid conversion | `order_paid` orders | `checkout_started` users | 24 hours | test orders | gateway, reconciled |

## 5. Dashboard

| Reader | Page | Charts (one decision each) | Grain | Refresh |
|---|---|---|---|---|
| Founder, Monday 9 a.m. | Ops one-pager | signups vs target; funnel drop-off; revenue collected | weekly | daily |

## 6. QA evidence

| Event | Fires once | Properties correct | Platform tested | Consent respected | Result |
|---|---|---|---|---|---|
| | | | | | |

**Reconciliation (one full day):** `order_paid` vs gateway: <n vs n, gap n%>.
**Not tested:** <event, platform, path>

## 7. Changelog

| Version | Date | Change | Migration |
|---|---|---|---|
| v1 | | Plan created | - |
