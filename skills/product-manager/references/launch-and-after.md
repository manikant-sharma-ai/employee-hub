# Launch and after

A launch is a checklist with owners and a way back. The date is the least interesting thing about it.

## The checklist

| Area | Item | Owner |
|---|---|---|
| Product | Acceptance criteria verified on production data, not just staging | |
| Product | Empty, loading, error and permission-denied states checked | |
| Content | Every new string written, reviewed and translated where needed | |
| Content | Help article, FAQ or macro for support, live before customers see it | |
| Permissions | Feature flag or access list correct; who can see it and who cannot | |
| Data | Migration run, reversible, and verified on a copy | |
| Money | Price, GST treatment and invoice wording correct if money is involved | |
| Analytics | The event fires, and the dashboard shows it | |
| Monitoring | Error alert, the threshold, and who is woken | |
| Support | The team knows what changed and what to say | |
| Sales | The team knows what to say, and what not to promise | |
| Rollback | Tested, with the trigger for using it and who decides | |
| Comms | Who is told, in what order, and by whom | |

Thirteen lines. The three that slip are always content, permissions and rollback.

## Rollout shapes

| Shape | Use | Risk |
|---|---|---|
| All at once | Internal tools, small user base, low risk | No containment |
| Percentage | Consumer features, gradual | Needs a flag and a way to segment |
| Named cohort | B2B, high-value accounts | Slower learning |
| Silent launch | Infrastructure, pricing plumbing | Nobody notices, so nobody complains - and nobody adopts |
| Beta with a promise | When feedback is the point | Creates an expectation of the feature staying |

## The two read dates

Set them before launch, in the PRD:

- **Two weeks** - is it being used at all? Adoption, error rate, support tickets. This read answers "is it broken or invisible".
- **Six weeks** - did the goal metric move? This read answers "was the hypothesis right".

Between them, the decision: iterate, keep, or kill. Write the decision rule in advance:

> "If adoption is under 10% of the target segment at six weeks, we kill it rather than iterate a second time."

A rule written after the numbers arrive is not a rule.

## The launch note

One page, sent the day it goes live:

1. **What changed** for the customer, in one sentence.
2. **Who it affects**, and whether anything they do today behaves differently.
3. **What to say** if someone asks, and what not to promise.
4. **Where to send problems**, with a name.
5. **When the first read is**, and what it will decide.

## Post-launch, honestly

- **Report the miss.** The feature that landed at 4% adoption is the most valuable information the team has that month.
- **Separate the failure modes**: not built right, not discoverable, not needed. Three different fixes.
- **Write the learning into `notes/learnings.md`** as a rule, not a story.
- **Do not quietly delete a failed feature.** Remove it deliberately, with a note, or it will be found later by someone who wonders what it was for.

## Anti-patterns

- **Launching on a Friday** in a business where nobody works the weekend.
- **A launch with no rollback** because "it's just a small change". Small changes cause most outages.
- **No analytics event**, so the six-week read is an argument.
- **Shipping to everyone because flags are extra work.** The flag is cheaper than the incident.
- **Announcing before it works** for the whole user base. Announce to a cohort, then to everyone.
- **A "beta" label left on for a year.** It stops being a beta and becomes an unfinished product.
