# POC plan

The document this employee produces. Copy the structure; the content illustrates form.

## Frame

| Field | Value |
|---|---|
| Buyer | <company> |
| Deal | <value, stage, close date> |
| Technical stakeholder | <name, role, what they are measured on> |
| Buyer-side POC owner | <name> - provides access and answers inside 2 working days |
| Start / end | <2026-11-17 / 2026-12-12> |
| Decision meeting | <2026-12-15, decision maker invited> |
| Cost to us | <engineer days x rate + infra> |
| Exit if met | <commercial next step and who signs> |
| Exit if not met | <no-go, and what would change it> |

## Success criteria

| # | Criterion | Measurable target | Weight | Evidence |
|---|---|---|---|---|
| 1 | Invoice reconciliation at their volume | 5,000 invoices in under 4 min, under 0.5% unmatched | 50% | run log + buyer sign-off |
| 2 | ERP integration | nightly S/4HANA export, 40 fields, no manual mapping | 25% | load report |
| 3 | Usability | 2 named users complete month-end unassisted | 15% | session notes |
| 4 | Performance | 200 concurrent users, p95 under 800ms | 10% | load test |

Thresholds agreed in advance: go at 85+, conditional 70-84, no-go below 70.
Conditional means: proceed only if the failed criterion is re-tested inside 10 working days.

## Scope

| In scope | Out of scope |
|---|---|
| the four criteria above | any custom development |
| their sandbox ERP export | production cutover |
| two user sessions | training the wider team |
| load test on their data shape | SLA commitment |

## Plan

| Week | What happens | Who | Output |
|---|---|---|---|
| 1 | access, data, environment, criteria restated | us + their owner | signed criteria sheet |
| 2 | integration build and first run | us | integration log |
| 3 | volume test, user sessions | us + their users | evidence pack |
| 4 | scorecard, decision meeting | all | go / conditional / no-go |

## Scorecard at the end

| # | Target | Actual | Score | Weighted |
|---|---|---|---|---|
| 1 | 4 min / 0.5% | 3m 20s / 0.2% | 100 | 50.0 |
| 2 | 40 fields nightly | 40 fields, 11 min | 100 | 25.0 |
| 3 | 2 users unassisted | 2 users, 1 needed help | 70 | 10.5 |
| 4 | p95 800ms | p95 940ms | 85 | 8.5 |
| | | | **total** | **94.0 - go** |
