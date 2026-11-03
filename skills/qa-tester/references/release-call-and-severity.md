# The release call

QA does not ship the release. QA produces the evidence the product owner needs to
take the risk knowingly.

## The three verdicts

| Verdict | When | What you attach |
|---|---|---|
| **Ship** | No critical or high open; regression list green; the money paths verified | The matrix and the retest result |
| **Ship with named risk** | A high bug with a workaround, or a medium in a low-traffic path | The bug, the workaround, who accepted it, and the date it gets fixed |
| **Hold** | Any critical open, or money/data paths unverified | The evidence, and what must be true to unblock |

Never "ship, it will be fine". A verdict without evidence is an opinion.

## The pre-release checklist

- [ ] Acceptance criteria all pass
- [ ] Money path tested including failure and refund
- [ ] Auth tested including OTP, reset, and expiry
- [ ] Permissions tested from a lower role, including deep links
- [ ] Regression list green (the ten flows that must never break)
- [ ] One small Android device and one iPhone tested
- [ ] Second language and long strings checked, if the product supports them
- [ ] Error and empty states exist, not just the happy path
- [ ] Analytics events fire once, not twice
- [ ] Rollback path known and tested, or explicitly absent and accepted

## The residual risk line

Every release carries one. Write it as a sentence:

"Not covered this cycle: bulk order import (no test data), iOS 16 (no device).
Accepted by <name> on <date>. If bulk import is used in week one, expect issues
with files over 500 rows."

That sentence is what protects both the business and the tester.

## Release-day habits

- **Smoke test in production** within 15 minutes of deploy: log in, one money path in test mode if possible, one critical read.
- **Watch the error rate for an hour**, not a day.
- **Know the rollback trigger** before the deploy, not during the incident.
- **Keep the build number** that passed, so a rollback is a fact and not an argument.

## After an escape

When a bug reaches customers, do three things in the same week: write the case
that would have caught it into the matrix, add the flow to the regression list if
it is not there, and say which step of the plan was skipped. Not blame - the gap.

## Anti-patterns

- QA holding a release hostage over a cosmetic bug.
- QA signing off on the happy path because the deadline was yesterday.
- A "ship with risk" where nobody named is actually accepting the risk.
- No rollback plan because "it is a small change".
