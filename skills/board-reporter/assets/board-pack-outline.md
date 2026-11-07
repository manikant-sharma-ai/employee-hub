# Board pack outline - <meeting date>

**Meeting:** <statutory board / advisory board> | **Date and time:** <date, time, IST>
**Attendees:** <names and roles> | **Quorum required:** <n>
**Papers due:** <date, seven days before> | **Pack owner:** board-reporter

## 1. The decisions being asked for

| # | Decision | Owner of the paper | Resolution wording | Pages |
|---|---|---|---|---|
| D1 | <the ask in one line> | <name> | "RESOLVED that ..." | <n> |
| D2 | | | | |
| D3 | | | | |

_If there are more than three, say why. More than five is a sign the meeting is
carrying decisions that belong to management._

## 2. Chair's summary (page 1)

- **Three numbers that moved:** <metric> <actual> (<movement> vs <comparison>) - <one clause why>
- **Note to board:** <what happened that is not being decided>
- **Bad news:** <in the first half of the page>
- **Deferred:** <what is deliberately not being asked, and when it returns>

## 3. Section plan

| # | Section | Owner | Pages min | Ready | Blocked on |
|---|---|---|---|---|---|
| 1 | Chair's summary | founder | 1 | y | - |
| 2 | Decisions required | <owners> | 2 | | |
| 3 | Financial pack | finance-ops | 4 | | |
| 4 | Trading and operations | mis-reporter | 3 | | |
| 5 | People | hiring-manager | 1 | | |
| 6 | Risk and compliance | compliance-watch | 1 | | |
| 7 | Actions and governance | board-reporter | 1 | | |

Generate the page allocation and the gap list with:

```
python3 scripts/pack_planner.py pack-spec.json --markdown
```

## 4. Provenance

| Figure | Value | Source | Pulled | Basis | Status |
|---|---|---|---|---|---|
| Revenue (Sep) | | Zoho Books P&L | | management | provisional |
| Cash at bank | | bank statement | | actual | - |
| Runway | | derived | | management | - |

## 5. Actions carried forward

| ID | Action | Owner | Opened | Due | Meetings open | This meeting |
|---|---|---|---|---|---|---|
| A-0xx | | | | | | close / re-date / decide |

## 6. After the meeting

- [ ] Minutes drafted within 5 working days
- [ ] Action register updated the same day
- [ ] Resolution log updated
- [ ] Next meeting's paper deadline in the calendar
- [ ] Late papers noted in the record
