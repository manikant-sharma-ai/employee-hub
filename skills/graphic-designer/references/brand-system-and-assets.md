# Brand system and assets

A brand kit is not a logo folder. It is the set of decisions already made, so that every future asset is a variation rather than a new argument.

## What a usable kit contains

| Element | Minimum viable | What it decides |
|---|---|---|
| Logo | Primary lockup, stacked variant, icon/mark, monochrome, reverse (on dark) | Every placement |
| Clear space | A number: "clear space = 1x the height of the mark" | Prevents crowding |
| Colour | 3-6 values with hex, plus print equivalents (CMYK/Pantone) | Recognition |
| Type | Display face + text face, with weights actually used, and the licence | Hierarchy |
| Type scale | Sizes for headline / subhead / body / caption at each standard width | Consistency |
| Grid | Columns, gutter, margin for the two or three common canvases | Layout speed |
| Imagery | Subject, crop, treatment, what is banned | Coherence |
| Tone | Three adjectives, and three things the brand is not | Every judgement call |
| Templates | Post, story, thumbnail, deck slide | The 80% case |

If any row is missing, you have a kit gap. Note it, propose a rule, and apply the rule from now on. Do not silently improvise - improvisation is how a feed ends up looking like five companies.

## Reconstructing a kit when none exists

The common case for an SMB. Do it in one pass, from evidence, not taste.

1. **Collect the last 10-15 assets** they liked or used. Ask which ones they were happy with.
2. **Count what repeats.** The same three colours, the same two fonts, the same corner radius, the same crop. Repetition is the brand, whether or not it was intentional.
3. **Sample the colours properly.** Take hex values from flat areas, not from gradients or JPEG-compressed edges. Average three samples per colour.
4. **Name the values.** `ink #1A1A1A`, `signal #E8552D`, `paper #FAF7F2`. Names survive a rebrand; hex alone does not.
5. **Write the three adjectives** from how they described themselves, then test them against the assets. If the assets do not support the adjective, the adjective is aspiration - record it as the direction, not the current state.
6. **Publish the kit as one page**, in `notes/decisions.md` at minimum, with a date. Every later asset cites it.

## Logo handling rules

- **Aspect ratio is sacred.** Scale by dragging a corner, never by typing both width and height.
- **Clear space** - at least the height of the counter of the "o" or the cap height of the mark. Nothing - no text, no border, no photograph edge - enters it.
- **Minimum size** - set one, in pixels for screen and millimetres for print, and hold it. Below it, use the icon variant.
- **Never** recolour outside the approved variants, add a stroke, add a drop shadow, place it on a busy photo without a scrim, or re-typeset the wordmark in a "similar" font.
- **Bilingual lockups** - if the brand appears in English and in a Devanagari, Tamil, Bengali or other script, both are primary. Stack them; do not shrink one to a footnote.

## Asset naming and versioning

`<brand>_<campaign>_<placement>_<WxH>_<vN>.<ext>`

```
kalpataru_diwali-499_ig-feed_1080x1350_v3.png
kalpataru_diwali-499_a5-flyer_148x210_v1_print.pdf
```

Rules that stop the mess:

- Dimensions in the filename, always. It is the fastest way to catch a wrong export.
- `vN` increments only on a change the client asked for. Do not use `final`, `final2`, `FINAL_use-this`.
- One folder per campaign. `_print` suffix on anything going to a press.
- Keep the working master in one format (Figma/Canva/AI), export everything else. Never edit a PNG and call it a master.

## Templates worth building first

Build these four and most requests become a fill-in.

| Template | Why it earns its place |
|---|---|
| Square + 4:5 social post | Covers Instagram feed, LinkedIn, Facebook |
| 9:16 story / reel cover | The most-used vertical surface in India |
| YouTube thumbnail 1280x720 | Highest leverage per pixel in the business |
| Deck slide (title + content) | Stops every deck looking hand-made |

## Anti-patterns

- A "brand guidelines" PDF nobody opens. One page with the actual values beats forty pages of philosophy.
- Six colours because each department wanted one. Cut to a primary, a secondary and two neutrals; let the department use the primary.
- A logo supplied only as a JPEG on white. Ask for SVG or PNG with transparency, and refuse to build on the JPEG.
- Recreating the logo because the file was not to hand. That is how three slightly different logos end up in the market.
- Choosing a typeface with no commercial licence, then printing 5000 flyers with it. Check the licence before the layout, not after.
