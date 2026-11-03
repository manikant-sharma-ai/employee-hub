# Bug report craft

A report exists to make someone else fix the thing without asking you a question.
If they have to ask, the report is unfinished.

## The seven fields

1. **Title** - what is broken, where, and under what condition. "Payment succeeds but order stays 'pending' on UPI failure retry".
2. **Steps** - numbered, from a known starting state. Include the exact values used.
3. **Environment** - build/version, browser, OS, device, locale, account role, URL.
4. **Expected** - what the spec or the acceptance criterion says.
5. **Actual** - what happened, in the same terms.
6. **Evidence** - screenshot, screen recording, console log, API response, the order ID. Attach at the moment of failure.
7. **Severity and impact** - in business terms: "customer charged twice, ₹499 each, 1 in 20 attempts".

## Severity ladder

| Level | Meaning | Example | Ship with it? |
|---|---|---|---|
| Critical | Money, data loss, security, total block | Double charge; orders invisible to admin | No |
| High | A main flow fails for a real segment | OTP not delivered on one carrier | Only with a named workaround |
| Medium | A flow is painful but passable | Address form loses the pin code | Yes, with a date |
| Low | Cosmetic, copy, alignment | Button 2px off | Yes |

Severity is the consequence. Priority is the business's call - a cosmetic bug on
the homepage can be higher priority than a medium bug in an admin screen.

## Reproducibility

- **If it happened once, say so.** An intermittent bug is still a bug; mark it "intermittent, 1 in 10" and include what was different.
- **If you cannot reproduce it, give the trace**: time, user, order ID, request ID. Logs are evidence; "I saw it" is not.
- **Reduce the steps** to the minimum that still fails, then report that minimum.

## Writing the impact line

The impact line is what gets the bug fixed. Compare:

- "Cart total is wrong." (nobody prioritises this)
- "Cart total shows ₹499 instead of ₹1,499 when a coupon is applied - customer pays a third, 12 of 40 test attempts." (this gets fixed today)

## What not to put in a report

- Three unrelated problems in one ticket.
- A customer's name, phone, address or card details. Redact; keep the shape.
- Blame. "The developer broke it" adds nothing.
- A fix suggestion as a requirement. Suggest it separately, as a note.

## Anti-patterns

- "Does not work" with a screenshot of the whole screen.
- Steps that start with "log in" and skip which account.
- A severity of critical on a typo, which trains everyone to ignore critical.
- Closing a bug as "cannot reproduce" without the trace attached.
