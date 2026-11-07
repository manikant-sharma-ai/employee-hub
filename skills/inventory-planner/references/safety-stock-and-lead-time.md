# Safety stock and lead time

Safety stock is insurance. It is bought with working capital, so the amount has to
be argued from lead-time variability and the cost of a stockout, not from a round
number somebody remembers.

## What lead time actually is

Ask for four numbers per supplier, not one:

1. **Quoted lead time** - what the supplier says.
2. **Observed lead time** - the median of the last six receipts, from PO date to stock-in date. This is the number to plan on.
3. **Observed worst case** - the longest of the last six, or the 90th percentile where there is more data.
4. **What sits inside it** - production, transport, octroi or checkpost delays, and the days the accounts team takes to release payment.

In India the gap between quoted and observed is routinely 30-60%, and the cause is
usually payment release or transport, not the factory.

## Sizing safety days

```
safety_days = (worst_case_lead_time - observed_lead_time) * criticality_factor
criticality_factor: A item 1.0, B item 0.6, C item 0.3
```

That is deliberately simple. The alternatives - service-level maths with a standard
deviation - are better when there is a year of clean receipt data, and worse when
there are six receipts and a spreadsheet. Start simple, and say which method was
used.

## The three ways businesses get this wrong

1. **One safety stock for the whole catalogue.** The A item with a single supplier and the C item with three substitutes do not need the same buffer.
2. **Safety stock set once and never reviewed.** A supplier who improved is now being paid for insurance nobody needs; a supplier who deteriorated is being under-insured.
3. **Safety stock used to cover a forecasting failure.** If cover is chronically wrong in one direction, the problem is the velocity input, not the buffer.

## When to override the arithmetic

- **Festival and season** - the peak week is not the average week. Size to the peak, not the mean, for the four to six weeks around Diwali, or around the local harvest, wedding or exam season that drives the category.
- **Single-source SKUs** - no substitute, no alternate supplier: treat as A regardless of revenue.
- **Shelf life** - safety stock on a perishable is a write-off waiting for a date. Cap it at the shelf life minus the selling window.
- **Price change announced** - a supplier price rise dated next month justifies buying ahead, and that decision belongs in `notes/decisions.md` with the date, not in the reorder point.
