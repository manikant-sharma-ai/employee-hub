# Variance and flags

A flag is a claim that something needs attention. It has to mean the same thing
every week, or it means nothing.

## The one rule

```
deviation = (actual - target) / |target| * (+1 if higher is better, else -1)

deviation >= -5%   -> ON TRACK
deviation >= -15%  -> WATCH
otherwise          -> OFF TRACK
target = 0 or blank -> NOT SET
```

That is the whole rule, and it is the one `scripts/mis_variance.py` implements.
Change it only in `notes/decisions.md`, with a date and a reason, and re-baseline
the whole page when you do.

Why a band rather than a single number: a metric 3% off target in week two of a
month is not news, and flagging it trains the reader to ignore the colour.

## Direction of good

The commonest error in a small business MIS is flagging a rising refund rate as
green because it went up. Every metric carries its direction in the dictionary,
and the flag rule inverts for lower-is-better metrics: refunds, churn, cost per
order, receivables days, stock cover beyond a ceiling.

## Variance against what

Three comparisons, each answering a different question:

| Comparison | Question | When to use |
|---|---|---|
| vs target | Are we where we said we would be? | Always |
| vs prior period | Is it getting better or worse? | Always |
| vs same period last year | Is this season or is this us? | Any seasonal business |

A page with only one comparison invites the wrong conclusion. Revenue up 8% on
last month and down 12% on last October is a different story from the reverse.

## Seasonality and known events

Before flagging, check the calendar: festivals (Diwali, Holi, Eid, Onam, Pongal),
exam periods, financial year end, monsoon for anything that ships, a price change,
a promotion, a stockout in the previous period. Write the event on the page next
to the flag. A red explained by a known event is a note, not an alarm.

## When not to flag

- **The period is incomplete.** A part-month against a full-month target is not a variance.
- **The target was never set or was set by nobody.** That is a `NOT SET` and a question for the owner.
- **The number is provisional and will move.** Say provisional and hold the flag until it settles.
- **The movement is inside normal noise for that metric.** Measure the last six periods once; if the week-to-week swing is routinely 6%, a 5% band is too tight for that metric and the band belongs in the dictionary.

## The two-decision rule

Every published page names at most two metrics that need a decision this week.
A page where everything is red names nothing. Pick the two that matter, name the
owner and the date, and leave the rest as context.
