# Regression and release gate

A regression suite is a memory. Its job is not coverage, it is preventing the second occurrence of a failure that already happened once.

## The rule that keeps the suite useful

**Every defect that reaches production adds exactly one test.** Not a paragraph in a post-mortem - a test, in the suite, that would have caught it. Within the same week.

A suite that grows this way stays small, stays trusted, and every test in it has a reason a person can name.

## The smoke suite - ten minutes, every deploy

| # | Check |
|---|---|
| 1 | Home page loads, no console errors |
| 2 | Login with a test account succeeds |
| 3 | The primary product or content page renders |
| 4 | Search returns results for a known term |
| 5 | Add to cart, or the primary conversion action |
| 6 | Checkout reaches the payment step (do not complete a real charge) |
| 7 | A test order is visible in admin |
| 8 | The confirmation email arrives, with the right amount |
| 9 | Logout works and the session is gone |
| 10 | The last two regression bugs are still fixed |

Ten checks, run before every deploy, beats a 400-case suite run monthly. Anything that cannot be checked in ten minutes belongs in the deeper suite, not the gate.

## The go/no-go gate

Ship when all of these are true:

- Smoke suite green.
- No open severity 1 or 2 defects.
- The critical paths from the test plan passed on this build.
- Rollback has been confirmed available, and someone knows how to run it.
- The untested list is written and accepted by name.
- Monitoring is on for the changed surface, with an alert that will actually fire.

Do not ship when any of these is true:

- "It worked on staging" is the only evidence and staging differs from production in a way nobody has described.
- A migration runs without a tested rollback.
- A new third-party integration has never failed in a test.
- The person who understands the change is unreachable for the next four hours.

## What to cut when time is short

Cut in this order, and say what you cut:

1. Cosmetic and rare-path cases.
2. Depth on low-risk surfaces.
3. Cross-browser coverage beyond the top two.
4. **Never** the money path, the auth path, the data-loss path, or the smoke suite.

A release tested for two hours on the right four paths is safer than one tested for two days on everything equally.

## After the release

| Window | What to watch |
|---|---|
| First hour | Error rate, 5xx count, checkout success rate |
| First day | Support ticket volume against the same weekday last week |
| First week | The defect that escaped, and the test it earns |

An escaped defect is not a failure of the tester, it is the suite telling you what it was missing. Add the test, and note in `notes/learnings.md` what class of failure the suite did not cover.

## Anti-patterns

- A regression suite nobody runs because it takes four hours.
- Tests that were written once and never updated when the feature changed.
- Skipping the smoke suite "because the change was small" - small changes cause most incidents.
- A gate with six conditions where five are routinely waived.
- Adding a test for every bug and never removing the ones that can no longer fail.
- Rollback that exists in a document and has never been run.
