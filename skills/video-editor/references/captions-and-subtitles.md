# Captions and subtitles

Most short-form video is watched muted, on a phone, in a place where sound is not available. The caption track is therefore the primary text of the video, not an accessibility add-on.

## Burned-in or sidecar

| Delivery | Captions | Why |
|---|---|---|
| Reels, Shorts, TikTok | Burned in | Native caption styling is weak and the viewer may not enable them |
| LinkedIn video | Burned in | Autoplay is muted, and native captions are inconsistent |
| Paid ads | Burned in, plus a sidecar SRT | Compliance review needs the text, and platforms may require it |
| YouTube long form | Sidecar SRT/VTT (uploaded) | Editable, searchable, indexable |
| Website hero | Burned in, or styled overlay | Depends on the player; ask |
| Any deliverable to a client | Both | The sidecar is the record; the burn-in is the product |

## Reading speed and line length

| Rule | Value |
|---|---|
| Characters per line | 32-42 for vertical video |
| Lines per card | 1-2, never 3 |
| Reading speed | 15-20 characters per second |
| Minimum duration per card | 1 second; below that, merge |
| Maximum duration per card | 5 seconds; above that, split |
| Gap between cards | 80-120ms, so the eye registers a change |

A card that is on screen for 0.6 seconds cannot be read. If the speech is that fast, shorten the text rather than speeding the card up.

## What the caption says versus what was said

- **Verbatim by default.** Captions are a transcript, not a summary.
- **Clean the obvious** - filler words can go, false starts can go, but the meaning cannot change.
- **Numbers in digits** ("11 days", not "eleven days") - easier to scan and to search.
- **Units always** - ₹, %, kg, km. "It went to 2" is meaningless; "11 days to 2 days" is a claim.
- **Never caption a claim that was not spoken.** If the speaker said "a lot", the caption does not say "40%".
- **Profanity:** follow the brand's rule, and remember most platforms reduce reach for it. Ask once, record it in `notes/decisions.md`.

## Hinglish and code-switching

| Situation | Approach |
|---|---|
| Speaker mixes Hindi and English | Caption in the same mix, in Latin script - do not translate to pure Hindi or pure English |
| Brand or product name inside a Hindi sentence | Keep the English spelling of the name |
| A word has no clean English equivalent | Keep the Hindi word; a caption is not a translation |
| Audience in one script only | Offer a second caption file in the target script rather than forcing one |
| Numbers and units in Hindi speech | Digits, same as English |

Never machine-translate a Hinglish caption into formal Hindi - it loses the register that made the video watchable.

## Placement and safe zones

| Platform | Avoid |
|---|---|
| Reels / Shorts | Bottom 20% (captions bar, CTA), right edge (buttons), top 12% (title) |
| LinkedIn | Bottom 15%, and the first 2 seconds where the mute icon sits |
| YouTube long form | Bottom 10% if the player controls will be visible |
| Paid ads | Any region where the platform overlays a CTA button |

Place captions at roughly 60-70% of the frame height on vertical, centred, with a solid or gradient backing only if the background is busy.

## Style rules worth fixing once

- One font, one weight, one size, one colour, one outline - recorded in the brand kit.
- High contrast: white with a dark outline or a dark box beats a coloured text on a coloured background.
- Highlight the keyword, not the whole line - one accent colour per card.
- No all-caps for more than three words; it reads as shouting at phone size.
- Never animate words in one at a time on a talking head; it costs reading time and adds nothing.

## Writing a real subtitle file

```
1
00:00:00,200 --> 00:00:02,800
If you run a godown, you are
losing stock every month.

2
00:00:02,900 --> 00:00:05,600
Not because of theft. Because
nobody counted the transfers.
```

Rules: sequential numbering, blank line between cues, `HH:MM:SS,mmm` for SRT (`HH:MM:SS.mmm` for VTT), no cue shorter than 1 second, no cue longer than 2 lines.

## Anti-patterns

- **Auto-captions shipped unchecked.** They mangle names, numbers and Hinglish, and a wrong number in a caption is a false claim in writing.
- **Captions that paraphrase.** The viewer hears one thing and reads another, and distrusts both.
- **A caption track with no punctuation.** It reads as a wall and gets skipped.
- **Text sitting under the platform's UI.** The most common reason a good cut looks careless.
- **Burned-in captions on a master file.** Burn only on derivatives; the master stays clean.
- **Dual-language captions stacked on one screen.** Two files, two versions - never both at once.
