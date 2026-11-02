# Footage intake and organising

Most editing time is lost before the first cut, in finding the right file. Ten minutes of intake saves an hour of hunting.

## The intake checklist

| Item | Why | If missing |
|---|---|---|
| Every source file, at original resolution | Proxies lose the ability to reframe | Ask for the originals; never upscale a compressed export |
| Frame rate and resolution per file | Mixed rates cause judder when conformed | Note it, and conform to the highest rate |
| Audio channels and sample rate | A mono phone clip in a stereo timeline is half-volume | Note it; fix in the audio pass |
| A transcript, or audio clean enough to transcribe | The transcript is where the hook is found | Extract audio and transcribe first |
| Brand kit - fonts, colours, logo, caption style | Consistency across the set | Ask; do not approximate a font |
| Consent and licence status | Testimonials, third-party music, stock | Stop and ask before cutting |

## Naming, before anything else

```
<client>-<topic>-<source>-<date>-<res>-<vNN>.<ext>
acme-stockcount-a7siii-20261014-4k-v01.mp4
acme-stockcount-voiceover-20261015-wav-v01.wav
```

Rules: no spaces, no `final`, no `new`, no dates written as `14-10`. Version numbers increase; they never become `final2`. A stranger must be able to pick the file from the name alone.

## The folder shape

```
project/
  01-source/        camera, phone, screen recordings, untouched
  02-audio/         extracted audio, voice-over, music, sfx
  03-graphics/      logo, lower thirds, end cards, brand kit
  04-project/       the editor's project file, autosaves
  05-exports/       masters and derivatives, named per the matrix
  06-review/        versions sent for feedback, with the date in the name
```

`01-source` is read-only for the life of the project. The moment a source file is overwritten, the ability to recut is gone.

## Building the selects reel first

1. **Transcribe everything** - Whisper locally, Descript, or the platform's own captions. Store the transcript beside the source file.
2. **Mark in the transcript**, not the timeline: `[HOOK]`, `[PROOF]`, `[PAYOFF]`, `[FILLER]`, `[REPEAT]`. This is faster than scrubbing and it survives a change of editor.
3. **Cut a stringout** - every usable line, in source order, no transitions. Usually 3-6x the final duration.
4. **Only then** arrange the stringout into the story. Arranging before stringing out produces a cut that keeps a line because it was convenient, not because it was needed.

## Reviewing footage you cannot watch

When you have a transcript and sampled frames rather than real-time playback:

- Sample one frame every 2-4 seconds at thumbnail size, and read them as a strip.
- Look for: framing changes, eyeline drift, hands in frame, blown highlights, a person walking behind, a phone screen showing something private.
- State plainly: "I have read the transcript and 40 sampled frames; I have not judged motion, focus pull or continuity."
- Ask for the one thing that would settle it: a screen recording of the take, or a note on which segments look soft.

## Anti-patterns

- **Editing from the file browser.** Opening files one at a time and watching each costs more than transcribing all of them.
- **Deleting "bad" takes before the selects pass.** The bad take often contains the only natural laugh or the clearest explanation.
- **Working on the only copy.** One accidental overwrite of `01-source` ends the project.
- **Accepting a WhatsApp-compressed clip as a master.** It arrives at 480p with crushed audio and cannot be recovered.
- **Starting the cut before the brand kit arrives.** Restyling captions across eight clips is a day of rework.
- **Guessing the frame rate.** A 25fps source in a 30fps timeline produces a stutter that reads as amateur.
