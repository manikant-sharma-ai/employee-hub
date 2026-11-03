#!/usr/bin/env python3
"""Generate a pairwise edge-case matrix from a spec of dimensions and values.

Deterministic and dependency-free. Pairwise (all-pairs) coverage finds the same
interaction defects as the full cartesian product at a fraction of the cases;
the coverage number is computed, not claimed.

Input JSON:
{"feature": "coupon",
 "dimensions": {"code": ["valid","expired"], "cart": ["one","many"], "user": ["guest","member"]},
 "bounds": {"amount": [0, 100000]}}      # optional: numeric ranges to expand

Output: TSV of cases plus a coverage summary. --json for JSON.

Usage:
    python3 edge_matrix.py spec.json
    python3 edge_matrix.py --self-test
"""
import argparse
import itertools
import json
import sys


def pairwise(dims):
    """Greedy all-pairs covering array. Deterministic for a given input order.

    Candidates are grown from each uncovered pair in a fixed sort order, and the
    candidate that covers the most uncovered pairs wins. Ties go to the earliest
    candidate, which is what makes repeated runs identical.
    """
    names = list(dims.keys())
    if not names:
        return []
    if len(names) == 1:
        return [{names[0]: v} for v in dims[names[0]]]

    uncovered = set()
    for a, b in itertools.combinations(range(len(names)), 2):
        for va in dims[names[a]]:
            for vb in dims[names[b]]:
                uncovered.add(((a, va), (b, vb)))

    rows = []
    while uncovered:
        ordered = sorted(uncovered, key=lambda p: (p[0][0], repr(p[0][1]), p[1][0], repr(p[1][1])))
        best_row, best_cov = None, frozenset()
        for (i, vi), (j, vj) in ordered:
            row = {names[i]: vi, names[j]: vj}
            for k, n in enumerate(names):
                if n in row:
                    continue
                best_v, best_g = None, -1
                for v in dims[n]:
                    g = 0
                    for m, other in enumerate(names):
                        if other not in row:
                            continue
                        if (k, v) == (m, row[other]):
                            continue
                        if ((min(k, m), v if k < m else row[other]),
                                (max(k, m), row[other] if k < m else v)) in uncovered:
                            g += 1
                    if g > best_g:
                        best_v, best_g = v, g
                row[n] = best_v
            cov = frozenset(p for p in uncovered
                            if row.get(names[p[0][0]]) == p[0][1]
                            and row.get(names[p[1][0]]) == p[1][1])
            if len(cov) > len(best_cov):
                best_row, best_cov = row, cov
        rows.append(best_row)
        uncovered -= best_cov
        if len(rows) > 5000:
            raise RuntimeError("pairwise generation did not converge")
    return rows


def coverage(dims, rows):
    names = list(dims.keys())
    total, covered = 0, 0
    for a, b in itertools.combinations(range(len(names)), 2):
        for va in dims[names[a]]:
            for vb in dims[names[b]]:
                total += 1
                if any(r.get(names[a]) == va and r.get(names[b]) == vb for r in rows):
                    covered += 1
    return covered, total


def expand_bounds(bounds, points=5):
    """Turn [min, max] into boundary values: min, min+1, mid, max-1, max."""
    out = {}
    for k, (lo, hi) in bounds.items():
        if hi <= lo:
            out[k] = [lo]
            continue
        mid = lo + (hi - lo) // 2
        vals = [lo, lo + 1, mid, max(mid, hi - 1), hi]
        seen, uniq = set(), []
        for v in vals:
            if v not in seen:
                seen.add(v)
                uniq.append(v)
        out[k] = uniq
    return out


def build(spec):
    dims = dict(spec.get("dimensions", {}) or {})
    dims.update(expand_bounds(spec.get("bounds", {}) or {}))
    if not dims:
        raise ValueError("spec has no dimensions - there is nothing to cross")
    for k, v in dims.items():
        if not isinstance(v, list) or not v:
            raise ValueError("dimension %r must be a non-empty list" % k)
    rows = pairwise(dims)
    covered, total = coverage(dims, rows)
    full = 1
    for v in dims.values():
        full *= len(v)
    return {
        "feature": spec.get("feature", "unnamed"),
        "dimensions": dims,
        "cases": rows,
        "summary": {
            "dimensions": len(dims),
            "full_cartesian": full,
            "pairwise_cases": len(rows),
            "reduction_pct": round(100.0 * (1 - len(rows) / full), 1) if full else 0.0,
            "pairs_covered": covered,
            "pairs_total": total,
            "complete": covered == total,
        },
    }


GOOD = {"feature": "coupon",
        "dimensions": {"code": ["valid", "expired", "unknown", "empty"],
                       "cart": ["one item", "many", "empty", "above threshold"],
                       "user": ["guest", "member", "returning"]},
        "bounds": {"amount": [0, 100000]}}


def self_test():
    r = build(GOOD)
    s = r["summary"]
    assert s["complete"] is True, s
    assert s["pairs_covered"] == s["pairs_total"], s
    assert s["pairwise_cases"] < s["full_cartesian"], s
    assert s["dimensions"] == 4, s
    # bounds expand to boundary values, deduplicated
    assert r["dimensions"]["amount"] == [0, 1, 50000, 99999, 100000], r["dimensions"]["amount"]
    # every case has a value for every dimension
    for c in r["cases"]:
        assert set(c) == set(r["dimensions"]), c
    # determinism
    assert json.dumps(build(GOOD)) == json.dumps(build(GOOD))
    # single dimension degenerates to one case per value
    one = build({"feature": "x", "dimensions": {"a": ["1", "2", "3"]}})
    assert len(one["cases"]) == 3, one["cases"]
    assert one["summary"]["complete"] is True
    # a two-dimension spec covers every pair
    two = build({"feature": "y", "dimensions": {"a": ["1", "2"], "b": ["x", "y"]}})
    assert two["summary"]["pairs_covered"] == 4, two["summary"]
    # an empty spec is an error, not a crash
    try:
        build({"feature": "z", "dimensions": {}})
        assert False, "empty dimensions should raise"
    except ValueError:
        pass
    print("self-test: all assertions passed (pairwise coverage complete, deterministic, bounds expanded)")


def emit(r, as_json=False):
    if as_json:
        print(json.dumps(r, indent=2))
        return
    dims = list(r["dimensions"].keys())
    print("feature: %s | dimensions: %d | cases: %d (full cartesian %d, -%s%%)"
          % (r["feature"], len(dims), len(r["cases"]), r["summary"]["full_cartesian"],
             r["summary"]["reduction_pct"]))
    print("\t".join(["#"] + dims))
    for i, c in enumerate(r["cases"], 1):
        print("\t".join([str(i)] + [str(c[d]) for d in dims]))
    s = r["summary"]
    print("\n# pairs covered %d/%d | complete=%s"
          % (s["pairs_covered"], s["pairs_total"], s["complete"]))


def main():
    ap = argparse.ArgumentParser(description="Pairwise edge-case matrix generator.")
    ap.add_argument("path", nargs="?", help="spec JSON; omit to read stdin")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return 0
    raw = open(a.path, encoding="utf-8").read() if a.path else sys.stdin.read()
    emit(build(json.loads(raw)), a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
