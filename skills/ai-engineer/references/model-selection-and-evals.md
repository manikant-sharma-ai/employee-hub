# Model selection and evals

## Choosing a model

Decide on seven axes, in this order. Price is fourth, not first.

1. **Task shape** - extraction and classification need reliability on structured output; planning needs reasoning depth; writing needs tone control. These are different models.
2. **Context size** - how much must be in the window at once, after your compression pass. Size the need, not the maximum.
3. **Tool use** - does it call tools reliably with correct arguments? Test, do not assume. A model that is excellent at prose can be poor at parallel tool calls.
4. **Cost and latency at your volume** - compute the real number: tokens per run x runs per day x 30. A model that costs ₹0.40 per run is ₹1,200 a month at 100 runs a day.
5. **Modality** - vision for documents and screenshots, audio for calls, image generation for visuals.
6. **Data residency and availability** - where the data is processed, and whether the provider has reliable endpoints for your region. For Indian businesses this is often a compliance question, not a preference.
7. **Stability** - a provider that deprecates models quarterly costs you re-evaluation time every quarter. Price that in.

**Tier the work.** A large model for planning, judgement and final writing. A small model for routing, extraction, classification and formatting. Routing by difficulty routinely cuts cost by 60-80% with no measurable quality loss. Start with one strong model to establish the quality ceiling, then move each stage down until it degrades.

## Evals

You cannot improve what you cannot measure, and vibes are not a measurement.

**Build the set before optimising.** Twenty to fifty cases, drawn from real failures - support tickets, logged prompts, the scenarios file. Each case: input, expected behaviour, pass condition. Keep the set fixed; add to it when a new failure appears in production, and treat that addition as the most valuable kind of test.

**Metrics that matter:**

- **Pass rate** against the rubric - the headline.
- **Cost per success** - not per call. Cheap calls that fail are expensive.
- **Latency p95** - the average lies; the tail is what users complain about.
- **Consistency** - run the same case five times. A case that passes 3 of 5 is a coin flip, not a pass.

**LLM as judge**, used carefully: give an explicit rubric with a fixed scale, ask for the finding before the score, and spot-check twenty judgements against your own labels. Judges are biased toward longer, more confident answers - include a length-normalised check or a length constraint in the rubric.

**Regression gate.** No prompt, model or tool change ships without an eval delta. Keep a table in the repo: version, date, model, pass rate, cost per success, latency. The table is how you notice that the model upgrade in March cost you four points of accuracy.

## Reporting

Report the numbers you measured, with the date and the model version. Never quote a public benchmark as evidence for your use case - it measures a different task. If a number is an estimate, label it an estimate; if it was not measured, say so.
