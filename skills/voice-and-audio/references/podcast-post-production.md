# Podcast post-production

The edit is where a recording becomes a show. Everything here is written so a
person with the transcript and a DAW can execute it in one sitting.

## The running order, fixed before the cut

| Slot | Target | What it does |
|---|---|---|
| Cold open | 0:00-0:40 | The strongest 40 seconds of the episode, no intro music |
| Title and intro | 0:40-1:10 | Show name, guest name and their one-line credential |
| Segment 1 | 1:10-15:00 | The guest's story or the core claim |
| Ad slot 1 | mid-roll | Host-read, 45-60 seconds, written into the edit |
| Segment 2 | to 30:00 | The how - specifics, numbers, failures |
| Segment 3 | to 38:00 | The disagreement or the contrarian take |
| Close | 38:00-42:00 | One action for the listener, where to find the guest |
| Outro | 42:00-43:00 | Next episode, subscribe line, credits |

## What to cut, in priority order

| Cut | Typical saving | Rule |
|---|---|---|
| Setup before the question lands | 2-6 min | If the first 60 seconds are "can you hear me", they go |
| Repeated points | 3-8 min | Keep the second telling only if it is better |
| Verbal tics | 30-90 sec total | Cut the tic, not the breath before it |
| False starts | 1-3 min | Cut to the last clean start of the sentence |
| Tangents with no listener payoff | 5-15 min | Test: would a stranger forwarding this clip need it |
| Dead air over 4 seconds | 30-60 sec | Under 3 seconds reads as thought, not as a fault |
| Host talking over the guest | varies | Keep the guest's version; cut the overlap |

Do not cut: laughter that follows a real joke, a pause before a hard answer, the
guest correcting themselves, an admission against interest.

## Writing the edit decision list

One row per cut, in timecode order, with the reason in five words or fewer.

| In | Out | Reason | Saves |
|---|---|---|---|
| 00:02:14 | 00:03:02 | Pre-question setup, no content | 0:48 |
| 00:07:41 | 00:08:05 | Repeated from 00:05:20 | 0:24 |
| 00:19:02 | 00:19:09 | "Sorry, can you repeat" | 0:07 |

The reasons matter: they are what lets the host disagree with a cut without
re-listening to the whole episode.

## Pacing

- **Change something every 90 seconds** - a new voice, a music bed, a chapter, a question. Attention decays on a flat stretch.
- **Cut the guest's answer to its first two sentences** when the third is a repeat, then let the host ask the follow-up. This reads as a better interview than it was.
- **Keep one long answer per episode** - the one where the guest thinks aloud. That is the moment people clip.
- **Never cut mid-laugh or mid-breath at a chapter boundary.** Crossfade 30-60 ms, and cut on the room tone, not on the word.

## Chapter marks

| Chapter name | Bad | Good |
|---|---|---|
| Opening | "Intro" | "Why 60% of D2C brands die in month 18" |
| Segment | "Part 2" | "The ₹4 lakh mistake in his first warehouse" |
| Close | "Outro" | "The one number to check every Monday" |

Chapters go into the ID3 tags (Podcasting 2.0 chapters), the YouTube description
and the show notes - the same names in all three, so search finds them.

## Masters and exports

| Use | Format | Setting |
|---|---|---|
| Podcast feed | MP3 192 kbps or AAC 128 kbps | 44.1 kHz, mono for one voice, stereo for two |
| YouTube | WAV or AAC 320 kbps | 48 kHz, -16 LUFS, with a static cover frame |
| Clips | MP4 with a waveform or caption card | 9:16, -14 LUFS, burned captions |
| Archive | WAV 48 kHz 24-bit | Unprocessed stems, kept forever |

## Anti-patterns

- **Cutting to a target length by trimming the ending.** The close is where the subscribe happens.
- **Adding music under speech with no ducking.** The voice disappears on a phone speaker.
- **Normalising to 0 dBFS.** Every platform will turn it down and the dynamics go with it.
- **Editing by waveform peaks alone.** A loud laugh and a loud word look the same.
- **Shipping an episode with no chapters** because the host was tired. It is 15 minutes of work and it is the difference between a show and a file.
