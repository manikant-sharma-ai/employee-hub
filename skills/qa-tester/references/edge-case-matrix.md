# Edge-case matrix

Edge cases are not invented, they are generated. Pick the inputs, pick the values, cross them, and the cases you would never have thought of appear on their own.

## The dimensions of almost any input

| Dimension | Values to include |
|---|---|
| Empty | "", null, whitespace only, no rows selected |
| Boundary | 0, 1, max, max+1, negative, ₹0.01, ₹0.00 |
| Length | 1 char, 255, 256, 10,000 |
| Format | valid, almost valid, valid but unusual |
| Encoding | Devanagari, Tamil, emoji, RTL, combining characters, zero-width joiner |
| Case | lower, UPPER, MiXeD |
| Duplicate | same value twice, same value in two fields |
| Sequence | double-click, back button, refresh, two tabs, retry after timeout |
| State | before login, after logout, expired session, mid-migration |
| Network | offline, slow (2G), timeout, response arrives twice |

## Indian realities that break software

| Input | The case people miss |
|---|---|
| Mobile number | 10 digits, `+91`, `0` prefix, `+91-` with spaces, 11 digits, a landline, a number starting with 6-9 only |
| Money | ₹ with paise, ₹1,00,000 lakh grouping, a ₹0 order, negative totals, rounding on 0.5 |
| Address | No house number, no PIN, PIN of 6 digits, a village with two names, "near the temple" |
| Name | One word only, Devanagari, Tamil script, 60 characters, an honorific, an apostrophe |
| Date | DD/MM vs MM/DD, a financial year starting in April, a Sunday, a holiday |
| GST | Inclusive vs exclusive, IGST vs CGST+SGST, a B2C order with a GSTIN |
| Payment | UPI timeout after debit, COD, a failed card then a retry, a partial refund |
| Language | Hinglish input, mixed script, a form that only validates ASCII |

## Generating rather than guessing

Use `scripts/edge_matrix.py` on a spec of dimensions and values. It produces a pairwise set - every pair of values covered at least once - which is typically 10-20% of the full cartesian product and finds the same interaction bugs.

```json
{"feature": "coupon", "dimensions": {
  "code": ["valid", "expired", "unknown", "empty", "lowercase", "already used"],
  "cart": ["one item", "multiple", "empty", "above threshold"],
  "user": ["guest", "logged in", "returning"]
}}
```

Nine tests instead of seventy-two, and the coverage is a number you can quote.

## Beyond pairwise

Three-way interactions matter when a single wrong combination has a high cost. The classic cases:

- **Permission × resource × action** - the URL that a role should not reach.
- **Currency × payment method × refund path.**
- **Language × number format × date field.**
- **Tenant A × tenant B × a shared cache.**

For those, enumerate three dimensions fully rather than sampling.

## The states nobody tests

- **Empty** - the first-run screen, the list with zero rows, the dashboard before any data.
- **Loading** - the skeleton, the spinner that never resolves, the retry.
- **Error** - a 500 on submit, a validation message on a field the user cannot see.
- **Partial** - some rows loaded, one image failed, one API of three returned.
- **Long** - 10,000 rows, a 400-character name, a 40-item cart.
- **Repeated** - the second click, the double submit, the duplicate webhook.

## Anti-patterns

- Testing boundaries only where the developer thought about them.
- Skipping the empty state because "nobody will have an empty cart".
- Testing with English names only, then shipping to a market that does not use them.
- Treating pairwise coverage as proof of quality rather than a floor.
- Edge cases with no expected result written down, so any behaviour counts as a pass.
