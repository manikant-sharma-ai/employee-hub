# Audio cleanup and loudness

Order matters more than plugins. Room first, voice second, level third, loudness
last. Every setting below is a starting point, not a law - but start here rather
than at zero.

## Diagnose from the description before touching anything

| What they say | What it usually is | First move |
|---|---|---|
| "Hollow, like a tunnel" | Comb filtering from a wall reflection | Move the mic off-axis, add absorption behind the speaker |
| "Hummy, buzzing" | Mains hum, 50 Hz in India, or a ground loop | Notch at 50 Hz and harmonics, then fix the earth |
| "Hissy, like a fan" | Noise floor too high, gain too low at the source | De-noise lightly, then fix the gain structure |
| "One guest is quiet" | Remote recording, separate track levels | Match by loudness, not by peak |
| "Sibilant, spiky S" | Mic close and bright, 5-8 kHz | De-ess, then a gentle shelf down |
| "Boomy, muddy" | Proximity effect, mic under 10 cm | High-pass at 80-100 Hz |
| "It cuts out and comes back" | Noise gate or bad connection | Remove the gate; check the recording, not the edit |
| "Echo on one voice only" | That guest was on a laptop speaker | Re-record that side, or accept and say so |

## The chain, in execution order

| Step | Setting to start with | Why it is here |
|---|---|---|
| 1. High-pass filter | 80 Hz, 12 dB/oct (male), 100 Hz (female) | Removes rumble, table thumps, AC noise before anything amplifies it |
| 2. De-noise / spectral repair | 6-10 dB reduction, not more | More than 10 dB gives the underwater warble |
| 3. De-hum | Notch 50 Hz, 100, 150, 200 Hz, Q 30 | India is 50 Hz mains; a 60 Hz notch does nothing |
| 4. De-ess | 5-8 kHz, 3-6 dB reduction | Before compression, which would exaggerate the sibilance |
| 5. Corrective EQ | Cut 200-400 Hz by 2-3 dB if muddy; +1-2 dB at 3 kHz for presence | Small moves; if you need 6 dB, the recording is wrong |
| 6. Compression | 3:1, threshold for 3-6 dB gain reduction, attack 10 ms, release 100 ms | Evens the delivery so the listener stops reaching for the volume |
| 7. Room tone / ambience match | Fill gaps with 200-500 ms of room tone | Silence between words is what makes a cut audible |
| 8. Limiter | -1 dBTP ceiling | Stops the platform's encoder from clipping |
| 9. Loudness | -16 LUFS integrated, -1 dBTP true peak | The delivery target; measure, do not guess |

Music beds: duck 12-18 dB under speech, and never let a bed sit above -30 LUFS
under a voice on a phone speaker.

## Loudness targets by destination

| Destination | Integrated | True peak |
|---|---|---|
| Podcast feed (Apple, Spotify, JioSaavn) | -16 LUFS | -1 dBTP |
| YouTube | -14 LUFS | -1 dBTP |
| Instagram / Reels / Shorts | -14 LUFS | -1 dBTP |
| TV or radio ad (India) | -23 LUFS EBU R128 | -1 dBTP |
| IVR / phone system | -18 to -20 LUFS, mono | -3 dBTP |
| Presentation or webinar recording | -16 LUFS | -1 dBTP |

Two rules that catch most mistakes: measure integrated loudness over the whole
file, not the loudest 10 seconds; and listen once on a phone speaker at 60%
before calling it done.

## When the room is the problem

Give a treatment brief instead of a plugin stack. Three moves, in cost order:

1. **Move the mic.** 15-25 cm from the mouth, slightly off-axis, away from the
   wall behind the speaker, with a soft surface behind the mic.
2. **Absorb one wall.** A curtain, a rug, a bookshelf, a mattress against the
   wall the speaker faces. This removes the flutter echo that no de-reverb fixes.
3. **Change the room.** A wardrobe, a car with the engine off, a small carpeted
   room with the door closed. Cheaper than any hardware.

## Anti-patterns

- **De-noising first and hard.** It removes the breath that makes speech human and leaves a metallic tail.
- **Stacking three EQs.** Each small correction adds phase smear; one corrective EQ and one tonal shelf is the ceiling.
- **Normalising to peak instead of loudness.** Peak normalisation makes a quiet guest loud and a laugh deafening.
- **Trusting the meter over the phone speaker.** The meter does not know your listener is on a ₹1,200 earbud in traffic.
- **Fixing the master instead of the source.** Every hour of repair is a message about the recording setup.
