# Context engineering

Context is a budget, not a bucket. Every token you spend on something irrelevant dilutes attention on what matters, and models reliably lose information in the middle of a long window.

Four moves, in this order: **select, compress, order, externalise.**

## Select

Ask two questions of every candidate piece of context:

1. Would a competent human need this to answer correctly?
2. Could the model fetch it on demand instead of holding it?

Anything that fails (1) is noise. Anything that passes (2) should be fetched just in time, not pre-loaded. Retrieval at the moment of need beats a large prompt assembled in advance - it is fresher and cheaper.

Typical over-feeding: full API docs when one endpoint is used, entire transcripts when the last three messages matter, all rows when the question is about one region.

## Compress

- **Summarise history** into decisions and open questions, not prose. "Agreed: net-30. Open: who pays freight."
- **Extract structure** from documents - the fields you need, with the source line quoted.
- **Deduplicate.** Retrieved chunks frequently overlap; overlapping chunks read as emphasis and skew the answer.
- **Drop boilerplate** - nav bars, legal footers, signatures, repeated headers.
- **Quote, do not paraphrase, when exactness matters** - prices, IDs, dates, policy wording.

## Order

- Instructions at the top, critical data adjacent to the question, the key constraint restated at the bottom.
- The middle of a long context is the least attended region. Never bury the deciding fact there.
- Group related items; do not interleave two sources in one block.
- Give every block a provenance tag and a timestamp. Undated data is data the model will treat as current.

## Externalise

State that does not need to be in the prompt should not be in the prompt.

- **Files and memory** for anything that must survive the turn.
- **Scratchpad sections** for intermediate work on long tasks.
- **Tool calls** instead of carrying a dataset in context - let the model query.
- **Sub-agents** for noisy subtasks: a sub-agent reads 200 pages and returns four lines. The noise never enters the parent context. This is the single biggest win on research-heavy work.

## Diagnosing context failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Ignores an instruction that is present | Instruction sits mid-context | Move to top and restate at end |
| Uses an old value | Stale chunk retrieved alongside the new one | Add timestamps, prefer newest, dedupe |
| Invents a field that exists in the data | Field buried in a wall of text | Extract to a labelled key-value block |
| Answers confidently about the wrong entity | Similar entities in context | One entity per call, or name-tag every block |
| Quality degrades as the task goes on | Context filling with its own output | Summarise the running state, drop raw turns |
| Good first answer, bad tenth | Accumulated history | Reset per item; carry only the state object |

## Caching and cost

Keep the stable prefix byte-identical between calls - same instructions, same examples, same order - so caching applies. Volatile data goes at the end. A reordered prompt silently doubles your cost.

## The test

Before shipping, print the assembled context and read it as if you were the model, knowing nothing else. If you cannot answer the task from that text alone, neither can it. This one check catches more production failures than any prompt tweak.
