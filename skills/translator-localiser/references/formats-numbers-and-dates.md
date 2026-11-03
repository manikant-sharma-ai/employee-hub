# Formats, numbers and dates

A correct translation with a foreign number format still reads foreign. These are
the mechanical rules that make copy feel local.

## Numbers

- **Indian grouping**: 1,00,000 (one lakh), 1,00,00,000 (one crore). Never 100,000 in customer-facing copy.
- **Lakh and crore in words** for amounts people say aloud: `₹1.5 लाख`, `₹2 करोड़`. Keep the numeral for exact prices: `₹1,499`.
- **Crore/lakh in English copy too** - your reader thinks in these units.
- **Decimals**: `₹499.00` is fine on an invoice, `₹499` in marketing.
- **Percentage**: `18%` in most Indian usage, not `18 %`.
- **Ordinals and counts**: `5वां`, `3री` - the suffix agrees with the gender of the noun in Hindi. Check it.

## Currency

- `₹` before the amount, no space: `₹499`. In Hindi text, `₹499` is fine; `499 रुपये` reads naturally in speech.
- Never `Rs. 499/-` in app UI; acceptable on an invoice or a cheque.
- Say which currency if the audience is international: `₹499 (about $6)`.

## Dates and time

- **Numeric**: `03/11/2026` (dd/mm/yyyy). Say the month in words when ambiguity costs money: `3 नवंबर 2026`.
- **Months in the target script** for consumer copy: `नवंबर`, `நவம்பர்`, `নভেম্বর`.
- **Time**: 12-hour with am/pm is common in cities; `सुबह 9 बजे` reads better in Hindi consumer copy. Use IST, and say `IST` only when the audience is outside India.
- **Relative dates** are risky: "within 3 days" needs a starting point. `3 कार्यदिवस` (working days) if that is what is meant.
- **Festival dates move**; never reuse last year's.

## Phone numbers and addresses

- **Phone**: `+91 98765 43210` with the 5-5 split for readability. Say the number in the local rhythm in voice copy.
- **PIN code before city** in Indian addresses: `411001, पुणे, महाराष्ट्र`.
- **Address order** differs by language; keep the postal order the courier needs, translate the labels, not the sequence.
- **Landmark** fields are normal in Indian addresses; keep them.

## Units

- **Metric always**: km, kg, litres, °C. `1.5 लीटर`, `25 किमी`.
- **Clothing and footwear sizes** often keep the UK/EU number with a local label; do not convert silently.

## Text mechanics per script

- **No capitalisation** in Devanagari, Tamil, Telugu, Kannada, Malayalam, Gujarati, Bengali, Odia, Punjabi - emphasis comes from word choice, not case.
- **Punctuation**: the danda `।` is correct for Hindi sentence endings; a full stop is also widely accepted. Be consistent.
- **Line breaking** differs; do not assume a word will not split. Test the longest string.
- **Urdu is right-to-left**: punctuation, numbers and mixed English terms need RTL-safe layout, not just translated text.

## Anti-patterns

- `100,000` in an Indian app.
- `$` left in a localised screen.
- `mm/dd/yyyy` in a date field for an Indian audience.
- A translated address that reverses the postal order and the courier cannot deliver.
- Converting sizes without saying so.
