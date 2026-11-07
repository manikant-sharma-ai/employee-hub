# Reorder worksheet - <period>

**Catalogue:** <n SKUs> | **Sales window used:** <from - to> | **Review cycle:** <weekly / fortnightly>
**Prepared:** <date> | **Owner of the PO:** <name> | **Re-run on:** <date>

## 1. Inputs and assumptions

| Input | Value | Source | Assumed? |
|---|---|---|---|
| Sales history window | <weeks> | <sheet / store panel> | no |
| Lead time (per supplier) | <days> | <supplier record / observed> | <yes/no> |
| Safety days | <days> | policy | <yes/no> |
| Review cycle | <days> | policy | no |
| Stock in transit included | <yes/no> | <open POs> | <yes/no> |

## 2. Plan

Generated with `python3 scripts/reorder_plan.py stock.csv`:

| SKU | Item | Position | Cover (days) | Reorder point | Order qty | Action | Value |
|---|---|---|---|---|---|---|---|
| | | | | | | ORDER / HOLD / DEAD / NO SALES | |

## 3. Orders to raise

| Supplier | SKUs | Qty after MOQ | Value | Lead time | Freight threshold met | Order by |
|---|---|---|---|---|---|---|
| | | | | | | |

## 4. Stockout risk inside 14 days

| SKU | Days to stockout | Revenue at risk | Expedite? | Owner |
|---|---|---|---|---|
| | | | | |

## 5. Dead and slow stock

| SKU | Qty | Cost value | Months since sale | Cure | Owner | By when | Cash released |
|---|---|---|---|---|---|---|---|
| | | | | bundle / reprice / bulk / donate / write down | | | |

## 6. Cash view

| Line | Amount (₹) |
|---|---|
| Orders to raise | |
| Dead-stock cash released | |
| **Net working-capital change** | |

## 7. What this plan could not see

- <live stock not connected>
- <open POs not supplied>
- <lead times assumed, not observed>
