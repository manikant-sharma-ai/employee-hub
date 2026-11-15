# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-16 | What this role owns, given `inventory-planner` | The demand number; reorder points and safety stock stay theirs | A forecast without a policy is a number; a policy without a forecast is a guess |
| 2026-11-16 | What this role owns, given `budget-planner` | Units by period; the revenue and cash plan stay theirs | Units forecast better than rupees, and rupees are derived |
| 2026-11-16 | Grain | Forecast where the signal is - SKU for high volume, family for low | A six-units-a-month SKU has no readable pattern |
| 2026-11-16 | Stockouts | Marked and restored or modelled at family level, never left as zeros | Zeros teach the model that demand fell exactly when it peaked |
| 2026-11-16 | Seasonality | Built from own history, aligned to festival weeks, never copied | The lunar calendar moves the peak every year |
| 2026-11-16 | Method | Chosen per series class, benchmarked against naive | A method that cannot beat last year's number is noise |
| 2026-11-16 | Accuracy | Out-of-sample only; bias reported with error | In-sample fit flatters and bias compounds in a purchase plan |
| 2026-11-16 | Output form | Point estimate plus an 80% interval | The interval is what a planner holds stock against |
| 2026-11-16 | Judgemental adjustment | Allowed for known events, logged, scored separately | Human overlays are usually worse than the model and the record proves it |
| 2026-11-16 | Targets | Never adjusted to a target or a founder expectation | A forecast that is a target is not a forecast |
