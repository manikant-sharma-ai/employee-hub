# Voice and tone

Voice is the person. Tone is the room. Voice does not change between a blog post and a support reply; tone does. Most "write in our voice" failures are an AI using its own default voice because nobody extracted theirs.

## Extracting a voice in one pass

Do this before writing a single sentence of their content.

1. **Get real samples, spoken and written.** Two emails they wrote, one post they liked, and ideally five minutes of them talking. Speech is where the real voice is - written samples are usually already filtered by a fear of looking unprofessional.
2. **Fill this table from the samples.** Every row must be answered with evidence, not a guess.

| Dimension | Read for | Example answer |
|---|---|---|
| Person | "I" / "we" / "you" / impersonal | "I, always - it is a one-person brand" |
| Sentence length | average words per sentence | "11-14 words, with one long one per paragraph" |
| Contractions | "we're" or "we are" | "Contractions throughout, except in pricing" |
| Formality | slang, slang-adjacent, neutral | "Neutral, with one Hindi word when it lands better" |
| Technicality | jargon tolerated, jargon explained | "Jargon fine for engineers, explained for buyers" |
| Humour | dry, warm, none | "Dry, self-deprecating, never at a customer's expense" |
| Directness | hedged or blunt | "Blunt. Says 'this is wrong' rather than 'this could be improved'" |
| Openings | how they start | "Starts with the problem, never with context" |
| Closings | how they end | "Ends on a question, never on a summary" |
| Banned words | what they would never say | "'Solutions', 'synergy', 'passionate', 'leverage'" |

3. **Write a voice card** - one paragraph plus the banned-words list. Keep it in `notes/decisions.md` and cite it on every brief.
4. **Test it.** Write one paragraph, then write the same paragraph as they would, and diff. If you cannot tell which is which, you have it.

## Tone: the same voice in different rooms

| Situation | Tone shift | What stays |
|---|---|---|
| Launch post | Energetic, short sentences | No hype words; proof still required |
| Pricing page | Plain, unambiguous, no jokes | The bluntness; jokes next to money read as evasive |
| Bad news / outage | Direct, no marketing, dated | First person, no passive voice |
| Onboarding email | Warm, second person, one action | No jargon |
| Support reply | Calm, specific, no apology theatre | Short sentences |
| Investor or B2B deck | Sober, numbers first | No superlatives |
| Social caption | Fastest version of the voice | Still no invented claims |

## Rules that keep a voice intact

- **Write to one person.** "You" singular. Content written for "businesses" reads like a brochure.
- **Keep their vocabulary, not a better one.** If they say "shop" not "storefront", use "shop". Synonym upgrades are the fastest way to lose a voice.
- **Preserve their imperfections.** A slightly odd comma habit is a fingerprint. Do not sand it into house style.
- **Hinglish is a voice choice, not a mistake.** If they code-switch in speech, decide with them whether it appears in writing. Never insert it to sound local.
- **Numbers are theirs.** Never round ₹1,49,999 to "about ₹1.5 lakh" unless they do.

## The generic-voice detector

Run any draft against this list. Three or more hits means the voice is gone.

- "In today's fast-paced world", "in an ever-evolving landscape"
- "Solutions", "empower", "unlock", "leverage", "seamless", "robust", "cutting-edge"
- "We are passionate about..."
- "It's not just X, it's Y"
- Three-item lists used as rhythm rather than content
- Every paragraph the same length
- A closing paragraph that restates the piece
- Adjectives stacked where a number belongs

## Anti-patterns

- Writing the whole piece, then asking for voice samples. The voice is an input, not a polish.
- Inventing a persona - "we'll write as a friendly expert". That is a default voice with a label on it.
- Copying a famous founder's voice wholesale. It reads as an impersonation, because it is one.
- Making the writing "professional" as a synonym for "longer and more passive".
- Keeping a voice card that nobody updates after the brand changes. Date it.
- Asking "does this sound like us?" without giving them a specific alternative. Show a before and after line instead.
