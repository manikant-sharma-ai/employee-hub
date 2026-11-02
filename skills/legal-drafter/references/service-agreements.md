# Service agreements

The document that decides whether a client engagement ends in a repeat order or a dispute. Almost every dispute in a services business is one of three things: scope creep, an acceptance test nobody wrote, or a payment trigger nobody agreed.

## The structure that works

| Section | Content | The specific thing to get right |
|---|---|---|
| Parties | Legal names, entity type | Match the name on the invoice and the GSTIN |
| Scope | What is included, in a schedule | Include an explicit "not included" list |
| Deliverables and milestones | Each with a date and an acceptance test | Dates absolute, acceptance objective |
| Change control | How scope changes, and what it costs | A written change note signed by both, or the change does not exist |
| Fees | Amount, GST treatment, invoicing trigger | State whether GST is extra and at what rate |
| Payment terms | Due date, mode, late interest | "Net 15 from invoice date", with the invoice raised on the trigger |
| Client obligations | Access, approvals, content, feedback turnaround | The client's delays must move the dates |
| Personnel | Named team or a role-based commitment | Substitution rights if named people matter |
| IP | Who owns deliverables, when it transfers | Transfer on full payment, licence back for portfolio use |
| Confidentiality | Mutual, with the purpose | Cross-reference the NDA if one exists |
| Warranty | What is promised, for how long | "Fit for the purpose stated in the SOW", not "error-free" |
| Liability | Cap, exclusions | Cap at fees paid; exclude indirect loss |
| Term and termination | Duration, notice, for cause | Payment for work done to date survives termination |
| Dispute resolution | Escalation, then arbitration or courts | A seat, a language, a number of arbitrators |
| Schedules | SOW, fee schedule, acceptance criteria | The schedule is the deal |

## The "not included" list

Every service agreement needs one. It is the cheapest protection available:

- Content, copy and images (client supplies, or billed separately).
- Third-party licences, hosting and ad spend.
- Travel and out-of-pocket, billed at actuals with prior approval.
- Revisions beyond two rounds.
- Anything requested after sign-off on the SOW.

A client who reads "not included" before signing does not argue about it later. A client who discovers it later argues about the invoice.

## Acceptance criteria

The clause that prevents the "we're not happy" standoff:

> The Client shall review each Deliverable within 5 business days of receipt and either accept it in writing or provide a single consolidated list of specific deficiencies against the acceptance criteria in Schedule 2. Absence of a response within that period is deemed acceptance.

Then Schedule 2 must contain criteria someone can check: page count, integrations supported, devices tested, accuracy threshold, uptime. Not "high quality".

## Payment triggers

| Trigger | Good clause | Bad clause |
|---|---|---|
| Advance | 40% on signature, non-refundable against the first milestone | "Advance as discussed" |
| Milestone | On acceptance of Milestone 1 per Schedule 2 | "On completion of phase 1" |
| Retainer | Monthly in advance, on the 1st, for the hours in Schedule 1 | "Monthly" |
| Final | On delivery, before handover of source files | "After the project" |

If the deliverable is a website or software, the final payment trigger should be *before* the production deployment or the source handover, not after.

## Scope creep, handled without a fight

- **Log every out-of-scope request** in a change note with an estimate, even when the answer is yes and free. The log is what makes the third request chargeable without accusation.
- **Reference the change note in the invoice.** "₹18,000 - change note CN-07, additional product pages" is not an argument, it is a line item.
- **Never absorb a change silently and mention it at the end.** That is how a good client becomes a bad one.

## Termination

- **For convenience**, either party, 30 days' notice, work done to date payable.
- **For cause**, 15 days to cure a material breach, then immediate termination.
- **Insolvency** - automatic.
- **Survival** - IP, confidentiality, payment and liability clauses survive.

A contract with no termination clause at all is the most common problem in Indian SMB service agreements, and it is the one that traps the business in a client it cannot leave.

## Anti-patterns

- **A scope in prose in the body of the contract.** It will be edited by accident and cannot be versioned; put it in a schedule.
- **"Unlimited revisions" to win the deal.** It wins the deal and loses the quarter.
- **A liability cap that exceeds the contract value** in a small engagement - the client's lawyer will remove it anyway, at cost.
- **Payment on "satisfaction"** with no acceptance test.
- **A fixed price with a variable scope** and no change control.
- **Signing the client's paper without reading the IP assignment.** It usually assigns everything you build, including your reusable components.
