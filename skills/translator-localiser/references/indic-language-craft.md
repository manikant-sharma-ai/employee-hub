# Indic language craft

Eleven languages, three script families, and one shared trap: translating words
instead of meaning. These are the decisions that come up on every project.

## The five decisions before any translation

1. **Script or Roman?** Devanagari for Hindi and Marathi, Tamil, Telugu, Bengali, Gujarati, Kannada, Malayalam, Gurmukhi for Punjabi, Odia, Urdu in Nastaliq. Roman transliteration is common in ads and SMS but reads as informal, and it is hard to read for older audiences.
2. **Tatsama or the everyday word?** `उपयोगकर्ता` (user) is correct and cold; `आप` or a rewritten sentence is warm. Prefer what people say. Government forms are the exception, not the model.
3. **Loan words or native coinage?** `मोबाइल`, `इंटरनेट`, `ऑफर` are the words people use. A purist coinage reads as a textbook. Keep English technical terms in Roman script where the reader says them that way.
4. **Sentence length.** English packs clauses; Indic languages put the condition first and the verb last. Split long sentences. A 25-word English sentence often becomes two sentences, and that is correct.
5. **Honorifics.** Hindi and Marathi have three levels (`तू`/`तुम`/`आप`), Tamil and Bengali have their own. Pick one per surface and hold it.

## Language-by-language notes

| Language | Watch for |
|---|---|
| Hindi | Register varies sharply by region; Delhi marketing Hindi is not Bhojpuri-influenced Hindi. Keep `आप` for commerce. |
| Marathi | Distinct from Hindi in vocabulary; do not pass Hindi off as Marathi. Loan words differ (`मोबाईल`). |
| Gujarati | Business register is common; transliterated English terms are widely accepted. |
| Bengali | Formal/literary register is normal in writing; colloquial in ads. `আপনি` default. |
| Tamil | Strong resistance to Hindi loan words; English loans are common and accepted. Avoid Sanskritised coinages. |
| Telugu | Two registers, `గ్రాంథికం` (literary) and `వ్యావహారికం` (spoken); use the spoken for product copy. |
| Kannada | Similar split; use the spoken register for UI, formal for legal. |
| Malayalam | Long compounds; break them up for UI. |
| Punjabi | Gurmukhi for Punjab; Shahmukhi in Pakistan. Keep it Gurmukhi. |
| Odia | Fewer translators available; review cost is higher, plan for it. |
| Urdu | Nastaliq script, right-to-left layout, and a register that leans Persian-Arabic. Needs RTL design support, not just translation. |

## The three traps

- **False friends and calques.** "Kindly do the needful" style English becomes a calque that native readers find odd. Translate the request, not the phrasing.
- **Idioms.** "Get your act together", "ballpark figure", "low-hanging fruit" have no equivalent. Replace with the meaning.
- **Puns and rhymes.** Untranslatable. Say so, and propose a rewrite in the source.

## Quality check, before a reviewer sees it

1. Read it aloud - if you stumble, the reader will.
2. Check every number, date and unit against the source.
3. Check the register is uniform across the batch.
4. Check glossary terms against the approved list, mechanically.
5. Check the longest string against the surface's limit.
6. Back-translate money, legal, medical and safety lines.

## Anti-patterns

- One Hindi for all of India.
- Translating brand names and acronyms.
- Machine translation with no native review, shipped as final.
- Mixing scripts mid-sentence (`आपका order ship हो गया` is a real convention in SMS; it is wrong in a formal legal notice).
- Refusing a loan word the customer uses, to look pure.
