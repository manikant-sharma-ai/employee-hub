# Quote comparison and total cost of ownership

Quotes are not comparable until they are on one basis. This file is the arithmetic
that turns three PDFs into a decision.

## Normalise first, compare second

| Element | Normalise to | Why it changes the ranking |
|---|---|---|
| Scope | The same inclusions and exclusions | One quote excludes installation, which is ₹40,000 |
| Unit | Per piece, per kg, per hour, per month | Per-kg and per-piece quotes are not the same offer |
| Tax | Ex-GST price, with the GST rate stated | Input credit makes GST neutral; composition makes it a cost |
| Freight | Landed at your gate, or FOB stated | Freight can be 8-15% on bulky goods |
| Installation | Included, or priced separately | Capital equipment without installation is not usable |
| Payment terms | Converted to a cost of money | 30 vs 90 days at 12% is about 2% of the invoice |
| Warranty | Years and what it covers, with the service response time | A one-year warranty on a machine with a two-year life is a cost |
| Consumables | Cost per output hour, not per unit | A cheap machine with expensive blades is expensive |

## The comparison table

| Line | Vendor A | Vendor B | Vendor C |
|---|---|---|---|
| Quoted unit price (ex-GST) | | | |
| Discount offered | | | |
| Freight to site | | | |
| Installation and commissioning | | | |
| GST rate / input credit available | | | |
| Cost of payment terms (n days at 12%) | | | |
| Consumables per year | | | |
| AMC after warranty, per year | | | |
| Downtime risk (days/year × daily cost) | | | |
| **Year-1 landed cost** | | | |
| **3-year TCO** | | | |
| Scored preferences (0-5, weighted) | | | |

## The cost-of-money line

`cost = invoice × rate × (days / 365)`

A ₹10 lakh invoice at 90 days, with money at 12%, costs ₹29,589 to carry. Two
vendors quoting the same price with different terms are not quoting the same price.

## TCO, honestly

Total cost of ownership is the purchase plus everything the thing will consume:

- **Energy and utilities** - a machine's kW rating times running hours times the
  unit rate. This alone reorders equipment comparisons.
- **Consumables and spares** - per output unit, from the vendor's own price list.
- **Maintenance** - the AMC after warranty, plus one unplanned repair a year.
- **Downtime** - lost output per day × the days a year it is likely to be down.
- **Operator time** - extra hours per week × the loaded wage.
- **Residual value** - what it is worth at the end, honestly, not optimistically.

State the assumptions in the table. A TCO that hides its assumptions is a
persuasion device, not an analysis.

## Leasing versus buying

| Question | Buy | Lease |
|---|---|---|
| Life of the asset | Long, slow-changing | Short, or fast-obsoleting |
| Cash position | Surplus, or a loan cheaper than the lease | Cash needed for working capital |
| Usage | Heavy, unpredictable | Predictable, or seasonal |
| Tax | Depreciation is useful | Lease rental is deductible |
| Exit | You keep the residual | You return it, and read the exit clause |

Compare the **total cash out over the same period**, not the monthly number. A
₹25,000-a-month lease for three years is ₹9 lakh for an asset that costs ₹6.5 lakh.

## Presenting the decision

Three lines, in this order:

1. **The number**: "Vendor B is ₹1.42 lakh more on day one and ₹38,000 cheaper over
   three years, because its consumable cost is 40% lower."
2. **The risk**: "Vendor B has no service engineer within 300 km; vendor A does."
3. **The recommendation**: which one, and what would change your mind.

## Anti-patterns

- Ranking on the quoted unit price and ignoring freight, GST and terms.
- A TCO with an assumed downtime of zero.
- Comparing a per-piece quote with a per-kg quote.
- Treating input GST as a cost when the business claims credit, or as neutral when
  it is under composition.
- A three-year TCO built on a vendor's optimistic consumable estimate.
- Hiding the recommendation in a spreadsheet instead of stating it in a sentence.
