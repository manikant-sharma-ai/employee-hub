# Reason codes: building a taxonomy that tells the truth

The picklist in the cancellation form is written by the person who built the form, not by the people who left.
This file replaces it with codes derived from the exits themselves.

## Why the form fails

| Failure | What it looks like | What it costs |
|---|---|---|
| "Other" is available and easy | 25-40% of exits coded "Other" | The largest real reason is invisible |
| Codes describe feelings | "Not satisfied", "Unhappy" | Nothing actionable; every fix looks equally valid |
| Codes mix reason and stage | "Too expensive" covers price, value-for-money and cash flow | Three different fixes collapse into one |
| Closing agent codes to avoid blame | Support codes "customer moved"; sales codes "budget" | The product problem never surfaces |
| One code per exit | The real exit had two causes | The primary cause is whichever was listed first |
| No version history | Codes change monthly | The trend measures the coding, not the customers |

## The taxonomy

Nine primary codes, each with a test that decides membership. A customer gets exactly one primary and up to two
secondary codes. If a code cannot be assigned from evidence, it is not assigned.

| Code | The test | Typical sub-reasons |
|---|---|---|
| `price-value` | They said the price is too high *for what they got* | Cheaper competitor, budget cut, usage too low for the price |
| `cash-flow` | They could not pay, not that they would not | Business closed, funding ended, seasonal cash crunch |
| `missing-feature` | A specific capability they needed did not exist | Integration, report, language, compliance document |
| `product-quality` | The thing did not work as promised | Errors, downtime, accuracy, speed |
| `onboarding-failure` | They never got to first value | Setup abandoned, no training, wrong expectation set |
| `switched-competitor` | They moved to a named alternative | Bundled elsewhere, better fit, acquired by their vendor |
| `business-change` | Their business changed, not their opinion of you | Closed, pivoted, acquired, moved country |
| `relationship` | The human side failed | Unanswered tickets, a bad escalation, an account owner who left |
| `no-longer-needed` | The need ended | One-off project finished, in-house team built |
| `unknown` | No evidence exists | Silence, no reply, form abandoned - and it stays visible |

`unknown` is not `other`. It is a measured gap, it appears in every report, and it is never redistributed across
the other codes.

## Coding free text, in four passes

1. **Read the raw sentence, not the code.** "We're not getting enough out of it" is `price-value`; "we're
   shutting the unit" is `business-change`. They are the same words to a picklist.
2. **Check the ninety days before the exit** for a contradicting signal - a burst of tickets is `product-quality`
   even when the form says price. The form records the last conversation; the tickets record the cause.
3. **Assign secondary codes** where a real second cause exists. Track which pairs repeat: `onboarding-failure` +
   `price-value` is a very different business problem from `product-quality` alone.
4. **Log the evidence** - one line per exit, in the workbook, not in the report: what they said, where it was
   said, and the code. The report shows counts; the workbook keeps the audit trail.

## When "unknown" is over 20%

Do not guess. Run one of these, in this order:

| Tactic | Cost | What it gets |
|---|---|---|
| A three-question exit email, sent within 48 hours of cancellation | Near zero | The reason, from the 10-20% who answer |
| A call from the account owner to the ten largest exits | An hour each | The real reason, and a referral sometimes |
| Read the last three support threads of every exit | Two hours a month | The cause, even when the customer never said it |
| Check the payment failure log | Minutes | Distinguishes `cash-flow` from `price-value` |

An exit survey answered by 15% of leavers is a biased sample and must be reported as one: "reasons from 12 of 74
exits" is honest, "12 customers said price" is not.

## Stability rules

- **Codes are added, never renamed or merged mid-year.** A merge invalidates the trend line.
- **Every taxonomy change is dated** in `notes/decisions.md` with the reason, and the report shows the break.
- **The taxonomy is reviewed every six months** against the free text of the last hundred exits, not against
  what the team finds convenient.
- **The closing agent's picklist is an input, not the record.** Where the picklist and the evidence disagree, the
  evidence wins and the disagreement is counted - a high disagreement rate is itself a finding about the team.

## Anti-patterns

- A single "reason" column with free text and no coding: unusable at more than thirty exits a month.
- Ten codes where four carry 80%: report the top four and lump the tail, do not build a taxonomy for the tail.
- Asking "why did you cancel?" in a modal with a mandatory field: produces the fastest click, not the truth.
- Coding churn causes from a support tag alone: a customer who never wrote in is not a happy customer.
- Reporting reason shares without revenue: 40% of exits by count can be 12% of revenue lost.
