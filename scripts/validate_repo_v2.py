#!/usr/bin/env python3
"""Validate the whole employee-hub repo against the v2 standard.

v2 is the tree the daily drop ships from 2026-11-03 onwards. It keeps every
check from validate_repo.py and adds the ones that make an employee testable
rather than merely well-written:

  - a fixed section order in SKILL.md, so a reviewer knows where to look
  - a frontmatter description under 1024 characters, so it fits a loader
  - 3-6 craft references, every one routed to from SKILL.md
  - at least one deterministic script that passes its own --self-test
  - one asset template
  - evals.json with five cases: happy path, thin brief, missing connector,
    wrong tool, handoff - and every routes_to naming a real role
  - notes.seed/ that is schema only, with no invented experience in it
  - a registry entry carrying level, category, permissions, cost, connector
    availability, status and reliability

Skills that do not declare `standard_version: 2` are checked against the v1
baseline only, and are listed under DRIFT rather than failing the gate. That
list is the tenth-drop review queue, not a licence.

Usage:
    python3 scripts/validate_repo_v2.py             # errors fail, warnings print
    python3 scripts/validate_repo_v2.py --strict    # warnings fail too
    python3 scripts/validate_repo_v2.py --skill NAME
Exit 0 = pass.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORE_FILES = [
    "core/employee-standard.md",
    "core/connector-preflight.md",
    "core/connector-catalog.md",
    "core/memory-and-notes.md",
    "core/performance-tracking.md",
    "docs/standard-v2.md",
]

# The fixed section order. A v2 SKILL.md has these nine H2s, in this order.
SECTIONS = [
    "What you are accountable for",
    "What you must be handed before you start",
    "Tools it assumes",
    "Routing: read the request, load the craft",
    "The workflow",
    "Standards you hold yourself to",
    "Output contract",
    "Guardrails",
    "Trigger test",
]

BASELINE_LINKS = [
    ("core/connector-preflight.md", "connector preflight"),
    ("core/memory-and-notes.md", "notes protocol"),
    ("core/performance-tracking.md", "performance tracking"),
]

EVAL_TYPES = ["happy_path", "thin_brief", "missing_connector", "wrong_tool", "handoff"]

LEVELS = ["L0", "L1", "L2", "L3", "L4"]
CATEGORIES = ["revenue-facing", "operations", "founder-leverage"]
STATUSES = ["probation", "stable", "deprecated"]
RELIABILITY = ["unverified", "measured", "disputed"]

MAX_DESCRIPTION = 1024
MIN_REFS, MAX_REFS = 3, 6

SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{20,}", "possible API key"),
    (r"AKIA[0-9A-Z]{16}", "possible AWS key"),
    (r"ghp_[A-Za-z0-9]{30,}", "possible GitHub token"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
]

errors = []
warnings = []
drift = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    block, body = text[3:end].strip(), text[end + 4:]
    data, key = {}, None
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            data[key] = m.group(2).strip()
        elif key and line.strip():
            data[key] = (data[key] + " " + line.strip()).strip()
    return data, body


def check_v2_skill(folder, name, fm, body):
    """Everything the v2 standard adds. Called only for standard_version 2."""
    desc = fm.get("description", "")
    if not desc:
        err("%s: v2 skill has no description" % name)
    elif len(desc) >= MAX_DESCRIPTION:
        err("%s: description is %d chars, must be under %d"
            % (name, len(desc), MAX_DESCRIPTION))

    heads = [l.strip()[3:].strip() for l in body.splitlines() if l.startswith("## ")]
    if heads != SECTIONS:
        missing = [s for s in SECTIONS if s not in heads]
        extra = [h for h in heads if h not in SECTIONS]
        order_ok = [h for h in heads if h in SECTIONS] == [s for s in SECTIONS if s in heads]
        if missing:
            err("%s: missing required section(s): %s" % (name, "; ".join(missing)))
        if extra:
            err("%s: section(s) outside the fixed order: %s" % (name, "; ".join(extra)))
        if missing == [] and extra == [] and not order_ok:
            err("%s: sections are in the wrong order - see docs/standard-v2.md" % name)

    # references
    refs_dir = os.path.join(folder, "references")
    refs = sorted(f for f in os.listdir(refs_dir) if f.endswith(".md")) if os.path.isdir(refs_dir) else []
    if not MIN_REFS <= len(refs) <= MAX_REFS:
        err("%s: %d reference files, v2 requires %d-%d" % (name, len(refs), MIN_REFS, MAX_REFS))
    for r in refs:
        if ("references/" + r) not in body:
            err("%s: reference %s is never routed to from SKILL.md" % (name, r))
        if os.path.getsize(os.path.join(refs_dir, r)) < 1500:
            err("%s: reference %s is under 1500 bytes - too thin to be craft" % (name, r))

    # deterministic script with a passing self-test
    scr_dir = os.path.join(folder, "scripts")
    # validate_skill.py is the per-skill wrapper, not a deterministic script.
    scripts = sorted(f for f in os.listdir(scr_dir)
                     if f.endswith(".py") and f != "validate_skill.py") \
        if os.path.isdir(scr_dir) else []
    if not scripts:
        err("%s: no script in scripts/ - v2 requires a deterministic script" % name)
    for s in scripts:
        path = os.path.join(scr_dir, s)
        if "--self-test" not in open(path, encoding="utf-8").read():
            err("%s: scripts/%s has no --self-test" % (name, s))
            continue
        r = subprocess.run([sys.executable, path, "--self-test"],
                           capture_output=True, text=True, cwd=folder)
        if r.returncode != 0:
            err("%s: scripts/%s --self-test failed:\n%s%s"
                % (name, s, r.stdout.strip(), r.stderr.strip()[-600:]))

    # one asset template
    assets_dir = os.path.join(folder, "assets")
    assets = [f for f in os.listdir(assets_dir)
              if f.endswith(".md")] if os.path.isdir(assets_dir) else []
    if not assets:
        err("%s: no asset template in assets/" % name)
    for a in assets:
        if ("assets/" + a) not in body:
            err("%s: asset %s is never referenced from SKILL.md" % (name, a))

    # evals
    ev_path = os.path.join(folder, "evals.json")
    if not os.path.isfile(ev_path):
        err("%s: evals.json missing" % name)
    else:
        try:
            ev = json.load(open(ev_path, encoding="utf-8"))
        except ValueError as e:
            err("%s: evals.json does not parse: %s" % (name, e))
            ev = None
        if ev:
            cases = ev.get("cases") or []
            if len(cases) != 5:
                err("%s: evals.json has %d cases, v2 requires exactly 5" % (name, len(cases)))
            got = [c.get("type") for c in cases]
            for t in EVAL_TYPES:
                if t not in got:
                    err("%s: evals.json is missing the %r case" % (name, t))
            ids = [c.get("id") for c in cases]
            if len(set(ids)) != len(ids):
                err("%s: evals.json has duplicate case ids" % name)
            for c in cases:
                cid = c.get("id", "?")
                if not (c.get("prompt") or "").strip():
                    err("%s: eval %s has no prompt" % (name, cid))
                if not (c.get("pass_criteria") or "").strip():
                    err("%s: eval %s has no pass_criteria" % (name, cid))
                expects = c.get("expects") or {}
                if not expects.get("must_include"):
                    err("%s: eval %s has no must_include" % (name, cid))
                if c.get("type") == "missing_connector" and not expects.get("must_name_connector"):
                    err("%s: eval %s does not name the connector that must be named" % (name, cid))
                if c.get("type") in ("wrong_tool", "handoff") and not expects.get("routes_to"):
                    err("%s: eval %s must declare routes_to" % (name, cid))

    # notes.seed - schema only
    seed = os.path.join(folder, "notes.seed")
    if not os.path.isdir(seed):
        err("%s: no notes.seed/ - v2 ships an empty schema, not filled notes" % name)
    else:
        for need in ("learnings.md", "contacts.md", "decisions.md"):
            if not os.path.isfile(os.path.join(seed, need)):
                err("%s: notes.seed/%s missing" % (name, need))
        journal = os.path.join(seed, "journal")
        jfiles = sorted(f for f in os.listdir(journal)
                        if f.endswith(".md")) if os.path.isdir(journal) else []
        if not jfiles:
            err("%s: notes.seed/journal/YYYY-MM.md missing" % name)
        for f in jfiles:
            if not re.match(r"^\d{4}-\d{2}\.md$", f):
                err("%s: notes.seed/journal/%s is not named YYYY-MM.md" % (name, f))
        for dirpath, _, files in os.walk(seed):
            for f in files:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(dirpath, f)
                rel = os.path.relpath(p, folder)
                body_txt = open(p, encoding="utf-8").read()
                if "How to fill this" not in body_txt:
                    warn("%s: %s has no 'How to fill this' guidance" % (name, rel))
                for ln in body_txt.splitlines():
                    if re.match(r"^\s*[-*]\s*\d{4}-\d{2}-\d{2}", ln):
                        err("%s: %s contains a dated entry - notes.seed must be empty" % (name, rel))
                    if ln.strip().startswith("|"):
                        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                        if all(re.fullmatch(r":?-{2,}:?", c) or not c for c in cells):
                            continue
                        if any(c not in HEADER_WORDS for c in cells if c):
                            err("%s: %s has a filled table row (%r) - schema only"
                                % (name, rel, ln.strip()[:60]))


HEADER_WORDS = {
    "Date", "Learning", "Why it matters", "Name", "Role", "What for", "Last useful",
    "Notes", "Decision", "Reason", "By", "Task", "Outcome", "What to do differently",
}


def check_registry_entry(entry):
    name = entry.get("name", "?")
    if entry.get("standard_version") != 2:
        return
    if entry.get("level") not in LEVELS:
        err("registry: %s level %r is not one of %s" % (name, entry.get("level"), LEVELS))
    if entry.get("category") not in CATEGORIES:
        err("registry: %s category %r is not one of %s" % (name, entry.get("category"), CATEGORIES))
    if not isinstance(entry.get("permissions"), list) or not entry["permissions"]:
        err("registry: %s has no permissions list" % name)
    cost = entry.get("cost")
    if not isinstance(cost, dict) or not cost.get("tier"):
        err("registry: %s has no cost object with a tier" % name)
    conn = entry.get("connectors")
    if not isinstance(conn, dict):
        err("registry: %s has no connectors object" % name)
    else:
        for k in ("required", "available_in_catalog", "works_without"):
            if k not in conn:
                err("registry: %s connectors.%s missing" % (name, k))
        if isinstance(conn.get("required"), list) and isinstance(conn.get("available_in_catalog"), list):
            stray = [c for c in conn["required"] if c not in conn["available_in_catalog"]]
            if stray:
                err("registry: %s requires connectors not in the catalog: %s" % (name, stray))
    if entry.get("status") not in STATUSES:
        err("registry: %s status %r is not one of %s" % (name, entry.get("status"), STATUSES))
    if entry.get("reliability") not in RELIABILITY:
        err("registry: %s reliability %r is not one of %s"
            % (name, entry.get("reliability"), RELIABILITY))


def main():
    strict = "--strict" in sys.argv
    only = None
    if "--skill" in sys.argv:
        only = sys.argv[sys.argv.index("--skill") + 1]

    for c in CORE_FILES:
        if not os.path.isfile(os.path.join(ROOT, c)):
            err("core standard incomplete: missing %s" % c)

    reg_path = os.path.join(ROOT, "registry.json")
    if not os.path.isfile(reg_path):
        print("ERROR: registry.json missing")
        return 1
    registry = json.load(open(reg_path, encoding="utf-8"))
    employees = registry.get("employees", [])
    names = [e.get("name") for e in employees]
    if len(names) != len(set(names)):
        err("duplicate names in registry")

    skills_dir = os.path.join(ROOT, "skills")
    on_disk = sorted(d for d in os.listdir(skills_dir)
                     if os.path.isdir(os.path.join(skills_dir, d))) if os.path.isdir(skills_dir) else []

    for n in names:
        if n not in on_disk:
            err("registry lists %r but skills/%s does not exist" % (n, n))
    for d in on_disk:
        if d not in names:
            err("skills/%s exists but is not in registry.json" % d)

    backlog = open(os.path.join(ROOT, "BACKLOG.md"), encoding="utf-8").read() \
        if os.path.isfile(os.path.join(ROOT, "BACKLOG.md")) else ""
    changelog = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read() \
        if os.path.isfile(os.path.join(ROOT, "CHANGELOG.md")) else ""
    backlog_roles = set(re.findall(r"`([a-z0-9][a-z0-9-]*)`", backlog))
    known_roles = set(names) | backlog_roles

    for n in names:
        if n not in changelog:
            warn("skill %r has no CHANGELOG entry" % n)
        if "`%s`" % n not in backlog:
            warn("skill %r not listed in BACKLOG.md" % n)

    for e in employees:
        check_registry_entry(e)

    v2_count = 0
    for d in on_disk:
        if only and d != only:
            continue
        folder = os.path.join(skills_dir, d)
        path = os.path.join(folder, "SKILL.md")
        if not os.path.isfile(path):
            err("skills/%s has no SKILL.md" % d)
            continue
        text = open(path, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        if fm is None:
            err("%s: missing YAML frontmatter" % d)
            fm = {}

        if fm.get("name") and fm["name"] != d:
            err("%s: frontmatter name %r does not match the folder" % (d, fm["name"]))
        for link, label in BASELINE_LINKS:
            if link not in body:
                err("%s: Employee Standard not wired in - no %s (%s)" % (d, label, link))
        for sec in ("Routing", "Guardrails"):
            if sec.lower() not in body.lower():
                err("%s: missing required section %r" % (d, sec))
        for link in sorted(set(re.findall(r"`(references/[\w./-]+\.md)`", body))):
            if not os.path.isfile(os.path.join(folder, link)):
                err("%s: broken reference link %s" % (d, link))
        for link in sorted(set(re.findall(r"`(assets/[\w./-]+\.md)`", body))):
            if not os.path.isfile(os.path.join(folder, link)):
                err("%s: broken asset link %s" % (d, link))

        entry = next((x for x in employees if x.get("name") == d), {})
        declared = str(fm.get("standard_version", "")).strip()
        reg_v2 = entry.get("standard_version") == 2
        if declared == "2" or reg_v2:
            v2_count += 1
            if declared != "2":
                err("%s: registry says standard_version 2 but frontmatter does not" % d)
            if not reg_v2:
                err("%s: frontmatter says standard_version 2 but the registry entry does not" % d)
            check_v2_skill(folder, d, fm, body)
            # routing targets in evals must be real roles
            ev_path = os.path.join(folder, "evals.json")
            if os.path.isfile(ev_path):
                try:
                    ev = json.load(open(ev_path, encoding="utf-8"))
                except ValueError:
                    ev = {}
                for c in ev.get("cases", []):
                    target = (c.get("expects") or {}).get("routes_to")
                    if target and target not in known_roles:
                        err("%s: eval %s routes to %r, which is not a role in the registry or backlog"
                            % (d, c.get("id"), target))
        else:
            if len(fm.get("description", "")) >= MAX_DESCRIPTION:
                drift.append("%s: description is %d chars, over the v2 limit of %d"
                             % (d, len(fm.get("description", "")), MAX_DESCRIPTION))

    # secrets
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [x for x in dirnames if x not in (".git", "__pycache__", "node_modules")]
        for fn in filenames:
            if fn.endswith((".md", ".json", ".py", ".txt", ".yml", ".yaml")):
                p = os.path.join(dirpath, fn)
                try:
                    body_txt = open(p, encoding="utf-8", errors="ignore").read()
                except OSError:
                    continue
                for pat, label in SECRET_PATTERNS:
                    if re.search(pat, body_txt):
                        err("%s: %s" % (os.path.relpath(p, ROOT), label))

    queued = backlog.count("| queued |")
    if queued < 50:
        warn("only %d queued roles - under 10 days of runway at 5 per day" % queued)

    if strict:
        for w in warnings:
            errors.append("strict: " + w)

    print("repo: %s v%s | employees: %d | folders: %d | v2 skills: %d | queued: %d"
          % (registry.get("name"), registry.get("version"), len(names), len(on_disk), v2_count, queued))
    print("mode: %s" % ("strict" if strict else "normal"))
    for e in errors:
        print("  ERROR   " + e)
    for w in warnings:
        print("  warning " + w)
    for d in drift:
        print("  DRIFT   " + d)
    print("RESULT: %s (%d errors, %d warnings, %d drift)"
          % ("PASS" if not errors else "FAIL", len(errors), len(warnings), len(drift)))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
