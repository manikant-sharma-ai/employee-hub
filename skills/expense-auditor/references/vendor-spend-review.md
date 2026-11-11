# Vendor spend review

The largest recoverable money is rarely in a duplicate. It is in a rate that was agreed two
years ago, a quantity billed above what was delivered, and a subscription nobody owns.

## Start with the concentration table

| Rank | Vendor | Category | Annual spend | % of total | Invoices | Rate basis |
|---|---|---|---|---|---|---|
| 1 | | Packaging | ₹18.4L | 21% | 46 | Per kg |
| 2 | | Logistics | ₹12.1L | 14% | 210 | Per shipment |
| 3 | | Software | ₹6.8L | 8% | 34 | Per seat |

Four rules: the top five vendors are usually 50-70% of controllable spend; anything above 5% of
total gets a contract review; anything above 10% gets a competitive quote; and a vendor with
spend that doubled in a year gets a conversation, not a finding.

## Three-way match, on the larger items

```
PO (what was agreed) -> GRN (what arrived) -> Invoice (what was billed)
```

| Mismatch | Usual cause | Action |
|---|---|---|
| Billed > PO | Rate change without a revised PO | Get the revised PO, or dispute the delta |
| Billed > GRN quantity | Short delivery billed in full | Debit note for the shortfall |
| Rate above contract | Escalation applied early, or wrong slab | Credit note from the contract date |
| Two invoices for one GRN | Duplicate billing | Credit note, and a PO-level check going forward |
| No PO, above threshold | Out-of-process spend | Retro-approval, and a control fix |
| No GRN | Nobody checked the delivery | Add a receipt step; this is the biggest control gap |

## The contract, read for what it charges

| Clause | What to extract | Where it leaks |
|---|---|---|
| Rate card | Slab, per-unit rate, zone rates | The old rate is in the system, the new one in the contract |
| Volume discount | Threshold and rate | Never applied because nobody tracks the cumulative |
| Escalation | % and date | Applied a quarter early, or twice |
| Fuel or input surcharge | Formula, revision frequency | Applied at the peak and never reduced |
| Minimum billing | Monthly minimum | Paid during a month of no usage |
| Payment terms | Days, early-payment discount | A 2% discount never taken on ₹18 lakh |
| Credits and returns | Process and turnaround | Returns given, credit note never issued |
| Rate review | Annual, with a benchmark | No review since signing |

## The recurring-charge audit

Every subscription and AMC, once a year:

| Column | Why |
|---|---|
| Tool | What it is |
| Annual cost | Total, not monthly |
| Seats paid | From the invoice |
| Seats used | From the admin console, by last login |
| Owner | The person who would notice it missing |
| Renewal date | The only date that matters |
| Overlap | Another tool doing the same job |

Three tests that recover money almost every time: **seats paid vs seats used** (a 40-seat
licence for 11 active users is a 70% waste), **overlapping tools** (two video call tools, two
project trackers, two design tools), and **renewals auto-charged with no owner** (the person who
signed up left).

## Consolidation, when it is worth doing

| Situation | Consolidate? |
|---|---|
| Five packaging vendors, each below ₹2 lakh a year | Yes - volume into two, and ask for the slab |
| Two logistics vendors on different zones | Only if the rate card improves; splitting is a hedge |
| One vendor, no alternate quote in two years | Get one alternate quote, even if you stay |
| A specialist vendor with no substitute | No - but benchmark the rate annually |
| Small vendors used for speed | Keep two; the price of speed is a premium you choose |

Consolidation has a real cost: dependency, and the loss of a fallback. Say so when recommending it.

## Rate benchmarks, without inventing them

Do not quote a market rate you cannot source. Instead:

- Ask for one alternate quote on the same specification (the cheapest benchmark available).
- Use the vendor's own other customers' published price, where it exists.
- Compare the same line across the company's own sites or periods.
- Ask the buyer what rate they expected when they raised the PO.
- Use a public price list where one exists (software, logistics slabs, packaging catalogues).

A benchmark without a source is a negotiating position, and it must be labelled as one.

## The output of this review

| Finding type | Route |
|---|---|
| Recoverable (overbilling, unapplied credit) | Credit note request, with the contract clause cited |
| Avoidable (unused seats, overlapping tools) | Downgrade or cancel, before the renewal date |
| Structural (rate above market) | `procurement` for the renegotiation or the alternate quote |
| Control (no GRN, no PO) | A process fix, named with an owner |
| Budget effect | `budget-planner` prices it into the next plan once agreed |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Auditing rate without the contract | Every finding is arguable |
| Chasing a ₹2,000 overcharge from a ₹40 lakh vendor | The relationship costs more than the finding |
| Recommending consolidation with no fallback | A single point of failure bought at a discount |
| Benchmarking from memory | A number that cannot be defended in the conversation |
| Ignoring renewal dates | The saving is agreed after the auto-charge |
| Counting "avoidable" as "recovered" | The result is inflated and the next audit is not commissioned |
