# Vendor spend review

The claims audit looks at what people spent. This looks at who is being paid, how much,
and whether anyone agreed to it.

## The pivot

One table, sorted by annual spend: vendor, category, spend, share of category, number of
invoices, average invoice, contract in place, contracted rate, last rate change, owner.

The four questions that come out of it:

1. **Concentration** - is more than 30% of a category with one vendor and no contract?
   That is a supply risk and a price risk at once.
2. **Drift** - has the unit rate moved since the contract or the last quote, without a
   change note?
3. **Creep** - are there subscriptions nobody can name an owner for, or two tools doing
   the same job?
4. **Maverick spend** - is a category being bought outside the agreed vendor, in small
   amounts, by many people?

## Price drift, tested

Keep the last agreed rate per vendor and item in the vendor master. Then:

- compare each invoice line rate against it,
- flag any increase above the agreed escalation or above 5%, whichever is lower,
- and name the date the rate changed.

A rate that rose with no change note is either an unrecorded negotiation or a billing
error, and both are worth a line. This is where a kickback usually shows up - not as a
claim, but as a price that quietly moved and stayed moved.

## Subscription creep

The single most reliable saving in a small business:

- list every recurring charge with its billing cycle, seats and owner,
- mark the ones with no owner, no login in 90 days, or no named use case,
- sum the annual value of the ones to cancel,
- and give the founder one number: "₹2.4 lakh a year in subscriptions with no owner".

Cancelling is a decision, not an audit output. This role produces the list and the
number.

## Contract versus invoice versus ledger

Three-way check on the top ten vendors by spend:

| Source | Question |
|---|---|
| Contract | what rate, what volume, what escalation, what term |
| Invoice | what was actually charged, and for what quantity |
| Ledger | what was booked, in which period, to which cost centre |

Disagreement between any two is a finding. A quantity billed above the contracted
quantity, or a period booked twice across a year-end, is the kind of thing that survives
right up to a statutory audit and then does not.

## GST and documentation consistency

- **GSTIN on the invoice** - a vendor billing without one may be unregistered, which
  costs the input credit and, above the threshold, is a compliance issue.
- **Name and GSTIN mismatch** between the invoice and the vendor master - the commonest
  cause of a failed input-credit match.
- **Invoice date versus return period** - a credit claimed in a period the supplier has
  not filed for will be reversed.

These are observations for the CA, not conclusions. State them as questions.

## What to recommend

- **Top three vendors by spend**: a written rate card and a review date.
- **Every vendor above the materiality threshold**: an owner in the vendor master.
- **Any category with more than five vendors**: consolidation or a policy on who may
  buy.
- **Any recurring charge with no owner**: cancel or assign, this month.

## Anti-patterns

- **Reviewing spend without the contract**, which produces opinions rather than findings.
- **Treating a big vendor as a problem.** Scale is often the reason the rate is good.
- **Recommending a switch without the switching cost** - setup, migration, retraining.
- **Ignoring the small vendors.** Forty ₹8,000 vendors a month is a control problem even
  though no single line is material.
