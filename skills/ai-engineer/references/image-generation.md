# Image generation

Images are a briefing problem before they are a prompt problem. A designer who is told "make it nice" produces something you cannot use; so does a model.

## The brief, before pixels

Answer these seven. If you cannot, you are not ready to generate.

1. **Subject** - what exactly is in frame.
2. **Purpose and placement** - thumbnail, banner, product page, print. This sets the aspect ratio and the safe zones.
3. **Composition** - close-up, wide, flat lay, three-quarter. Where the subject sits in frame, where text will go.
4. **Lighting and mood** - soft daylight, hard studio, neon night, high-key clean.
5. **Palette** - literal hex values from the brand, not "vibrant".
6. **Style reference** - "clean editorial product photography", not an artist's name.
7. **Negative constraints** - no text, no hands, no logos, no extra fingers, no cluttered background.

## Prompt structure

Subject and action, then environment, then lighting, then lens or style, then mood, then technical. Keep it to a dense paragraph rather than a keyword soup - modern models read sentences better than comma lists.

Example: "A single matte ceramic mug on a pale oak desk, morning window light from the left casting a soft shadow, shot at 50mm with shallow depth of field, calm minimal editorial style, warm neutral palette (#F4EFE8, #8A6E4B), 3:2 aspect."

## Consistency across a set

The hard problem is not one good image; it is ten that look like a family.

- Lock a **style block** - the exact same sentence about lighting, palette and lens - and reuse it verbatim in every prompt.
- Use **reference images** where the model supports them. One reference does more for consistency than three paragraphs.
- **Fix the seed** while iterating on a single image; change only one variable per attempt.
- Build a **contact sheet**: generate all variants, view them side by side at final size, then pick. Judging one image at a time hides inconsistency.

## Text in images

Models still mangle text. Keep it under five words, high contrast, large, and centred in a flat area. Then read the render - literally read it - and expect at least one retry. For anything with more text, generate the image and set the type in Canva, Figma or code.

## Thumbnails and social

- Must be legible at 20% size. Squint test: if the focal point is unclear when shrunk, it fails.
- One focal point. Two subjects compete and both lose.
- Leave a safe zone for the platform's overlay UI - bottom-right on most video surfaces.
- Face or object in the left third, text right, works for most feeds; check the specific platform's crop.

## Rights and ethics

- Do not ask for a living artist's style by name. Describe the qualities instead.
- Do not generate a real person's likeness for anything resembling endorsement.
- Check the licence of every reference image before it goes into a commercial asset.
- Generated imagery for products must not misrepresent what the customer receives.

## QA checklist

Hands and fingers, eyes, text, edges and backgrounds, reflections, jewellery and straps, shadows that match the light. Then view at final size and at thumbnail size. A defect invisible at 100% is often obvious at 20%.

## Cost

Draft at low resolution, pick, then upscale the winner. Iterating at full resolution is the most common way to waste an image budget.
