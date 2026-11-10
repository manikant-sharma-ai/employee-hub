# Expense policy and caps

You cannot audit a policy that has no numbers in it. This file is how a policy becomes
testable, and what to do when it is not.

## The four things every rule needs

| Element | Bad | Testable |
|---|---|---|
| Category | "travel" | "travel - local conveyance, inter-city, lodging, per-diem" |
| Cap | "reasonable hotel" | "lodging up to ₹4,500 a night in metros, ₹2,800 elsewhere" |
| Evidence | "with bills" | "receipt mandatory above ₹500; card statement acceptable below" |
| Approval | "manager approval" | "above ₹10,000 needs the department head; above ₹1,00,000 the founder" |

A rule missing any one of the four produces findings you cannot defend and flags nobody
will accept.

## The categories that matter

Group by how the money is spent, not by the chart of accounts - the audit tests behaviour
and the ledger tests classification.

- **Travel** - local conveyance, inter-city, lodging, per-diem, visa and insurance.
- **Client and sales** - meals, entertainment, gifting, samples, event passes.
- **Workplace** - supplies, furniture, repairs, pantry, courier.
- **Software and subscriptions** - per-seat, per-usage, annual prepay, renewals.
- **Professional services** - CA, legal, consultants, agencies, freelancers.
- **Marketing** - ad spend, influencers, print, events, photography.
- **People** - recruitment, training, medical, relocation, team events.
- **Communication and utilities** - phone, internet, power, rent, CAM.

## Per-diem, done properly

A per-diem is a cap per day that removes the need to audit every meal. Three rules:

1. **Rate by city tier, not by person.** Mumbai, Delhi, Bengaluru, Hyderabad, Chennai,
   Pune get one rate; other cities another.
2. **It covers meals and incidentals, not lodging or travel.** One cap, one purpose.
3. **Either per-diem or actuals with bills - never both** for the same day. Mixed
   policies are the commonest source of duplicate claims.

## The approval matrix

Write it as a table and keep it to five rows. Every row answers: who may approve, up to
what amount, and what happens above it.

- **Self-approval is a design flaw, not a behaviour problem.** If the system allows it,
  the audit will find it every month. Fix the setting.
- **Approval in mail is approval** - but it must be attached, or the claim is
  unevidenced.
- **Emergency spend has a path** - a named approver, a 48-hour regularisation window,
  and the same evidence requirement. Without it, the emergency path becomes the default.

## India-specific items to put in the policy

- **A GST invoice is not the same as a bill.** For input credit the supplier's GSTIN,
  invoice number and HSN are needed; a plain receipt does not carry them. Say which
  categories require a GST invoice and which accept a receipt.
- **TDS on certain payments** - rent, professional fees, contract labour, commission.
  The policy should say who checks the deduction before payment; the rate and the
  section are the CA's call.
- **MSME suppliers** - the statutory payment window for a registered micro or small
  supplier is short, and the consequence of missing it is a tax one. Confirm the
  position with the CA and put the flag in the vendor master, not in a person's memory.
- **Cash claims** - a cap, a receipt rule and a reason. Cash without a receipt is the
  one category where the audit cannot distinguish error from loss.
- **Gifts and hospitality** - a value cap, a register, and a rule about public officials
  that is absolute rather than a threshold.

## When there is no policy

Say it in the first line and audit against the only standard you have: what the business
has consistently allowed. That is defensible if it is stated as such - "no written
policy; tested against the pattern of the last six months and flagged the deviations".

Then deliver the three sentences that would make the policy testable, in the categories
where the most money moved. A full policy rewrite is a different job; three sentences is
what an audit can justify.

## Anti-patterns

- **"As per company policy"** with no policy attached.
- **A cap that has not been revised in three years** while the category has inflated -
  it produces constant breach and constant exception, which trains everyone to ignore
  both.
- **Different caps for different people** without a documented reason.
- **A policy nobody has read.** Check: does the approval screen link to it? If not,
  breach is a design outcome.
