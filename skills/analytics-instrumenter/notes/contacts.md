# Contacts

| Who | For | How | Notes |
|---|---|---|---|
| <Implementing developer> | Event code, trigger fixes | | Needs the plan before the sprint, not after |
| <Analytics account owner> | Property IDs, admin access, data streams | | The person who can see volumes |
| <Warehouse / data owner> | Server-side events, reconciliation | | Owns the source of truth |
| <Privacy / consent owner> | DPDP basis, consent banner, retention | | Approves any new property with personal data risk |
| <Dashboard reader, per page> | What the page must answer | | One named reader per dashboard |
| <finance-ops> | Gateway settlement for reconciliation | | The money truth to compare against |

## Rules

- One owner per event. An event with no owner stops firing silently.
- Record who has admin access to the analytics property; it is a security surface.
