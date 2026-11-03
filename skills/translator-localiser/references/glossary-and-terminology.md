# Glossary and terminology

The glossary is the only defence against three freelancers producing three products. It is also the cheapest quality intervention available: build it once, use it forever.

## The glossary entry

```
Term (EN):        subscription
Do not translate: no
Rendering:        hi: सदस्यता | mr: सदस्यत्व | ta: சந்தா | te: సబ్‌స్క్రిప్షన్
Notes:            "सदस्यता" for the plan; keep "subscribe" as "सब्सक्राइब करें" on buttons
Approved by:      <name>, <date>
```

Six fields. Anything less and the entry will be contradicted by the next person.

## What goes in the glossary

| Category | Example | Rule |
|---|---|---|
| Product and brand names | "Cold Press" | Never translated; transliterate only if the brand says so |
| Feature names | "Smart Basket" | Translated only if it is a generic feature, not a brand |
| Recurring nouns | invoice, order, delivery, refund, plan | One rendering, everywhere |
| Verbs in UI | save, cancel, continue, retry | Short, imperative, consistent |
| Statutory terms | GST, TDS, e-way bill, invoice | Official rendering, never invented |
| Units and measures | kg, litre, 500ml | Keep the unit; localise the number format |
| Honorifics | ji, sir, madam | Decide per language, keep consistent |
| Do-not-translate | API, UPI, OTP, KYC, PDF | Acronyms stay |

## Building one in an hour

1. **Export every string** from the product, or take the ten most-read pages.
2. **Extract the recurring nouns** - the words that appear more than three times. Usually 40-80 terms.
3. **Group them** by category above.
4. **Decide each one**: translate, transliterate, or keep. Write the reason for the ones that were argued about.
5. **Get a native speaker to confirm** the renderings in one sitting, in the target language, with the term in a real sentence - not in a list. A term that looks right in a list often fails in a sentence.
6. **Store it where the translators actually work** - a sheet, the CAT tool, or the platform's terminology feature. A glossary in a PDF is a glossary nobody uses.

## Transliteration, not translation

| English | Transliterate | Translate | Why |
|---|---|---|---|
| WhatsApp | व्हाट्सएप | - | A brand |
| UPI | यूपीआई | - | An acronym with an official form |
| OTP | ओटीपी | - | Understood as-is |
| EMI | ईएमआई | - | Understood as-is |
| GST | जीएसटी | - | Official form |
| "Dashboard" | डैशबोर्ड | "नियंत्रण पटल" (avoid) | Nobody says the second |
| "Cloud" | क्लाउड | "बादल" (wrong sense) | The metaphor does not carry |

Rule: **if the audience already says the English word, transliterate it.** Translating a word the audience does not use in that sense is how products end up sounding foreign in their own language.

## Consistency checks that catch drift

- The same English term appears with two different renderings in the target file.
- A term is translated in a heading and transliterated in the body.
- A button says one word and the confirmation message says another for the same action.
- The glossary says one thing and the shipped strings say another - the glossary loses, every time, unless someone checks.

`scripts/glossary_check.py` runs the first and third of these mechanically.

## Anti-patterns

- A glossary with 400 entries nobody can hold in their head - keep the core 60 to 100.
- Entries with no approval, so the next reviewer reverses them.
- Translating acronyms (एपीआई, यूआरएल) that everyone reads in English.
- Different renderings for the same term on the home page and in the app.
- Building the glossary after the translation, as documentation.
- A glossary that lives in one freelancer's head.
