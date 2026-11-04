# SQL and queries

Most business data is not in a spreadsheet; it is in a database or a warehouse.
The craft is asking the question in a way that cannot be wrong by accident.

## The shape of every query

```sql
SELECT   <grain columns>, <aggregates>
FROM     <table>
WHERE    <row filters: date range, status, tenant>
GROUP BY <grain columns>
HAVING   <aggregate filters>
ORDER BY <the one that answers the question>
LIMIT    <sanity cap>
```

Write the grain first: "one row per order per day". Almost every wrong number is
a wrong grain, and the query runs happily either way.

## The five mistakes that produce a confident wrong number

| Mistake | What it does | The check |
|---|---|---|
| Join fan-out | A one-to-many join multiplies the rows and inflates every sum | Count rows before and after the join |
| Filtering after aggregation | `WHERE` on an aggregate fails silently or filters too late | Use `HAVING` for aggregates, `WHERE` for rows |
| Nulls in a comparison | `NULL <> 'cancelled'` is unknown, not true - rows vanish | Add `OR col IS NULL` deliberately, or exclude on purpose |
| Timezone | A day in UTC is not a day in IST | Convert at the boundary, state which zone the report uses |
| Partial period | Comparing a 28-day month to a 31-day one | Normalise, or compare like windows |

## Date ranges, in IST

- Store UTC, report IST. The offset is +5:30, so a "day" boundary is 18:30 UTC the previous day.
- `BETWEEN` on timestamps includes the last day only up to midnight - use `>= start AND < end`.
- Month-to-date, last full month, same period last year - name which one you used in the readout.

## Joins, honestly

- **Inner join silently drops rows.** Before trusting a total, `LEFT JOIN` and count the misses.
- **Join on the most specific key** available; joining on name or email creates duplicates.
- **Check cardinality first**: `SELECT key, COUNT(*) ... GROUP BY key HAVING COUNT(*) > 1`.

## Validation before you present

1. Row count at the grain - does it match an independent count?
2. Sum check against a known total (revenue, orders) from another source.
3. One manual spot check: pick three rows and verify by hand.
4. Sanity: does the number pass the smell test, and if not, why?

## Warehouse specifics

- **Partition filters save money.** A query without a date filter on a partitioned table scans everything.
- **BigQuery/Supabase cost is per byte scanned.** `SELECT *` on a wide table is a budget decision.
- **Materialise what you reuse**, and name the freshness.

## Anti-patterns

- `SELECT *` in a query you will paste into a report.
- Aggregating without stating the grain.
- A "revenue" column that is actually gross, before refunds and fees - name the definition.
- Testing a query by whether it runs, not by whether the total is right.
- Hardcoding a date range nobody will remember to change.
