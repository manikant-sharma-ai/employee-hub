# Charting and the readout

A chart is an argument, not a decoration. If the reader cannot get the point in three seconds without you talking, the chart has failed - and if it gets the point across by distorting the data, it has done worse than fail.

## Chart choice, by the question

| The question | Chart | Never |
|---|---|---|
| How has it changed over time? | Line, with the period on the x-axis | Pie |
| How do categories compare? | Horizontal bar, sorted by value | 3D bar |
| What is the composition? | Stacked bar, or a single stacked bar for one total | Pie with more than 4 slices |
| How are two things related? | Scatter | Line chart between unordered categories |
| Where is the concentration? | Pareto (bar + cumulative line) | Word cloud |
| How does the funnel drop? | Horizontal funnel or a bar with rates annotated | A literal funnel drawing |
| What is the distribution? | Histogram or box plot | Mean-only summary |

Rules that do not bend:

- **Sort bars by value**, unless the categories have a natural order (months, stages).
- **Start the y-axis at zero for bars.** A bar chart truncated at 80 distorts by construction.
- **Line charts may start away from zero** if the variation is the point - and then say so in the subtitle.
- **One chart, one message.** Put the message in the title: "Revenue fell 9% in October, entirely in the North" not "Monthly Revenue".
- **Label the units and the period** on the axis or the subtitle. ₹ lakh, FY26, IST.
- **No more than 4-5 series.** Beyond that, small multiples or a table.

## Titles that do the work

| Weak | Strong |
|---|---|
| "Sales by month" | "October sales fell ₹18 lakh, all of it in two SKUs" |
| "Customer distribution" | "Eleven customers produce 62% of margin" |
| "Churn rate" | "Churn is flat at 4%, but revenue churn has doubled" |
| "Marketing spend" | "Spend is up 40% and new customers are down 12%" |

The title is the finding. The chart is the evidence. If you cannot write a finding-shaped title, you have not found anything yet.

## Honest charting

| Distortion | How it happens | Fix |
|---|---|---|
| Truncated axis | Starting a bar chart at 90 | Zero for bars; annotate a truncated line |
| Wrong aspect ratio | A flat line made steep by a tall frame | Keep the frame proportional; show the full range |
| Dual axes | Two series on different scales implying a relationship | Two charts, or index both to 100 |
| Cherry-picked window | Starting the line where the story begins | Show the longer series, mark the chosen window |
| Cumulative-only | A cumulative line that can only go up | Show the monthly deltas too |
| Percentage without base | "300% growth" from 4 to 16 | Annotate the counts |
| 3D and shadows | Any | Remove |
| Rainbow colours | 12 categories in 12 hues | One accent colour, greys for the rest |

## Tables vs charts

Use a table when the reader needs the exact number, when there are fewer than ~12 rows, or when the data is a comparison across two dimensions. Use a chart when the shape of the data is the point.

A table people will act on should: sort by the column that matters, right-align numbers, use one unit per column, and bold only the total.

## The one-page readout

The format that gets read. Everything else is appendix.

```
1. The answer          - one or two sentences, with the number and the comparison
2. The definition      - numerator, denominator, window, exclusions (three lines)
3. The evidence        - one chart or table, titled with the finding
4. What is driving it  - the decomposition, factor by factor, with contribution
5. What to do          - the specific action, and who owns it
6. What would change my mind - the condition under which this is wrong
7. What I could not check    - gaps, exclusions, assumptions
8. The artifact        - script / sheet / query, so it can be re-run
```

Rules:

- **The answer goes first.** A readout that builds to the finding is a readout that gets skimmed and misquoted.
- **One page.** If it needs two, the second is the appendix.
- **Every number has a unit, a period and a source.**
- **The recommendation is an action, not an observation.** "Stock is over-concentrated" is an observation. "Stop reordering the 9 slow SKUs and clear them at 30% through bulk" is an action.
- **Say what would prove you wrong.** It is the cheapest way to be trusted.

## Presenting numbers in a deck

- **One number per slide**, in the headline, at a size that cannot be missed.
- **The chart is evidence, not the slide.** The slide is the sentence.
- **Round for the audience.** ₹18.4 lakh in the room; ₹18,41,250 in the appendix.
- **Never show a chart you cannot explain in one sentence**, including where the data came from.

## Anti-patterns

- A pie chart with nine slices.
- A dashboard where every metric is the same size, so nothing is prioritised.
- A chart with a legend the reader has to match by colour to a line.
- Red/green used for anything other than bad/good, and only where that reading is universal.
- Showing a metric that went up because the denominator went down, without saying so.
- A readout that ends with "more analysis is needed" and no named next step.
- Rebuilding the chart in PowerPoint instead of exporting the one that matches the table.
