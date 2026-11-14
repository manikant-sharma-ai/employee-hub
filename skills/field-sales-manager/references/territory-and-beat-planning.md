# Territory and beat planning

A territory is a set of outlets and a number of days. Most field plans fail because nobody divided one by the
other before assigning the route.

## The arithmetic that decides everything

```
productive calls per day = (calls available per day) - (travel time / time per call)
days per cycle         = outlets by class / calls per day, per class frequency
```

Worked shape for a small Indian FMCG or hardware business:

| Input | Value |
|---|---|
| Outlets | 1,400, of which A 180, B 420, C 800 |
| Frequency | A weekly (4/month), B fortnightly (2/month), C monthly (1/month) |
| Calls needed per month | 180x4 + 420x2 + 800x1 = 2,360 |
| Reps | 6 |
| Working days per month | 26, minus 1 admin = 25 |
| Calls needed per rep per day | 2,360 / (6 x 25) = **15.7** |
| Realistic productive calls per day | 12-18 in a dense town, 8-12 in a spread-out district |

If the number is above 20, the plan is a wish. Fix it by dropping C outlets to a two-monthly frequency, or by
serving the smallest through the distributor's own salesman, or by adding a rep - in that order of cost.

## Outlet classification

| Class | Definition | Frequency | Time per call |
|---|---|---|---|
| A | Top 10-15% by monthly value or footfall | Weekly | 15-20 min |
| B | Next 25-30% | Fortnightly | 10-12 min |
| C | The long tail | Monthly or two-monthly | 5-8 min |
| New | Added in the last 90 days | Weekly for 4 weeks, then by class | 15 min |
| Dormant | No order in 60-90 days | One revival attempt, then class C | 10 min |
| Do not visit | Credit risk, dispute, or commercially excluded | None | - |

Classification by potential, not by current sales. An outlet with a big footfall and a small order is an A with
a share-of-shelf problem, and it is where the growth is.

## Clustering: the map before the plan

1. Plot the outlets on a map by pin code.
2. Cluster into groups a rep can cover in one day: 12-18 outlets in a dense town, 8-12 in a district.
3. Check the cluster against the market day and the shut day of that town - a cluster that lands on the shut day
   is a wasted day, every week, forever.
4. Measure the actual travel: distance and time between consecutive outlets, from the map, not from a guess.
5. Assign clusters to reps by where they live, not by an even split on paper. A rep who lives in the cluster
   starts at 9am; one who does not starts at 11am.

## The PJP, as a document

| Day | Beat | Outlets | Class mix | Calls planned | Travel share |
|---|---|---|---|---|---|
| Mon | Town A, north | 16 | A4 B6 C6 | 15 | 22% |
| Tue | Town A, south | 15 | A3 B7 C5 | 14 | 25% |
| Wed | Town B | 11 | A2 B5 C4 | 10 | 38% |
| Thu | Town C + market day | 14 | | 13 | 20% |
| Fri | Town A, north (repeat A outlets) | 10 | A10 | 10 | 15% |
| Sat | New outlets + dormant revival | 12 | | 10 | 30% |

A PJP is printed, signed and posted. It changes on a stated review, not on a Tuesday because a rep felt like it.

## Travel share, the hidden cost

| Travel share of the day | Reading |
|---|---|
| Under 20% | Dense beat; watch for too many small outlets |
| 20-30% | Healthy for a district |
| 30-40% | Acceptable only for high-value outlets |
| Over 40% | The territory is too large, or the cluster is wrong |

At ₹6,000 of fuel a month plus a ₹28,000 salary, a rep at 40% travel costs the business about ₹13,600 a month in
travel time alone. That is the number to put beside a beat that "looks fine on paper".

## Territory design, four decisions

| Decision | Options | The trade-off |
|---|---|---|
| Split by geography or by channel | Town-based beats vs modern-trade-only beats | Channel splits need different skills and pay |
| Split by value or by count | Equal potential vs equal outlet count | Equal count produces unequal income and attrition |
| Overlap or not | One rep per outlet vs shared | Overlap causes credit and order disputes, always |
| Distributor-led or direct | Distributor's salesman vs your rep | Distributor-led is cheaper and gives you no data |

## Opening a new territory

| Step | Detail |
|---|---|
| 1 | Count outlets and potential from a market survey, not a census list |
| 2 | Find the distributor before the rep: coverage and credit decide viability |
| 3 | Start with A and B only, at a frequency the rep can hold |
| 4 | Set a 90-day coverage target, not a sales target |
| 5 | Add C outlets only when the A and B coverage is above 90% |
| 6 | Review at day 30, 60 and 90 against coverage, strike rate and drop size |

## Anti-patterns

- **A beat designed in the office with no map.** Travel time is the thing that breaks it, and it is invisible on a
  spreadsheet.
- **Uniform frequency.** Every outlet visited equally means the A outlets are underserved and the C outlets are
  over-served, at the same cost.
- **A rep covering two towns 40km apart, daily.** The fuel and the fatigue both show up as "market is slow".
- **New outlets folded into an existing beat with no extra time.** They are the first thing dropped on a busy day.
- **A PJP that ignores market day.** One day a week, structurally, at zero return.
- **A territory with no dormant-outlet process.** The list shrinks by attrition and nobody notices for a year.
