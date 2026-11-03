# States and edge cases

The hero screen is 20% of the work. The other 80% is what happens when the data
is missing, slow, wrong, too long, or not allowed.

## The eight states every data-bearing screen needs

| State | What the person sees | What the action is |
|---|---|---|
| Loading | Skeleton of the real layout, not a spinner in the middle | None - the screen is already shaped |
| Empty (first use) | What this screen is for, and the one action that fills it | The primary action |
| Empty (filtered) | "No results for <term>" plus how to widen the search | Clear filters |
| Partial | What loaded, what did not, and a retry on the part that failed | Retry that piece |
| Error (recoverable) | What went wrong in plain words, what to do | Retry, or the alternate route |
| Error (terminal) | What happened, what is preserved, who to contact | Contact, or back to safety |
| No permission | Why it is locked and who can unlock it | Request access |
| Success | What happened, and what happens next | The next step, not "OK" |

Plus, for every list and form: **too many items** (pagination or infinite scroll
with a real end state) and **too long text** (two lines with ellipsis, or wrap -
decide per element).

## Copy rules for states

- **Name the thing, not the system.** "We could not load your orders" beats "Error 500".
- **Say what is preserved.** "Your cart is saved" is the sentence that stops the second attempt.
- **Give one next action.** Two options in an error state is a decision the person cannot make.
- **Never blame the person.** "That code did not match" not "You entered an invalid code".
- **No error codes alone.** The code can sit underneath, small, for support.

## Form edge cases

- **Validation on blur, not on every keystroke.** Red while typing is punishment.
- **Show the rule before the failure.** "Password: 8 characters, one number" above the field.
- **Keep the value on error.** Never clear a form because one field failed.
- **OTP**: resend after a visible countdown, and a change-number route.
- **Payment failure**: say whether money was deducted, and what to do if it was. This is the single highest-anxiety screen in Indian commerce.
- **Address**: pin code first, then city and state prefilled; allow a landmark field.
- **Amounts**: Indian digit grouping (₹1,00,000), never ₹100,000 in customer-facing copy.

## Text and language

- **Test with the longest realistic string** - a 40-character product name, a 60-word address, a name with no spaces.
- **Test with Hindi, Tamil or Bengali** if the product supports them: strings grow 20-35%, and line height needs more room. See `translator-localiser` for the wording; your job is the layout surviving it.
- **Numbers and dates** follow the locale, not the design file.

## Accessibility minimums

- Contrast 4.5:1 body, 3:1 large text and icons.
- Every input has a visible label, not only a placeholder.
- Focus order follows the visual order; focus ring always visible.
- Icon-only buttons carry an accessible name.
- Errors are announced, not only coloured red.

## Anti-patterns

- An empty state that says "No data".
- A spinner where a skeleton would keep the layout stable.
- An error that says "Something went wrong" with no next step.
- A disabled button with no explanation of why it is disabled.
- A confirmation dialog on every action, so people stop reading them.
