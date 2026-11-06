# Writing for search

A help article has two readers: the person who opens it from a ticket reply, and the
person who types a phrase into the help centre's search box. The second one is the
one who never contacts you, and the one this file is about.

## The search box is the real test

Open the help centre, type the customer's phrase, and see what comes back. If the
article is not in the top three, it will not be read, however good it is.

| What the customer types | What the article is probably called | Result |
|---|---|---|
| "money deducted but no order" | "Payment gateway failure handling" | Not found |
| "refund kab aayega" | "Refund policy and timelines" | Not found |
| "change address" | "Modifying delivery details post-order" | Not found |
| "otp not coming" | "Two-factor authentication troubleshooting" | Not found |

The fix is not better search. It is the title and the first paragraph using the
words people actually type.

## Building the term list for one article

For each article, write down:

1. **The exact phrases from tickets** - copy them, do not paraphrase.
2. **The synonyms** - "refund / money back / credit", "address / location / delivery point".
3. **The Hindi and Hinglish variants** if that is how your customers write.
4. **The error messages**, verbatim, including the code if there is one.
5. **The feature name**, for the people who do know it.

Then place them: title, first sentence, and a short "Also known as" line if the
synonyms are genuinely different. Do not keyword-stuff; the help centre search is
usually a basic match, and three natural mentions beat twelve awkward ones.

## Internal links do the ranking work

| Link | Why |
|---|---|
| From the related how-to | A reader who is stuck in a flow is one click from the answer |
| From the policy page | The policy question always follows the how-to question |
| From the product's error screen | The best placement in the whole system, and the least used |
| From the support macro | The reply that says "here is how" should link, not explain |

Two links per article, maximum, chosen for the next question the reader will ask.

## The pages that are not help articles

| Page | Owner | Why not here |
|---|---|---|
| "How to file GST" landing page, written for Google | `seo-specialist` | Search intent is commercial, not support |
| A blog post about the feature | `content-writer` | It persuades; an article unsticks |
| A pricing or plan comparison | `content-writer` with `pricing-analyst` | It is a sales page |
| An internal runbook | `sop-writer` (backlog #91) | It is for staff, not customers |

If a help article starts ranking on Google for a commercial query, that is a signal
for `seo-specialist`, not a reason to make the article sell.

## Multilingual help centres

- **Translate the top five clusters, not all 200 articles.** Coverage of the questions that actually arrive beats uniform thin coverage.
- **Keep the title in the language the search is typed in**, and put the English term in the first line for the readers who search in English.
- **Do not machine-translate the steps without a check.** A mistranslated button name sends the reader to the wrong screen.
- **Hindi help content is often read in Roman script.** Include the Roman variant in the term list.

## Measuring findability

| Metric | Where | Good |
|---|---|---|
| Zero-result searches | Help centre analytics | Falling month on month |
| Search → click rate | Analytics | Above 40% for the top clusters |
| Article views per ticket | Analytics vs support desk | Rising for clusters you wrote |
| "Was this helpful" ratio | Widget | Above 70%, and read the comments |

A zero-result search is the cheapest piece of product feedback a business gets.
Log the phrase, the date and the cluster it belongs to.

## Anti-patterns

- **SEO thinking applied to a help centre.** Volume and keywords matter less than the exact phrase a stuck person types.
- **One giant FAQ page.** It ranks for nothing and answers nothing.
- **A category tree five levels deep.** Two levels, and search.
- **Titles generated from the feature name by the product team.**
- **No synonyms.** The customer and the product use different words for the same thing, always.
- **Ignoring the error message.** The exact string is what gets pasted into search.
