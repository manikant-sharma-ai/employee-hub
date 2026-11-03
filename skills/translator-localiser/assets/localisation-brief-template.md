# Localisation brief - <product / page> into <language>

Date: <date> | Owner: <name> | Reviewer: <native speaker, named> | Round: <1 / 2>

## 1. The decision line

| Field | Answer |
|---|---|
| Target language | |
| Script | Devanagari / Tamil / Latin (romanised) |
| Register | Formal / Neutral / Informal - and the pronoun chosen |
| Audience | B2B or consumer, region, age |
| Mode by section | literal / faithful / transcreated - list the sections |
| Source approved? | yes / no - if no, say what translating now costs later |

## 2. Bilingual table

| ID | Source (EN) | Target (<lang>) | Glossary terms used | Notes for the reviewer |
|---|---|---|---|---|
| | | | | |

Notes column: why a line was transcreated, where a length problem exists, where a term is new and needs approval.

## 3. Glossary additions

| Term (EN) | Rendering | Translate / transliterate / keep | Approved by | Date |
|---|---|---|---|---|
| | | | | |

## 4. Mechanical check

```
$ python3 scripts/glossary_check.py strings.json
RESULT: PASS (0 errors, n warnings)
```

Accepted warnings and why:

## 5. Length flags

| ID | Source chars | Target chars | Ratio | Allowance | Where it sits | Action |
|---|---|---|---|---|---|---|
| | | | | | | |

## 6. Needs a native reviewer

| Section | Language | Risk if unreviewed |
|---|---|---|
| | | |

## 7. What I could not verify

- Source not final: <what may change>
- Glossary unapproved for: <terms>
- Strings not rendered in the product, so overflow is predicted, not seen:
