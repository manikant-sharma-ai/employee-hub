# POC and pilot design

A proof of concept is a paid-for decision, or it should not happen. The design is what turns three
months of free support into a dated answer.

## The one-page POC plan

| Field | Content |
|---|---|
| Objective | The single question this POC answers, in one sentence |
| Success criteria | 3-5 measurable tests, agreed in writing, with the threshold |
| Exit criteria | What makes it a no - agreed before the start, not after |
| Duration | Start and end dates, typically 2-4 weeks |
| Decision date | The date the buyer's decision-maker commits to |
| Owners | A named technical owner on each side |
| Data | What is provided, by when, and how it is handled and deleted |
| Environment | Sandbox, staging or production-like, and who pays for it |
| Support | Who is on call, during what hours |
| Cost | Free, paid, or credited against the contract - stated plainly |
| Outcome | What happens at the end either way: a proposal, a contract, or a written no |

## Success criteria that are actually testable

| Bad | Good |
|---|---|
| "The integration works" | "95% of 1,000 test orders sync within 15 minutes with zero manual correction" |
| "Users find it easy" | "3 of 4 named users complete the create-invoice task unaided in under 4 minutes" |
| "Performance is acceptable" | "The dashboard loads in under 3 seconds at 40,000 records" |
| "Reports are accurate" | "All 12 reconciliation lines match the ERP extract for 3 consecutive days" |

Every criterion needs a **number**, a **test method** and a **who measures it**. If two people would
score it differently, it is not a criterion.

## Exit criteria, agreed before the start

| Exit | Why it protects both sides |
|---|---|
| A mandatory field cannot be mapped | Stops a build on a broken assumption |
| The client cannot provide data by week 1 | Stops an open-ended wait |
| A required control fails the security review | Stops work that can never be deployed |
| Volumes exceed the documented limit | Stops a design that will not hold |
| The client's owner is unavailable for 10 days | Stops a POC that dies of inattention |

Write them as facts, not opinions. "If the API returns no item-level stock, the POC ends on that
date" is an exit criterion.

## The timeline that holds

| Week | Activity | Client dependency |
|---|---|---|
| -1 | Plan signed, data requested, environment prepared | Named owners, data format |
| 1 | Data received, mapping, first integration run | Data by day 2 |
| 2 | End-to-end test, exception handling, first review | 2 hours of owner time |
| 3 | User testing with the named users, tuning | 4 users, 45 minutes each |
| 4 | Score against criteria, decision meeting | Decision-maker, 60 minutes |

The most common failure is week one: the data arrives in week three and the POC is now six weeks
with a decision that has lost its momentum. Put the data date in the plan with a name against it.

## Security and compliance review, run in parallel

| Item | Ask for it in week 1 |
|---|---|
| Security questionnaire | Sent with the plan, answered in writing |
| Data residency and hosting | The specific region, and the sub-processors |
| Certifications | The certificate, current, with the scope |
| DPA and NDA | Signed before any real data is loaded |
| Access model | SSO, roles, audit log - demonstrated, not described |
| Data deletion | The date and the method, in writing |

A security review that starts in week three ends the POC in week six. It runs in parallel from day
one or the deal is not ready.

## Running it

| Rule | Why |
|---|---|
| One shared channel with the client's owner | Email threads lose the decision |
| A weekly 20-minute review with a written status | The buyer's boss needs a line to read |
| A defect log, visible to both | Perceived silence reads as failure |
| No scope additions without a date change | The classic POC death |
| A mid-point check against the criteria | Catches a "no" while there is time to act |
| The decision meeting booked at the start | A date in the diary is the only thing that ends a POC |

## Scoring, at the end

| Criterion | Threshold | Result | Pass |
|---|---|---|---|
| Sync accuracy | 95% | 97.4% | Yes |
| Sync latency | < 15 min | 11 min median | Yes |
| User task | 3 of 4 under 4 min | 3 of 4 | Yes |
| Dashboard load | < 3 s | 4.1 s at 40,000 records | No |

Then the recommendation: proceed, proceed with conditions (name them), or stop. A POC that ends
"we will continue to evaluate" was not a POC - it was a trial, and it should be said so in the
debrief.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| No decision date | The POC becomes free support with no end |
| Criteria written after the result | Every result passes, and nobody believes it |
| Real data before the DPA | A compliance incident in the first week |
| Scope added mid-POC without a date change | The POC fails on time, not on capability |
| No named client owner | Nothing gets scheduled, and the POC stalls |
| Security review started late | The deal dies after the technical win |
| Free POC with no exit criteria | The competitor's evaluation, at your cost |
| No debrief on a loss | The next POC repeats the same failure |
