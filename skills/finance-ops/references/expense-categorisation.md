# Expense categorisation

Categorisation decides what the P&L tells you six months later. A book where everything is "Office Expenses" is a book that cannot answer a single question.

## Use the chart of accounts that exists

Rules, in order:

1. **Read the chart of accounts first.** It is an input, not a suggestion.
2. **Map to the nearest existing category** and note the misfit in the exception list.
3. **Propose a new category only when three or more items a month land in the same gap.** One-off items go to the nearest bucket.
4. **Never create a category silently.** It needs an owner's approval, and a note in `notes/decisions.md`.

## A working chart for an Indian SMB

| Group | Typical categories |
|---|---|
| Direct costs | Raw material, traded goods, freight inward, job work, direct labour |
| People | Salaries, contract staff, PF/ESI, staff welfare, recruitment, training |
| Premises | Rent, electricity, water, society charges, repairs, housekeeping |
| Selling | Advertising, marketplace fees, gateway fees, commissions, travel for sales, samples |
| Technology | Software subscriptions, hosting, domains, IT support, hardware (capital) |
| Professional | Audit, legal, consulting, CA fees, company secretary |
| Admin | Printing, stationery, courier, telephone, internet, insurance, bank charges |
| Statutory | GST payable, TDS payable, professional tax, property tax |
| Finance | Interest, processing fees, forex loss |
| Owner | Director remuneration, drawings, loan to/from directors |

## Decisions that come up constantly

| Question | Rule |
|---|---|
| Capital or revenue? | Capitalise if it creates an asset used beyond 12 months and above the business's capitalisation threshold; otherwise expense it |
| Personal or business? | If it benefits the owner personally and has no business nexus, it is a drawing, not an expense - flag it, do not silently expense it |
| Client entertainment? | Often disallowed or restricted for tax; flag it and let the CA decide |
| Advance to a vendor? | Not an expense. It is an asset until the bill arrives |
| Deposit (rent, electricity)? | Not an expense. Asset until refunded or adjusted |
| Software subscription, annual? | Prepaid asset, amortised monthly - or expensed if the policy says so; state which |
| Freight outward on a sale? | Selling cost, not direct cost, unless the policy is to include it in landed cost |
| Free samples? | Selling or promotional expense, at cost |
| Interest on a late GST payment? | Statutory, non-deductible in some cases - flag to the CA |
| Bank charges | Admin, and always small enough to be forgotten - post them |

## GST-relevant attributes to capture per bill

| Attribute | Why |
|---|---|
| GSTIN of the vendor | Without it, no input credit |
| Invoice number and date | Required for the 2B match |
| Taxable value and tax split | For GSTR-3B and the ITC register |
| HSN/SAC | For classification consistency |
| Whether it is in GSTR-2B | The reconciliation that decides whether ITC is claimable |
| Reverse charge applicable | The business pays the tax, not the vendor |

A bill without a GSTIN, for a vendor who should be registered, is a bill you cannot claim credit on. Flag it at entry, not at filing.

## Volume handling

- **Batch by vendor**, not by date. The same vendor's bills use the same category, so decide once.
- **Handle the top 20 vendors first** - they are usually 70-80% of the value.
- **Everything under a small threshold** (₹500 is a reasonable default) goes to the dominant category for that vendor and is listed separately.
- **Keep an "unsure" list** rather than guessing. A wrong category is harder to find than a blank one.

## Anti-patterns

- **"Miscellaneous" as a category.** Within three months it holds a third of the spend and answers nothing.
- **Categorising by who paid, not by what it was for.** It makes cost control impossible.
- **Expensing a deposit.** It overstates cost in one month and understates assets in every month.
- **Putting the owner's personal spends through the business** without recording them as drawings. It creates a tax problem and a reconciliation problem.
- **Recording a bill without the GSTIN** and remembering it later. You will not remember it later.
- **Retro-fitting categories to make a month look better.** Reclassifications need a reason and a note.
