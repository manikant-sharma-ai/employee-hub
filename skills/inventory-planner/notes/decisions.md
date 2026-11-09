# Decisions

| Date | Question | Decision | Why |
|---|---|---|---|
| 2026-11-10 | What this role owns, given `procurement`, `bookkeeper` and `demand-forecaster` | The stock policy: classification, reorder points, safety stock, dead-stock action, season build, purchase plan | Procurement buys one thing well; this role decides how much of everything to hold |
| 2026-11-10 | Who places the order | `procurement` and the buyer; this role recommends quantity and date | A policy that also negotiates loses its objectivity on the buffer |
| 2026-11-10 | Forecast depth | Simple baseline plus a written season adjustment; statistical uplift is `demand-forecaster` (backlog #70) | One role cannot own both the policy and the model without one of them being thin |
| 2026-11-10 | Service levels | Set by class: A 97-98%, B 95%, C 90%, each with the cost of the step up shown | The founder buys the service level; this role prices it |
| 2026-11-10 | Dead-stock floor | Written before any negotiation, with a named approver | A floor set during the negotiation is not a floor |
| 2026-11-10 | Liquidation ladder | Bundle first, B2B lot third, marketplace clearance only with a separate listing | Clearance in the main channel resets the price reference permanently |
| 2026-11-10 | Valuation and provision | Recommended by this role, set by the accountant | Inventory valuation is an accounting judgement with tax consequences |
| 2026-11-10 | Confidentiality | No supplier terms, stock values or customer names in the repo or in notes | The repo is public; the commercials are not |
