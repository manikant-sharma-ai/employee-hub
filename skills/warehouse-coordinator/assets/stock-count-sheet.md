# Stock count pack - <warehouse / location> - <YYYY-MM-DD>

**Count date:** <YYYY-MM-DD> | **System export:** <YYYY-MM-DD HH:MM> | **Cut-off applied:** <HH:MM>
**Counted by:** <names> | **Recounted by:** <name, blind> | **Approver for adjustments:** <name>

## Summary

| Measure | Value |
|---|---|
| SKUs counted | <n> of <n> in scope |
| SKUs not counted (area) | <n> - <which area, share of stock value> |
| Units of variance (short / excess) | <n> / <n> |
| Value at cost (short / excess) | ₹<n> / ₹<n> |
| Variance as share of stock value | <%> |
| Variances with a named cause | <n> of <n> |

## Variance - top ten by value

| SKU | Description | Unit | System | Physical | Variance | Value at cost | Class | Action | Cause |
|---|---|---|---|---|---|---|---|---|---|
| <SKU> | <desc> | <uom> | <n> | <n> | <+/-n> | ₹<n> | <A/B/C> | <recount/investigate/adjust/clear> | <paperwork/misplacement/damage/unexplained> |

## Recount list

| SKU | Variance | Recount by | When | Blind result | Matched |
|---|---|---|---|---|---|
| <SKU> | <n> | <name> | <YYYY-MM-DD> | <n> | <yes/no> |

## Causes, counted

| Cause | SKUs | Units | Value at cost | What it means |
|---|---|---|---|---|
| Paperwork | <n> | <n> | ₹<n> | A movement was never entered |
| Misplacement | <n> | <n> | ₹<n> | Found in another location |
| Damage | <n> | <n> | ₹<n> | In the bin, never written off |
| Unexplained | <n> | <n> | ₹<n> | The shrinkage finding |

## Adjustment proposal - for approval, not posted

| SKU | Units | Value | Reason code | Evidence | Approver | Date |
|---|---|---|---|---|---|---|
| <SKU> | <n> | ₹<n> | <recount matched / damage / paperwork> | <photo, doc ref> | <name> | <YYYY-MM-DD> |

## The one process change

- **Change:** <what will be different>
- **Owner:** <name> | **Date:** <YYYY-MM-DD>
- **Metric it moves:** <variance value / wrong-item rate / GRN exceptions>
- **Checked at:** <the next read date>

## What I could not verify

- <movement history missing for these SKUs / area not counted / connector not available>
- Verified by: <ERP or WMS connector used, or "not verified - <what is missing>">
