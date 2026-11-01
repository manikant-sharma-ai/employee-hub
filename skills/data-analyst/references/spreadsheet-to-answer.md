# Spreadsheet to answer

The practical method for going from a file to a defensible number. Choose the tool by the size and the need to re-run, not by habit.

## Which tool

| Situation | Tool | Why |
|---|---|---|
| Under ~5,000 rows, one-off, the client will keep the file | Google Sheets or Excel | They can open it, change a filter, and trust it |
| Under ~5,000 rows, one-off, you are the only reader | Either | Sheets is faster to share |
| 5,000-500,000 rows, or repeated monthly | Python + pandas | Reproducible, fast, reviewable |
| Joined data from two systems, or a recurring report | Python + pandas, saved as a script | The next run should be one command |
| Live data in a warehouse | SQL against the source | Do not export what you can query |
| A dashboard someone will look at weekly | Hand off to `ai-engineer` after the analysis is settled | The analysis and the automation are different jobs |

The rule: **if it will be run twice, write it as code.** A sheet built by hand cannot be re-run, and the second month always differs slightly from the first.

## The pandas skeleton

Save it, name it, keep it. This is the shape of a re-runnable analysis.

```python
import pandas as pd

RAW = "october_sales.xlsx"          # never edited
df = pd.read_excel(RAW, sheet_name="Orders")

# 1. Profile
print(len(df), df.columns.tolist())
print(df["order_date"].min(), df["order_date"].max())
print(df.isna().sum())

# 2. Clean - flag, do not delete
df["amount"] = (df["amount"].astype(str)
                  .str.replace("₹", "", regex=False)
                  .str.replace(",", "", regex=False)
                  .astype(float))
df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True, errors="coerce")
df["is_excluded"] = df["order_date"].isna() | df["status"].eq("cancelled")
print("excluded:", df["is_excluded"].sum())

# 3. Analyse on the included rows only
d = df[~df["is_excluded"]].copy()
by_month = d.groupby(d["order_date"].dt.to_period("M"))["amount"].sum()
print(by_month)

# 4. Reconcile
print("total:", d["amount"].sum(), "source total:", 4_218_500)
```

Rules: read the raw file, never write to it; print the counts you rely on; assert the total.

## The sheet pattern

If the deliverable is a spreadsheet, structure it so a stranger can audit it.

```
Sheet 1  README        - what this is, source, period, definitions, date built
Sheet 2  Raw           - untouched copy of the source
Sheet 3  Clean         - flagged exclusions, added columns
Sheet 4  Analysis      - pivot tables or formulas, no hardcoded numbers
Sheet 5  Readout       - the one-page answer
```

- **No hardcoded values in the Analysis sheet.** Every number comes from a formula or a pivot, so it updates when the data does.
- **Name the ranges.** `orders`, `period_start` - a formula with `A2:A4821` is unreadable in six weeks.
- **One metric per column**, with the unit in the header: `Revenue (₹, net of GST)`.
- **Colour-code inputs vs calculations** and say which is which in the README.
- **Freeze the header, filter everything, no merged cells.** Merged cells break every pivot and every export.

## Useful formulas that come up constantly

| Need | Formula |
|---|---|
| Growth rate | `=(B2-A2)/A2` formatted as % |
| Share of total | `=B2/SUM($B$2:$B$20)` |
| Rank with ties handled | `=RANK.EQ(B2,$B$2:$B$20)` |
| Cumulative share | `=SUM($B$2:B2)/SUM($B$2:$B$20)` |
| Safe lookup | `=IFERROR(XLOOKUP(A2,keys,vals),"not found")` |
| Distinct count | `=COUNTA(UNIQUE(range))` (Sheets) / a pivot in Excel |
| Weighted average | `=SUMPRODUCT(values,weights)/SUM(weights)` |
| Cohort month | `=TEXT(MINIFS(dates,ids,A2),"YYYY-MM")` |

Never use `VLOOKUP` with an approximate match. It is the single most common source of a quietly wrong spreadsheet.

## Reconciling two files

The most common real request, and it has a fixed method.

1. **Match on a key.** Invoice number, order ID, phone. Not on name, not on amount.
2. **Full outer join**, so you see both sides.
3. **Classify every row**: matched, only in A, only in B, matched but different amount.
4. **Report the four counts and the net difference**, then the top 10 mismatches by value.
5. **Do not "fix" the difference.** Explain it. A ₹2.4 lakh gap is usually 3 invoices, a timing cut-off, or GST.

## Reproducibility

- **Date the script and the data.** A result without a vintage cannot be re-checked.
- **Pin the assumptions at the top of the file**, as constants, not buried in the middle.
- **Print the numbers you quote.** If the readout says ₹18.4 lakh, the script should print ₹18.4 lakh.
- **Keep the artifact with the readout.** The next person will need to change one filter.

## Anti-patterns

- Copy-pasting a pivot table's values into a new sheet, then losing the link to the data.
- A 40-tab workbook nobody can navigate, including its author.
- Analysing 200,000 rows in Excel with 40 volatile formulas, then waiting ten minutes per change.
- A script with a hardcoded path to someone's Downloads folder.
- Overwriting the raw export "to clean it up".
- Reporting a number from a sheet that was edited after the analysis.
- Building the dashboard before anyone has agreed what the number means.
