# Loop engineering

An agent is a loop: **observe -> decide -> act -> verify -> stop.** Most agent failures are loop failures. The prompt is usually fine; the loop has no brakes, no verification, or no way to notice it is repeating itself.

## Design the stop condition first

Before writing a single step, answer: how does this end?

- **Success stop** - a checkable condition on the state, not the model's opinion that it is done.
- **Budget stop** - max steps, max tokens, max wall-clock, max money. All four, all explicit.
- **Stuck stop** - state unchanged across two iterations.
- **Escalation stop** - a condition that means a human must decide.

When a budget is hit, the loop must **return what it has plus a clear statement of what is unfinished**. Silent truncation is worse than failure.

## Verify separately from acting

The step that produced the work should not be the only thing judging it. Add an explicit verification step: does the output satisfy the contract? Does the file exist and parse? Did the API return the shape we expected?

Prefer mechanical verification - a schema check, a regex, a test run, a diff - over asking the model "is this correct?". Models grade their own homework generously, and with no ground truth the critic pass just burns tokens.

## Detect no-progress

Hash the state each iteration. If the hash repeats, the loop is not converging; break out with a report rather than retrying. Common causes: the same tool error returning, the model reformatting the same failed attempt, or a plan that cannot be executed with the tools available.

## Error taxonomy

Handle three classes differently - treating them alike is why agents thrash.

- **Transient** (timeout, rate limit, 502): retry with exponential backoff, cap at 3, jitter the delay.
- **Repairable** (bad argument, wrong enum, missing field): feed the error text back to the model once with the schema restated. If it fails twice on the same argument, stop - the tool description is wrong.
- **Fatal** (no permission, resource does not exist, auth expired): do not retry. Report and escalate.

## Tool result hygiene

Tool output goes into context and stays there. Truncate aggressively.

- Cap at a few thousand characters, keep head and tail, mark the elision.
- Never echo raw HTML or full JSON when three fields matter - extract in code before it reaches the model.
- Summarise long results with a code-side reducer, not another model call, when the shape is known.

## Human checkpoints

Place them by irreversibility, not by step count. Anything that sends, pays, publishes, deletes or writes to a system of record gets a confirmation gate - and the gate shows exactly what will happen, not a summary of intent.

## Reflection, in moderation

One critic pass can help on open-ended writing or planning. More than one is almost always waste. Reflection without new information cannot improve an answer - it just re-samples.

## Observability

Log per step: iteration number, the decision, the tool and arguments, a digest of the result, tokens in and out, latency, cumulative cost. Keep traces replayable so a failure can be reproduced without re-spending.

The question you must be able to answer after an incident: at which iteration did it go wrong, and what did it see at that moment?

## Anti-patterns

- Loop with no max steps "because it usually finishes".
- Retrying a fatal error until the budget dies.
- The agent checking its own work with no external signal.
- Unbounded fan-out - a loop that spawns a sub-agent per row of a 10,000-row sheet.
- Passing the entire conversation forward every iteration instead of a compact state object.
- Treating "the model said it is done" as the success condition.
