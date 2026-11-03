# Event taxonomy

A taxonomy is a naming system, and its only job is that two people describe the
same action the same way without asking each other.

## The naming rule

`object_action`, snake_case, past tense for something that completed.

| Good | Bad | Why |
|---|---|---|
| `signup_completed` | `SignUp`, `sign_up`, `signedup` | Case, spacing and tense drift across platforms |
| `order_paid` | `payment`, `pay_now_click` | Says what happened, not what was clicked |
| `cart_viewed` | `viewCart` | camelCase breaks SQL and BigQuery column names |
| `plan_upgraded` | `upgrade` | The object makes the question answerable |
| `invoice_downloaded` | `download` | `download` of what? |
| `search_performed` | `search` | Completed action, not intent |

Rules: lowercase, underscores, no spaces, no dots, no version suffix in the name,
maximum 40 characters, and the same string on web, iOS, Android and server.

## The property rules

| Rule | Example | Why |
|---|---|---|
| Fixed type per property name | `amount` is always a number, never sometimes a string | Breaks every aggregate silently |
| Currency and unit in the name or the value | `amount_inr`, `weight_kg` | Mixed currencies destroy a revenue chart |
| Enumerated values, not free text | `plan_tier: "starter" \| "growth" \| "scale"` | Free text becomes 400 spellings |
| No personal data | Never email, phone, name, address, PAN, Aadhaar, full IP | Privacy incident and a DPDP problem |
| No user-entered text | Not the search query, not the note, not the address | People type their phone number into search boxes |
| IDs, not joins | `customer_id` internal, joined in the warehouse | Keeps events small and lawful |
| A screen or route where relevant | `screen: "checkout_payment"` | Makes funnel debugging possible |

## The core set - twenty events most businesses need

Not a template to copy wholesale; a checklist to prune.

| Area | Events |
|---|---|
| Acquisition | `session_started`, `page_viewed`, `campaign_landed` (with utm params) |
| Signup | `signup_started`, `signup_completed`, `verification_completed` |
| Activation | `onboarding_step_completed` (with `step_name`), `first_key_action_completed` |
| Core use | `feature_used` (with `feature_name`), `search_performed`, `item_viewed` |
| Commerce | `product_viewed`, `add_to_cart`, `checkout_started`, `order_paid`, `payment_failed` |
| Retention | `session_started` (repeat), `subscription_renewed`, `subscription_cancelled` |
| Support | `support_requested`, `refund_requested` |

`payment_failed` is the event most often missing and the one most often needed: it
is where revenue leaks and where the fix is usually a UI change.

## What not to track

- Every button click. It produces volume and answers nothing.
- Page scroll depth as a proxy for interest, unless the page is a long article.
- Hover and mouse movement.
- Anything that can be derived - `order_count` on the event, when it can be counted.
- Anything that identifies a person, or that a person typed.
- Health, biometric, caste, religion, sexual orientation, political opinion - unless
  there is a lawful basis, a written approval and a genuine product need.
- A "user_score" computed in the client, which will disagree with the warehouse.

## Versioning the taxonomy

| Change | Handling |
|---|---|
| New event | Add to the plan with an owner and a question; no migration |
| New property | Add as optional, backfill not required; note the date |
| Renamed event | New event, dual-fire for 30-90 days, then retire; record in `notes/decisions.md` |
| Removed property | Deprecate with a date; check dashboards first |
| Changed type | Never in place; new property name |

## Anti-patterns

- One event called `click` with a property describing what was clicked.
- Platform prefixes (`android_signup`) instead of a platform property.
- `event_name`, `eventName` and `EventName` in the same warehouse.
- Sending the whole user object as properties "for convenience".
- Tracking the campaign in the event name (`diwali_2026_sale_view`) instead of in UTM parameters.
- A taxonomy that lives in a slide deck and nowhere near the code.
