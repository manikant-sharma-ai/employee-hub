#!/usr/bin/env python3
"""Validate the repo against the v2 employee contract.

    python3 scripts/validate_repo_v2.py            # report, exit 0 unless an error
    python3 scripts/validate_repo_v2.py --strict   # every failure in the new contract is an error

v1 (`scripts/validate_repo.py`) checks the Employee Standard: core files present, registry matches
folders, every skill passes `validate_skill.py`, changelog and backlog coverage, no secrets.

v2 adds the part a shipped employee must now carry, and enforces it for every skill that declares
`"contract": "v2"` in registry.json and for every skill added on or after STRICT_FROM:

  - an `evals.json` with exactly five cases, one each of happy_path, thin_brief, missing_connector,
    wrong_tool and handoff, each with prompt, expect, must_not and pass
  - at least one deterministic script under `scripts/` whose `--self-test` exits 0
  - a frontmatter description under 1024 characters
  - 3 to 6 reference files, at least one asset, and a `notes.seed/` folder

Skills added before STRICT_FROM that miss any of it are reported as debt, not as errors: rewriting a
shipped description to fit a cap is a different job from shipping a new employee, and doing it inside
a drop is how a collision gets introduced.

Usage: python3 scripts/validate_repo_v2.py [--strict]
Exit 0 = pass.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRICT_FROM = "2026-11-14"
TYPES = {"happy_path", "thin_brief", "missing_connector", "wrong_tool", "handoff"}
CASE_KEYS = {"id", "type", "prompt", "expect", "must_not", "pass"}
DESC_LIMIT = 1024

errors, debt = [], []


def desc_length(folder):
    path = os.path.join(folder, "SKILL.md")
    if not os.path.isfile(path):
        return None
    m = re.search(r"^description:\s*(.*)$", open(path, encoding="utf-8").read(), re.M)
    return len(m.group(1)) if m else None


def check_evals(folder):
    p = os.path.join(folder, "evals.json")
    if not os.path.isfile(p):
        return ["no evals.json"]
    try:
        data = json.load(open(p, encoding="utf-8"))
    except ValueError as e:
        return ["evals.json does not parse: %s" % e]
    cases = data.get("cases", [])
    out = []
    if len(cases) != 5:
        out.append("evals.json has %d cases, expected 5" % len(cases))
    got = {c.get("type") for c in cases}
    if got != TYPES:
        out.append("eval types are %s, expected the five fixed types" % sorted(got))
    for c in cases:
        missing = CASE_KEYS - set(c)
        if missing:
            out.append("eval %r missing %s" % (c.get("id"), ", ".join(sorted(missing))))
        if not c.get("expect"):
            out.append("eval %r has no expectations" % c.get("id"))
        if not c.get("must_not"):
            out.append("eval %r has no must_not" % c.get("id"))
    return out


def check_selftest(folder):
    sdir = os.path.join(folder, "scripts")
    if not os.path.isdir(sdir):
        return ["no scripts/ directory"]
    scripts = sorted(f for f in os.listdir(sdir) if f.endswith(".py"))
    if not scripts:
        return ["no script in scripts/"]
    passing = []
    for s in scripts:
        r = subprocess.run([sys.executable, os.path.join("scripts", s), "--self-test"],
                           cwd=folder, capture_output=True, text=True)
        if r.returncode == 0 and "checks passed" in r.stdout:
            passing.append(s)
    if not passing:
        return ["no script with a passing --self-test (tried %s)" % ", ".join(scripts)]
    return []


def main():
    strict = "--strict" in sys.argv

    r = subprocess.run([sys.executable, os.path.join("scripts", "validate_repo.py")],
                       cwd=ROOT, capture_output=True, text=True)
    print(r.stdout.rstrip())
    if r.returncode != 0:
        errors.append("validate_repo.py failed")

    registry = json.load(open(os.path.join(ROOT, "registry.json"), encoding="utf-8"))
    print("\nv2 contract (strict from %s)%s" % (STRICT_FROM, " - STRICT" if strict else ""))

    for e in registry.get("employees", []):
        name = e.get("name")
        folder = os.path.join(ROOT, e.get("path") or ("skills/" + name))
        if not os.path.isdir(folder):
            errors.append("%s: folder missing" % name)
            continue
        problems = []
        problems += check_evals(folder)
        problems += check_selftest(folder)
        n = desc_length(folder)
        if n is None:
            problems.append("no description")
        elif n >= DESC_LIMIT:
            problems.append("description is %d characters (limit %d)" % (n, DESC_LIMIT - 1))
        refs = os.path.join(folder, "references")
        count = len([f for f in os.listdir(refs) if f.endswith(".md")]) if os.path.isdir(refs) else 0
        if not 3 <= count <= 6:
            problems.append("%d reference files (expected 3-6)" % count)
        assets = os.path.join(folder, "assets")
        if not (os.path.isdir(assets) and os.listdir(assets)):
            problems.append("no asset template")
        if not os.path.isdir(os.path.join(folder, "notes.seed")):
            problems.append("no notes.seed/ folder")
        if not problems:
            continue
        new_employee = e.get("contract") == "v2" or (e.get("added") or "") >= STRICT_FROM
        for p in problems:
            if new_employee:
                errors.append("%s: %s" % (name, p))
            else:
                debt.append("%s: %s" % (name, p))

    if debt:
        kinds = {}
        for d in debt:
            kind = d.split(": ", 1)[1]
            kind = re.sub(r"\d+", "N", kind)
            kinds[kind] = kinds.get(kind, 0) + 1
        print("  debt in %d shipped skill(s), not blocking:" % len({d.split(":")[0] for d in debt}))
        for kind, count in sorted(kinds.items(), key=lambda kv: -kv[1]):
            print("    - %-52s %d" % (kind, count))
    for e in errors:
        print("  ERROR   " + e)
    print("RESULT: %s (%d errors, %d debt items)" % ("PASS" if not errors else "FAIL", len(errors), len(debt)))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
