# Learnings - analytics-instrumenter

1. **Questions come before events.** An event that serves no named question is storage cost, app weight and privacy surface.
2. **Money events fire server-side.** Client-side `order_paid` loses 10-30% to ad blockers and iOS limits, and revenue charts then argue with the gateway forever.
3. **`payment_failed` is the event everyone forgets and the one that finds the leak.** Instrument the failure path in the first plan, not the second.
4. **One name, everywhere, or the funnel has a missing step.** Platform differences are properties, not prefixes.
5. **A rename is a migration, not an edit.** Dual-fire for 30-90 days, record the date, or last quarter stops being comparable.
6. **Instrumentation is a release gate.** Saying it once at the start is cheaper than a retrofit after the launch.
