# Counting and prioritisation

A theme list becomes a decision when it is ranked, and ranking is where most reads quietly cheat.

## The four axes

| Axis | How to measure | Why it is separate |
|---|---|---|
| Frequency | Customers raising it ÷ customers in the corpus | Demand |
| Severity | Does it block the job, cost the customer money, or merely annoy | A blocking issue at 5% outranks an annoyance at 40% |
| Revenue at stake | Sum of monthly value of the customers raising it, or the deals lost | Weight, and the argument that wins a meeting |
| Strategic fit | Does fixing it compound with where the business is going | Prevents fixing something the business is leaving |

Do not collapse them into one score. Show four columns and rank by a stated rule. A single composite score hides
the judgement, and a hidden judgement cannot be argued with, which is the opposite of what evidence is for.

## The severity scale

| Level | Definition | Example |
|---|---|---|
| S1 - Blocking | The customer cannot complete the core job | Checkout fails; the app will not log in |
| S2 - Costly | It works, but the customer loses money or time every time | Wrong invoice, GST details missing, 9-day delivery |
| S3 - Trust | It works, but the customer stops believing the business | Damaged packaging, unanswered messages, surprise charge |
| S4 - Friction | Extra steps, confusion, minor annoyance | Hard-to-find setting, unclear label |
| S5 - Preference | A wish, not a problem | "Please add dark mode" |

A theme's severity is the severity of its typical case, not its worst. Say which you used.

## Weighting, when it is honest

| Weighting | Use it when | Do not use it when |
|---|---|---|
| By monthly value | The top 10% of customers pay 60% of revenue | It silences the long tail that will be the base next year |
| By plan | Tiers have genuinely different needs | The cheap plan is where all the growth is |
| By tenure | Onboarding themes need new customers weighted | You are trying to make an old complaint look small |
| Unweighted | The default | Never - always at least show the unweighted count beside it |

Show the weighted and unweighted counts side by side, always. The gap between them is the finding: if a theme
is huge unweighted and small weighted, it is a small-customer problem, and the business should decide whether
that is where it is going.

## The ranking rule, written down

A defensible default, in order:

1. Any S1 theme above 5% of the corpus goes first.
2. Then the theme with the highest revenue at stake.
3. Then the highest unweighted frequency.
4. Then the highest strategic fit.
5. Ties broken by the cheapest fix.

Write the rule in the read. If the founder overrides it, the override is visible and can be recorded in
`notes/decisions.md`, which is what stops the same argument next quarter.

## What a percentage can and cannot say

| Sentence | Allowed | Why |
|---|---|---|
| "31 of 214 customers who wrote to us raised this" | Yes | Counted, with a denominator |
| "14% of our customers want faster delivery" | No | The corpus is not the customer base |
| "This theme grew from 12 to 31 between Q2 and Q3" | Yes, if the corpus size is comparable | Movement is the useful signal |
| "This is our number one issue" | Only with the rule stated | Ranked by what, on what basis |
| "Customers are furious" | No | Sentiment is not measured by counting themes |

## Theme movement, the part that pays for the exercise

| Movement | Reading | Action |
|---|---|---|
| Grew, corpus stable | A real regression, or a launch side-effect | Investigate the release calendar |
| Grew, corpus grew | Possibly proportional - check the share | Compare shares, not counts |
| Shrank after a fix | The fix worked | Say so publicly, and tell the customers who raised it |
| Shrank with no fix | The affected customers churned | Cross-check the churn list; a theme can disappear because its customers left |
| Appeared from nowhere | A new cause, often a vendor or a policy change | Check the date distribution inside the theme |

That fourth row is the trap. A vanishing complaint is not always a solved one.

## Costing a theme, when the numbers exist

| Input | Where it comes from |
|---|---|
| Tickets per theme | The codebook count |
| Minutes per ticket | The helpdesk's handling time, or a sample of ten |
| Fully loaded cost per agent hour | Payroll ÷ productive hours |
| Refunds or credits tied to the theme | The ledger, by reason |
| Churned customers citing it | Cancellation forms and the churn list |

A theme that costs ₹1.8 lakh a year in support time and ₹4 lakh in refunds is a different conversation from one
that costs nothing but annoys people. Put the number in when it exists; write "not costed" when it does not.

## Anti-patterns

- **Ranking by the loudest voice in the room.** The read exists to prevent this; a read that agrees with the
  loudest person has failed.
- **A weighted score with no weights shown.** That is a preference wearing a spreadsheet.
- **Counting mentions.** One angry customer with forty messages becomes the top theme.
- **Ignoring the cheap fix.** A 20-minute copy change that removes a 30% friction theme should be done before the
  six-week feature.
- **Comparing two quarters with different codebooks.** Then the movement is the codebook, not the customers.
