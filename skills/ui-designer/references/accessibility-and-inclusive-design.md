# Accessibility and inclusive design

Accessibility is not a compliance checkbox at the end; it is a set of decisions
that make the screen work for a thumb, a screen reader and a 45-year-old on a
budget Android phone. In India that last user is the majority.

## The four things that break most products

| Failure | Who it locks out | The fix |
|---|---|---|
| Contrast under 4.5:1 | Everyone outdoors, older eyes, low-quality screens | Measure the pair, do not eyeball |
| Icon-only buttons | Screen readers, first-time users | Visible label, or an accessible name |
| Placeholder as the only label | Anyone who forgets what the field was | Persistent label above the field |
| Colour-only status | Colour-blind users, about 1 in 12 men | Add an icon or a word |

## The checklist that fits on one page

- Contrast: 4.5:1 body text, 3:1 large text and UI edges, 3:1 focus indicator.
- Tap targets: 44x44pt iOS, 48x48dp Android, 8dp between destructive and safe.
- Focus: visible ring, order matches the visual order, never `outline: none` with no replacement.
- Labels: every input has a programmatic label; errors are announced, not only coloured.
- Motion: respect reduced-motion; nothing flashes more than three times a second.
- Text: resizable to 200% without clipping; no text in images that carries meaning.
- Media: captions on video, alt text on informative images, empty alt on decorative ones.
- Forms: one question per field, errors next to the field, and the value preserved on failure.

## Screen readers, in practice

- Name, role, value. A custom control needs all three, or it is invisible to a screen reader.
- Headings in order (H1 then H2), so the page can be skimmed by heading.
- Announce dynamic changes with a live region - a price update that is only visual did not happen for a screen-reader user.
- Test with one real screen reader (TalkBack on Android, VoiceOver on iOS) for ten minutes. It finds what no checklist does.

## Inclusive design beyond disability

- **Literacy and language**: short sentences, one idea per line, and the language the customer actually reads. A form in English for a Hindi-first user is an access barrier.
- **Bandwidth**: a 3MB hero image is an accessibility failure on 3G.
- **Device age**: test on a three-year-old mid-range Android, not the newest flagship.
- **Context**: one-handed use on a moving bus is the real use case for half of Indian mobile commerce.

## What to write into the spec

A short block per screen: contrast pairs used, tap target sizes, focus order,
label text for icon buttons, error announcement text, and the reduced-motion
behaviour. That block is what makes accessibility buildable rather than aspirational.

## Anti-patterns

- An accessibility audit at launch, after the components are locked.
- `aria-label` pasted onto everything to silence a checker.
- Grey-on-grey "elegant" text at 2.8:1.
- A modal with no focus trap and no Escape.
- Testing only on a desktop browser with a mouse.
