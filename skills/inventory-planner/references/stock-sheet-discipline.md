# Stock sheet discipline

The plan is only as good as the sheet. Ten minutes of cleaning prevents a month of
confidently wrong orders.

## The checks to run before planning

| Check | What it catches | Fix |
|---|---|---|
| Duplicate SKUs (case, spaces, dashes) | Two rows for one item, each half the stock | Normalise the key, merge, re-total |
| Negative stock | Unrecorded issues, or a returns posting error | Investigate, never plan on a negative |
| Blank lead time | The plan silently assumes zero | Fill from the supplier record or mark as assumption |
| Blank unit cost | Dead-stock value computed at zero | Pull cost from the accounting system |
| Units mismatch | "Box" in the sheet, "piece" in the store | Convert to one base unit and say which |
| Multiple locations | Warehouse plus shop plus marketplace stock | Sum for cover, report by location for transfer decisions |
| Stock in transit missing | Double ordering | Add open POs to position |
| Sales window too short | Seasonality read as death | State the window on the page |

## The minimum columns

`sku, name, on_hand, on_order, avg_daily, lead_days, safety_days, review_days, unit_cost`

Anything else - location, category, supplier, MOQ - is useful context and belongs
on the sheet, but those nine are what the arithmetic needs. A sheet missing one of
them produces a plan with a hidden default, which is the failure this role exists
to prevent.

## Reconciling the sheet to the store

Where the business sells online, three stock figures usually exist: the sheet, the
store panel and the physical shelf. Name which is authoritative for what - the
store panel for what a customer can buy, the sheet for what is in the building -
and reconcile monthly, noting the gap. A permanent gap that is explained is fine.
An unexplained one means at least one of the three is wrong, and the plan is built
on it.

## Units and GST

- **One base unit.** Pieces, not boxes; kg, not bags. Convert at the top of the sheet and keep the conversion factor on the page.
- **Cost is exclusive of recoverable GST** for a registered business. Mixing inclusive and exclusive cost in one column understates or overstates the stock value by the tax rate.
- **HSN per SKU** matters for both the stock value and the listing; a missing HSN is a data gap worth flagging.
