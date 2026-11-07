# Compliance matrix

The matrix is the control document. The prose serves the matrix, not the other way
round.

## The columns

| Column | Purpose |
|---|---|
| Req ID | The buyer's numbering, preserved exactly |
| Requirement | One sentence, the buyer's words |
| M | Mandatory or desirable |
| Response | What we do, in one line, with the page reference |
| Evidence | Certificate number, reference customer, past project, or "none" |
| Owner | The person accountable for the answer |
| Status | answered / partial / gap / todo |

## The scoring rule

```
mandatory coverage = answered mandatory / total mandatory
ready to send     = mandatory coverage == 100%
```

`scripts/compliance_matrix.py` computes exactly this and `--gate` exits non-zero
until every mandatory line is answered. "Partial" is not answered, and treating it
as answered is how a bid gets disqualified on a technicality the team could see.

## Working the matrix

1. **Fill it before drafting.** A matrix filled after the prose is a reconciliation exercise and it always finds a gap too late.
2. **One owner per row.** An unowned row is nobody's deadline; the script flags it.
3. **Evidence or none.** "We have extensive experience" is not evidence. "Three hospital deployments, 2023-2025, reference: <name, agreed>" is.
4. **Read it as the evaluator**, row by row, and score yourself out of ten on each. The rows where you score five are the ones to fix.
5. **The page reference is not optional.** An evaluator who has to search for the answer marks the row as not addressed.

## What the buyer does with it

Many buyers require a compliance matrix as a submission annexure, in their format.
Where they do, use their template and their column order; where they do not, send
yours - it costs nothing and it makes the evaluation easy, which is worth real
marks.

## The readiness gate

Run before the file is sent:

```
python3 scripts/compliance_matrix.py requirements.csv --gate
```

It prints coverage, the open mandatory items with owners, and exits non-zero if
anything mandatory is unanswered. A proposal that has not passed this gate is not
ready, however good the writing is.
