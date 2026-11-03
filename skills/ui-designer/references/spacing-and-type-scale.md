# Spacing and type scale

Consistency is not a style preference; it is what makes screen nine look like
screen one without anyone remembering the rules.

## Spacing

- **One base unit, usually 4px.** Every gap is a multiple: 4, 8, 12, 16, 24, 32, 48, 64.
- **Name the steps by role, not by number**, when you hand off: `space-xs` 4, `space-sm` 8, `space-md` 16, `space-lg` 24, `space-xl` 32, `space-2xl` 48.
- **Space inside a group is smaller than space between groups.** This one rule fixes most "it feels cramped" complaints.
- **Vertical rhythm over perfect alignment.** Content grows; the 8px grid survives, pixel-perfect centring does not.
- **Padding in components, margin between them.** Never both at once - that is how double gaps appear.

## Type

A five-step ramp is enough for almost every product screen:

| Role | Size (mobile) | Weight | Use |
|---|---|---|---|
| Display | 28-32 | 600-700 | One per screen, if any |
| Title | 20-22 | 600 | Screen and section titles |
| Body | 16 | 400 | Default text - never below 16 on mobile inputs |
| Label | 14 | 500 | Field labels, metadata |
| Caption | 12-13 | 400 | Timestamps, helper text - the floor |

Rules:

- **Line height**: 1.4-1.5 for body, 1.2-1.25 for titles. Never 1.0 on multi-line text.
- **Measure**: 45-75 characters per line on desktop. Longer needs a wider gutter or a narrower column.
- **Two weights minimum, three maximum.** Hierarchy from size and weight, not from six colours.
- **No font below 12px**, ever, on any screen a customer touches.
- **Numbers align.** Use tabular figures for prices and tables, or columns wobble.
- **One typeface unless the brand kit says two.** See `graphic-designer` for the brand side.

## Colour tokens

Define by role, not by hex, so dark mode and rebrand are one change:

`color-bg`, `color-surface`, `color-text`, `color-text-muted`, `color-border`,
`color-primary`, `color-primary-hover`, `color-danger`, `color-success`, `color-warning`.

Rules: never colour alone to carry meaning (pair with an icon or a word); never
pure black on pure white for long text (use a near-black); check every pair for
contrast rather than trusting the palette.

## Radius, elevation, borders

- **Two radii** - one for controls, one for cards. A third needs a reason.
- **Elevation is a hierarchy signal**, not decoration: 0 for flat content, 1 for cards, 2 for menus and modals. If everything floats, nothing does.
- **Borders or shadows, not both**, on the same element.

## Icons

- **One set, one weight.** Mixing filled and outline icons inside a screen reads as sloppy.
- **Sizes on the ramp**: 16 inline with label text, 20 in buttons, 24 in navigation.
- **Every icon has a label or an accessible name.** An icon nobody recognises is a support ticket.

## Anti-patterns

- A new spacing value invented for one screen.
- Type sizes that are not on the ramp (17px, 19px, 21px).
- Four font weights used decoratively.
- Colour as the only signal for an error.
- Placeholder text as the only label.
