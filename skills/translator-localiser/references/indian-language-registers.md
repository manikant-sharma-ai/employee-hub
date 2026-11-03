# Indian language registers

Language is the first decision; register is the one that decides whether the output is usable. This file is a working note, not a grammar - use it to choose a rung and to know what to check with a native reviewer.

## Choose the rung first

| Rung | Pronouns | Sounds like | Use for |
|---|---|---|---|
| Formal | आप / तुम्ही / நீங்கள் | Respectful, slightly distant | B2B, finance, health, government, older audiences |
| Neutral | आप / तुम्ही / நீங்கள் with warmer verbs | Respectful and human | Most D2C, services, education - the safe default |
| Informal | तू / तू / நீ | Peer-to-peer, warm or blunt | Youth brands, gaming, food, streetwear |
| Romanised | aap / tum / nee | Same as above, Latin script | Social, WhatsApp, app notifications for urban users |

Write the chosen rung into the file header of every job. The second translator's biggest failure is not vocabulary, it is a different pronoun.

## Script or romanised

| Situation | Script | Romanised |
|---|---|---|
| Website, app UI, invoices, legal | Yes | No |
| Email newsletters | Usually | For young urban lists |
| WhatsApp broadcasts | Either - ask | Common |
| Instagram captions | Either - match the brand | Common |
| Search and SEO | Yes - people search in script | Both, test |
| Print, packaging | Yes, and check the statutory language requirement | No |

Mixing script and romanisation inside one sentence is not a register, it is an error. Mixed *vocabulary* is normal: "order", "delivery", "offer", "tracking", "invoice" are how people speak.

## Per-language working notes

**Hindi (hi)** - the register split is the whole game. Formal written Hindi drifts towards Sanskritised vocabulary that no one speaks; a shop sign and a news bulletin are different languages. Prefer the everyday word: "पैसे" over "धन", "जानकारी" over "सूचना" in consumer copy. Devanagari numerals (१,२,३) read as bureaucratic; use 1,2,3.

**Marathi (mr)** - formal by default, and "तुम्ही" is the safe address in almost every commercial context. Hindi loanwords are heard as not-from-here; Marathi has its own everyday vocabulary for the same things. Avoid Hindi slang in Marathi copy entirely.

**Tamil (ta)** - purist Tamil for technical and product terms reads like a textbook and is often not understood by the audience it is meant to serve. Code-mixing with English nouns is standard in commerce ("order", "delivery", "offer" stay English). Register is more about verb endings than pronouns.

**Telugu (te)** - register varies sharply between Telangana and Andhra usage, and between urban and rural readers. Keep sentences short; long subordinate clauses are where translations fall apart. English nouns for anything technical.

**Bengali (bn)** - warmth in the opening is expected; a flat, efficient sentence reads as curt. "আপনি" for almost all commercial contexts. Watch the West Bengal / Bangladesh vocabulary split for anything read across the border.

**Gujarati (gu)** - trade register: price, terms, delivery up front, pleasantries after. Business audiences read fast and dislike ornament.

**Kannada (kn)** - formal address for services and government-adjacent content; Hindi loanwords that Marathi would accept are heard as imports. Bengaluru consumer audiences accept heavy English mixing; the rest of the state less so.

**Malayalam (ml)** - longest expansion of the major languages; UI strings need the most headroom. English nouns are normal, English syntax is not.

**Hinglish** - a real register, not laziness. Rules: one script (Latin), consistent transliteration, English for nouns and technical terms, Hindi for verbs and connectives. "Order kal tak pahunch jayega" is right; "Order tomorrow tak deliver hoga" is neither language.

## What to check with a native reviewer

- **Every pronoun** in the output, against the chosen rung.
- **Every idiom** that was transcreated - the reviewer is checking that it lands, not that it is grammatical.
- **Every statutory term.**
- **Anything a customer reads as a promise.**
- **Region-specific vocabulary** where the audience is outside the metro.

## Anti-patterns

- Sanskritised Hindi in a consumer app.
- Purist Tamil for "download", "upload", "settings".
- Hindi for Maharashtra because "everyone understands Hindi".
- Romanised Hindi in a formal invoice.
- One register on the home page and another in the checkout.
- Translating "you" without deciding which you.
