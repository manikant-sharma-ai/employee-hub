# Ticket mining

The list of what to write is the strategy. Everything else is typing.

## From export to clusters

1. **Take 100-500 tickets**, last 90 days, closed, with the first customer message.
2. **Strip the surface.** Order numbers, names, product names, and greetings go. What is left is the cause.
3. **Group by cause, not by keyword.** "Payment failed", "money debited but no order", "OTP not received" look similar and are three different articles.
4. **Name each cluster as a customer would say it.** The name becomes the title later, so spend the time here.
5. **Count** tickets in the cluster, and the **median handling time** in minutes.
6. **Multiply**: tickets per month × minutes = minutes saved per month if the article deflects half of them.

| Cluster | Tickets/month | Median handling (min) | Minutes/month | In top five? |
|---|---|---|---|---|
| Money debited, order not confirmed | 84 | 11 | 924 | Yes |
| Refund not received after 7 days | 61 | 9 | 549 | Yes |
| Cannot change delivery address | 44 | 6 | 264 | Yes |
| Invoice with GST number | 38 | 12 | 456 | Yes |
| App crashes on Android 12 | 22 | 18 | 396 | Yes - but see below |
| How to apply a coupon | 19 | 4 | 76 | No |
| Want to cancel subscription | 12 | 15 | 180 | No - needs a product fix |

The last two rows are the discipline: a low-volume cluster with a high handling
time can outrank a high-volume one, and a cluster that is really a product bug does
not get an article - it gets a ticket to engineering.

## What does not become an article

| Ticket type | Why not | Where it goes |
|---|---|---|
| A bug with no workaround | The article would document the bug | `qa-tester`, then engineering |
| A policy decision | It changes; the article becomes wrong | The owner of the policy, in writing |
| A single customer's special case | It teaches 10,000 people an exception | Support macro, not help centre |
| A question about a feature that does not exist | It advertises a roadmap item | Sales or product, honestly |
| Anything that needs a person's judgement | An article cannot decide | Support, with a named escalation |

## The top five, and why not more

An article costs 1-3 hours to write, review and publish, and 30 minutes a quarter
to keep true. Eight articles is a quarter's maintenance load for a small team.
Choose by minutes saved per month, not by how annoying the question is.

A working rule: if a cluster is under 10 tickets a month and under 5 minutes to
handle, it is a macro, not an article.

## Reading the exports for what customers actually say

- **The first sentence** is the customer's mental model. Use their nouns.
- **The second message** is the real question, after the first answer failed.
- **Repeat contacts** on the same order are the strongest signal: the answer exists and does not work.
- **Channel matters.** WhatsApp messages are shorter and more frustrated; email is longer and more polite. Write for the shorter one.
- **Language.** If 20% of tickets are in Hindi or Hinglish, the help centre needs those articles, not a translation of all of them. Start with the top three clusters.

## The zero-result search report

Before writing, pull the help centre's searches with no clicks. That list is
customers telling you what they looked for and did not find. It outranks ticket
volume for the first batch, because those people already tried self-service.

## Anti-patterns

- **Writing from the product team's list of features.** It produces articles nobody searches for.
- **Clustering by tag.** Tags are applied after the fact by tired people and are inconsistent.
- **A cluster of one.** One ticket is a person, not a pattern.
- **Counting tickets without handling time.** The loudest problem is rarely the most expensive one.
- **Ignoring the resolution field.** The fix is already written in the ticket; the article is mostly editing.
