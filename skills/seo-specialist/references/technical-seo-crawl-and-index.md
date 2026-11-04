# Technical SEO: crawl, index, speed

Rankings are decided after the page is crawled and indexed. If either fails, no
amount of content or links helps. This is the layer to check before writing a brief.

## The four gates

| Gate | Question | Where to look |
|---|---|---|
| Crawlable | Can the bot reach the page? | robots.txt, internal links, JS rendering |
| Indexable | Is it allowed in the index? | meta robots, canonical, status code |
| Understandable | Does the page say what it is about? | title, H1, structured data |
| Fast enough | Does it load before the user leaves? | Core Web Vitals, server response |

## The checks that find real problems

- **`site:` search** - is the page in the index at all, and how many pages are indexed against how many exist?
- **Search Console Coverage** - "Excluded" reasons are the honest list: `noindex`, canonical mismatch, soft 404, duplicate.
- **Canonicals** - one canonical per page, self-referencing on the real page, absolute URL. A wrong canonical is the most common invisible de-indexing.
- **Sitemap** - submitted, current, contains only indexable 200-status URLs. Not a dumping ground.
- **robots.txt** - blocks staging, never blocks CSS/JS if you want rendering, and never a substitute for `noindex`.
- **Redirects** - 301 for permanent, no chains longer than one hop, no redirect loops, no redirect to the homepage for a dead product page.
- **Pagination and filters** - decide canonical or `noindex` per pattern, and be consistent; ecommerce filter pages are where crawl budget dies.
- **Duplicate content** - `www` vs non-`www`, http vs https, trailing slash, UTM variants.

## JavaScript rendering

- **Test with the JS disabled** or with the crawler's rendering view. Content that only exists after a client-side fetch may be indexed late or not at all.
- **Server-render or pre-render the content that must rank.** For a small business site, static output is usually the cheapest fix.

## Speed, measured not guessed

- **LCP under 2.5s, INP under 200ms, CLS under 0.1** on mobile, on a real 4G profile, not on office wifi.
- **The usual culprits in India**: unoptimised hero images, a font loaded from a slow origin, third-party scripts (chat, pixels, reviews) and shared hosting with a 1.5s TTFB.
- **Fix the top three by impact**, not all twenty by checklist.

## Indian specifics

- **Mobile-first is not a slogan here** - the majority of search traffic is Android on 4G. Test on a mid-range device.
- **Hosting location matters less than TTFB.** Measure from India, not from a US CI runner.
- **Hinglish and transliterated queries** need the page to carry the words people type, not only the English ones.

## The technical report a business can act on

Not a 60-row audit. Three sections: what blocks indexing today (fix now),
what slows the site (fix this month), and what is fine (leave it alone). Each line
with the URL, the evidence and the owner.

## Anti-patterns

- An audit that lists 200 issues with no priority.
- `noindex` left on after staging went live.
- Blocking CSS in robots.txt and blaming the framework for "poor rendering".
- Chasing a 98 Lighthouse score while the product page takes 6 seconds on 4G.
- Redirecting every dead URL to the homepage.
