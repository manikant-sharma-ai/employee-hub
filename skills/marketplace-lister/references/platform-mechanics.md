# Platform mechanics

Four platforms, four different buyers. The same product needs a different listing on each,
and the first decision is which buyer you are trying to reach.

## The comparison

| | IndiaMART | Amazon.in | Flipkart | GeM |
|---|---|---|---|---|
| Buyer | Bulk B2B, traders, procurement | Consumer and small business | Consumer, price-led | Government departments |
| Discovery | Search + seller response | Search, filters, ads | Search, filters, ads | Search by category, bid |
| Unit of work | Product + seller response | Listing + buy box | Listing + buy box | Catalogue + bid participation |
| Fee model | Subscription + lead credits | Referral + closing + FBA/storage | Commission + shipping + collection | Transaction fee, EMD for bids |
| Price competition | Medium, relationship matters | High, buy box decides | Very high, price-led | Low price, high compliance |
| Content that wins | Specifications, capacity, certifications | Title, images, reviews, A+ | Title, images, price, offers | Specs, eligibility documents, delivery terms |
| Time to first enquiry | Days, with a good catalogue | Weeks, needs reviews | Weeks, needs reviews | Weeks, needs a live bid |
| Returns risk | Low, negotiated | Medium, RTO on COD | High, RTO on COD | Low, but penalty clauses |

## IndiaMART - the B2B catalogue

- The listing is a **catalogue entry plus a seller response**. Buyers send enquiries; the
  speed and quality of the reply decides the sale as much as the listing does.
- **Specifications carry the search.** Capacity, material, grade, size range, power rating,
  certification. A buyer searching "MS pipe 2 inch 6 metre" filters on attributes.
- **Company profile matters.** Years in business, certifications, factory address, response
  rate. A thin profile loses to a complete one at the same price.
- **Lead credits are the real cost.** A listing that attracts unqualified enquiries burns
  credits. Write the specification tightly to filter.
- **Best for:** industrial goods, components, packaging, machinery, bulk commodities,
  anything sold to a business that will ask for a quote.

## Amazon.in - the consumer catalogue

- **Search decides everything.** The title and backend keywords are indexed; the main
  image and price decide the click; reviews and A+ content decide the conversion.
- **The buy box** is won by a combination of price, fulfilment (FBA vs self-ship),
  availability and account health. A listing without the buy box sells almost nothing.
- **Fees stack**: referral (category-dependent), closing fee (price slab), weight-based
  shipping, storage, and a returns provision. Model all of them before setting a price.
- **Variations** (size, colour) belong in one parent listing. Splitting them creates two
  weak listings instead of one strong one.
- **Best for:** branded consumer products with reviews, and anything a buyer will compare
  on a phone.

## Flipkart - price-led consumer

- Similar mechanics to Amazon with a sharper price focus and different fee slabs.
- **Flipkart Advantage / F-Assured** improves visibility and needs fulfilment discipline.
- **Offers and bank discounts** move volume; the seller pays for part of them.
- **Returns and RTO are the margin killer**, especially on COD. Model a return rate per
  category, not a company average.
- **Best for:** value-led consumer goods, fashion, accessories, large appliances where
  price comparison is the purchase behaviour.

## GeM - the government marketplace

- **A bid, not a listing.** You catalogue the product, then participate in bids; L1 price
  usually wins, with eligibility checked first.
- **Eligibility is the gate**: MSME/Udyam status, OEM or reseller authorisation,
  turnover thresholds, certifications, and sometimes a local-content declaration.
- **EMD and performance security** are real cash commitments; a bid without the EMD ready
  is a bid you will lose.
- **Delivery terms and penalties are contractual.** A late delivery on GeM is a penalty,
  not a bad review.
- **Best for:** manufacturers and authorised resellers with the paperwork in order.
  Discovery and eligibility for tenders is `tender-bidder` (backlog #121); this role writes
  the catalogue entry and the product content that a bid refers to.

## Choosing, in one table

| Situation | Platform |
|---|---|
| Selling fasteners to factories | IndiaMART, and GeM if you can meet eligibility |
| Selling a branded consumer product | Amazon.in first, Flipkart second |
| Selling a commodity where price is the only difference | Flipkart, with a hard look at the return rate |
| Selling to government departments | GeM, with `tender-bidder` for discovery |
| Selling both B2B and D2C | Two listings, two titles, two price points - never one |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| One title for all four platforms | It is written for none of them |
| Consumer copy on IndiaMART | Buyers want specifications and capacity, not benefits |
| B2B copy on Amazon | The consumer cannot tell what the product is |
| Ignoring buy box mechanics | A live listing that never sells |
| Listing on GeM without EMD ready | A lost bid and a damaged seller rating |
| Same price everywhere | Each platform's fee stack is different; one of them is a loss |
