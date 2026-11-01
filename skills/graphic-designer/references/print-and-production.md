# Print and production

Screen work can be fixed in an afternoon. Print work is a physical object, and a mistake is a reprint. This file is the checklist that stops the reprint.

## The five numbers that cause most reprints

| Setting | Correct value | What goes wrong otherwise |
|---|---|---|
| Colour mode | CMYK for process print, Pantone for spot | RGB files print dull and shift - especially oranges and greens |
| Resolution | 300 DPI at final size | 72 DPI screenshots print blurry; upscaling cannot invent detail |
| Bleed | 3 mm on every edge (5 mm for large format) | White slivers on the trimmed edge |
| Safe margin | 5 mm inside the trim | Text clipped by the guillotine |
| Fonts | Outlined or embedded | Substituted fonts reflow the whole layout |

Add a sixth: **total ink coverage under 300%** on coated stock, or the sheet does not dry and sets off on the reverse.

## File setup, in order

1. **Set the document size to the trim size**, not the bleed size. Add bleed as a document setting.
2. **Place images at 300 DPI** at the size they appear. Check the effective DPI after scaling - a 6000 px photo scaled to A0 is 72 DPI.
3. **Set black text as 100K only.** Rich black (C40 M30 Y30 K100) on small type produces misregistration fringing.
4. **Large solid black areas** get rich black. Different rule, different use.
5. **Convert RGB to CMYK yourself** and check the result, rather than letting the printer's RIP do it blind. Blues and bright greens lose the most.
6. **Outline the fonts** in the print PDF, or embed them. Then check the text is still there - outlining can merge overlapping glyphs.
7. **Export PDF/X-4** where the printer accepts it. Otherwise a press-ready PDF with marks and bleed.
8. **Name the file** `<brand>_<job>_<size>_<vN>_print.pdf` and put the stock, quantity and finish in the covering email.

## Common Indian print jobs

| Job | Stock and spec | Watch out for |
|---|---|---|
| A5 / A4 flyer | 130-170 gsm art paper, 4-colour both sides | Text within 5 mm of trim; dark backgrounds cracking on the fold |
| Standee / roll-up | 300-400 gsm flex or vinyl, 3x6 ft typical | Bottom 100 mm hidden in the cassette - keep the logo out of it |
| Packaging carton | 250-350 gsm FBB or duplex board, with dieline | Artwork must follow the dieline exactly, including glue flaps |
| Label | Self-adhesive, gloss or matte, die-cut | Barcode quiet zone, statutory declarations, MRP block |
| Visiting card | 300 gsm matte, optional spot UV | Anything within 3 mm of the edge |
| Shop signage | Flex, vinyl or ACP, viewed from 3-15 m | Readability from 10 m, not from 30 cm |
| Sticker / pouch | 80-120 micron BOPP | Small type under 6 pt fills in |

## Statutory and legal text on Indian print

Missing this is the most expensive kind of design error.

- **Packaged goods** need the legal metrology declarations: net quantity, MRP inclusive of taxes, month and year of manufacture, consumer care details, and the importer's name where applicable.
- **MRP block** must be prominent and in the prescribed form. Never design around it - design with it.
- **FSSAI licence number** on food; **drug licence** on pharma; **BIS mark** only where actually certified.
- **Barcodes** need a 2 mm quiet zone and a minimum width; do not place them over a fold or a curve.
- **Green dot / recycling marks** only where the claim is true.
- The manufacturer's address is a legal field, not a design element to shrink.

## Talking to the printer

Send a covering note with every job. It takes two minutes and prevents most reprints.

```
Job: <name>  |  Quantity: <n>  |  Size: <trim, mm>  |  Bleed: 3 mm
Stock: <gsm and type>  |  Colours: <4C / 4C + 1 spot Pantone X>
Finish: <lamination, spot UV, foil, die-cut>
Files: <name>_print.pdf (PDF/X-4, fonts outlined, 300 DPI)
Proof: please send a soft proof before plate-making
```

Ask for a **soft proof** for anything above a few thousand rupees of print. Ask for a **hard proof** when colour accuracy is the point - packaging, brand collateral, anything matching an existing printed piece.

## Anti-patterns

- Sending a Canva PNG export to a printer and calling it print-ready. It is 72-96 DPI RGB with no bleed.
- Designing the dieline instead of downloading the printer's. The box will not fold.
- Text in a colour that is a 4-colour build of a light tint - it will look dirty and misregister.
- Thin white type knocked out of a dark solid. On uncoated stock it fills in.
- Forgetting the reverse side is printed and designing one side only.
- A QR code at 1 cm with a 4-colour background. Print it at 2 cm minimum, black on white, and test it on two phones.
- Approving a proof on a backlit monitor. Print is subtractive; the screen lies about darkness.
