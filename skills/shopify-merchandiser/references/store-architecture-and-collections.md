# Store architecture and collections

A catalogue is not a stock list. It is an argument about what belongs together, and a shopper
either follows the argument or leaves.

## The rule that decides everything

**One collection = one reason to buy.** Not one category, not one fabric, not one price band - a
reason. "Under ₹999 gifting for colleagues" is a reason. "Cotton" is a filter.

| Collection type | Rule | Sorts by | Example |
|---|---|---|---|
| **Hero / bestseller** | Top 12 by 60-day revenue, in stock | Manual | "Most loved" |
| **Category** | Product type | Bestselling | "Kurtas" |
| **Occasion** | Use case | Bestselling | "Work wear", "Festive" |
| **Price band** | Under a round number | Price ascending | "Under ₹999" |
| **New** | Published in the last 30-45 days | Newest | "New in" |
| **Bundle / set** | Products designed to be bought together | Manual | "The complete desk set" |
| **Clearance** | Aged stock, end of line | Discount descending | "Last few" |

Anything else is a filter, not a collection. Filters belong in the theme's filter panel, not in
the navigation.

## How many collections

| Catalogue size | Collections | Navigation depth |
|---|---|---|
| Up to 30 SKUs | 4-6 | Flat, one level |
| 30-150 | 8-12 | Two levels |
| 150-600 | 12-20 | Two levels plus filters |
| 600+ | 15-25, filters do the work | Two levels plus a strong search |

Overlapping collections are not a problem if each has a distinct entry point. They are a problem
when three collections contain the same eight products and the home page features all three.

## Sorting rules that earn money

| Collection | Sort | Why |
|---|---|---|
| Hero | Manual, curated monthly | Control the story |
| Category | Bestselling, with in-stock first | Social proof at the top |
| New in | Newest first | The point of the collection |
| Price band | Price ascending | The shopper is price-led |
| Clearance | Discount % descending | The shopper is bargain-led |
| Search results | Relevance, then bestselling | Relevance alone surfaces dead stock |

Never leave a collection on "alphabetical" or "product name". It is the default nobody chose, and
it puts the worst-performing product first.

## Navigation, in the order a shopper uses it

```
Header:  Shop [mega menu] | New | Bestsellers | Sale | About | Help
Mega menu columns:  Category | Occasion | Price | Gifting
Footer:  Shipping and delivery | Returns | Size guide | Contact | Policies | Track order
```

Rules: no more than seven top-level items; the mega menu shows an image and three to five links
per column, not forty; "Sale" is a permanent item only if a sale is genuinely permanent (and then
it is not a sale); every policy page is one click from the footer, because its absence is a
checkout abandonment.

## The collection page itself

| Block | Content | Failure |
|---|---|---|
| Banner | One line of what this collection is for | A stock photo with no words |
| Sub-copy | 2-3 lines: who it is for, what makes it different | SEO stuffing nobody reads |
| Product grid | Image, name, price, one differentiator, quick add | Six lines of description in the grid |
| Sort and filter | Visible, above the grid on mobile | Hidden behind an icon nobody taps |
| Empty state | "Nothing here yet" plus a route to the hero collection | A blank page |
| Bottom copy | 150-250 words, useful, for search | The same paragraph on all 40 collections |

## Product placement rules

| Situation | Placement |
|---|---|
| Out of stock, coming back in 7 days | Keep in collection, badge it, offer a notify-me |
| Out of stock, no return date | Remove from hero and category; keep the URL alive |
| Slow mover, good margin | Put it in a bundle or a "complete the set" block |
| Slow mover, thin margin | Clearance, and stop buying it |
| New product, no reviews | Pair it with a hero in a "pairs well with" block |
| One size or colour left | Badge it; scarcity is honest here |
| A product that returns above 15% | Fix the page (fit, sizing, expectations) before promoting it |

## Anti-patterns

| Anti-pattern | Cost |
|---|---|
| 40 collections, 8 of them empty | Navigation reads as neglect |
| Every collection sorted alphabetically | The worst product is always first |
| Filters built as collections | Navigation grows, and the filter panel stays unused |
| A hero collection nobody curates | The founder's favourite outsells the actual bestseller |
| Out-of-stock heroes on the home page | Traffic lands on a dead end |
| The same eight products in four collections | The store looks smaller than it is |
| No collection-level copy | Category pages never rank, and shoppers get no orientation |
