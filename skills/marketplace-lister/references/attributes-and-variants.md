# Attributes and variants

Attributes are not metadata, they are the search and the filter. A listing missing
them is invisible to the buyers who use filters, which is most of them.

## The three tiers of attribute

1. **Mandatory** - the channel rejects or suppresses without it. Brand, HSN, size or model, colour, material.
2. **Filter** - the attribute that appears as a filter in the category. Filling it puts the listing in front of buyers who narrow their search.
3. **Descriptive** - useful detail: care instructions, country of origin, warranty period, pack size.

Fill tier 1 completely, tier 2 wherever it applies, tier 3 where it sells.

## Variants

- **Create one family, not many listings.** Size and colour belong in the variation family; separate listings split reviews, split ranking and confuse the buyer.
- **The parent carries the shared attributes**; the child carries the size, colour and its own SKU and price.
- **SKU naming**: `<brand>-<category>-<style>-<size>-<colour>`, stable, never reused for a different product.
- **The size chart is mandatory for apparel and footwear** - measurements in centimetres and inches, with a note that Indian labels vary by manufacturer.

## Statutory fields

| Field | Rule | Where it comes from |
|---|---|---|
| HSN | 4 digits for a heading, 6 for a subheading, 8 where the category needs it. Must match the product, not the nearest guess | The CA or the GST rate chart for the category |
| GST rate | 0, 5, 12, 18 or 28 depending on the HSN and the price point for some apparel | The CA, in writing |
| GSTIN | 15 characters: 2 state code, 5 PAN letters, 4 digits, 1 letter, 1 alphanumeric, Z, 1 checksum | The GST certificate |
| Legal metrology | Net quantity, MRP, manufacturer and packer address on the pack and often in the listing | The label file |
| Category licence | FSSAI for food, BIS for several electronics and toys, CDSCO for medical devices, seeds and pesticides licences | The certificate, with its number and expiry |
| Country of origin | Mandatory on Indian marketplaces | The supplier declaration |

An invented HSN is worse than a missing one: it changes the tax treatment and the
correction is a credit note and a penalty, not an edit.

## The completeness check

Before upload, for each row: every tier-1 field non-empty, every tier-2 field
either filled or explicitly marked "not applicable", the HSN digits valid, the
GSTIN format valid, the image count at or above the minimum, and the price above
zero. `scripts/listing_qa.py` runs exactly these checks.
