# Test plan and risk

A test plan is a ranked argument about what could go wrong, not a list of everything that exists. If it does not tell the reader what will *not* be tested, it is not a plan.

## Risk, as arithmetic

Score every surface on two axes and multiply. The number is only a sorting device - the argument is in the inputs.

| Surface | Likelihood (1-5) | Cost (1-5) | Score | Depth |
|---|---|---|---|---|
| Checkout, payment capture | 3 | 5 | 15 | Full - every path, every failure mode |
| Order confirmation email | 2 | 3 | 6 | Happy path plus a failure |
| Login and session | 2 | 5 | 10 | Full, including expiry |
| Profile picture upload | 4 | 1 | 4 | Smoke |
| Admin CSV export | 1 | 4 | 4 | Smoke, and one bad file |

**Likelihood** rises with: new code, changed code paths, third-party dependencies, anything with a race, anything with money or time.
**Cost** is what the business pays when it fails in production: a refund, a support queue, a statutory filing, a customer who does not come back.

## The test plan, in seven lines

```
Change:      what shipped, in one line
Blast radius: what else touches it
Critical:    the three to five paths that must work
Risky:       the two or three that probably do not
Not tested:  what is out of scope, and why
Data:        the accounts, fixtures and environments
Exit:        the condition that means "ship" - written as a number
```

## Depth, chosen deliberately

| Depth | What it means | Use for |
|---|---|---|
| Full | Every branch, every failure mode, every boundary | Money, auth, data loss |
| Standard | Happy path, two failures, boundaries | Most features |
| Smoke | It loads, it does not error, it does the one thing | Low-risk surfaces, every deploy |
| Eyes only | Read the diff, reason about the risk | Config, copy, and anything with no runtime path |

## The four things to test first

1. **Money.** Anything that charges, refunds, discounts, invoices or reconciles.
2. **Data loss and duplication.** Delete, overwrite, double-submit, retry, two tabs open.
3. **Access.** Login, session expiry, permission boundaries, and the URL a user is not supposed to reach.
4. **Anything that leaves the building** - an email, an SMS, a WhatsApp message, a webhook, a printed label.

Everything else is a queue that can be worked in order.

## Writing a case someone can run

```
ID:        TC-CHK-07
Given:     a cart with one item at ₹499 and a valid coupon of ₹100
When:      the user applies the coupon and pays by UPI
Then:      ₹399 is charged once, the order shows the discount, and the confirmation
           email shows ₹399 with the coupon named
Data:      test buyer account, UPI test handle, coupon TEST100
```

A case without data is a wish. A case with "verify it works" as the Then is not a case.

## Exit condition

Written before testing starts, agreed with whoever ships:

- All Critical cases pass.
- No open defects of severity 1 or 2.
- Severity 3 defects listed, with an owner and a date.
- Regression suite green.
- The untested list is signed off by name.

## Anti-patterns

- A 300-row checklist that was run once and never updated.
- Testing the feature and not the blast radius.
- "Regression testing" that means "click around for an hour".
- Equal depth everywhere, so the payment path gets the same attention as the footer.
- A plan written after the testing, as documentation.
- Exit conditions that change once the deadline arrives.
