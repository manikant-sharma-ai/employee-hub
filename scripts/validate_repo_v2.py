#!/usr/bin/env python3
"""Validate the repo against the v2 bar for a new employee.

`scripts/validate_repo.py` is the v1 gate: the standard every employee in the hub must
meet. This is the gate a *new* employee must clear on the day it ships.

v2 checks, per employee:

  1. frontmatter description is 25-170 words, at most 1024 characters, and carries both
     a "Use when" clause and a "Not for" boundary
  2. the fixed section order (accountability, inputs, tools, routing, workflow, standards,
     notes, output contract, guardrails, trigger test)
  3. three to six reference files, each at least 400 bytes and routed from SKILL.md
  4. at least one deterministic script, and every script passes its own --self-test
  5. at least one asset template
  6. evals.json with five cases covering happy path, thin brief, missing connector, wrong
     tool and handoff
  7. notes/ seeded as schema only - the seed marker present, no filled lessons, no named
     contacts, no dated journal entries
  8. a registry entry carrying level (L0-L4), category, permissions, cost, connector
     availability, status "probation" and reliability "unverified"
  9. no trigger phrase that collides with another employee's description

Scope. The v2 rules apply to employees whose registry status is "probation" - the current
drop. Employees shipped before v2 existed are grandfathered and counted in the output, so
the debt is visible rather than hidden. Every drop from now on adds probation employees,
so the bar tightens by attrition.

Usage:
    python3 scripts/validate_repo_v2.py
    python3 scripts/validate_repo_v2.py --strict     # warnings in a v2 employee fail

Exit 0 = pass.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRICT = "--strict" in sys.argv

LEVELS = {"L0", "L1", "L2", "L3", "L4"}
CATEGORIES = {"revenue-facing", "operations", "founder-leverage"}
CASE_TYPES = {"happy_path", "thin_brief", "missing_connector", "wrong_tool", "handoff"}

SECTION_ORDER = [
    "accountable for",
    "handed before you start",
    "tools it assumes",
    "routing",
    "the workflow",
    "standards you hold yourself to",
    "notes and self-tracking",
    "output contract",
    "guardrails",
    "trigger test",
]

SEED_MARKER = "seed: schema only"


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    data, key = {}, None
    for line in text[3:end].strip().splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, data[key] = m.group(1), m.group(2).strip()
        elif key and line.strip():
            data[key] = (data[key] + " " + line.strip()).strip()
    return data


def trigger_phrases(desc):
    """Quoted trigger phrases from a description's 'Trigger phrases' run."""
    m = re.search(r"trigger phrases?(.*?)(?:\.\s*not for|$)", desc, re.I | re.S)
    if not m:
        return []
    return [p.strip().lower() for p in re.findall(r'"([^"]{6,})"', m.group(1))]


