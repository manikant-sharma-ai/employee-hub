#!/usr/bin/env python3
"""Plan a board pack: allocate pages, order the sections, flag what cannot be assembled.

Deterministic by design - no clock, no network, no randomness. The same spec always
produces the same outline, so two people preparing the same pack get the same page
budget and the same gap list.

Spec shape (JSON):
{
  "meeting_date": "2026-11-20",
  "horizon": "Q2 FY27 (Jul-Sep 2026)",
  "page_budget": 14,
  "sections": [
    {"id": "1", "title": "Chair's summary", "owner": "founder",
     "pages_min": 1, "weight": 2, "ready": true},
    {"id": "2", "title": "Financial pack", "owner": "finance-ops",
     "pages_min": 4, "weight": 3, "ready": false,
     "blocked_on": "September bank reconciliation not closed"}
  ]
}

Usage:
  python3 pack_planner.py --self-test
  python3 pack_planner.py spec.json [--markdown]

Exit 0 = outline produced (readiness gaps are reported, not fatal).
Exit 1 = the spec itself is unusable.
"""
import json
import sys

REQUIRED_KEYS = ("id", "title", "owner", "pages_min")


def validate(spec):
    errs = []
    if not isinstance(spec, dict):
        return ["spec is not a JSON object"]
    sections = spec.get("sections")
    if not isinstance(sections, list) or not sections:
        errs.append("spec has no sections")
        return errs
    try:
        budget = int(spec.get("page_budget", 0))
    except (TypeError, ValueError):
        return ["page_budget is not an integer"]
    if budget <= 0:
        errs.append("page_budget must be a positive integer")
    seen = set()
    for i, s in enumerate(sections):
        if not isinstance(s, dict):
            errs.append("section %d is not an object" % i)
            continue
        for k in REQUIRED_KEYS:
            if k not in s:
                errs.append("section %d missing %r" % (i, k))
        sid = str(s.get("id", ""))
        if sid in seen:
            errs.append("duplicate section id %r" % sid)
        seen.add(sid)
        try:
            if int(s.get("pages_min", 1)) < 0:
                errs.append("section %r has negative pages_min" % sid)
        except (TypeError, ValueError):
            errs.append("section %r pages_min is not an integer" % sid)
    total_min = sum(int(s.get("pages_min", 1)) for s in sections if isinstance(s, dict))
    if total_min > budget:
        errs.append("minimum pages (%d) exceed the budget (%d)" % (total_min, budget))
    return errs


def allocate(spec):
    """Return (allocations, total_min, leftover).

    Every section gets its minimum; the leftover is spread by weight using the
    largest-remainder method, ties broken by section order. Integer arithmetic only,
    so the result is reproducible on any machine.
    """
    sections = spec["sections"]
    budget = int(spec["page_budget"])
    mins = [int(s.get("pages_min", 1)) for s in sections]
    total_min = sum(mins)
    leftover = budget - total_min
    alloc = list(mins)
    if leftover <= 0:
        return alloc, total_min, 0
    weights = []
    for s in sections:
        try:
            w = float(s.get("weight", 1))
        except (TypeError, ValueError):
            w = 1.0
        weights.append(w if w > 0 else 1.0)
    wsum = sum(weights) or 1.0
    raw = [leftover * w / wsum for w in weights]
    floors = [int(r) for r in raw]
    alloc = [m + f for m, f in zip(mins, floors)]
    remainder = leftover - sum(floors)
    order = sorted(range(len(sections)), key=lambda i: (-(raw[i] - floors[i]), i))
    for i in order[:remainder]:
        alloc[i] += 1
    return alloc, total_min, leftover


def readiness(spec):
    gaps = []
    for s in spec["sections"]:
        if not s.get("ready", False):
            gaps.append({
                "id": str(s.get("id", "")),
                "title": s.get("title", ""),
                "owner": s.get("owner", "unassigned"),
                "blocked_on": s.get("blocked_on", "not stated"),
            })
    return gaps


