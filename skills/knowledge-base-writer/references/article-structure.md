# Article structure

An article is read by a person who is already stuck, usually on a phone, usually
annoyed. The structure exists to get them unstuck before they lose patience.

## The anatomy

| Part | Job | Length |
|---|---|---|
| Title | The search phrase, in the customer's words | Under 60 characters |
| The answer | What to do, in one or two sentences | 2 lines |
| Conditions | When this applies, and when it does not | 1-2 lines |
| Steps | Numbered, one action each, with what they should see | 3-10 steps |
| Edge cases | The two variants that break the steps | 3-5 lines |
| If it still fails | The next action, and who to contact | 2-3 lines |
| Related | Two links, maximum | 1 line |

Nothing else. No history, no "we are excited to announce", no explanation of why
the feature works this way unless the why changes what the reader does.

## Titles

| Bad | Why | Better |
|---|---|---|
| "Payment gateway error handling" | Feature language | "Money debited but order not confirmed" |
| "Refund policy" | Names a document | "When will my refund arrive?" |
| "How to use the dashboard" | Too broad | "Change your delivery address after ordering" |
| "Troubleshooting login issues" | A category, not a question | "OTP not arriving on your phone" |

Rules: under 60 characters, contain the words a customer would type, no internal
jargon, no product codenames, and one question per title.

## The answer block

The first two lines must contain: **the action**, **the time it takes**, and **the
condition** if there is one.

> Refunds are processed within 7 working days of the return being picked up. You do
> not need to do anything else - the money goes back to the original payment method.

Not this:

> Thank you for reaching out about refunds. We understand that waiting for a refund
> can be frustrating. Our team works hard to process refunds as quickly as possible.

The second version says nothing, and the reader has now scrolled past the only
useful sentence.

## Steps

- **One action per step.** "Click Settings, then go to Billing, then update your
  card" is three steps.
- **Name what they see after each action.** "You will see a green confirmation bar."
- **No screenshots of everything.** One screenshot per step that is genuinely hard to find.
- **Numbers, not bullets,** when order matters. Bullets when it does not.
- **Test the steps on the real product**, in the state a new customer would be in.

## Writing for a stuck person

| Do | Do not |
|---|---|
| "You will need your order number" | "Simply locate your order number" |
| "If this does not work, reply to this email" | "Contact support for further assistance" |
| "This takes about 2 minutes" | "The process is quick and easy" |
| "Your card will not be charged twice" | "Rest assured, your card will not be charged" |
| "We cannot change the address after dispatch" | "Unfortunately, address changes are not possible at this time" |

Short sentences. Active voice. Second person. No hedging verbs - "may", "might",
"should" - unless the behaviour is genuinely conditional, and then say the condition.

## Screenshots and video

- **Dated.** "As of November 2026" under the image, or in the alt text.
- **Cropped to the relevant area**, with the button circled once, not five times.
- **No personal data.** No names, emails, order numbers or phone numbers visible.
- **A 30-second clip beats six screenshots** for anything involving a sequence.
- **Alt text describes the action**, not the image: "The Address button in the order summary".

## Article types and their shape

| Type | Shape | Example |
|---|---|---|
| How-to | Answer, steps, edge cases | "Change your delivery address" |
| Troubleshooting | Symptom, cause, fix, if it fails | "OTP not arriving" |
| Policy | The rule, the timeline, the exception | "When will my refund arrive" |
| Reference | A table, and how to read it | "Delivery timelines by pin code" |
| Getting started | The first 10 minutes, in order | "Set up your first invoice" |

Do not mix types in one page. A policy page with a how-to in the middle is not
findable as either.

## Anti-patterns

- **A wall of text with no steps.** The reader is looking for the one action.
- **Screenshots of the old UI.** Worse than no screenshot, because it is trusted.
- **"Contact support" as the answer.** That is the thing the article exists to avoid.
- **Numbered lists of 20 steps.** Break it into two articles.
- **Internal jargon** - "the reconciliation job", "the webhook retry".
- **A title written by the person who built the feature.**
