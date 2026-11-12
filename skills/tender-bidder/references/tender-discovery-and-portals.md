# Tender discovery and the portals

Government demand is published, which means the work is not finding it - it is filtering it. This file
is the filter.

## Where the tenders are

| Portal | What it covers | How to use it |
|---|---|---|
| GeM (gem.gov.in) | Central and state buyers buying catalogue and custom items | Category browse, bid search, seller catalogue; the largest single source for goods |
| CPPP / eprocure.gov.in | Central ministries, PSUs, autonomous bodies | Keyword and organisation search, tenders by product category |
| State e-procurement portals | State departments, local bodies, state PSUs | Each state has its own; registration is separate |
| PSU and defence portals | Large PSUs and defence procurement | Often their own registration and vendor approval |
| Indian Railways (IREPS) | Railway stores and works | Separate registration and vendor approval |
| Co-operative and institutional buyers | Universities, hospitals, housing societies | Often not on a portal at all; the website or a notice board |

## The search that works

Search by what the buyer calls the item, not by what the business calls it. "Office chair" finds four
tenders; "executive revolving chair, mesh back, gas lift" finds the one that matters. Keep a keyword
list per product family with the buyer's vocabulary, HSN code and synonyms, and run it weekly.

| Filter | Why it removes the noise |
|---|---|
| Category and HSN | Removes 80% of the irrelevant results |
| Value band | Below the effort threshold, above the capacity ceiling |
| Geography | Delivery and installation distance decide the margin |
| Buyer type | A repeat buyer beats a new one; a state department beats a one-off society |
| Bid type | Direct purchase, L1, bid with reverse auction, custom bid - each needs a different price |
| MSE exemption | A tender restricted to MSEs removes the large competitors entirely |

## Reading a notice, in this order

1. **Bid end date and time, in IST**, and whether it is extended. Screenshot it.
2. **The item and the specification** - is it a catalogue item or a custom specification, and does the
   business actually make or supply exactly that.
3. **Eligibility criteria** - OEM or dealer, turnover, past performance, certifications, registrations.
4. **Evaluation method** - L1, QCBS, or a technical-plus-commercial split, and the minimum technical
   score.
5. **EMD, tender fee, PBG** - amount, instrument, and the MSE or startup exemption.
6. **Delivery period, delivery point, LD clause, payment terms** - this is where the margin lives.
7. **ATC and corrigenda** - the additional terms usually override the notice, and the corrigendum
   overrides both.
8. **The buyer's contact and the clarification window** - ask early, in writing, and keep the reply.

## The weekly rhythm

Monday: run the saved searches, log new matches in the bid register. Tuesday-Wednesday: eligibility
grids on the shortlist. Thursday: go/no-go. Friday: packs for the ones that passed. A tender discovered
with two days left is a tender bid badly or not at all.

## Anti-patterns

- **Searching by product name only.** The buyer's vocabulary is not the seller's.
- **Ignoring corrigenda.** A date extension or a specification change that goes unread loses the bid.
- **Bidding everything under the value band.** Ten bad bids cost more than two good ones.
- **Registering on the portal the week a bid is due.** Registration and DSC mapping take days.
- **Skipping the clarification window.** The answer to "is a dealer bid allowed" decides the whole bid.
- **No bid register.** Without one, the same unsuitable tender is rediscovered every month.

## The bid register

One row per tender considered, and it is the only memory this function has:

| Column | Why |
|---|---|
| Tender ID, portal, buyer | Identity, and the route back to the notice |
| Item, category, quantity, value | The match test |
| Bid end date and time (IST) | The hard constraint |
| Eligibility verdict | Met, not met, unverified |
| Go / no-go and reason | The decision, and who made it |
| Effort in person-days | The cost of the bid |
| Submitted on | Proof against the 24-hour rule |
| Outcome and reason | Technical, L1, lost, cancelled |
| Debrief note | What to change next time |

After twenty rows the register stops being a log and becomes a strategy: the categories that qualify,
the buyers who pay, and the tenders that were never worth reading.
