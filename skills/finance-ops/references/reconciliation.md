# Reconciliation

Reconciliation is not "does the total match". It is "every rupee that moved has a document behind it, and every rupee that did not move has a reason".

## The bridge, always in this shape

```
Opening balance (per books)          X
+ Sales invoiced in the period       X
+ Other receipts (interest, refunds) X
- Collections received               X
- Payments made                      X
- Adjustments (credit notes, TDS)    X
= Closing balance (per books)        X

Closing balance per bank statement   Y
Difference (X - Y)                   D  -> itemised below
```

A bridge that jumps straight from "expected" to "actual" hides the error. The itemisation is the deliverable.

## The five reconciliation types in an Indian business

| Type | Sources | Typical gap | Where it hides |
|---|---|---|---|
| Bank | Bank statement vs cash/bank ledger | Cheques issued not cleared, bank charges, interest, standing instructions | Charges and interest, because nobody posts them |
| Gateway | Razorpay/PayU settlement vs sales | Fee, GST on fee, refunds, failed-then-succeeded, T+2 timing | The payout is net, the sale is gross |
| Cash | Cash book vs physical count | Petty expenses without bills, owner drawings | Unrecorded small spends |
| Card / POS | POS settlement vs sales | MDR, settlement lag, chargebacks | Settlement date versus sale date |
| Vendor | Purchase ledger vs vendor statement | Missing bills, debit notes, TDS deducted but not recorded | Bills received after month end |

## Bank reconciliation, in order

1. **Start from the bank statement, not the books.** The bank is the external truth; the books are what we think happened.
2. **Match exact amounts and dates first** (±3 days), then amount-only, then fuzzy.
3. **List unmatched bank lines** - these are real movements with no book entry: charges, interest, auto-debits, customer direct transfers.
4. **List unmatched book lines** - usually cheques issued and not cleared, or deposits in transit.
5. **Investigate anything over a threshold** you set with the owner (₹10,000 is a reasonable default for an SMB).
6. **State the closing difference.** Zero, or a named amount with the question attached.

## The gateway gap, worked out

Sales of ₹10,00,000 through a gateway, payout of ₹9,78,000. The ₹22,000 is not a mystery, it is four known things:

| Item | Amount | Where it appears |
|---|---|---|
| Gateway fee (2%) | ₹20,000 | Settlement report, per-transaction column |
| GST on fee (18%) | ₹3,600 | Fee invoice from the gateway |
| Refunds in period | ₹5,000 | Refund report |
| Prior-period settlement | -₹6,600 | Opening timing difference |

Rule: **book the gross sale, the fee and the GST on fee separately.** Booking the net payout understates revenue and overstates margin, and the error compounds every month.

## Common reconciling items, and whether they are fine

| Item | Normal? | Action |
|---|---|---|
| Cheque issued, not cleared | Yes | Carry forward, flag after 90 days (stale cheque) |
| Bank charges | Yes | Post them; they are small and always forgotten |
| Interest credited | Yes | Post to other income |
| Customer paid into the wrong account | No | Trace and reallocate; do not leave in suspense |
| Vendor debited twice | No | Stop, raise a dispute, do not net it off |
| UPI collect pending | Yes | Match on the next statement |
| Round-number transfer from the owner | No | It is either a loan, a drawing or capital - ask which |
| Unknown credit with a reference number | Sometimes | Chase the reference before month end |

## Suspense accounts

A suspense balance is a to-do list, not an account. Rules:

- **Every suspense entry has an owner and a question**, in the exception list.
- **Nothing stays in suspense across two closes** without a written reason.
- **Report the balance prominently** in the close pack. A growing suspense account is the earliest signal of a process failure.

## Anti-patterns

- **Plugging the difference into "miscellaneous".** It converts a question into a permanent error.
- **Reconciling the net payout only.** Revenue is understated, fees are invisible, and the P&L lies.
- **Matching on amount alone across a large file.** Two ₹5,000 entries a day apart are not necessarily the same transaction.
- **Reconciling a period that is not closed.** Transactions landing mid-reconciliation make the difference move under you.
- **Treating a bank charge as immaterial forever.** Twelve months of unposted charges is a real, auditable gap.
- **Reconciling in the accounting system only, with no working paper.** The next person cannot see how the number was reached.
