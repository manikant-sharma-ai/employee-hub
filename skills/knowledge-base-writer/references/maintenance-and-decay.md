# Maintenance and decay

A help article starts dying the day it is published. This file is the review that
keeps it true, and the rules for retiring what no longer applies.

## The decay clock

| Article type | Decays when | Review every |
|---|---|---|
| How-to with screenshots | Any UI change | 90 days, or on every release that touches the screen |
| Troubleshooting | Error messages, platform versions change | 90 days |
| Policy | The policy changes, quietly | 180 days, or on any policy change |
| Reference tables (timelines, fees) | Rates and SLAs change | 90 days |
| Getting started | Onboarding flow changes | 180 days |

A product release that changes a screen must list the articles it invalidates.
That checklist item belongs in the release, not in the writer's memory.

## The review, in 15 minutes per article

1. Open the product and follow the steps as written. Do they work, in this order?
2. Check the screenshots against the current UI. Dated or replaced.
3. Check every number: timelines, fees, limits, SLAs.
4. Read the first two lines. Is the answer still the answer?
5. Check the links - two internal, no 404s.
6. Update the "last reviewed" date and the owner. If nothing changed, the date still moves.

An article reviewed without opening the product is a guess with a fresh date on it.

## What to do when the product changes

| Change | Action |
|---|---|
| A button moved | Update screenshots and step text; no rewrite |
| A flow changed | Rewrite the steps; check the failure path |
| A feature was removed | Retire the article with a redirect to the closest survivor |
| A policy changed | Rewrite, add "updated on", tell support before publishing |
| A bug became permanent behaviour | Rewrite honestly, and log the product decision |

## Retiring an article

Never delete. Retire:

1. **Redirect** to the closest live article, or to the category page.
2. **Keep the URL** for at least 12 months - support macros and emails point at it.
3. **Log the retirement** with the date and the reason in the journal.
4. **Check the traffic first.** An article with 200 views a month is telling you something, even if it is out of date.

## Ownership

Every article carries three fields: **owner** (a person, not a team), **last
reviewed** (a date), and **applies to** (product version or plan, where it matters).

An article with no owner is reviewed by nobody, and the person who reads it next is
a customer who will act on the wrong instructions.

## The quarterly sweep

Once a quarter, 90 minutes:

| Check | Output |
|---|---|
| Articles not reviewed in 180 days | A list, ranked by traffic |
| Zero-result searches | Three new articles or three title changes |
| Top ten articles by traffic | One improvement each, or a note that it is fine |
| Articles with no owner | Assign or retire |
| Duplicate clusters | Merge, with a redirect |

## Anti-patterns

- **"We will review it next quarter."** The date is the mechanism; without it nothing happens.
- **A big rewrite every 18 months.** It is expensive, it breaks links, and it teaches nobody.
- **Screenshots with no date.** The reader cannot tell whether they are current.
- **Retiring by deletion.** Every external link and macro now 404s.
- **The writer owning 180 articles alone.** Owners sit with the team that answers the ticket.
- **Reviewing without testing the steps.** The most common way a wrong article survives.
