# Motion and animated assets

A still is seen; motion is watched for two seconds before it is judged. The craft
is deciding what moves and what stays still, not adding movement everywhere.

## The formats that get used

| Asset | Size | Length | Where |
|---|---|---|---|
| Story / reel cover | 1080x1920 | 3-8s loop | Instagram, WhatsApp Status |
| Feed video | 1080x1350 or 1080x1080 | 5-15s | Instagram, Facebook, LinkedIn |
| Animated banner | 300x250, 728x90 | Under 15s, 3 loops | Display, and most networks cap file size |
| Logo sting | 1920x1080 | 1-3s | Video intros, decks |
| Animated carousel slide | 1080x1350 | 2-4s | Where the platform allows it |

## Principles that make motion read

- **One idea per animation.** If two things move, the eye picks neither.
- **Ease, never linear.** Ease-out for arrivals, ease-in for exits; linear motion reads mechanical.
- **12-24 frames for a transition**, not 60 - fast enough to feel responsive, slow enough to read.
- **Move the thing that matters**, hold the brand mark still. A logo that flies in is a logo people cannot read.
- **Text: fade or a 20px rise**, nothing more. Kinetic type is a genre, not a default.
- **Loop cleanly**: the last frame should be able to cut to the first without a jump.
- **Respect reduced motion** - ship a static fallback for anything with a strobe or a fast pan.

## Sound

- **Most feed video autoplays muted.** Design for silence: the message must survive with no audio, then be better with it.
- **If there is sound**, one clean track, no stock whoosh-and-ding stack.
- **Captions burned in** for anything with speech.

## Handing motion to production

The designer specifies; the animator or the tool executes. The spec is: duration,
frame rate, the easing curve per element, the exact start and end states, the
loop behaviour, and the export settings. Without the easing curve you get a
different animation every time.

## Tools, honestly

- **Canva / Figma prototype / After Effects / DaVinci** - pick by who will edit it next month.
- **A 3-second GIF is 4MB.** Use MP4 or WebM for anything over a second; GIF is for reaction images only.
- **File size limits are real** on display networks; check before you animate 12 elements.

## Anti-patterns

- Everything sliding in from a different direction.
- A 15-second animation with a 4-second logo intro.
- Text that moves while it is being read.
- A loop with a visible jump.
- Motion added to a still because the brief said "make it dynamic".
