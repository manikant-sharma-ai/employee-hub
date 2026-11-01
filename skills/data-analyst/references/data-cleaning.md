# Data cleaning

Every wrong business number starts as a plausible-looking file. This is the ten-minute pass that catches the errors before they become a memo.

## Profile before you analyse

Run these on any new file. Write the answers down; they go in the readout's "what I checked" section.

| Check | How | What it catches |
|---|---|---|
| Row count | `len(df)` | A truncated export - the most common silent failure |
| Date range | min and max of the date column | Data that stops three weeks before the period claimed |
| Grain | What one row means | The duplicate that is actually a line item, not an error |
| Key uniqueness | Duplicate count on the supposed key | Two exports stacked on top of each other |
| Missing values | Count and percent per column | Blank prices, blank cities, blank dates |
| Money column distribution | min, max, mean, median, p1, p99 | Negative amounts, ₹0 orders, a ₹40 lakh typo |
| Category counts | `value_counts()` on every text column | "Delhi", "delhi", "New Delhi", "DEL" as four cities |
| Zero and negative rows | filter and eyeball | Returns, refunds, test orders, corrections |

## The grain question

Before anything else: **what does one row mean?** Order? Order line? Invoice? Payment attempt? Customer-day?

Getting this wrong invalidates every sum that follows. A file where some orders have three rows (one per line item) and others have one will produce a revenue total that is right and an order count that is wrong - or the reverse.

Test: pick one order ID you know. Count its rows. Explain why.

## The five errors that account for most bad analysis

| # | Error | Symptom | Fix |
|---|---|---|---|
| 1 | **Double counting** | Total is roughly 2x the system figure | Deduplicate on the true key; check for stacked exports |
| 2 | **Partial period** | Last month looks like a collapse | Compare date ranges, not just totals |
| 3 | **Mixed currency or units** | Averages skewed by one huge row | Check for a currency column; look at p99, not the mean |
| 4 | **Text where number should be** | Sums return 0 or an error | Strip ₹, commas, spaces; watch for Indian grouping |
| 5 | **Category sprawl** | 340 cities for a 40-city business | Normalise, then map to a canonical list |

## Cleaning rules that do not destroy evidence

- **Never edit the source file.** Copy it, work on the copy, keep the original and say where it is.
- **Clean in a script, not by hand.** Hand edits cannot be re-run and cannot be reviewed.
- **Log every transformation.** "Dropped 412 rows with no date" belongs in the readout, not in your memory.
- **Prefer flagging to deleting.** Add a column `is_excluded` with a reason, then report both with and without. A silent deletion is a hidden assumption.
- **Keep a row ID.** Generate one if the file has none, so a spot-check can point at a specific row.

## Dates

- **Indian files mix DD/MM/YYYY and MM/DD/YYYY.** `03/04/2026` is 3 April. If any row has a day above 12, use it to determine the format for the whole column, then apply it everywhere.
- **Excel serial numbers** appear as 45,000-odd integers. Convert, do not average.
- **Time zones** - a sale at 23:50 IST on 31 March belongs to March, not April. Decide the cut-off and state it.
- **Financial year** runs April-March in India. "Q4 FY26" is January-March 2026. State it once, clearly, in every readout.
- **Future dates and 1970 dates** are errors, not data. Count them.

## Money

- **Indian grouping:** ₹1,49,999. Parse commas before casting to numeric.
- **Inclusive or exclusive of GST** - the single most common revenue discrepancy between two teams. Ask, do not assume.
- **Currency mixes** - if any row is in USD or AED, find the conversion rate and the date used, or exclude and say so.
- **Negative amounts** are usually returns or corrections. Decide whether to net them, and say which.
- **Discounts and shipping** - is the revenue line gross or net? Does it include freight? State it.

## Duplicates

| Kind | Example | Action |
|---|---|---|
| True duplicate | Same order ID, same line, exported twice | Drop one, log the count |
| Legitimate repeat | Same customer, same product, two different order IDs | Keep both |
| Near duplicate | Same phone, name spelled two ways | Merge only for customer-level analysis, and say so |
| Refund pair | Original order plus a negative reversal | Keep both; net them |

Deduplicate on the **business key**, never on "all columns identical" - that drops legitimate identical orders.

## Outliers

1. **Look at the row before you decide.** A ₹40 lakh order may be real, and it may be the most important row in the file.
2. **Report with and without.** "Revenue ₹4.2 crore, or ₹2.1 crore excluding the one ₹2.1 crore institutional order" is an honest sentence.
3. **Never winsorise silently.** Trimming the top 1% changes the answer, and the person reading the memo does not know you did it.
4. **Check for unit errors** - a price entered in paise, a quantity of 1000 instead of 1.

## A reusable cleaning checklist

```
[ ] Source copied, original untouched, path recorded
[ ] Row count, and does it match the system's count
[ ] Grain confirmed with one known record
[ ] Date range covers the claimed period, with no gap at the end
[ ] Key uniqueness checked, duplicates counted and explained
[ ] Missing values counted per column, decision recorded
[ ] Money column: min, max, median, p99, negatives explained
[ ] Text categories normalised, sprawl mapped
[ ] GST in/out, net/gross, freight included - all decided and stated
[ ] Exclusions flagged, not deleted, with a reason per flag
[ ] Totals reconciled to the source total, difference explained
```

## Anti-patterns

- Analysing the file before counting its rows.
- Sorting by a column and eyeballing - the top of a sorted list hides the duplicates in the middle.
- Deleting blank rows, when the blank is meaningful (a cancelled order with no value).
- Fixing a category by hand in the sheet, then emailing the sheet on.
- Assuming the export is complete because it opened without error.
- Reporting a total that does not tie to the accounting system, without explaining the gap.
- Cleaning so aggressively that the data becomes clean and useless.
