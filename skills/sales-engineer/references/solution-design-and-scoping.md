# Solution design and scoping

A solution design is not an architecture diagram. It is a commitment, written in a form the buyer
can agree to and the delivery team can be held to.

## The one-page design

| Block | Content |
|---|---|
| **The problem** | Their words, one sentence, with the measurable cost of it |
| **The picture** | One diagram: their systems, the product, the data flows, the actors |
| **How it works** | Five to seven numbered steps, in their workflow order |
| **What changes for a user** | Before and after, for each role affected |
| **Scope** | The list of what is included, as deliverables |
| **Out of scope** | The list of what is not, written as explicitly as the scope |
| **Effort** | A range per workstream, with assumptions |
| **Dependencies** | What the client must provide, and by when |
| **Risks** | Each with a likelihood, an impact and a mitigation |
| **Success measure** | How both sides will know it worked |

If it does not fit on one page, the scope is not understood. The annexures can carry detail; the
page carries the commitment.

## Scope, written as deliverables

| Good scope line | Bad scope line |
|---|---|
| "Two-way sync of item master and stock, every 15 minutes, for 4,200 SKUs" | "Integration with ERP" |
| "Invoice creation from a confirmed order, with GST fields mapped to their chart" | "Billing integration" |
| "Dashboard with 8 defined metrics, refreshed daily by 07:00" | "Reporting" |
| "Migration of open items and master data; history not migrated" | "Data migration" |

Every line has a **thing**, a **volume** and a **frequency**. Anything without all three will be
argued about at delivery.

## Out of scope, the list that saves the project

| Usual exclusion | Why it must be written |
|---|---|
| Historical data beyond a stated period | It is the largest hidden effort in any migration |
| Custom reports beyond the defined eight | Every stakeholder has a ninth |
| Changes to their ERP or its master data quality | Not your system, not your fix |
| Third-party licences (iPaaS, storage, SMS) | A cost the client must own |
| Training beyond two sessions | Scope creep's favourite door |
| On-premise deployment or a private cloud | Changes the architecture entirely |
| Support outside business hours | Becomes an implicit SLA |
| Regulatory certification for their jurisdiction | A legal commitment, not a feature |

## Effort estimation, in ranges

| Workstream | Basis | Typical range |
|---|---|---|
| Configuration and setup | Days per environment | 2-5 days |
| Data mapping | Fields × complexity | 1-3 days per system |
| Migration | Records, exceptions, reconciliation | 3-15 days |
| Integration | Surface type, from the discovery table | 2-20 days |
| Testing and UAT support | 25-40% of build effort | - |
| Training and handover | Sessions and material | 2-4 days |
| Contingency | By risk, not by habit | 15-25% |

Rules: give a range, name the assumption behind the low end and the high end, and state what would
push it beyond. A single number is a promise you will break.

## The risk register, four lines that matter

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Their API is undocumented or rate-limited | Medium | High | Spike it in week one, before the POC | You |
| Master data is dirty | High | High | A data quality report as a paid first step | Client |
| The decision-maker changes | Medium | High | Written criteria and a named sponsor | Sales |
| A custom requirement appears in UAT | Medium | Medium | A change-request route agreed upfront | Both |

## Handover to delivery

The design must be usable by the person who implements it:

| Include | Because |
|---|---|
| The environment map with versions | Otherwise week one is discovery again |
| Field-level mapping for the main entities | The most common cause of a rework |
| The named client owners and their availability | Dependencies fail on people, not technology |
| The acceptance criteria as tests | "Done" must be checkable |
| The known gaps and their workarounds | Otherwise they are discovered as defects |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| Scope with no out-of-scope list | Every exclusion becomes an argument at delivery |
| A single-number effort estimate | It is treated as a fixed price and a fixed date |
| Architecture with no data mapping | The build starts by redoing discovery |
| A design written for the buyer, not the builder | Delivery re-scopes, and the promise slips |
| Risks with no owner | The register becomes decoration |
| "Phase 2" used to hide the expensive half | The buyer discovers it and the trust ends |
| No success measure | Nobody can say whether it worked, so nobody renews |
