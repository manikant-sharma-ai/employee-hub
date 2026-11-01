# Source quality and verification

The memo is only as good as its worst load-bearing source. This file is the discipline that keeps a plausible number from becoming a decision.

## The hierarchy

| Tier | Source | Trust for | Do not trust for |
|---|---|---|---|
| 1 | Regulatory filings, court records, statutes, official registers, audited accounts | Facts of record | Anything about the future |
| 2 | Company's own disclosures - annual report, price list, published policy, job posts | Their claims about themselves | Their market position |
| 3 | Primary research - your own interviews, store visits, price checks, test purchases | Behaviour and price | Scale |
| 4 | Reputable trade press, industry bodies, credit rating agencies | Context and direction | Exact figures |
| 5 | Consultancy reports, market research summaries | Framing, definitions | Their headline numbers, which are usually recycled |
| 6 | Blogs, listicles, SEO content, AI-written summaries | Nothing load-bearing | Anything |

A memo may rest on tier 5 for framing. It may not rest on tier 6 at all.

## Triangulation

- **One source is a rumour with a citation.** Two independent sources, or one tier-1 source, for any number the decision turns on.
- **"Independent" means not derived from each other.** Ten articles citing the same press release are one source.
- **When sources disagree, report the range and the reason.** "Estimates run from ₹2,400 crore to ₹6,800 crore depending on whether unorganised players are counted; the decision does not change across that range" is a stronger finding than a false precision.
- **Date everything.** Two sources from different years disagreeing is not a conflict, it is growth.

## Spotting a source that will not survive

| Signal | Why it is a problem |
|---|---|
| No author, no date, no methodology | Nobody is accountable for it |
| A precise number with no stated method | Precision without provenance is invented |
| Every figure rounds to a suspiciously clean number | Recycled from a press release |
| The page exists only to rank, with 40 similar pages | SEO content, generated to be found, not to be true |
| Statistics that all predate 2022 but are described as current | Stale data wearing a fresh headline |
| Content that reads fluently and says nothing verifiable | Often machine-generated at scale |
| A market report whose publisher you cannot find | The report may not exist |

**The test:** can you name who produced this, when, from what data, and would they be embarrassed to be wrong? If not, it is context at best.

## Verification of a specific claim

For any claim the decision turns on, do all four:

1. **Find the primary.** The filing, the statute, the price list, the dataset. Not the article about it.
2. **Read the definition.** The number usually depends on what was counted. Market size especially.
3. **Check the date and the vintage** of the underlying data, not the publication date.
4. **Look for the contradiction.** Search deliberately for the claim being wrong. "X is not true", "X criticism", "X debunked".

If you cannot complete 1-4, the claim goes in the memo as `assumed`, with the reason.

## Confidence labels

Use these four words consistently and never blur them.

| Label | Means | In the memo |
|---|---|---|
| **Verified** | Tier 1-3 source, retrieved in this session, definition checked | State plainly |
| **Computed** | You did the arithmetic; show the inputs and the formula | State with the working |
| **Inferred** | Follows from verified facts but is your reasoning | "This suggests..." |
| **Assumed** | No source; a placeholder for the model | "Assumed; if wrong, the answer changes by X" |

## Citing in the memo

- **Inline and short:** claim, then `(Source, date)`.
- **Every appendix entry:** title, publisher, date, URL, and one line on what it supports and what it does not.
- **Never cite a source you did not open in this session.** Not from memory, not from a similar report, not from what the client said the report said.
- **If a link is paywalled or dead**, say so and cite what you could see - the abstract, the summary table - and downgrade the confidence.

## Anti-patterns

- A number with a source attached that does not contain the number. The most common citation failure.
- Chaining: citing an article that cites a report, without opening the report.
- Presenting a range as a point estimate to look decisive.
- Averaging two conflicting estimates to produce a number neither source supports.
- Using a global figure for a local market. "$50 billion globally, so India is 18% of that" is a fabricated derivation.
- Letting the strongest-sounding source win rather than the best-tiered one.
- Keeping a claim because the memo is already written around it.
