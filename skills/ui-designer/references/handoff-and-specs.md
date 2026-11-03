# Handoff and specs

A handoff is finished when the developer has no questions. Every question that
comes back is a spec you did not write, and it costs a day.

## What a spec contains

1. **The flow** - screens in order, with every exit and where it lands.
2. **Per screen**: purpose, the states table, layout in numbers, the components used, the copy.
3. **The scale** - spacing steps, type ramp, colour tokens by role, radii, elevation.
4. **Breakpoints** - the widths that matter (360, 390, 768, 1024, 1280) and what changes at each. Not "responsive" - what changes.
5. **Behaviour** - what happens on tap, on long-press, on back, on empty, on error, on success, on a slow network.
6. **Content rules** - max characters per field, truncation, what is prefilled, what is required.
7. **The one thing that must not break** - the sentence that tells the developer where to spend care.
8. **Open questions** - at most three, each with a recommendation.

## Writing it so it gets read

- **Numbers, not adjectives.** "24px gap, 16px padding, 48px height" not "comfortable spacing".
- **Name components the way the codebase names them.** Ask for the component list; if there is none, propose names and say they are proposals.
- **Annotate the state, not the obvious.** Do not annotate a title as "title".
- **Keep the copy in one block** so it can be pasted, not retyped.
- **Show the long and empty case next to the happy one.** A single annotated happy path is how empty states get invented in code.

## Figma specifics, when Figma is connected

- **Components with variants for state**, not copies of a frame.
- **Auto layout on everything** that will be filled with real content.
- **Tokens as variables** where the system supports them, so dark mode is not a second file.
- **Dev mode for the handoff**: real spacing, real assets, real names.
- **A cover frame per flow** with the flow name, version, date and the open questions.

## Reviewing a build against the spec

Check in this order, and report the first failure, not all of them:

1. Does every state exist? (Most builds ship the happy path only.)
2. Do the numbers match the scale?
3. Does the copy match, word for word?
4. Does it survive the long string, the second language, 200% zoom?
5. Do the tap targets and contrast pass?
6. Does the flow behave as specced on back, cancel, and error?

## Anti-patterns

- A handoff that is a link to a file with no words.
- Redlines exported as an image nobody opens.
- Copy in the design file but not in the spec, so it gets retyped and changed.
- "Use your judgement" on a destructive action.
- A spec that grows to 40 pages for two screens. The developer reads the first two.
