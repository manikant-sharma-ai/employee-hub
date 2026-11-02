# Platform delivery specs

Specs change. State what you are assuming, and check the platform's own help page before a paid campaign. What follows is the shape of the answer, with the numbers that have been stable.

## The master-and-derivatives rule

Cut one **master**: the highest resolution, clean, no burned captions, no logos, full colour grade. Everything else is exported from it.

| Derivative | From the master |
|---|---|
| 9:16 captioned | Reframed, captions burned |
| 1:1 feed | Reframed, captions burned |
| 16:9 clean | Cropped, no captions (for YouTube upload) |
| 15s cutdown | Re-cut, not sped up |
| Silent-loop version | Audio removed, hook card added |

Never export a derivative from another derivative. Two generations of compression is visible at phone size.

## Aspect ratios

| Ratio | Use |
|---|---|
| 9:16 (1080x1920) | Reels, Shorts, TikTok, Stories, status |
| 4:5 (1080x1350) | Instagram feed - the largest area in the feed |
| 1:1 (1080x1080) | Feed, carousels, some LinkedIn placements |
| 16:9 (1920x1080) | YouTube, website, presentations |
| 2.39:1 | Cinematic only; wastes vertical space on social |

## Export settings that hold up

| Setting | Value | Note |
|---|---|---|
| Resolution | 1080x1920 vertical, 1920x1080 horizontal | 4K only if the delivery needs it; it is 4x the upload |
| Frame rate | Match the source (24, 25 or 30) | 60fps only for motion-heavy product footage |
| Codec | H.264 High profile, 2-pass | H.265 for smaller files, but compatibility is patchier |
| Bitrate | 8-12 Mbps at 1080p vertical | Below 6 Mbps, gradients band visibly |
| Audio | AAC, 48 kHz, 320 kbps stereo | Never 128 kbps for a music-led cut |
| Colour | sRGB / Rec.709 | HDR only if the platform supports it and the source is HDR |
| Filename | `<client>-<topic>-<ratio>-<version>.mp4` | No spaces, no `final` |

## Duration limits worth knowing

| Platform | Limit | Practical sweet spot |
|---|---|---|
| Instagram Reels | ~90s (varies) | 15-30s |
| Instagram Stories | 60s per card | 15s |
| YouTube Shorts | ~60s (varies) | 20-45s |
| LinkedIn video | 10 minutes | 30-90s |
| YouTube long form | 12 hours | As long as the value holds |
| Meta ads | 240s | 15s and 30s |
| WhatsApp status | 30s per card | 15s |

Because limits move, the honest answer is: "I have exported 9:16 at 24s and 38s; check the current Reels limit before upload, it has changed twice in two years."

## Safe zones and interface overlap

| Platform | Reserved area |
|---|---|
| Reels / Shorts | Top ~12%, bottom ~20%, right ~15% |
| Stories | Top ~15% (profile), bottom ~20% (reply bar) |
| LinkedIn | Bottom ~15% |
| YouTube long form | Bottom ~10% for controls |

Keep text and faces out of those bands. A caption under the platform's own caption bar is invisible.

## Thumbnails and covers

You do not design them - that is `graphic-designer` - but you supply what they need:

- The exact frame at 0:00, exported as a still at full resolution.
- Three alternative stills at moments that read at thumbnail size.
- The one-line hook, so the cover text matches the spoken hook.
- The safe crop: the region of the frame that survives a 16:9, 1:1 and 9:16 crop.

## The delivery note

Every delivery ends with this table filled in:

| File | Ratio | Duration | Size | Captions | Where it goes |
|---|---|---|---|---|---|
| `acme-stockcount-9x16-v03.mp4` | 1080x1920 | 0:28 | 42 MB | burned EN | Reels, Shorts |
| `acme-stockcount-9x16-v03.srt` | - | - | 3 KB | sidecar | upload to YouTube |

## Anti-patterns

- **Upscaling a 720p source to 1080p** and calling it HD. It is soft, and the viewer can tell.
- **Exporting at 60fps from a 24fps source.** Duplicated frames, judder, no benefit.
- **One file for every platform.** Black bars in a vertical feed signal a repost.
- **Text inside the interface bands.** The commonest reason a polished cut looks careless on a phone.
- **Delivering without a sidecar caption file.** The client has no editable record of what the video says.
- **Trusting a spec sheet from last year** for a paid campaign. Check the ad platform's current requirements.
