# Retention and watch time

Retention is the only number that tells you whether the video was worth making. Views say somebody clicked;
retention says somebody stayed, and YouTube pays and recommends on the second.

## The three numbers

- **Average view duration (AVD)** - absolute minutes watched. Compare it against the video's own length.
- **Percentage viewed** - AVD divided by length. The fair comparison between a 4-minute and a 20-minute video.
- **The retention curve** - where people leave. This is the diagnostic; the first two are the headline.

## Reading the curve

| Pattern | Diagnosis | Fix |
|---|---|---|
| A cliff in the first 30 seconds | The hook did not match the packaging, or the intro was a logo and a greeting | Open on the promise; cut the intro |
| A steady slide from minute one | The body is longer than the promise needs | Cut a third; move the payoff earlier |
| A spike, then a drop | A specific moment was clipped and shared | Make that moment the video |
| Flat, then a cliff at the end | The video delivered and the viewer left satisfied | Nothing to fix - check the call to action |
| Flat and high throughout | The video is the right length | Make more like it, and note why |

## Percentage viewed, by length

Short videos look better on this metric for structural reasons. Judge against these bands, not against a target
someone quoted:

| Length | Percentage viewed worth having |
|---|---|
| Under 60s (Shorts) | 70-90% - below 60% the hook is failing |
| 3-8 minutes | 40-55% |
| 8-20 minutes | 30-45% |
| Over 20 minutes | 25-35%, and AVD matters more than the percentage |

## The first thirty seconds

Write it before the video is shot. It has four jobs, in this order: confirm the click was right, state the promise,
show the payoff exists, and give the reason to stay to the end. Anything else in those thirty seconds - a channel
intro, a sponsor read, a long greeting - is a paid-for loss.

## Diagnosing before prescribing

Use `scripts/packaging_audit.py` on the export. It classifies each video as `packaging` (click-through below the
channel median), `hook` (click-through fine, percentage viewed low), `body` (retention slides from the first
minute), or `fine`. Fix in that order: a hook fix on a packaging problem wastes a reshoot, and a packaging fix on
a hook problem makes the same bad video more visible.

## Watch time against the business

A video with 40% retention and 3,000 views from the right audience beats one with 65% retention and 40,000 views
from schoolchildren. Put the enquiry count next to the retention number in the read-out, every month, so the
channel is judged as a business rather than as a scoreboard.
