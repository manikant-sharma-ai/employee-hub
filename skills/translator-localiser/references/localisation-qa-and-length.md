# Localisation QA and length

A translation is not finished when the words are right. It is finished when it fits, the placeholders survived, the numbers read correctly, and a native speaker has read it.

## The mechanical checks, in order

| Check | What fails | How to catch it |
|---|---|---|
| Placeholder parity | `{name}` dropped, `%s` reordered, `{{count}}` renamed | Automated - `scripts/glossary_check.py` |
| Empty or copied strings | Target identical to source where it should not be | Automated |
| Untranslated leftovers | An English sentence in a Hindi file | Automated, plus a read |
| Glossary drift | Two renderings of one term | Automated against the glossary |
| Length | Overflowing button, truncated card, broken table | Automated ratio + visual check |
| Numbers and dates | 1,00,000 turned into 100,000; DD/MM swapped | Automated pattern check + read |
| Script mixing | Devanagari inside a Tamil string | Automated |
| Punctuation | Devanagari danda (।) replaced by a full stop, or vice versa | Read |
| Sorting and search | Collation differs from the Latin assumption | Manual test in the product |

## Expansion ratios

Rough guide for text translated *from* English. Budget the UI to the high end.

| Target | Typical expansion | Safe allowance |
|---|---|---|
| Hindi | 10-20% shorter to 10% longer | +15% |
| Marathi | +10-20% | +25% |
| Gujarati | +5-15% | +20% |
| Bengali | +10-20% | +25% |
| Tamil | +20-35% | +40% |
| Telugu | +15-30% | +35% |
| Kannada | +20-35% | +40% |
| Malayalam | +25-40% | +45% |

A 12-character button in English is 17 in Tamil. If the design cannot take it, that is a design finding, not a translation problem - flag it rather than shortening the meaning.

## What to do when it does not fit

1. **Shorten the target, not the meaning.** Drop honorifics and articles first.
2. **Use the imperative.** "जारी रखें" beats "आप आगे बढ़ सकते हैं" in a button.
3. **Move the detail out of the label** - into helper text or a tooltip.
4. **Flag it.** "Tamil label needs 40% more width at 14px" is a UI ticket, and it is the translator's finding to raise.
5. **Never truncate mid-word** or with an ellipsis in a language where the verb comes last - the meaning disappears.

## Numbers, dates, money

| Item | Indian convention | Failure |
|---|---|---|
| Large numbers | 1,00,000 (lakh), 1,00,00,000 (crore) | "100,000" or "10,000,000" reads foreign |
| Currency | ₹1,499; "₹1,499 (GST अतिरिक्त)" | "Rs. 1499.00" in a consumer string |
| Date | 03/11/2026 in DD/MM; spell the month when ambiguous | 11/03/2026 read as March |
| Time | 6 pm IST, 18:00 | "6:00 PM" with no zone in a multi-city product |
| Phone | +91 98765 43210, 10 digits | Grouping into (987) 654-3210 |
| Decimal | ₹499.50, two places for money | Rounding away paise in an invoice |
| Percent | 18% GST, written as 18% | "18 percent" in a table cell |

## The review loop

1. **Translator** produces the bilingual table with notes.
2. **Mechanical check** runs first - never send a reviewer a file with broken placeholders.
3. **Native reviewer** reads the target only, in context (a screen, a page, a message), and marks: wrong, unnatural, wrong register, too long.
4. **Two rounds maximum.** A third round means the glossary or the brief was wrong, and it should be fixed there instead.
5. **Record the feedback as glossary entries**, not as corrections to one file.

## Anti-patterns

- Shipping strings that were never rendered in the actual UI.
- Reviewing a translation as a list of sentences with no context.
- Placeholder bugs found in production.
- Trusting a 100% "translated" count from the platform - it counts copied strings as translated.
- Reviewing in the wrong register because nobody wrote down which one was chosen.
- Letting the reviewer rewrite the source, which silently changes the English too.
