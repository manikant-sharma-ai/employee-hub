# Commercials and pricing

The price is the last thing built and the first thing evaluated. It is an offer with
assumptions attached, not a number.

## The cost build-up

```
Direct cost
  + Labour (rate × hours × on-costs)
  + Materials or licence (unit × quantity)
  + Subcontract or third-party
  + Logistics, travel, installation
  + Contingency (state the %)
= Gross cost
  + Overhead allocation (state the method)
= Full cost
  + Margin (state the %)
= Price before tax
  + GST at the applicable rate
= Price quoted
```

Every line has a source. A price that cannot be reconstructed by someone else is a price
that will be argued about in the contract.

## The price schedule

Match the client's format exactly. Where they give a template, use it; where they do not:

| # | Item | Unit | Qty | Rate | Amount | Notes |
|---|---|---|---|---|---|---|
| 1 | Implementation | lump sum | 1 | | | Fixed |
| 2 | Annual support | per year | 3 | | | Escalation capped at 5% |
| 3 | Consumables | per unit | as used | | | Capped at ₹x/year |
| | **Total (excl. GST)** | | | | | |
| | GST @ 18% | | | | | |
| | **Total (incl. GST)** | | | | | |

Rules: rates and amounts in the same units the client uses, totals arithmetically checked
twice, and no blank cell without a "not applicable" note.

## Options, when they asked for them

| Option | What it is | Price | Trade-off |
|---|---|---|---|
| Base | The compliant minimum | | Meets every mandatory requirement |
| Recommended | Base plus the two items that reduce their risk | | Higher price, lower total cost of ownership |
| Premium | Full scope, extended warranty, resident engineer | | Highest price, best service level |

The base option must be fully compliant. An "option" that fails a mandatory requirement is
a disqualification with extra pages.

## Assumptions and exclusions - the clause that saves the margin

Write them, always, even when the client did not ask:

- Volumes and the basis (per site, per month, per transaction).
- What is included in support hours and what is chargeable.
- Client responsibilities: access, data, approvals, site readiness.
- Price validity: 90 days is standard; 180 days needs a currency or commodity clause.
- Escalation: fixed for the term, or capped at a stated percentage per year.
- Taxes: GST extra as applicable; TDS as per law.
- Payment terms and milestones, matching the client's contract where possible.
- Exclusions: travel beyond a stated radius, third-party licences, statutory approvals.

An assumption not written is a cost the company absorbs. An exclusion not written is a
scope dispute in month three.

## The commercial risks to price deliberately

| Risk | Price it as | Or avoid it |
|---|---|---|
| Payment at 90 days | Working capital cost in the margin | Negotiate 45, or a discount for early payment |
| Penalty clauses (LD) | A contingency line, capped | Cap the LD at 10% of contract value |
| Volume uncertainty | A rate per unit, not a lump sum | A banded price with a floor |
| Currency exposure on imports | A clause, or a buffer | Quote in INR with a validity window |
| Escalation on labour over 3 years | A capped annual escalation | A fixed rate with a review date |
| EMD and PBG | The bank charge, in the price | Nothing - it is a cost of bidding |

## EMD and bank guarantee

| Instrument | Purpose | Cash effect | Note |
|---|---|---|---|
| EMD | Bid security | Blocked until award or refund | DD or BG, in the client's format |
| Performance BG | Post-award security, typically 3-10% | Margin and limit consumed | Bank charges are a real cost |
| Advance BG | Against a mobilisation advance | Same | Price the bank charge |

Confirm the format, the validity period and the claim conditions before the bid. A BG
that expires before the contract does is a default.

## Taxes and compliance

- **GST**: rate by HSN or SAC, place of supply, and whether the client is entitled to
  input credit. Quote exclusive, state the rate.
- **TDS**: the client deducts at source; the price is not reduced by it, but the cash flow
  is.
- **MSME status**: where the client is required to pay MSMEs within 45 days, say so, and
  attach the Udyam certificate.
- **Liquidated damages and indemnity**: read them, price them, and route the clause to
  `legal-drafter` and the lawyer before signing.

This role builds the commercial response; the tax position is the CA's and the contract
terms are the lawyer's.

## The price approval

Before submission: the build-up, the options, the assumptions, the deviations and the
margin go to the approver in one page. The approval is recorded in `notes/decisions.md`
with the date, the approver and the number. A price changed after approval is a new
approval.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| A single lump-sum number with no build-up | Margin disappears in the first change request |
| Assumptions left implicit | Every unstated assumption is absorbed as cost |
| A "competitive" price with no cost base | The contract is won and the year is lost |
| Base option that misses a mandatory clause | Disqualification |
| EMD arranged after the deadline | The bid is not accepted |
| Price validity open-ended | Costs rise and the price cannot |
| Price changed verbally after submission | No record, no defence |
