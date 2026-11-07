# Listing sheet - <channel> - <batch>

**Channel:** <IndiaMART / Amazon.in / Flipkart / GeM> | **Buyer:** <B2B bulk / retail / government>
**Batch:** <n SKUs> | **Prepared:** <date> | **Owner of the upload:** <name>

## 1. Channel rules applied

| Rule | Value used | Source |
|---|---|---|
| Title limit | <characters> | category template, dated <date> |
| Minimum images | <n> | channel help |
| Mandatory attributes | <list> | category template |
| Statutory fields | HSN, GSTIN, <licence> | CA / certificate |

## 2. Listings

| SKU | Title | Attributes | Images | Price | HSN | GSTIN | QA |
|---|---|---|---|---|---|---|---|
| | | brand=;material=;size=;colour= | | | | | |

## 3. Bullets - the six buyer questions

1. **What it is** - <one line>
2. **What it fits / who it is for** - <one line>
3. **What it is made of** - <material, weight, finish>
4. **What is in the box** - <contents, quantity>
5. **Actual measurements** - <cm and inches>
6. **If it is wrong** - <return window and condition, in plain words>

## 4. Price working (per unit)

| Line | Amount (₹) |
|---|---|
| Selling price (incl. GST) | |
| GST component | |
| Marketplace commission | |
| Closing fee | |
| Shipping | |
| Returns provision | |
| Product cost | |
| **Contribution per unit** | |

## 5. QA check

```
python3 scripts/listing_qa.py listings.csv --gate
```

| SKU | Result | Issues to fix |
|---|---|---|
| | | |

## 6. Rejection log

| Date | SKU | Reason | Rule learned | Template fix |
|---|---|---|---|---|
| | | | | |
