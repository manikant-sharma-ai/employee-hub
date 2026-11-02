# Story slicing

A story is a unit of shippable value, not a unit of work. If it cannot be released on its own and observed by a user, it is a task inside a bigger story, or an epic pretending to be one.

## The shape

> As a **<specific user>**, I want **<capability>** so that **<outcome they care about>**.

The test: could a real user say the "so that" clause out loud? If not, the story is written for the team, not for the user.

| Weak | Why | Strong |
|---|---|---|
| "As a user I want a dashboard so that I can see data" | No user, no outcome | "As a shop owner, I want to see yesterday's orders and revenue on one screen so that I know whether today needs a push before 11am" |
| "Build the export feature" | A project | "As an accountant, I want to export October's invoices as a CSV with GST split into two columns, so that I can import it into Tally without editing" |

## Acceptance criteria

Three forms, in order of preference:

1. **Given / when / then** - for behaviour with a state.
   `Given an order marked delivered, when the customer opens the order page, then a "Return" button appears for 7 days and disappears after.`
2. **A checklist** - for content, layout or a static change.
   `[ ] Price shows with GST included [ ] Currency is ₹ [ ] Mobile layout stacks at 360px`
3. **A measurement** - for performance or scale.
   `p95 render under 1.5s at 500 rows on 4G`

Never: "works correctly", "as expected", "looks good", "handles errors".

## The definition of done

Agree it once, per team, and apply it to every story:

- Acceptance criteria met and checked by someone other than the author.
- Empty, loading and error states exist.
- Mobile checked at 360px.
- Text and copy reviewed (a product change is a content change).
- Analytics event fires, if the metric depends on it.
- No new console errors; no new accessibility regressions on the changed screen.
- Release note line written, or "not user-visible" stated.

## Seven ways to slice an epic

| Slice by | Example | Good when |
|---|---|---|
| Workflow step | "Checkout: address step only, payment stays as-is" | The flow is long and each step is independently useful |
| User segment | "Refunds for prepaid orders first, COD later" | Segments have different constraints |
| Data | "Filter by status; date range later" | The cheap half proves demand |
| Channel | "Web first, app later" | Platforms are separate codebases |
| Happy path | "Ship the success case with a manual fallback for failures" | Failures are rare and recoverable by hand |
| Read before write | "Show the report; edit it next" | Read-only delivers most of the value |
| One hard thing | "One real integration done end to end, then the other three" | Integration risk is the whole risk |

The first slice should be the one that produces the most learning per week of work - usually a real user doing the real thing with a manual step behind it.

## Sizing

| Size | Meaning | Action |
|---|---|---|
| S | Half a day to two days | Fine |
| M | Three to five days | Fine, if it can ship alone |
| L | One to two weeks | Slice it |
| XL | More than two weeks | It is an epic; stop and slice |

If a story is XL, the slicing question is: what could we ship in week one that a user could touch?

## Anti-patterns

- **Horizontal slicing** - "database schema", "API layer", "UI". None of these ships value; a user cannot see any of them.
- **A story with 14 acceptance criteria.** It is three stories.
- **Stories written by whoever is building them, with no user.** Usually technically clean and commercially pointless.
- **"Spike" with no timebox and no output.** A spike produces a written answer by a date, or it is a project.
- **An epic in the sprint board for six months.** It hides the fact that nothing has shipped.
- **Estimate in days with no range.** Every estimate is a range; writing a single number invites a promise.
