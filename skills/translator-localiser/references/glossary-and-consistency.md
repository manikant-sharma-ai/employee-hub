# Glossary and consistency

Inconsistency is the most visible sign of a translated product. One word per
concept, decided once, written down, obeyed.

## The glossary row

| Term (English) | Approved | Rejected | Script | Why |
|---|---|---|---|---|
| subscription | सदस्यता | सब्सक्रिप्शन, अंशदान | Devanagari | Reviewers accepted the native word in the app; `सब्सक्रिप्शन` kept for SMS where characters are costly |
| OTP | OTP | वन टाइम पासवर्ड | Roman | Everyone says OTP; the expansion is unreadable at button size |
| cart | कार्ट | झोला, टोकरी | Devanagari | `टोकरी` reads as a physical basket; `कार्ट` is understood |
| plan | प्लान | योजना | Devanagari | `योजना` reads as a government scheme in this category |
| refund | रिफंड | वापसी | Devanagari | `वापसी` is ambiguous with a return of goods |

Rules for the table:

- **One approved word per concept per language.** If two surfaces need different words, that is a second row with the surface named.
- **Record the rejected alternative**, always. It is what stops the third round of the same debate.
- **Name the script decision.** Roman-script terms inside Devanagari text are a real convention; they are not a mistake, and they must be consistent.
- **Date and owner per row.** A glossary without an owner drifts back within two releases.

## Where the glossary lives

One source of truth: a sheet, a repo file, or the translation memory - not the
designer's memory. If the team uses a CAT tool or a platform with a term base,
the glossary lives there and the sheet is a mirror. Say which is authoritative.

## Applying it mechanically

- **Run a term check** before review: every glossary term found in the source must appear as its approved translation. A script beats an eye.
- **Check the reverse**: any rejected alternative appearing in the output is a fail, even if it reads well.
- **Check the UI strings separately** from marketing copy - they have different length limits and often different register.

## Term decisions that recur

| Problem | The way through |
|---|---|
| No equivalent exists | Keep the English term in Roman script, or coin a word and test it with five native readers before shipping |
| Two words are equally common | Pick by region and audience, record both, and choose the one the support team already uses |
| The legal team needs one word, marketing another | Two rows, surface named, and the legal row wins on any screen that can be filed |
| A word carries a religious or caste connotation | Avoid it entirely; find a neutral phrase |
| A brand term must stay English | Record it as a "do not translate" entry, and apply it everywhere including subtitles |

## Consistency across a project

- **Translate in batches by surface**, not by file, so the register holds.
- **Review in one sitting per language**, so the reviewer holds the register in mind.
- **Keep a changelog of glossary changes**; a change must trigger a re-check of shipped strings, or the app splits in two.

## Anti-patterns

- A glossary that only the translator can see.
- Different words for the same button on two screens.
- Changing a term without re-checking what shipped.
- Forcing a native word the customer does not use, to look pure.
- Translating a brand name because it appears in the source.
