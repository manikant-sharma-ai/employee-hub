# Ticket to article

The queue is the specification. This file turns a pile of conversations into a
ranked list of articles worth writing.

## The export you want

| Field | Why |
|---|---|
| Ticket id | Counting and de-duplication |
| Created date | Seasonality, and whether the topic is growing |
| Subject | The customer's own words for the search |
| First message | The question, before any agent shaped it |
| Resolution | The answer that actually worked |
| Category or tag | Only if the team tags consistently - usually they do not |
| Channel | Email, chat, WhatsApp, marketplace: each has a different tone |
| Order or account value | Cost of the topic, so you can rank by money and not by noise |

Thirty tickets is enough to find a pattern; three hundred is enough to rank it.

## Grouping, the right way

Group by **the question being asked**, in the customer's words. Not by product
area, not by the tag the agent chose.

| Grouping that fails | Grouping that works |
|---|---|
| "Billing" (400 tickets, no action) | "Where is my refund" (96), "GST number wrong" (61), "Card declined" (44) |
| "Account" | "Cannot log in, OTP not arriving" (73), "Change the email on my account" (38) |
| "Product" | "How do I add a second user" (52), "Why is stock showing zero" (47) |

A good group has a title you could publish as-is, and every ticket in it would be
answered by the same article.

## Ranking the topics

Score each group, then sort.

| Factor | Weight | How to score |
|---|---|---|
| Volume | 40% | Tickets in the last 90 days |
| Cost per ticket | 25% | Handle time x loaded agent cost, or the refund value at stake |
| Self-service potential | 20% | Can this be answered without an account-specific check? |
| Growth | 15% | This quarter against last: rising topics are worth more than stable ones |

Self-service potential is the one that gets ignored. A question that needs an
order lookup - "where is my order" - cannot be deflected by an article alone; it
needs a tracking page. Write the article anyway, but expect it to reduce a
fraction, and say so rather than promising a 40% deflection.

## The five article types you will find in any queue

| Type | Signal in the tickets | What to write |
|---|---|---|
| How-to | "How do I...", repeated steps | A numbered how-to |
| Policy | "Can I still...", "what is your...", a date in the answer | A policy page with a table, and the policy owner's name behind it |
| Troubleshooting | "It is not working", "it says error" | A decision tree with the three commonest causes first |
| Timing | "When will...", "how long does..." | A table of timelines, per case, with the exceptions |
| Pre-purchase | "Do you support...", "can it do..." | A capability page, linked from the pricing page |

## Reading the resolution, not the question

The question tells you the topic; the resolution tells you the truth.

- **The agent's first reply is often wrong** and corrected later in the thread. Read to the end.
- **The workaround is the valuable part.** "We cannot do it in the app, but here is the web link" is exactly what an article must say.
- **Repeated escalations mean a policy gap**, not a writing gap. Route those to the owner in a list, separately, rather than writing an article that promises an exception.
- **A ticket resolved by a phone call** has no written answer, so interview the agent for the steps before you write.

## The gap log

One sheet, five columns, refreshed monthly.

| Topic (customer words) | Tickets (90d) | Handle time or cost | Article exists? | Status |
|---|---|---|---|---|
| Where is my refund | 96 | 11 min | No | Writing |
| GST number wrong | 61 | 7 min | Outdated | Rewrite |
| Cannot log in, OTP | 73 | 9 min | No | Needs product fix first |
| Add a second user | 52 | 6 min | Yes, ranks badly | Retitle |
| Card declined | 44 | 5 min | No | Writing |

The log is the deliverable that gets the work approved. An article list without
counts is an opinion about what customers want.

## The first hour on a new queue

1. Export 90 days.
2. Read 30 tickets end to end, in order. Not skim - read. The tone, the confusion and the vocabulary are all in there.
3. Write down every question in the customer's words, as a list.
4. Cluster into eight to twelve topics. Name each as a search.
5. Rank, and check each against the existing help centre.
6. Propose the top five, with counts and the one-line outcome. That is the batch.

## Anti-patterns

- **Writing from the product documentation.** It answers the question the product team asked, in nouns the customer has never seen.
- **Trusting the ticket tags.** They are applied under time pressure and are usually a product area, not a question.
- **Writing all twelve topics at once.** Five good articles with review dates beat twelve drafts nobody approves.
- **Skipping the tickets that were closed by phone.** They are the invisible half of the queue.
- **Treating an angry ticket as a tone problem.** It is usually a timing or policy problem, and the article must state the timing honestly.