def render(spec, alloc, total_min, leftover, gaps):
    lines = []
    lines.append("# Board pack outline - meeting %s" % spec.get("meeting_date", "date not set"))
    if spec.get("horizon"):
        lines.append("Period covered: %s" % spec["horizon"])
    lines.append("Page budget: %d (minimum %d, distributed %d)" % (
        int(spec["page_budget"]), total_min, leftover))
    lines.append("")
    lines.append("| # | Section | Owner | Pages | Status |")
    lines.append("|---|---|---|---|---|")
    for s, pages in zip(spec["sections"], alloc):
        status = "ready" if s.get("ready", False) else "MISSING INPUT"
        lines.append("| %s | %s | %s | %d | %s |" % (
            s.get("id", ""), s.get("title", ""), s.get("owner", ""), pages, status))
    lines.append("")
    if gaps:
        lines.append("## Cannot be assembled yet")
        for g in gaps:
            lines.append("- **%s %s** - owner %s - blocked on: %s" % (
                g["id"], g["title"], g["owner"], g["blocked_on"]))
    else:
        lines.append("Every section has a source. The pack can be assembled.")
    return "\n".join(lines)


def _fixture():
    return {
        "meeting_date": "2026-11-20",
        "horizon": "Q2 FY27",
        "page_budget": 14,
        "sections": [
            {"id": "1", "title": "Chair's summary", "owner": "founder", "pages_min": 1, "weight": 2, "ready": True},
            {"id": "2", "title": "Financial pack", "owner": "finance-ops", "pages_min": 4, "weight": 3, "ready": False, "blocked_on": "September reconciliation open"},
            {"id": "3", "title": "Trading review", "owner": "mis-reporter", "pages_min": 2, "weight": 2, "ready": True},
            {"id": "4", "title": "Risk register", "owner": "compliance-watch", "pages_min": 1, "weight": 1, "ready": True},
            {"id": "5", "title": "People", "owner": "hiring-manager", "pages_min": 1, "weight": 1, "ready": True},
            {"id": "6", "title": "Minutes and actions", "owner": "board-reporter", "pages_min": 1, "weight": 1, "ready": False, "blocked_on": "no minutes received from the July meeting"},
        ],
    }


def self_test():
    checks = []

    def check(label, got, want):
        ok = got == want
        checks.append((label, ok, got, want))

    spec = _fixture()
    check("valid spec has no errors", validate(spec), [])
    alloc, total_min, leftover = allocate(spec)
    check("total minimum", total_min, 10)
    check("leftover", leftover, 4)
    check("allocation sums to budget", sum(alloc), 14)
    check("first section gets its minimum plus a share", alloc[0], 2)
    check("financial section gets the largest share", alloc[1], 5)
    check("allocation is stable across runs", allocate(spec)[0], alloc)

    gaps = readiness(spec)
    check("two gaps reported", len(gaps), 2)
    check("gap owner is carried through", gaps[1]["owner"], "board-reporter")

    out = render(spec, alloc, total_min, leftover, gaps)
    check("outline names the blocked section", "MISSING INPUT" in out, True)
    check("outline lists the blocker", "September reconciliation open" in out, True)
    check("outline is reproducible", render(spec, *allocate(spec), gaps) == out, True)

    bad = {"page_budget": 2, "sections": [{"id": "1", "title": "a", "owner": "x", "pages_min": 3}]}
    check("over-budget spec is rejected", any("exceed the budget" in e for e in validate(bad)), True)
    check("missing key is rejected", any("missing 'owner'" in e for e in validate({"page_budget": 5, "sections": [{"id": "1", "title": "a", "pages_min": 1}]})), True)

    failed = [c for c in checks if not c[1]]
    for label, ok, got, want in checks:
        print("%-46s %s" % (label, "ok" if ok else "FAIL (got %r, want %r)" % (got, want)))
    print("SELF-TEST: %s (%d/%d)" % ("PASS" if not failed else "FAIL", len(checks) - len(failed), len(checks)))
    return 0 if not failed else 1


def main(argv):
    if "--self-test" in argv:
        return self_test()
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: pack_planner.py <spec.json> [--markdown] | --self-test")
        return 2
    try:
        spec = json.load(open(args[0], encoding="utf-8"))
    except OSError as exc:
        print("ERROR: cannot read %s: %s" % (args[0], exc))
        return 1
    except json.JSONDecodeError as exc:
        print("ERROR: %s is not valid JSON: %s" % (args[0], exc))
        return 1
    errs = validate(spec)
    if errs:
        for e in errs:
            print("ERROR: " + e)
        return 1
    alloc, total_min, leftover = allocate(spec)
    print(render(spec, alloc, total_min, leftover, readiness(spec)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