def check_employee(entry, registry, skills_dir, errors, warnings):
    name = entry.get("name")
    folder = os.path.join(skills_dir, name)
    path = os.path.join(folder, "SKILL.md")
    add = errors if STRICT else warnings
    if not os.path.isfile(path):
        errors.append("%s: SKILL.md missing" % name)
        return
    text = open(path, encoding="utf-8").read()
    fm = parse_frontmatter(text)
    desc = fm.get("description", "")
    body = text[text.find("\n---", 3) + 4:]

    # 1. description
    words = len(desc.split())
    if not 25 <= words <= 170:
        add.append("%s: description is %d words (25-170)" % (name, words))
    if len(desc) > 1024:
        errors.append("%s: description is %d characters (max 1024)" % (name, len(desc)))
    if "use when" not in desc.lower():
        errors.append("%s: description has no 'Use when' clause" % name)
    if "not for" not in desc.lower():
        errors.append("%s: description has no 'Not for' boundary" % name)

    # 2. section order
    headings = [(i, line.strip("# ").strip().lower())
                for i, line in enumerate(body.splitlines()) if line.startswith("## ")]
    positions = []
    for sec in SECTION_ORDER:
        found = [i for i, h in headings if sec in h]
        if not found:
            errors.append("%s: missing section %r" % (name, sec))
            return
        positions.append(found[0])
    if positions != sorted(positions) or len(set(positions)) != len(positions):
        errors.append("%s: sections are not in the fixed order" % name)

    # 3. references
    refs_dir = os.path.join(folder, "references")
    refs = sorted(f for f in os.listdir(refs_dir) if f.endswith(".md")) \
        if os.path.isdir(refs_dir) else []
    if not 3 <= len(refs) <= 6:
        errors.append("%s: %d reference files (3-6)" % (name, len(refs)))
    for f in refs:
        p = os.path.join(refs_dir, f)
        if os.path.getsize(p) < 400:
            add.append("%s: reference %s is under 400 bytes" % (name, f))
        if ("references/" + f) not in body:
            add.append("%s: reference %s is never routed to" % (name, f))

    # 4. scripts with a passing self-test
    scripts_dir = os.path.join(folder, "scripts")
    scripts = sorted(f for f in os.listdir(scripts_dir) if f.endswith(".py")) \
        if os.path.isdir(scripts_dir) else []
    if not scripts:
        errors.append("%s: no deterministic script" % name)
    for f in scripts:
        r = subprocess.run([sys.executable, os.path.join("scripts", f), "--self-test"],
                           cwd=folder, capture_output=True, text=True, timeout=120)
        if r.returncode != 0 or "self-test" not in r.stdout.lower():
            errors.append("%s: scripts/%s --self-test failed (%s)"
                          % (name, f, (r.stdout or r.stderr).strip().splitlines()[-1:]))

    # 5. asset template
    assets_dir = os.path.join(folder, "assets")
    assets = [f for f in os.listdir(assets_dir) if not f.startswith(".")] \
        if os.path.isdir(assets_dir) else []
    if not assets:
        errors.append("%s: no asset template" % name)

    # 6. evals
    ev_path = os.path.join(folder, "evals.json")
    if not os.path.isfile(ev_path):
        errors.append("%s: evals.json missing" % name)
    else:
        try:
            ev = json.load(open(ev_path, encoding="utf-8"))
        except ValueError as exc:
            errors.append("%s: evals.json does not parse (%s)" % (name, exc))
            ev = None
        if ev is not None:
            cases = ev.get("cases", [])
            if len(cases) < 5:
                errors.append("%s: %d eval cases (need 5)" % (name, len(cases)))
            got = {c.get("type") for c in cases}
            for need in sorted(CASE_TYPES - got):
                errors.append("%s: evals.json has no %r case" % (name, need))
            for c in cases:
                if not c.get("prompt") or not (c.get("expect") or {}).get("must_include"):
                    add.append("%s: eval case %r lacks a prompt or must_include"
                               % (name, c.get("id")))

    # 7. notes seeded as schema only
    notes = os.path.join(folder, "notes")
    if not os.path.isdir(notes):
        errors.append("%s: no notes/ folder" % name)
    else:
        for need in ("learnings.md", "contacts.md", "decisions.md"):
            p = os.path.join(notes, need)
            if not os.path.isfile(p):
                errors.append("%s: notes/%s missing" % (name, need))
                continue
            body_n = open(p, encoding="utf-8").read()
            if SEED_MARKER not in body_n[:400]:
                add.append("%s: notes/%s has no schema-only seed marker" % (name, need))
        if not os.path.isdir(os.path.join(notes, "journal")):
            add.append("%s: notes/journal/ missing" % name)
        for f in ("learnings.md", "decisions.md"):
            p = os.path.join(notes, f)
            if os.path.isfile(p):
                for line in open(p, encoding="utf-8"):
                    if re.match(r"^\|?\s*\d+\.?\s*\|", line) or re.match(r"^\d+\.\s", line):
                        errors.append("%s: notes/%s contains a filled lesson at seed"
                                      % (name, f))
                        break
        p = os.path.join(notes, "contacts.md")
        if os.path.isfile(p):
            rows = [l for l in open(p, encoding="utf-8") if l.startswith("|")]
            data_rows = [r for r in rows[2:] if "---" not in r]
            for r in data_rows:
                if "<" not in r:
                    errors.append("%s: notes/contacts.md has a named contact at seed" % name)
                    break
        jdir = os.path.join(notes, "journal")
        if os.path.isdir(jdir):
            for f in os.listdir(jdir):
                if re.match(r"^\d{4}-\d{2}\.md$", f):
                    errors.append("%s: notes/journal/%s is a dated entry at seed"
                                  % (name, f))

    # 8. registry fields
    lvl = entry.get("level")
    if lvl not in LEVELS:
        errors.append("%s: registry level %r not in L0-L4" % (name, lvl))
    if entry.get("category") not in CATEGORIES:
        errors.append("%s: registry category %r invalid" % (name, entry.get("category")))
    perms = entry.get("permissions") or {}
    if not isinstance(perms, dict) or set(perms) < {"read", "write", "never"}:
        errors.append("%s: registry permissions need read, write and never" % name)
    elif not perms.get("never"):
        add.append("%s: permissions.never is empty" % name)
    cost = entry.get("cost") or {}
    if not isinstance(cost, dict) or not cost.get("band"):
        errors.append("%s: registry cost needs at least a band" % name)
    conn = entry.get("connector_availability") or {}
    if not isinstance(conn, dict) or not conn.get("needs_user_connect"):
        errors.append("%s: registry connector_availability needs needs_user_connect" % name)
    if entry.get("status") != "probation":
        errors.append("%s: new employee must be status 'probation'" % name)
    if entry.get("reliability") != "unverified":
        errors.append("%s: new employee must be reliability 'unverified'" % name)
    if not entry.get("version"):
        errors.append("%s: registry version missing" % name)

    # 9. trigger collision with any other employee
    mine = trigger_phrases(desc)
    if len(mine) < 3:
        add.append("%s: only %d trigger phrases (3 or more)" % (name, len(mine)))
    for other in registry.get("employees", []):
        if other.get("name") == name:
            continue
        other_text = ""
        p = os.path.join(skills_dir, other.get("name", ""), "SKILL.md")
        if os.path.isfile(p):
            other_text = parse_frontmatter(open(p, encoding="utf-8").read()).get(
                "description", "").lower()
        if not other_text:
            continue
        for phrase in mine:
            if len(phrase) >= 10 and phrase in other_text:
                errors.append("%s: trigger %r collides with %s"
                              % (name, phrase, other.get("name")))


