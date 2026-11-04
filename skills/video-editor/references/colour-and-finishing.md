# Colour and finishing

Finishing is the difference between footage and a film. It is also the cheapest
quality win available: most small-business video is badly exposed, badly balanced
and badly levelled, not badly shot.

## The order of operations

1. **Normalise exposure** per clip - lift the shadows, protect the highlights.
2. **White balance** to a neutral, so skin does not read orange or green.
3. **Match shots** in a scene, so a cut does not jump in colour.
4. **Look** - contrast and saturation, applied consistently across the piece.
5. **Levels** - audio last but not least; viewers forgive picture, not sound.

## The three mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Pushing saturation | Skin turns orange, reds clip | Saturation in the 100-110 range, never 140 |
| Crushing blacks | Detail lost in shadow | Keep the black point at 0-5, not -20 |
| Unmatched shots | The cut "jumps" | Match on skin tone, not on the background |

## Scopes over eyes

- **Waveform**: keep highlights under 100 IRE, skin around 60-70.
- **Vectorscope**: skin sits on the skin-tone line; if it drifts, the white balance is wrong.
- **Your monitor is lying** unless it is calibrated. Do not grade on a laptop at 100% brightness in a bright room.

## Audio finishing

- **Target -14 LUFS integrated** for YouTube and social; -16 for podcasts.
- **True peak under -1 dBTP**, or the encoder will distort.
- **Noise reduction before compression**, or you amplify the hiss.
- **De-ess** the sibilance, and check on phone speakers - that is where it is watched.
- **Duck the music** under speech by 8-12dB, and never let it fight the voice.

## Deliverable checks

- [ ] No frame is black where it should not be, none frozen
- [ ] Audio in sync at the start, middle and end (drift shows late)
- [ ] Captions timed to speech, not to the transcript's guess
- [ ] Safe margins respected for the platform's UI
- [ ] File plays on a phone before it is delivered

## Anti-patterns

- A "cinematic" teal-and-orange LUT on a product demo.
- Heavy grain added to hide compression - it makes it worse.
- Music louder than the speaker.
- Grading each clip independently, so the film flickers.
- Delivering a file nobody has played end to end.
