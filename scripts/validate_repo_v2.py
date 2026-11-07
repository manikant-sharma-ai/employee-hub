#!/usr/bin/env python3
"""Validate the whole employee-hub repo against the v2 standard.

A superset of `scripts/validate_repo.py`. The v1 validator is still run first, so
nothing that used to fail can now pass; this adds the five things the v2 standard
made enforceable:

  1. a fixed section order in every SKILL.md
  2. `evals.json` with the five named cases
  3. `notes.seed/` that is schema only - no fabricated experience
  4. at least one deterministic script that passes its own `--self-test`
  5. registry fields needed to make a hire decision: level (L0-L4), category,
     permissions, cost, connectors, status probation, reliability unverified

Which skills get the full v2 tree checks: those that declare a `level` in
`registry.json`. Employees added before the v2 standard keep being validated on
v1 - back-filling their evals with invented cases would be the fabrication the
standard exists to prevent.

Usage:
  python3 scripts/validate_repo_v2.py            # errors fail, warnings reported
  python3 scripts/validate_repo_v2.py --strict   # warnings fail too
Exit 0 = pass.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRICT = "--strict" in sys.argv

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


SECTION_ORDER = [
    "## What you are accountable for",
    "## What you must be handed before you start",
    "## Tools it assumes",
    "## Routing",
    "## The workflow",
    "## Standards you hold yourself to",
    "## Notes and self-tracking",
    "## Output contract",
    "## Guardrails",
    "## Trigger test",
]

EVAL_TYPES = ["happy_path", "thin_brief", "missing_connector", "wrong_tool", "handoff"]

REQUIRED_REGISTRY = ["level", "category", "permissions", "cost", "connectors", "status", "reliability"]
LEVELS = ("L0", "L1", "L2", "L3", "L4")
PERMISSION_KEYS = ("read", "write", "never")
COST_KEYS = ("tier", "estimate_inr_per_month", "note")
CONNECTOR_KEYS = ("needed", "first_connect", "works_without")

SCHEMA_ONLY_MARKERS = ("no entries yet", "no rules yet", "no contacts yet", "no decisions recorded yet",
                       "no entries yet -", "(no entries yet)", "no task has been run")
DATED_ENTRY = re.compile(r"^\s*[-*]\s*\*\*20\d\d-\d\d-\d\d\*\*", re.MULTILINE)
NUMBERED_RULE = re.compile(r"^\s*\d+\.\s+\*\*", re.MULTILINE)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    data, key = {}, None
    for line in text[3:end].strip().splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            data[key] = m.group(2).strip()
        elif key and line.strip():
            data[key] = (data[key] + " " + line.strip()).strip()
    return data


def run_v1():
    path = os.path.join(ROOT, "scripts", "validate_repo.py")
    if not os.path.isfile(path):
        err("scripts/validate_repo.py missing - the v1 gate cannot be run")
        return
    r = subprocess.run([sys.executable, path], capture_output=True, text=True)
    if r.returncode != 0:
        tail = [ln for ln in (r.stdout or "").splitlines() if "ERROR" in ln or "RESULT" in ln]
        err("v1 gate failed:\n    " + "\n    ".join(tail or ["(no output)"]))


def check_sections(name, body):
    positions = []
    for heading in SECTION_ORDER:
        idx = body.find(heading)
        if idx == -1:
            err("%s: missing required section %r" % (name, heading))
            return
        positions.append((idx, heading))
    for i in range(1, len(positions)):
        if positions[i][0] < positions[i - 1][0]:
            err("%s: section order broken - %r appears before %r"
                % (name, positions[i][1], positions[i - 1][1]))
            return


def check_evals(name, folder):
    path = os.path.join(folder, "evals.json")
    if not os.path.isfile(path):
        err("%s: evals.json missing" % name)
        return
    try:
        data = json.load(open(path, encoding="utf-8"))
    except json.JSONDecodeError as exc:
        err("%s: evals.json is not valid JSON: %s" % (name, exc))
        return
    cases = data.get("cases")
    if not isinstance(cases, list):
        err("%s: evals.json has no cases list" % name)
        return
    if len(cases) != 5:
        err("%s: evals.json has %d cases, the standard requires exactly 5" % (name, len(cases)))
    found = [c.get("type") for c in cases if isinstance(c, dict)]
    for want in EVAL_TYPES:
        if found.count(want) != 1:
            err("%s: evals.json needs exactly one %r case, found %d" % (name, want, found.count(want)))
    ids = [c.get("id") for c in cases if isinstance(c, dict)]
    if len(ids) != len(set(ids)):
        err("%s: evals.json has duplicate case ids" % name)
    for c in cases:
        if not isinstance(c, dict):
            err("%s: evals.json case is not an object" % name)
            continue
        for key in ("id", "type", "title", "prompt", "must_include", "must_exclude", "pass_criteria"):
            if not c.get(key):
                err("%s: evals case %r is missing %r" % (name, c.get("id", "?"), key))
        if not isinstance(c.get("must_include"), list) or not isinstance(c.get("must_exclude"), list):
            err("%s: evals case %r must_include/must_exclude must be lists" % (name, c.get("id", "?")))


def check_scripts(name, folder):
    scripts_dir = os.path.join(folder, "scripts")
    if not os.path.isdir(scripts_dir):
        err("%s: no scripts/ directory - the deterministic check is missing" % name)
        return
    candidates = sorted(f for f in os.listdir(scripts_dir)
                        if f.endswith(".py") and f != "validate_skill.py")
    if not candidates:
        err("%s: scripts/ carries no deterministic script of its own" % name)
        return
    passed = []
    for fn in candidates:
        path = os.path.join(scripts_dir, fn)
        r = subprocess.run([sys.executable, path, "--self-test"],
                           capture_output=True, text=True, timeout=120)
        if r.returncode == 0 and "SELF-TEST: PASS" in (r.stdout or ""):
            passed.append(fn)
        else:
            err("%s: scripts/%s --self-test did not pass (exit %d)" % (name, fn, r.returncode))
    if not passed:
        err("%s: no script in scripts/ passes --self-test" % name)


def check_assets(name, folder):
    assets_dir = os.path.join(folder, "assets")
    if not os.path.isdir(assets_dir) or not os.listdir(assets_dir):
        err("%s: no assets/ template" % name)
        return
    files = [f for f in os.listdir(assets_dir) if os.path.isfile(os.path.join(assets_dir, f))]
    if not files:
        err("%s: assets/ is empty" % name)


def check_references(name, folder):
    refs_dir = os.path.join(folder, "references")
    if not os.path.isdir(refs_dir):
        err("%s: no references/ directory" % name)
        return
    files = sorted(f for f in os.listdir(refs_dir) if f.endswith(".md"))
    if not 3 <= len(files) <= 6:
        err("%s: %d reference files, the standard requires 3 to 6" % (name, len(files)))


def check_notes(name, folder):
    for sub in ("notes", "notes.seed"):
        path = os.path.join(folder, sub)
        if not os.path.isdir(path):
            err("%s: %s/ missing" % (name, sub))
            continue
        for need in ("learnings.md", "contacts.md", "decisions.md"):
            f = os.path.join(path, need)
            if not os.path.isfile(f):
                err("%s: %s/%s missing" % (name, sub, need))
                continue
            body = read(f)
            if DATED_ENTRY.search(body) or NUMBERED_RULE.search(body):
                err("%s: %s/%s carries fabricated experience - seed files are schema only"
                    % (name, sub, need))
            if not any(m in body.lower() for m in SCHEMA_ONLY_MARKERS):
                err("%s: %s/%s has no empty-state marker - it is not schema only" % (name, sub, need))
        journal = os.path.join(path, "journal")
        if not os.path.isdir(journal):
            err("%s: %s/journal/ missing" % (name, sub))
        else:
            for fn in os.listdir(journal):
                if fn.endswith(".md") and DATED_ENTRY.search(read(os.path.join(journal, fn))):
                    err("%s: %s/journal/%s has dated entries - seed files are schema only"
                        % (name, sub, fn))


def check_registry_entry(e):
    name = e.get("name", "?")
    for key in REQUIRED_REGISTRY:
        if key not in e:
            err("%s: registry entry missing v2 field %r" % (name, key))
    if e.get("level") not in LEVELS:
        err("%s: level %r is not one of L0-L4" % (name, e.get("level")))
    perms = e.get("permissions")
    if not isinstance(perms, dict):
        err("%s: permissions must be an object with read/write/never" % name)
    else:
        for key in PERMISSION_KEYS:
            if not isinstance(perms.get(key), list) or not perms.get(key):
                err("%s: permissions.%s must be a non-empty list" % (name, key))
    cost = e.get("cost")
    if not isinstance(cost, dict):
        err("%s: cost must be an object" % name)
    else:
        for key in COST_KEYS:
            if key not in cost:
                err("%s: cost.%s missing" % (name, key))
    conn = e.get("connectors")
    if not isinstance(conn, dict):
        err("%s: connectors must be an object" % name)
    else:
        for key in CONNECTOR_KEYS:
            if not isinstance(conn.get(key), list) or not conn.get(key):
                err("%s: connectors.%s must be a non-empty list" % (name, key))
    if e.get("status") != "probation":
        err("%s: a new employee must register as status 'probation', got %r" % (name, e.get("status")))
    if e.get("reliability") != "unverified":
        err("%s: a new employee must register as reliability 'unverified', got %r"
            % (name, e.get("reliability")))


def main():
    run_v1()

    reg_path = os.path.join(ROOT, "registry.json")
    if not os.path.isfile(reg_path):
        print("ERROR: registry.json missing")
        return 1
    registry = json.load(open(reg_path, encoding="utf-8"))
    employees = registry.get("employees", [])
    levels_defined = registry.get("levels", {})
    for key in LEVELS:
        if key not in levels_defined:
            warn("registry.levels does not define %s" % key)

    v2_names = []
    legacy_over = []
    for e in employees:
        folder = os.path.join(ROOT, e.get("path", ""))
        name = e.get("name", "?")
        if not os.path.isdir(folder):
            err("%s: path %r does not exist" % (name, e.get("path")))
            continue
        skill = os.path.join(folder, "SKILL.md")
        if not os.path.isfile(skill):
            err("%s: SKILL.md missing" % name)
            continue
        text = read(skill)
        fm = frontmatter(text)
        body = text[text.find("\n---", 3) + 4:] if text.startswith("---") else text

        desc = fm.get("description", "")
        if "level" not in e:
            # Legacy employee: the 1024 limit was never enforced before v2. Report the
            # debt as information; it is not this drop's failure to fix, and inventing a
            # rewrite of 17 shipped descriptions would be worse than reporting it.
            if len(desc) > 1024:
                legacy_over.append((name, len(desc)))
            continue
        if len(desc) > 1024:
            err("%s: description is %d characters, the limit is 1024" % (name, len(desc)))
        v2_names.append(name)
        check_registry_entry(e)
        check_sections(name, body)
        check_references(name, folder)
        check_assets(name, folder)
        check_scripts(name, folder)
        check_evals(name, folder)
        check_notes(name, folder)

    if STRICT:
        errors.extend(warnings)
        strict_note = " (--strict: warnings counted as errors)"
    else:
        strict_note = ""

    print("repo: %s | employees: %d | v2-standard employees: %d%s" % (
        registry.get("name"), len(employees), len(v2_names), strict_note))
    if v2_names:
        print("v2 checked: " + ", ".join(v2_names))
    if legacy_over:
        print("legacy note: %d pre-v2 description(s) exceed 1024 characters (%s) - not enforced on legacy employees"
              % (len(legacy_over), ", ".join("%s %d" % x for x in sorted(legacy_over, key=lambda y: -y[1])[:4]) + ", ..."))
    shown = errors if STRICT else errors + warnings
    for e in errors:
        print("  ERROR   " + e)
    if not STRICT:
        for w in warnings:
            print("  warning " + w)
    print("RESULT: %s (%d errors, %d warnings)" % (
        "PASS" if not shown else "FAIL", len(errors), len(warnings)))
    return 0 if not shown else 1


if __name__ == "__main__":
    sys.exit(main())
