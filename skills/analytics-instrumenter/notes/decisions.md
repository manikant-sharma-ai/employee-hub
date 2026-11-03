# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-04 | Client-side or server-side for revenue? | Server-side, from the gateway webhook, keyed to `order_id` | Ad blockers and iOS limits make client-side revenue an estimate |
| 2026-11-04 | One event with a `feature_name` property, or one event per feature? | One `feature_used` with an enum property | Keeps the taxonomy stable as features change |
| 2026-11-04 | Renaming an event in place? | Never - new event, dual-fire 30-90 days, then retire | Silent renames break every historical comparison |
| 2026-11-04 | Can the plan ship after the release? | No - events firing is a release gate | Retrofit costs a sprint and loses the launch data |
