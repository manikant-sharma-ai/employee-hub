# Maintenance and decay

Help content is wrong by default. The product ships, the interface changes, the
policy moves, and every article written last year is a small liability.

## The review cycle

| Article type | Review every | Trigger for an early review |
|---|---|---|
| How-to with screenshots | 3 months | Any UI change, any rename |
| Troubleshooting | 3 months | A new error message, a fix shipped |
| Policy and pricing | 6 months, or on change | Any policy decision |
| Timing tables | 6 months | A courier, gateway or bank change |
| Getting started | 6 months | Onboarding change |
| Archived | Never, but dated | - |

Every article carries three fields at the bottom: **last reviewed**, **owner**,
**next review**. An article without them is already decaying.

## The monthly maintenance hour

1. Pull the list of articles past their review date. Sort by views.
2. Open the top ten. Check each step in the live product, on a customer account.
3. Fix or flag. A step that cannot be verified gets a note to the product owner, not a guess.
4. Check the broken links report. Fix or redirect.
5. Check the zero-result searches and the new tickets for a topic that has no article.
6. Update the review dates, and log the batch in the journal.

One hour a month keeps a help centre of a hundred articles honest. Without it, the
centre is 40% wrong within a year.

## Signs an article needs rewriting, not editing

| Sign | Rewrite or edit |
|---|---|
| The answer changed | Edit |
| The steps changed but the question is the same | Edit, and re-screenshot |
| The question is now asked differently | Rewrite the title and the opening |
| Two articles now cover it | Merge |
| Nobody reads it and nobody asks the question | Archive with a dated note |
| It is accurate but nobody finds it | Retitle, re-link, do not rewrite the body |

## Retiring an article

- Archive, do not delete. Old emails, chat threads and search results point at it.
- Put one line at the top: "This article is out of date. See <new article>."
- Redirect the URL if there is a replacement, and keep the redirect for a year.
- Remove the links from the hub pages, so nobody lands on it by browsing.
- Note the retirement in the journal, with the reason.

## Versioning, when the product has plans or regions

| Situation | Approach |
|---|---|
| Same flow, different plan | One article, a table of what differs by plan |
| Same flow, different region | One article, a region table - unless the flow itself differs |
| Genuinely different interface | Separate articles, cross-linked, titled by the product name the customer sees |
| Beta feature | One article, clearly marked beta, with the date it becomes general |

Duplicating an article per plan is how a help centre reaches 400 pages that all
say the same thing slightly differently.

## When the product team ships without telling you

This is the normal case, not the exception. Defend against it:

1. Ask for a standing weekly note of what shipped - one line per change is enough.
2. Watch the ticket queue for a spike in a topic. A spike in an old topic is a shipped change.
3. Keep a "changed but undocumented" list, with the date, and send it weekly.
4. Put the release notes page in the help centre, and make the product team own the content of it.

## The style sheet

Keep one page, versioned in the repo, with the decisions that get argued about:

- Product names, capitalisation, and what to call the customer.
- Currency and number format: ₹1,20,000 and not ₹120,000, for an Indian audience.
- Dates: 7 Nov 2026, never 11/07/26.
- The words banned: simply, just, easy, obviously, unfortunately.
- Screenshot standard: crop size, annotation colour, sample data policy.
- Reading level: plain, short sentences, no jargon that the interface does not use.

A style sheet settles the same argument once a quarter instead of once a week.

## Anti-patterns

- **A big annual rewrite.** It never happens, and meanwhile everything is wrong.
- **Screenshots with no date.** You cannot tell whether they are current, so nobody checks.
- **Deleting old articles to "clean up".** You break every link in every old mail.
- **No owner per article.** Shared ownership is no ownership.
- **Rewriting the body when the title was the problem.** The reader never got that far.
