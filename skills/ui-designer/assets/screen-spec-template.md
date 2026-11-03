# Screen spec - <flow name>

**Version:** 1.0  **Date:** <YYYY-MM-DD>  **Designer:** ui-designer
**Platform:** responsive web / Android / iOS  **Breakpoints:** 360, 390, 768, 1024, 1280

## The job

<One line: who, on what screen, finishing what, in how long.>

## The flow

1. Entry: <where from>
2. Screen 1 - <name>  exits: continue -> 2 / back -> entry / error -> 1 error state / cancel -> <where>
3. Screen 2 - <name>  exits: ...
4. Success - <what it says, what is next>

## States

| Screen | State | What is shown | Copy | Action |
|---|---|---|---|---|
| 1 | loading | skeleton | - | - |
| 1 | empty (first use) | | | |
| 1 | error | | | retry |
| 2 | no permission | | | request access |

## Scale in use

| Token | Value | Where |
|---|---|---|
| space-md | 16 | padding inside cards |
| type-body | 16/1.5 | default text |
| color-primary | <hex / variable> | primary button |

## Components

| Name (as in code) | Variants needed | Notes |
|---|---|---|
| Button | primary, secondary, ghost, disabled, loading | |

## Copy - final

| Key | String | Max chars |
|---|---|---|
| cta.pay | Pay Rs. 499 | 20 |
| error.payment | Your payment did not go through. No money was deducted. Try again. | 90 |

## Behaviour

- Tap primary: <what happens, what is disabled while waiting>
- Back: <where, what is preserved>
- Slow network: <what is shown, after how long>
- Long text: <truncate at n lines, ellipsis>
- Second language: <what grows, what wraps>

## The one thing that must not break

<e.g. the amount and the pay button must stay visible with the keyboard open>

## Open questions

1. <question> - recommendation: <...>
