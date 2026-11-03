# Dashboard spec

A dashboard is a decision surface, not a data display. One reader, one page, one
decision per chart.

## The spec header

| Field | Content |
|---|---|
| Reader | A named role - "founder, Monday 9 a.m." not "the team" |
| Cadence | Daily, weekly or monthly - decides the grain |
| The five questions | What this person must be able to answer in two minutes |
| Source of truth | Which tool, and what it reconciles against |
| Owner | Who fixes it when a number looks wrong |

## Chart selection by question

| Question | Chart | Not this |
|---|---|---|
| How is the trend? | Line, with the same period last year faint behind it | A pie |
| What is the mix? | Stacked bar or a table with percentages | A 3-D pie with 9 slices |
| Where do we lose people? | Funnel with absolute counts | A bar chart of percentages alone |
| Which segment is different? | Small multiples or a sorted bar | A scatter of everything |
| Did the change work? | Before/after with the intervention marked | Two charts side by side with no annotation |
| Is anything off today? | One big number with a threshold and a sparkline | A wall of 24 tiles |

## The one-page layout

1. **Top row: three numbers**, each with the target, the trend and the threshold
   that turns it red.
2. **Second row: the funnel or the trend** that explains those three numbers.
3. **Third row: the segment cut** that tells the reader where to look next.
4. **Footer: definitions and the "what this cannot tell you" line.**

Everything else goes to a second page that is opened once a month, not daily.

## Grain and filters

- **Grain**: daily for operational, weekly for trend, monthly for financial. Mixing
  grains on one page produces the "the daily chart says up, the monthly says down"
  conversation.
- **Filters**: at most three, defaulted to the useful case (last 28 days, all
  channels, all platforms). Every filter combination someone can pick is a
  definition nobody has checked.
- **Timezone**: IST, stated.
- **Currency**: INR, with the format and whether it includes GST stated.

## Alerts, where the tool allows

| Alert | Threshold | Who |
|---|---|---|
| `order_paid` volume down >40% day on day | compared to the same weekday, last 4 weeks | founder + engineer |
| Payment failure rate >8% for 2 hours | rolling | engineer |
| Signup completion rate down >25% week on week | with a minimum volume of 50 | product |
| Event volume zero for a live event | any | engineer |

An alert that fires weekly and is ignored is worse than none: it trains the team to
ignore the channel.

## The "what this cannot tell you" line

Every dashboard ends with one sentence, for example:

> This shows client-side events only. About 15% of sessions are lost to ad blockers
> and iOS limits, so treat totals as a floor. Revenue is reconciled to the payment
> gateway monthly; the two differ by under 2% in a normal month.

That single line prevents most of the arguments the dashboard would otherwise start.

## Reviewing an existing dashboard

1. Who opens it, and when did they last act on it?
2. Which charts have never changed a decision? Delete them.
3. Do two tiles disagree? Then one is defined wrongly - fix the definition, not the tile.
4. Is the grain mixed? Split the page.
5. Is there a definition for every metric? If not, write them in the footer.

## Anti-patterns

- Twenty-four tiles because the tool made it easy.
- A "revenue" tile that is actually bookings, next to a "collections" tile with no labels.
- Averages with no counts.
- A dashboard owned by nobody, so a broken tile stays broken for a month.
- Colour used decoratively; red should mean one thing.
- A filter set that lets anyone produce a number nobody can reproduce.
