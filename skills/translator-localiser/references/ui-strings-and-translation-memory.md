# UI strings and translation memory

App and product copy is not prose. It is a few thousand fragments with length
limits, variables, plurals and a build pipeline, and it breaks in ways prose does not.

## The anatomy of a string

```
key: checkout.pay_button
en: Pay {amount}
hi: {amount} भुगतान करें
context: primary button, bottom of checkout, max 24 chars
```

- **Never translate the key.** The key is the contract with the code.
- **Never translate inside `{variables}`.** Word order changes; the variable does not.
- **Ask for context per key** - a screenshot, a note, or the neighbouring strings. "Post" is a noun in one screen and a verb in another.
- **Respect the character limit**, and rewrite rather than overflow.

## Plurals and gender

- **Hindi, Marathi, Gujarati, Punjabi, Odia** use one/other plural forms; **Bengali, Tamil, Telugu, Kannada, Malayalam** commonly use the same form with a numeral. Do not import the English two-form rule blindly.
- **Verbs agree with gender in Hindi and Marathi.** "आपने भेजा" vs "आपने भेजी" depends on the object. A string that works for "order" fails for "invoice".
- **Avoid constructions that force a gender** where the product does not know it. Rewrite to a neutral form.
- **Urdu and Bengali** have their own agreement patterns; check with the reviewer rather than assuming.

## Length, measured

- **Strings grow 20-35%** from English into Indic scripts, and buttons break first.
- **Give the developer the longest string per key** so the layout is tested against the real worst case.
- **Truncation is a translation decision too**: if the platform cuts at 40 characters, the translation must carry the meaning in the first 40.
- **Report every key that exceeds its limit**, with the screen and the limit, in one table.

## Translation memory and consistency

- **A TM is only as good as its segmentation.** Sentence-level, keyed to the string key where possible.
- **Never let a 100% TM match through unreviewed** when the source changed by one word - the meaning may have inverted.
- **Fuzzy matches are a draft**, not a decision.
- **Keep the TM in the repo or the platform**, not in a translator's personal file, or the next translator starts from zero.
- **Version the glossary with the strings**; a glossary change without a string re-check splits the product.

## The delivery format

A sheet or a locale file with: key, source, translation, limit, status, reviewer,
date. Status values only: draft, reviewed, approved, needs-decision. No "done-ish".

## Anti-patterns

- Translating in a spreadsheet with no keys, then a developer re-typing it.
- A string that concatenates two fragments, which cannot be translated correctly in any language.
- Hardcoded punctuation in the code, so the localised sentence ends with a full stop after a danda.
- One reviewer approving 2,000 strings in an afternoon.
- Machine translation merged to production with no review status.
