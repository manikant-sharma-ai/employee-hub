# Test plan and scope

A test plan is a promise about what will and will not be covered. Without the
second half, it is a wish list.

## The one-page plan

| Field | Content |
|---|---|
| Change | What is different in this release, in one line |
| Intent | What the user can now do that they could not before |
| In scope | The flows and screens being tested |
| Out of scope | What is deliberately not tested, and who accepted that |
| Environments | Build, URL, device, browser, OS, locale, account role |
| Data | Test account, test card, seeded records |
| Time-box | How long, and what gets cut when it runs out |
| Owner | Who signs the release call |

## Risk-first ordering

Test in the order a failure would hurt, not the order the screens appear:

1. **Money** - payment, refund, invoice, price, tax.
2. **Data** - save, delete, edit, export, permissions.
3. **Access** - login, OTP, password reset, role changes.
4. **Core journey** - the one path 80% of users take.
5. **Edge journeys** - the second and third most common.
6. **Cosmetics** - alignment, copy, icons. Last, always.

When the time-box runs out, the cut is always from the bottom.

## What "acceptance criteria" looks like

Bad: "Checkout works."
Good:
- A first-time buyer can pay with UPI and sees a confirmation with the order ID.
- A failed payment shows the failure, states that no money was deducted, and keeps the cart.
- The order appears in the admin panel within 30 seconds.
- The confirmation email arrives once, not twice.

Each line is testable, and each line can fail on its own.

## Test types worth naming, and their limits

- **Smoke**: five minutes, does it open and can you log in. Before every deploy.
- **Functional**: the acceptance criteria. The bulk of the work.
- **Regression**: the ten flows that must never break. A fixed list, run every release.
- **Exploratory**: 30 minutes of deliberate curiosity after the scripted tests. Finds what the script does not ask.
- **Cross-device**: two real devices minimum - one small Android, one iPhone.
- **Localisation**: the second language, the long string, the Indian number format.

Out of scope for this role, and to say so plainly: load, stress, penetration,
and accessibility certification. They need their own tools and their own owners.

## Anti-patterns

- A plan with no out-of-scope section.
- Testing every screen equally.
- A regression list of 200 cases nobody runs.
- Testing only the happy path because the build was late.
- Signing off because "it worked on my machine".
