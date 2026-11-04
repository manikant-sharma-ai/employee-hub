# Cost, latency and scaling

An AI feature that works in a demo and costs ₹40 per request is not a feature. Two
numbers decide whether it ships: rupees per successful task, and seconds to first
useful output.

## The cost model, written down

```
cost per request = (input tokens × in-price) + (output tokens × out-price)
cost per successful task = cost per request ÷ success rate
```

The second line is the one people forget. A cheap model that needs three retries
and a human fix is the expensive option.

## Where the money actually goes

| Lever | Effect | Cost of using it |
|---|---|---|
| Shorter system prompt | Linear saving on every call | Rewrite once, benefit forever - do this first |
| Cache the stable prefix | Large saving on repeated context | Only works when the prefix is byte-identical |
| Retrieval instead of stuffing | Cuts input tokens 5-20x | Needs a retrieval pipeline that works |
| Smaller model for routing and classification | 5-30x cheaper | Quality drop on the hard 10% |
| Batch instead of real-time | Cheaper, sometimes much | Latency of minutes to hours |
| Fewer output tokens | Output is usually priced higher than input | Terser answers, sometimes worse |
| Distillation / fine-tune | Long-run saving | Upfront data and evaluation cost |

## Latency

- **Time to first token** is what the user feels. Stream it.
- **Perceived latency** improves more from a skeleton and a progress line than from a faster model.
- **Parallelise independent calls.** Three sequential 2-second calls is 6 seconds; in parallel it is 2.
- **Set explicit timeouts and a fallback.** A request that hangs for 60 seconds is worse than a fast failure with a retry.
- **Do not put a model call inside a loop** over 500 rows without batching, a queue and a progress record.

## Budgeting before building

Write these five numbers before the first line of code:

1. Requests per day at launch, and at 10x.
2. Acceptable cost per request in rupees.
3. Acceptable p95 latency in seconds.
4. The success-rate bar that makes the feature worth having.
5. The monthly ceiling that triggers a review.

If the fifth number is missing, the first invoice is the review.

## Scaling patterns that survive

- **Queue the heavy work**, stream the light work. Anything over about 10 seconds belongs in a job with a status the user can poll.
- **Cache aggressively and name the key**: prompt hash + model + parameters + a version. A cache keyed on the prompt alone serves stale answers after a prompt fix.
- **Rate limits are per minute and per day.** Design for the per-minute one; it is the one that breaks a launch.
- **Idempotency keys on writes**, so a retry does not create two records.
- **Log tokens, model and latency per call**, or you cannot answer "why is the bill ₹80,000".

## Anti-patterns

- Optimising the model before measuring where the tokens go.
- A 6,000-token system prompt repeated on every call, with no cache.
- Retry storms with no backoff.
- Choosing a model by benchmark score rather than by cost per successful task on your own evaluation set.
- No per-tenant accounting, so one customer's usage is invisible until the invoice.
