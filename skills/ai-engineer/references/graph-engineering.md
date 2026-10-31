# Graph engineering

A single loop is the right shape when the steps are unknown. A graph is the right shape when the steps are known, when subtasks are independent, or when different stages need different models, tools or permissions.

## Choose the topology before you build

| Situation | Topology |
|---|---|
| Steps known, run in order, each depends on the last | Chain |
| Steps known, independent of each other | Fan-out / fan-in |
| Input type decides the path | Router + specialist branches |
| Steps unknown, discovered as you go | Loop (single agent) |
| A big job with known subtasks of varying difficulty | Orchestrator + workers |
| Output quality matters more than latency, and a rubric exists | Generator + critic (+ one revision) |
| Bulk transform over many items | Map-reduce with bounded concurrency |

If you cannot draw it on one page with named boxes and arrows, it is not designed yet. Draw first, code second.

## Nodes

Every node has one job, one input contract and one output contract. Useful types:

- **Planner** - decomposes, produces a task list. Runs on the strong model.
- **Worker** - executes one task with a narrow toolset. Runs on a cheap model.
- **Retriever** - fetches and compresses. Returns excerpts, not documents.
- **Critic** - scores against a rubric, returns structured findings.
- **Router** - classifies, picks a branch. Small model, enum output.
- **Formatter** - enforces the final output contract. Deterministic where possible.
- **Human gate** - pauses for approval. Always before irreversible actions.

## State

One typed object travels through the graph. Nodes read named fields and write named fields. Nothing else is shared.

Define the state schema explicitly: field, type, who writes it, who reads it. Undeclared state is how graphs become unmaintainable - two nodes silently writing the same field with different meanings.

Keep it small. If the state grows past a page, you are carrying context that should be in files or refetched.

## Edges

- **Conditional** - the router's enum decides. Every enum value must map to a branch; add a default.
- **Fan-out** - parallel branches, bounded concurrency. Unbounded fan-out is how you discover rate limits.
- **Fan-in** - a defined merge policy: concatenate, vote, pick highest score, or LLM-merge with a rubric.
- **Retry edge** - back to the same node, max twice, then an escalation edge.
- **Escalation edge** - to a human gate or a failure report. Every graph needs one.

## Contracts between nodes

Each handoff needs a written contract: what the next node may assume, and what it must never assume. Most multi-agent failures are one node assuming the previous one validated something it did not.

Cheap, effective pattern: each node returns `{status, output, confidence, notes}`. The graph checks `status`; the model never has to infer success from prose.

## Failure policy

Decide per graph, before building:

- **Fail fast** - any branch failure aborts. Right for financial or compliance work.
- **Best effort** - failed branches are reported and skipped. Right for research and enrichment.
- **Partial commit** - write what succeeded, flag the rest. Right for bulk imports, with idempotency.

Make every node idempotent so a resumed run does not duplicate work. Checkpoint after each node so a failure at node 7 does not re-run nodes 1-6 and re-pay for them.

## Depth and cost

Keep graphs shallow. Depth beyond four or five is usually a sign that a node should be collapsed into a single well-prompted call. Parallelism only pays when branches take more than a second each and are genuinely independent - otherwise it adds coordination cost and a rate-limit bill.

## Anti-patterns

- Agents talking to each other in free prose instead of typed contracts.
- A critic node with no rubric, which produces agreeable noise.
- Fan-out over thousands of items with no concurrency cap.
- Shared mutable state between nodes.
- A graph whose only failure path is an exception.
- Three agents where one would do. Every node must earn its latency.
