# Deflection and measurement

The claim "this article reduced tickets" is easy to make and hard to prove. This
file is how to make it honestly, and what the number does not mean.

## The measure, in order

1. **Pick the cluster**, defined the same way as when it was mined: the same cause, the same words.
2. **Record the baseline** - tickets in the cluster per week, for the four weeks before publishing. Not the whole help centre.
3. **Publish and wait four weeks.** Two weeks is noise, especially in a business with a weekly cycle.
4. **Count again**, same cluster, same weeks.
5. **Check the confounders** - volume, seasonality, a product fix, a marketing push, a price change.
6. **Report as a range with the method**: "tickets in this cluster fell from 84 to 51 a month, a 39% drop, over four weeks with no release touching this flow."

## What deflection is not

| Tempting claim | Why it is wrong |
|---|---|
| "Tickets fell 12% after we published 8 articles" | Volume may have fallen 20%; the rate went up |
| "The article has 4,000 views, so it is working" | Views include support agents and internal staff |
| "Nobody contacts us about this any more" | They may have given up, or gone to a competitor |
| "Search ended in a click, so it deflected" | They clicked, read, and contacted support anyway |
| "Deflection rate is 60%" | A platform metric with its own definition, not yours |

## The four numbers that are actually observable

| Number | Source | Use |
|---|---|---|
| Cluster ticket count per week | Support desk, filtered by cause | The primary measure |
| Article views from external traffic | Help centre analytics, excluding staff IPs | Findability |
| Search → click, for the cluster's phrases | Help centre analytics | Title and term quality |
| "Was this helpful" ratio | Widget | Whether the article answers |

Anything else - saved hours, cost avoided, ROI - is a derived estimate. Derive it,
label it, and show the arithmetic.

## Estimating hours saved, honestly

```
hours saved per month = (baseline tickets − current tickets) × median handling time ÷ 60
```

Then discount it: not every avoided ticket would have been handled by a person,
and some move to another channel. A defensible statement is "between 6 and 11
support hours a month, at a median handling time of 9 minutes".

## When the number does not move

| Symptom | Likely cause | Fix |
|---|---|---|
| Views high, tickets unchanged | The article is findable but wrong, or answers a different question | Read the first two lines as a stuck person |
| Views low, tickets unchanged | Title and terms do not match the search | Rewrite the title, add synonyms, link from the error screen |
| Views low, tickets rising | The cluster was defined wrong, or a new cause appeared | Re-mine the tickets |
| Tickets fell, complaints rose | The article is being used to refuse help | Check the tone and the failure path |
| Everything fell | A product fix, a season, or a price change | Check the release log before claiming credit |

## Reporting to the founder

Four lines, monthly:

- Clusters written this month, and the hours they should save.
- The cluster that moved, with before and after.
- The cluster that did not move, and the diagnosis.
- The one article that should be retired.

No dashboard. A founder reads four lines; nobody reads a dashboard.

## Anti-patterns

- **Measuring the help centre as a whole.** Every other change lands in that number.
- **Claiming deflection in the week of publishing.** There has been no time to observe it.
- **Optimising for views.** Views are a proxy for findability, not for help.
- **Counting staff views.** They inflate every number and teach the wrong lesson.
- **A target deflection percentage set by management.** It produces articles written to hit a number, and a support team that stops logging causes.
