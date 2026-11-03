# Flow and screens

A flow is a decision tree, not a set of pictures. Get the tree right and the
screens become obvious; get the screens pretty and the tree wrong and the product
still fails.

## Write the flow as text first

```
Entry (from where?)
  -> Screen 1: <what the person sees>
     exit A: continue  -> Screen 2
     exit B: back      -> Entry
     exit C: error     -> Screen 1 with error state
     exit D: abandon   -> (what is saved? what is lost?)
```

Four things to label on every screen:

1. **Where the person came from.** A screen that can be reached from five places has five different mental states.
2. **What is already known.** Prefill what the business already has; every field you ask for twice is a drop-off.
3. **What the person must decide.** One decision per screen; two decisions means two screens.
4. **Where they land after each exit**, including back and cancel.

## Flow rules

- **Three taps to the value, or a progress indicator.** If the job genuinely needs six steps, show the steps.
- **Never lose work on back.** Persist the draft, or warn before discarding.
- **Confirm destructive actions, never confirm safe ones.** A "are you sure you want to continue" on the happy path trains people to tap through.
- **One primary action per screen.** Secondary actions are text links or ghost buttons, not equal-weight buttons.
- **Show the cost before the commitment.** Price, fees, delivery date and what happens next, before the pay button.
- **Success is a screen.** Not a toast that disappears; a screen that says what happened and what to do next.

## Mobile reality

- **360px wide is the target**, not 390. If it works at 360 it works everywhere.
- **Thumb zone**: primary actions in the lower third, destructive ones out of it.
- **One-hand use**: nothing critical in the top-right corner.
- **Slow connection**: the screen must say something before the data arrives (see the loading state rules).
- **Keyboard open**: the CTA must stay visible or the form must scroll to the focused field.

## When the flow is the problem

Red flags: more than two data-entry screens before value, a step that exists only
for the business, an OTP with no resend, a login before the person has any reason
to log in. Say the flow is the problem and propose the shorter one - that advice
is worth more than any screen you draw.

## Anti-patterns

- Screens designed one at a time, never as a flow.
- A flow that only exists in the designer's head and the prototype.
- "Back" that goes to the wrong place, or exits the app.
- A modal on top of a modal on top of a form.
- Onboarding screens that explain the product instead of letting it be used.