def main():
    errors, warnings = [], []

    v1 = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate_repo.py")],
                        cwd=ROOT, capture_output=True, text=True)
    if v1.returncode != 0:
        errors.append("v1 gate failed:\n" + v1.stdout.strip())

    reg_path = os.path.join(ROOT, "registry.json")
    registry = json.load(open(reg_path, encoding="utf-8"))
    employees = registry.get("employees", [])
    skills_dir = os.path.join(ROOT, "skills")

    cohort = [e for e in employees if e.get("status") == "probation"]
    grandfathered = [e for e in employees if e.get("status") != "probation"]
    if not cohort:
        errors.append("no probation employees found - nothing to validate at the v2 bar")

    for entry in cohort:
        check_employee(entry, registry, skills_dir, errors, warnings)

    print("v2 gate%s | employees %d | probation %d | grandfathered %d"
          % (" --strict" if STRICT else "", len(employees), len(cohort),
             len(grandfathered)))
    print("probation cohort: " + ", ".join(e.get("name", "?") for e in cohort))
    for e in errors:
        print("  ERROR   " + e)
    for w in warnings:
        print("  warning " + w)
    if grandfathered:
        print("  note    %d employees shipped before v2 are grandfathered - the bar "
              "tightens as they are re-touched" % len(grandfathered))
    print("RESULT: %s (%d errors, %d warnings)"
          % ("PASS" if not errors else "FAIL", len(errors), len(warnings)))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
