# Send brief and copy - <campaign name>

Date: <date> | Owner: <name> | Platform: <ESP> | Send window: <date, time IST>

## 1. The brief

| Field | Answer |
|---|---|
| The one job | sell / teach / announce / re-engage / ask - pick one |
| Segment | who exactly, and how these addresses consented |
| Size | <n> addresses, <n> after hygiene pass |
| The one action | what the reader does, and where it lands |
| Success number | clicks on the primary link, or replies, or orders |
| Cadence and exit | if part of a sequence: days, and what ends it |
| What is compared against | the last send to this segment, with its numbers |

## 2. Subject and preview

- **Subject** (38-50 chars, hard limit 60): 
- **Preview** (40-90 chars, continues the subject, does not repeat it): 
- **Sender name** (a person, not the company): 

## 3. Body

> First line continues the subject. No "hope you are well".

<80-150 words, one idea, one primary link>

<proof: a number, a name, a date - something checkable>

<sign-off from a person, reply-able address>

[ Primary button: <label> -> <url> ]

## 4. Plain text version

```
<the same email, no images, links as bare URLs, unsubscribe as a sentence with a link>
```

## 5. Footer

- Sender identity: <registered name, postal address>
- Unsubscribe: one click, honoured within 48 hours
- Preference centre: <link, if it exists>

## 6. Lint

```
$ python3 scripts/sequence_linter.py sequence.json
RESULT: PASS (0 errors, n warnings)
```

Accepted warnings and why:

## 7. Measurement plan

| Metric | Last send | This send | What it decides |
|---|---|---|---|
| Delivered | | | list health |
| Click rate (of delivered) | | | the real signal |
| Unsubscribes | | | promise drift |
| Complaints | | | stop and fix |
| Revenue attributed (last click) | | | whether to repeat the angle |

Read at 72 hours. Decision rule written before sending: <if X, then Y>.

## 8. What I could not verify

- Platform not connected, so list size and past performance are unconfirmed.
- Consent for this segment: <confirmed from which source, or unknown>.
