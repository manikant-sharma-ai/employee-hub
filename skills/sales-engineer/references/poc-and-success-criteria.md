# Proof of concept and success criteria

A POC is a paid-for decision, even when nobody pays for it. It costs engineering hours, it
occupies a buyer's team, and it either ends in a decision on a date or it ends in drift.

## The four things agreed before it starts

1. **Success criteria** - three to five, written, weighted, and measurable by the buyer.
2. **A timebox** - a start date, an end date, and the date of the decision meeting.
3. **A buyer-side owner** - a named person who provides access and answers questions
   inside two working days. Without this, the POC's clock is not real.
4. **The exit** - what happens if the criteria are met, and what happens if they are not.
   Both in writing, both agreed before the build.

`assets/poc-plan-template.md` is the document. `scripts/poc_plan.py` scores it.

## Writing a criterion that can fail

| Bad | Good |
|---|---|
| "Improved efficiency" | "Invoice reconciliation for 5,000 invoices completes in under 4 minutes with under 0.5% unmatched" |
| "Works with our ERP" | "Nightly export from S/4HANA loads 40 fields into the staging tenant without manual mapping" |
| "Easy to use" | "Two named finance users complete the month-end flow unassisted after one 30-minute session" |
| "Scales" | "Sustains 200 concurrent users at p95 under 800ms in a load test on their data volume" |

If the buyer cannot say how it will be measured, the criterion is not ready and the POC
is not either.

## Weighting

Weights make the decision arithmetic instead of emotional. Typical split: the one
criterion that decides the deal gets 50%, the integration 25%, usability 15%, performance
10%. Score each 0 to 100 against its target, multiply by weight, and the go/no-go is a
number the buyer agreed to in advance.

Set thresholds before the POC: go at 85 and above, conditional between 70 and 85, no-go
below 70 - and write what "conditional" means, because it is where deals go to die slowly.

## Scope discipline

- **Three criteria decide a deal.** Ten is a project with a steering committee.
- **No custom development inside a POC.** Configure, integrate and demonstrate; if the
  answer needs a build, the answer is "not yet" and the POC is the wrong instrument.
- **The buyer's data, the buyer's access, the buyer's owner.** A POC run entirely on our
  sample data proves nothing about their environment.
- **A change to scope is a new decision** with a new date and, usually, a price.

## Running it

- **Week 1** - access, data, environment, and the criteria restated in writing.
- **Weekly** - a 20-minute check: what was proven, what is blocked, what the buyer's owner
  needs to unblock, and the days remaining.
- **Evidence** - every criterion gets an artefact: a screenshot, a log, a test result, a
  signed note from the buyer's owner.
- **The decision meeting is on the calendar from day one**, with the buyer's decision
  maker invited.

## The cost to us

Compute it and put it in the plan. `scripts/poc_plan.py` does the arithmetic: engineer
days x blended rate plus infrastructure. Then compare it to the gross profit of one won
deal. A POC that costs a tenth of the gross profit of a deal is a marketing expense; one
that costs half is a build project and should be approved as one.

## Anti-patterns

- **The open-ended POC** with no end date, which is an unpaid implementation.
- **Success criteria written after the POC** by the seller.
- **The POC that quietly becomes the deployment**, with no contract and no price.
- **The buyer's IT team not involved**, so the POC passes and procurement fails.
- **Extending the timebox to be helpful**, which teaches the buyer that the deadline is
  not real.
