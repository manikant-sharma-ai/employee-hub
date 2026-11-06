# Dispute and shortfall

A dispute is not a delay with an excuse. Treating it as a delay is how a ₹9,000
disagreement freezes a ₹9 lakh relationship.

## Triage in three questions

1. **What exactly is disputed** - the whole invoice, one line item, a rate, a
   quantity, or the quality of what was delivered?
2. **How much is it worth** - the disputed amount, not the invoice amount.
3. **Is there a written basis** - the PO, the contract, the delivery challan, the
   email approving the change?

The answer decides the track:

| Situation | Track | Ladder |
|---|---|---|
| Whole invoice disputed, written basis | Dispute track only | Frozen, 5-working-day resolution target |
| Part disputed, rest undisputed | Split | Chase the undisputed balance on the normal ladder |
| No written basis, customer withholding | Evidence track | Send the documents, ask for specifics in writing |
| Dispute used repeatedly to delay | Escalation | Stage 4 with the evidence attached |

## Splitting the invoice

This is the single most valuable move in this file. A customer disputing ₹9,000 on
a ₹9,00,000 invoice should pay ₹8,91,000 this week.

> Subject: INV-2041 - paying the undisputed portion
>
> Hello <name>,
>
> You have raised a question on ₹9,000 of INV-2041 (the installation charge). I am
> looking into that today and will come back by Thursday.
>
> The remaining ₹8,91,000 is not in dispute. Please release that this week, and we
> will settle the balance separately.

If the customer refuses to split, the dispute is not the real reason. Say so
plainly, once, and move to stage 4.

## The dispute resolution, in five working days

| Day | Action | Output |
|---|---|---|
| 1 | Acknowledge in writing, restate the disputed amount | A dated note the customer agrees to |
| 1 | Collect the evidence - PO, challan, approval email, rate card | A file per dispute |
| 2 | Check our side first. Assume we might be wrong | A finding: we erred, or we did not |
| 3 | Propose the resolution - credit note, corrected invoice, or a documented refusal | A written proposal |
| 5 | Close or escalate to a person on both sides | A decision, not a thread |

A dispute older than 15 working days with no written position from us is a
collections failure, not a customer failure.

## Credit notes and deductions

| Situation | Treatment | Who approves |
|---|---|---|
| We billed the wrong rate | Credit note for the difference, corrected invoice | `finance-ops` |
| Short delivery, accepted by us | Credit note against the challan | `finance-ops` |
| Customer deducted without agreement | Do not accept; send the evidence; chase the balance | Account owner |
| Customer deducted TDS | Expected, not a shortfall - reconcile against Form 26AS | `finance-ops` and the CA |
| Cash discount taken outside terms | Treat as a shortfall, ask for the difference | Account owner |

TDS deductions are the most common false alarm in Indian B2B collections. Check the
TDS rate and the section before writing an angry email.

## Part payment

Accept it, record it, and be explicit about what remains:

> Received ₹5,00,000 today against INV-2041. Balance ₹3,91,000, due 30 November.
> If that date does not work, tell me now and we will agree a plan in writing.

Rules for a part payment:

- **Always confirm the balance in writing the same day.** Memory diverges within a week.
- **Apply it to the oldest invoice first**, unless the customer specifies and the contract allows otherwise.
- **Never let a part payment reset the ladder.** The balance continues at its stage.
- **A part payment plan is a written schedule** - amount, date, and what happens on a miss.

## When the customer cannot pay

| Signal | What it means | What to do |
|---|---|---|
| "Our customer has not paid us" | Cash chain problem | Ask for a dated plan; consider a post-dated cheque or a partial release |
| Asks for a longer term retroactively | Cash stress | Founder decision, in writing, with a deadline |
| Stops responding after a promise | Avoidance | Stage 4, and the account owner calls |
| Announces a funding crisis | Insolvency risk | Escalate immediately; a lawyer and the CA decide the route |
| Offers goods instead of cash | Distress | Founder decision; usually a bad trade unless the goods are sellable |

Under the MSMED Act, a supplier registered as a micro or small enterprise has
statutory recourse on delayed payments. Whether it applies, and what interest is
payable, is a question for the CA and `legal-drafter` - this role names it and does
not compute it.

## Anti-patterns

- **Freezing the whole invoice over a small line item.** The most expensive habit in collections.
- **Arguing the dispute in the same thread as the payment chase.** Two tracks, two threads.
- **Accepting a deduction to keep the peace** without a written reason. It becomes the new price.
- **Treating a TDS deduction as non-payment.**
- **Resolving a dispute verbally.** It reopens in the next invoice cycle.
- **Letting a dispute run past 15 working days with no position from us.**
