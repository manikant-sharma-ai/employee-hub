# Prioritisation

Prioritisation is not a ranking exercise; it is a rule that produces the same answer twice. The value of a rule is that the tenth decision looks like the first, and the argument moves from status to inputs.

## The rule that works for a small business

Score every candidate on four inputs, 1-5 each, and multiply the first two and divide by the third:

**Score = (Value x Confidence) / Effort**

| Input | 1 | 3 | 5 |
|---|---|---|---|
| Value | Nice to have, no number attached | Moves a metric by a few percent | Unblocks revenue or retention directly |
| Confidence | A hunch | Some tickets, no interviews | Interviews plus usage data |
| Effort | A day | Two to four weeks | A quarter |

Then adjust with one tie-breaker, stated openly: **reversibility**. A cheap, reversible bet outranks a slightly higher-scoring irreversible one.

Write the scores down where everyone can see them. The argument about the inputs is the useful part; the ranking is just arithmetic.

## The four tests before anything gets scored

1. **Is it frequent?** Does this happen weekly to the same users, or once a year to someone?
2. **Is it costly?** Money, time, a lost order, a support call. Quantify it in the customer's terms.
3. **Is a product change the cheapest fix?** A help article, a policy change, a sales script or a manual step is often cheaper and faster.
4. **Is it already solved?** Check the tracker and the codebase before adding the fifty-first thing that does what the fifth thing does.

Most requests fail at 3, not at 1 or 2. That is the finding worth reporting.

## Frameworks, and when they lie

| Framework | Use | Where it misleads |
|---|---|---|
| RICE | Comparing many candidates with real inputs | Reach numbers are usually invented in a small business |
| MoSCoW | Agreeing scope in one meeting | "Must" becomes everything |
| Kano | Understanding what delights vs what is expected | Survey-heavy, slow, and the answers drift |
| Weighted scoring | When stakeholders need explicit weights | Weights get tuned to produce the answer someone wanted |
| Cost of delay | When timing genuinely matters - a season, a regulation | Encourages urgency theatre |

Use one, name it, and do not switch frameworks to get a different answer.

## The four buckets that make a roadmap honest

Every quarter's work fits in one of these, and the split matters more than the list:

| Bucket | Share | Content |
|---|---|---|
| Keep the lights on | 20-30% | Bugs, support escalations, security, compliance |
| Make it work better | 20-30% | Reliability, speed, the flow everyone complains about |
| Grow | 30-40% | The thing that moves the goal metric |
| Bets | 10-20% | One experiment that might be nothing |

A plan with 100% in "grow" ships nothing, because the lights go out. A plan with 100% in "keep the lights on" is a business standing still.

## Saying no with the rule, not with the mood

> "This scores 12 against the 30 of the top item. It is not that it is a bad idea - it is that the effort is three weeks and the confidence is a hunch. If we can get five customer conversations by Friday, the confidence doubles and it moves up."

This works because it is not a rejection of the person. It names what would change the answer, which is the only respectful no.

## Sequencing, not just ranking

Two items can both be worth doing and still not be doable in the same month, because they touch the same code, the same person, or the same customer conversation. Check:

- **Technical coupling** - does one change the data model the other needs?
- **Person coupling** - does one person have to do both?
- **Learning order** - does one answer the question the other depends on?

Do the one that unblocks the other first, even when it scores lower.

## Anti-patterns

- **The loudest customer's request at the top.** It is one data point with a phone call attached.
- **A stack rank with no scores.** It is a preference list with authority behind it.
- **Scoring after the decision** to justify it.
- **A roadmap with 30 items.** A quarter has room for three to five things that matter.
- **"We'll do both."** Then neither ships on time, and the team learns that estimates are fiction.
- **Prioritising features when the bottleneck is onboarding or pricing.** Say so; it is often the highest-value finding in the document.
