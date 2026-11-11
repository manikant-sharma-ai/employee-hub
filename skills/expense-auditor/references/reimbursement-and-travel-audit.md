# Reimbursement and travel audit

Travel and reimbursement claims are the highest-frequency, lowest-value, highest-friction part of
any expense audit. The goal is a clean answer in one pass, not a hunt.

## The claim pack, checked in this order

| # | Check | Fails when |
|---|---|---|
| 1 | Claim submitted inside the window | Date of expense is older than the policy allows |
| 2 | Purpose and the person or client named | "Meeting" with nobody named |
| 3 | Receipt for every line above the receipt floor | A claim line with no document |
| 4 | Amount on the receipt equals the claim | GST or tip added on top |
| 5 | Category eligible | Alcohol, personal shopping, family travel |
| 6 | Within the category cap | Hotel above the city tier |
| 7 | Approved by the right person | Self-approval, or a peer |
| 8 | Not previously reimbursed | Same trip claimed in the last cycle |
| 9 | Advances adjusted | An advance paid but not knocked off |
| 10 | Bank details match the employee record | A changed account with no verification |

## Travel arithmetic that catches most overclaims

| Item | Test |
|---|---|
| Air or rail | Claimed fare vs the booking confirmation vs the fare class policy |
| Hotel | Nights claimed vs nights between travel dates; rate vs the city cap |
| Local conveyance | Trips claimed vs the meeting schedule; two claims for one leg |
| Mileage | Km claimed vs the distance on a map, plus a from-to log |
| Per diem | Days claimed vs travel dates, and per diem plus actual meals for the same day |
| Meals | More than three meal claims in a day, or a meal during a flight that served one |
| Incidentals | A flat allowance claimed alongside itemised incidentals |
| Extended stay | A weekend inside a trip with no business reason |

The single most common finding: **per diem and actual bills claimed for the same day.** The
policy must say which one applies, and the claim must show it.

## The interview, when a claim needs one

Three rules, and they decide whether the person helps or defends:

1. **Ask for the document, not the explanation.** "Can you send the hotel invoice for the 14th?"
   gets a document. "Why did you claim ₹8,400?" gets a story.
2. **One question per item, in writing, with a date to reply.** A list of eleven questions reads
   as an accusation and gets an escalation to the founder.
3. **Give the correction path up front.** "If the invoice shows ₹6,200, I'll adjust the claim to
   that and close it." Most findings close here, which is the outcome you want.

Never threaten, never imply intent, never copy a manager on the first query unless the policy
requires it. Escalate to the founder only when the document contradicts the claim and the person
will not correct it.

## Recurring patterns, and what they usually mean

| Pattern | Likely cause | Fix |
|---|---|---|
| One team consistently at the cap | The cap is the real cost of travel in that role | Raise it, or pre-approve a rate |
| Claims with no receipts, repeatedly | A receipt floor set too low for small spends | A no-receipt allowance with a declaration |
| Late submissions | No consequence, and a slow approver | A 30-day window and a named approver with a service level |
| Advances never settled | No settlement step in the process | A settlement date, and no new advance until the last is closed |
| Same trip claimed twice | Two systems, or a resubmission after rejection | One submission channel, and a status visible to the claimant |
| A changed bank account | Often innocent, sometimes not | Verify by phone against the HR record, always |

## The advance ledger

If advances exist, they are a control point, not a convenience:

| Column | Why |
|---|---|
| Advance paid, date | The outflow |
| Purpose and trip | What it was for |
| Settlement claimed | What came back as bills |
| Balance returned | Cash back, with a receipt |
| Age | Anything over 60 days is a recovery item |

Unsettled advances are effectively unrecorded expenses. They belong in the exceptions register
with an age, not in a reminder email.

## The finding, written the way that closes it

```
Claim RE-2025-0412, 14-16 Oct, Mumbai.
Claimed ₹18,420. Hotel invoice shows ₹13,860 for two nights; the third night was billed to the
client. Category cap is ₹6,500 per night in a metro, so ₹13,860 is within the cap.
Adjustment: -₹4,560. Requested 6 Nov; corrected by the claimant on 7 Nov; closed.
Control note: the client-billed night was not marked in the claim. Add a "billed to client"
field.
```

That block is worth more than a page of summary, because it shows the amount, the document, the
rule, the action and the fix.

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Rejecting a whole claim for one line | The person resubmits everything and trust drops |
| Auditing travel and ignoring the vendor ledger | The smaller half of the leak |
| Per diem and actuals both allowed | The most common systematic overclaim |
| No advance ledger | Cash leaves and never comes back on record |
| Public shaming in a group email | Every future claim becomes adversarial |
| No fix after three identical findings | The same audit next quarter, for the same rupees |
