# Duplicate and anomaly detection

Most leakage is not fraud. It is the same claim submitted twice, two people paying for
the same subscription, and an invoice split to stay under an approval line. These tests
find it.

## The tests, in order of yield

| Test | Rule | Typical severity |
|---|---|---|
| Exact duplicate | same vendor, same amount, same date | high |
| Near duplicate | same vendor, same amount, dates within 7 days | medium |
| Split invoice | same vendor and person, 2+ claims each under the approval threshold, within 14 days, summing above it | high |
| Cap breach | a single claim above the category cap | medium |
| Monthly cap breach | a person's month in a category above the monthly cap | medium |
| Missing receipt | above the receipt threshold, no document | medium |
| Duplicate vendor master | two vendor records, similar name or same GSTIN | high - it hides both price drift and duplicate payment |
| Price drift | invoice rate above the contracted or last-paid rate by more than a set percentage | medium |
| Concentration | one vendor above a share of category spend with no contract | info to medium |
| Round-number pattern | repeated round amounts just under a threshold | low - justify, do not accuse |

`scripts/expense_check.py` runs the first seven and the concentration test. Run it, then
read the queue; do not eyeball 3,000 rows.

## Why vendor plus amount, not amount alone

Two ₹4,999 claims from two different vendors are two purchases. Two ₹4,999 claims from
the same vendor in the same week are one purchase paid twice, or a split. The vendor
string needs normalising first - "Amazon", "AMAZON IN", "Amazon Seller Services" are the
same payee, and GSTIN is the reliable key where it exists.

## The split-invoice pattern

The most common deliberate evasion in a small business, and the easiest to test:

- each claim is under the approval threshold (say ₹10,000),
- same vendor, same person, same or adjacent weeks,
- the sum crosses the threshold,
- and the invoices are sequential numbers or the same description.

Report it as a pattern with the sum, not as four separate findings. The question to the
approver is "was this one purchase?" - because sometimes it genuinely was four.

## Ghost and conflict vendors

- **A vendor with no GSTIN, a personal bank account and one payer** deserves a check
  against the employee master.
- **An employee whose address, phone or bank matches a vendor's** is a conflict, not a
  crime; it needs a declaration on file.
- **A vendor created in the same month as its first invoice** with no contract and no
  quote is a control gap even when it is honest.

These go to the founder in a separate note. Never into the general finding list, and
never with a name attached to a conclusion.

## The review queue

Aim for a queue a human can clear in twenty minutes per month:

1. **High** - duplicates, splits, ghost vendors. Confirm or kill each one.
2. **Medium** - caps, receipts, drift. Batch by owner: one mail per owner with their
   lines, not one per line.
3. **Low** - patterns and heuristics. Show the count and the total, not the rows.

Every test carries its false-positive rate in the journal. A test that flags 60 claims
and confirms 2 is not a control; it is noise, and it will get the whole audit ignored.

## What the tests cannot see

- A legitimate-looking invoice for work that was never done.
- A personal purchase inside a plausible category, at a plausible amount, with a
  receipt.
- Kickbacks, which show up as price drift, not as a claim.
- Anything paid outside the system - cash, a personal card reimbursed in a lump sum, a
  director's account.

Say this in the output. An audit that claims completeness invites the one finding that
matters to be dismissed.

## Anti-patterns

- **Fuzzy matching without a threshold**, which flags every "Sharma" as a duplicate.
- **Testing amount only**, which finds coincidences.
- **Reporting the same duplicate four times** because it appeared in four exports.
- **Flagging a claim twice** - once as a duplicate and once as a cap breach - and
  double-counting the amount at risk.
