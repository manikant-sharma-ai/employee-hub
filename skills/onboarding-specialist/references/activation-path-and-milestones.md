# Activation path and milestones

The activation path is the shortest honest route from "signed" to "getting value". It is three to five steps,
never twelve, and every step has one owner per side and one date.

## Finding the steps

Work backwards from the activation event. Ask what must be true one step before it, and again, until you reach
the signature. That list is the path. Anything that is not on it is either training or nice-to-have, and both
belong in the sequence, not on the critical path.

A typical path for a product that replaces a manual process:

1. **Access granted** - accounts created, roles set. Ours, same day.
2. **Data in** - the customer's export, cleaned and loaded. Mostly theirs; the usual slip.
3. **First run** - one real transaction or cycle done end to end, with us watching. Both sides, one call.
4. **The habit** - the customer does it unaided for a week, and the old method is switched off. Theirs.
5. **Confirmed live** - the witness named at kickoff confirms the criterion. Theirs, on the day-thirty call.

## Rules that keep a plan honest

- **One owner, one date, per step.** Two owners is no owner. "Week of" is not a date; pick the day.
- **Mark the critical path.** Any step that can move the go-live date is on it. Steps off the path can slip
  without a conversation.
- **Put the customer's dependencies first.** Data, access and approval are the three that slip, in that order,
  and all three belong to them. Ask for each on the day it is needed, in writing, with the consequence stated.
- **A step is done when the evidence exists**, not when the meeting ended. The evidence is a screenshot, a record
  count, a confirmation - say which, in the plan.
- **Plan the switch-off.** The old spreadsheet, the old process, the parallel run: name the date it stops. An
  onboarding that leaves the old method alive has not onboarded anyone.

## When the path is longer than thirty days

Some products genuinely take ninety. Then the thirty-day target is not "live" but "the first milestone that
proves the direction", and it is named as such. Do not stretch a thirty-day promise over ninety days of work;
re-cut the promise and write the new date down.

## Sequencing the customer's people

- **The champion does the work.** Give them one page per step, not a manual.
- **The decision maker unblocks.** They get one message per milestone that is at risk, from the account owner,
  not from you.
- **The technical contact gets specifics.** Endpoint, file format, field mapping, timing. Vague asks get
  deprioritised.
- **Finance gets the invoice question once**, answered by `billing-support`, not by this role.

## Measuring the path

`scripts/activation_report.py` computes, per account, the days from signed to first value, which milestone is
overdue, and the activation rate by day seven, fourteen and thirty. Run it weekly. A path that is right for one
segment and wrong for another shows up as a cohort of accounts stuck on the same step - which is a finding about
the product or the sales promise, not about the customer.
