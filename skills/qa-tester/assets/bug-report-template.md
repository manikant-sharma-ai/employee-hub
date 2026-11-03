# Bug report - <one line: what breaks, where, under what condition>

| Field | Value |
|---|---|
| ID | BUG-<n> |
| Severity | 1 / 2 / 3 / 4 - impact on the user and the business |
| Priority | set by the release owner, not the reporter |
| Frequency | always / 1 in <n> / seen once |
| Build | <commit SHA>, <version> |
| Environment | staging / production, <URL> |
| Reported | <date, time IST> |
| Reporter | <name> |

## 1. Environment detail

| | |
|---|---|
| Browser and version | |
| OS and device | |
| Screen size | |
| Network | wifi / 4G / throttled |
| Account and role | test account only - never a real customer |

## 2. Steps to reproduce

From a fresh state, including the click that starts it.

1. 
2. 
3. 

## 3. Expected

<what should happen>

Written down where: <acceptance criterion, spec section, or "not specified">

## 4. Actual

<what did happen, in the same terms>

```
<error text, verbatim>
```

## 5. Evidence

- Screenshot / recording: <link, with URL and timestamp visible>
- Request: `<METHOD> <path>` -> `<status>`
- Response body: <relevant part>
- Trace ID / log line: <verbatim>

## 6. Impact

Who is affected, how many, and what it costs them or the business. One or two lines.

## 7. Workaround

<none, or the steps a user can take>

## 8. Suspected area

<only if you have evidence - a file, a component, a recent change. Otherwise "unknown">

## 9. Test this defect earns

One line, added to the regression suite: `<test name> - <what it asserts>`
