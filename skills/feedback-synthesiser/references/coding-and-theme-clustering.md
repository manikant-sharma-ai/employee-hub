# Coding and theme clustering

Coding is the step everyone skips, and it is the step that decides whether the numbers mean anything.

## The order that works

1. **Read 30 records cold.** No theme list, no spreadsheet, no counting. Just read.
2. **Write the theme list from what you read**, in the customer's words, not the product's.
3. **Write the rules file** - what belongs in each theme, what does not, and the boundary cases.
4. **Code 50 more with the rules.** Adjust the rules, not the themes, when something does not fit.
5. **Code the rest**, with "other" as a valid destination.
6. **Re-read "other"** at the end. If it is over 15%, the theme list is wrong.

A theme list invented before reading is a projection of what the team already believes. It will find
exactly what the team expected, which is the definition of a useless synthesis.

## Theme definitions that survive contact

| Good theme | Bad theme | Why |
|---|---|---|
| "Onboarding takes more than a day" | "Onboarding" | One is a finding, the other is a folder |
| "Invoice does not match the purchase order" | "Billing issues" | Specific enough to fix |
| "Delivery arrived a day late" | "Logistics" | Names the failure and the unit |
| "Support replied but did not solve it" | "Support quality" | Says what to change |
| "App crashes when uploading a photo over 5 MB" | "Bugs" | Reproducible |

A theme should be phrased so that a product or operations person could act on it without reading the
records. If it needs a meeting to interpret, it is a category.

## The rules file

One page, kept beside the coding sheet:

```
THEME: onboarding-too-long
IN:  "took me two days", "could not finish setup", "the import kept failing"
OUT: "the UI is confusing" (that is usability, theme usability-confusing)
BOUNDARY: a setup problem that resolves within an hour goes to setup-friction, not this theme
MAX THEMES PER RECORD: 2
```

Rules make the coding reproducible and defensible. Without them, two people coding the same 200
records get different counts and the readout loses its authority.

## One record, several themes

| Approach | When | Risk |
|---|---|---|
| Single theme per record | Simple, fast, adds to 100% | Discards the second complaint |
| Up to two themes per record | Most feedback | Shares can exceed 100% unless stated |
| Multi-label, unlimited | Rich datasets | Counting becomes meaningless |

Pick one, state it in the output, and keep the arithmetic consistent. The default: up to two themes,
shares computed as records-mentioning over records-total, with a note that shares do not sum to 100%.

## Counting rules

- **Count records, not sentences.** One ticket with four complaints is one record against two themes.
- **Count per source**, then total. A theme at 30% of tickets and 2% of reviews is a support problem,
  not a product one.
- **Exclude empty and test records** before counting, and say how many you excluded.
- **Do not weight by sentiment.** "Love it but it crashes" is a crash record.
- **Keep the raw coding sheet.** The counts must be re-derivable by someone else from the same file.

## The taxonomy, by business type

| Business | Themes that tend to matter |
|---|---|
| SaaS | Onboarding, a specific broken workflow, price-value, support responsiveness, missing integration |
| D2C | Delivery time, packaging condition, product quality, size or fit, return experience |
| Services | Response time, quality of the deliverable, communication, billing clarity, scope creep |
| Marketplace | Trust and fraud, delivery, refund handling, seller responsiveness, listing accuracy |
| Restaurant | Wait time, food consistency, portion against price, hygiene, staff behaviour |
| B2B wholesale | Lead time, credit terms, damage in transit, price consistency, rep responsiveness |

Start from the list, then let the records correct it. The list is a prior, not a filter.

## When the data is a survey

- **Segment by the rating.** Free text from 1-2 star answers and from 4-5 star answers are two
  different datasets that happen to share a column.
- **Read the middle.** 3-star answers carry the specific, actionable complaint more often than either
  extreme.
- **Check the skip pattern.** A question answered by 40% of respondents is a different claim from one
  answered by 90%.
- **Never average a free-text field.** There is no mean of a sentence.

## Anti-patterns

- **Clustering by keyword alone.** "Slow" appears in praise ("slow-cooked") and complaint. Read enough
  to know which.
- **Themes named after internal teams.** "Marketing feedback" tells nobody anything.
- **A long tail of 40 themes with two records each.** Collapse to 8-12 themes plus "other".
- **Coding by whoever is available.** Coding quality is the whole output; do it yourself or check it.
- **Changing the theme list halfway through** without re-coding the first half.
