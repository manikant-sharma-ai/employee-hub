# Requirement decomposition

The requirements document is the specification of the score. Decompose it before
you write a word of prose.

## What to extract

For every numbered item in the buyer's document, one row:

| Field | What goes in it |
|---|---|
| `req_id` | The buyer's own number. Never renumber - the evaluator scores by it |
| `requirement` | The requirement in one sentence, in the buyer's words, trimmed of legal padding |
| `mandatory` | Y where the document says shall, must, mandatory, essential, or lists it as a pass/fail criterion |
| `section` | The buyer's section or the evaluation criterion it belongs to |
| `owner` | The person in this business who answers it |
| `status` | answered / partial / gap / todo |

## The reading rules

1. **"Shall" and "must" are mandatory. "Should" and "may" are not** - unless the evaluation criteria say otherwise, which they sometimes do. Read the criteria.
2. **A table is a requirement list.** Every row of a specification table is a separate requirement.
3. **Annexures count.** "The bidder shall comply with Annexure C" makes every line of Annexure C mandatory.
4. **The submission instructions are requirements.** Page limit, file format, signed declarations, the commercial envelope. These disqualify.
5. **Numbers in the requirement are commitments.** "Response within 4 hours", "99.5% uptime", "45-day implementation" - each one is a promise the delivery team must sign off.

## The gap decision

For each mandatory requirement, one of three things is true:

- **We have it** - evidence exists, name it.
- **We can build it** - say by when, and what it costs, in writing.
- **We do not have it** - say so. A compliant bid with a stated gap sometimes wins on the rest; a bid that pretends loses on the reference check.

The gap conversation happens with the founder and the delivery lead before the
proposal is written, not in the paragraph that gets softened at 11pm.

## Scoping the boundaries

Write down, in the proposal, what is not included. The three commonest delivery
disputes are all exclusions nobody wrote: data migration volume, third-party
licence costs, and on-site vs remote delivery. If the buyer's document is silent,
the proposal says what you assume.
