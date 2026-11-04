# RAG and retrieval

The model does not know your business. Retrieval is how you put the right 800
tokens in front of it, and it is where most "the AI gives wrong answers" problems
actually live.

## The pipeline, in order

| Stage | The decision | The common failure |
|---|---|---|
| Ingest | What is a document? A PDF page, a table row, a ticket thread | Splitting a table into rows with no header |
| Chunk | 300-800 tokens with overlap, or semantic sections | Fixed 1000-character chunks that cut sentences in half |
| Embed | Which model, what dimension | Changing the model later without re-embedding everything |
| Store | Vector DB plus the metadata you will filter on | No metadata, so you cannot filter by date, tenant or language |
| Retrieve | Top-k, hybrid (vector + keyword), rerank | Vector-only search that misses an exact product code |
| Assemble | Order, deduplicate, cite | Stuffing 20 chunks and calling it context |
| Answer | Instruct citing, refuse when absent | The model filling the gap with a plausible invention |

## Rules that decide quality

- **Hybrid beats pure vector.** Business queries contain SKUs, invoice numbers and names; keyword search finds those, vectors do not. Run both, merge, then rerank.
- **Chunk by meaning, not by character count.** A section heading is a better boundary than a byte offset.
- **Metadata is the product.** Date, source, tenant, language, permission level - you cannot filter what you did not store.
- **Always retrieve with a permission filter**, never after. Post-filtering leaks a document's existence and sometimes its content.
- **Cite every claim to a chunk.** If the answer cannot cite, it should refuse. "I could not find this in the documents" is a correct answer.
- **Evaluate retrieval separately from generation.** Recall@k first; a good model cannot fix a chunk that was never retrieved.
- **Reranking is the cheapest quality win** for a mediocre pipeline; a cross-encoder over the top 30 costs little and fixes a lot.
- **Freshness is a policy, not a hope.** Say how old the index may be, and show the date with the answer.

## Sizing, honestly

- Under about 200 documents, put the whole corpus in a keyword index and skip the vector store. Complexity has a cost.
- Between 200 and 50,000 chunks, hybrid retrieval with reranking is the sane default.
- Above that, tenant partitioning and incremental re-indexing matter more than the embedding model.

## Indian-language corpora

- **Multilingual embeddings** matter: Devanagari, Tamil and Bengali queries against English documents need a model that crosses scripts, or a translation step you must disclose.
- **Transliteration is a real query pattern.** A user types "gadi" for गाड़ी. Normalise transliteration variants in the keyword leg.
- **Do not chunk across scripts.** A chunk that mixes Hindi and English mid-sentence embeds poorly.

## Anti-patterns

- A vector store with no metadata and no reranker, sold as "RAG".
- Retrieving 20 chunks because the context window is large.
- Answering from model memory when retrieval returned nothing.
- Re-embedding the corpus monthly by hand, with no record of which model version produced which vectors.
- No evaluation set, so every change is a guess.
