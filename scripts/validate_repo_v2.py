#!/usr/bin/env python3
"""Validate the employee-hub repo against the v2 employee standard.

v2 is the drop gate. It runs the v1 validator first, then adds the things v1
never asked for and a probation employee now has to prove:

  - description under 1024 characters (hard limit on every skill)
  - SKILL.md sections in the fixed order
  - three to six reference files, 50-160 lines each
  - at least one asset template
  - evals.json with the five required cases
  - notes.seed/ that is schema only - no invented experience
  - at least one deterministic script whose --self-test passes
  - registry entry carrying level, category, permissions, cost, connectors,
    status probation and reliability unverified (entries marked "schema": 2)
  - the batch mix: two revenue-facing, two operations, one founder-leverage
  - backlog, changelog, router and manifests agree with the registry

Usage:
    python3 scripts/validate_repo_v2.py            # errors fail, warnings print
    python3 scripts/validate_repo_v2.py --strict   # warnings fail too

Exit 0 = pass.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
TODAY = "2026-11-04"

DESC_LIMIT = 1024
DESC_WORD_LIMIT = 170

SECTION_ORDER = [
    "what you are accountable for",
    "what you must be handed before you start",
    "tools it assumes",
    "routing",
    "the workflow",
    "standards you hold yourself to",
    "notes and self-tracking",
    "output contract",
    "guardrails",
    "trigger test",
]

EVAL_TYPES = ["happy_path", "thin_brief", "missing_connector", "wrong_tool", "handoff"]
CATEGORIES = ["revenue-facing", "operations", "founder-leverage"]
LEVELS = ["L0", "L1", "L2", "L3", "L4"]
COST_BANDS = ["low", "medium", "high"]
CONNECTOR_STATES = ["connected", "needs_authorisation", "not_available"]

errors, warnings, infos = [], [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def info(msg):
    infos.append(msg)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


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


def check_v1():
    v1 = os.path.join(ROOT, "scripts", "validate_repo.py")
    r = subprocess.run([sys.executable, v1], capture_output=True, text=True)
    if r.returncode != 0:
        tail = "\n".join(l for l in r.stdout.splitlines() if "ERROR" in l)
        err("v1 repo validation failed:\n" + (tail or r.stdout.strip()))


def check_description(name, desc):
    if not desc:
        err("%s: description missing" % name)
        return
    if len(desc) > DESC_LIMIT:
        err("%s: description is %d characters, limit is %d" % (name, len(desc), DESC_LIMIT))
    words = len(desc.split())
    if words > DESC_WORD_LIMIT:
        warn("%s: description is %d words - trim below %d" % (name, words, DESC_WORD_LIMIT))
    if "use when" not in desc.lower():
        warn("%s: description has no 'Use when' clause" % name)
    if "not for" not in desc.lower():
        warn("%s: description has no 'Not for' boundary" % name)


def check_section_order(name, body):
    headings = [
        re.sub(r"^#+\s*", "", l).strip().lower()
        for l in body.splitlines()
        if l.startswith("## ")
    ]
    positions = []
    for want in SECTION_ORDER:
        hit = next((i for i, h in enumerate(headings) if h.startswith(want)), None)
        if hit is None:
            err("%s: missing section '## %s'" % (name, want.title()))
            return
        positions.append((want, hit))
    order = [i for _, i in positions]
    if order != sorted(order):
        err("%s: sections out of order - expected %s" % (name, " > ".join(SECTION_ORDER)))


def check_references(name, folder, body):
    refs = os.path.join(folder, "references")
    if not os.path.isdir(refs):
        err("%s: no references/ directory" % name)
        return 0
    files = sorted(f for f in os.listdir(refs) if f.endswith(".md"))
    if not 3 <= len(files) <= 6:
        err("%s: %d reference files, standard is 3-6" % (name, len(files)))
    for f in files:
        path = os.path.join(refs, f)
        lines = read(path).splitlines()
        if len(lines) < 50:
            err("%s: references/%s is %d lines, minimum is 50" % (name, f, len(lines)))
        elif len(lines) > 160:
            warn("%s: references/%s is %d lines - move the excess out" % (name, f, len(lines)))
        if "references/" + f not in body:
            err("%s: references/%s is never routed to from SKILL.md" % (name, f))
    return len(files)


def check_assets(name, folder):
    assets = os.path.join(folder, "assets")
    if not os.path.isdir(assets):
        err("%s: no assets/ directory - the role has no template to hand over" % name)
        return 0
    files = [f for f in os.listdir(assets) if not f.startswith(".")]
    if not files:
        err("%s: assets/ is empty" % name)
    for f in files:
        if os.path.getsize(os.path.join(assets, f)) < 400:
            warn("%s: assets/%s is under 400 bytes" % (name, f))
    return len(files)


def check_evals(name, folder):
    path = os.path.join(folder, "evals.json")
    if not os.path.isfile(path):
        err("%s: evals.json missing" % name)
        return 0
    try:
        data = json.loads(read(path))
    except json.JSONDecodeError as exc:
        err("%s: evals.json does not parse - %s" % (name, exc))
        return 0
    cases = data.get("cases", [])
    if data.get("employee") != name:
        err("%s: evals.json 'employee' is %r" % (name, data.get("employee")))
    seen_types, seen_ids = [], []
    for case in cases:
        cid = case.get("id", "")
        ctype = case.get("type", "")
        if not cid:
            err("%s: eval case without an id" % name)
        if cid in seen_ids:
            err("%s: duplicate eval id %r" % (name, cid))
        seen_ids.append(cid)
        if ctype not in EVAL_TYPES:
            err("%s: eval %r has unknown type %r" % (name, cid, ctype))
        seen_types.append(ctype)
        if not str(case.get("prompt", "")).strip():
            err("%s: eval %r has no prompt" % (name, cid))
        checks = case.get("checks") or []
        if len(checks) < 2:
            err("%s: eval %r has fewer than two checks" % (name, cid))
        for field in ("expect_owner", "expect_must", "expect_must_not"):
            if field not in case:
                err("%s: eval %r is missing %r" % (name, cid, field))
    for t in EVAL_TYPES:
        if t not in seen_types:
            err("%s: evals.json has no %r case" % (name, t))
    if len(cases) != 5:
        err("%s: %d eval cases, the standard is exactly 5" % (name, len(cases)))
    return len(cases)


DATE_ENTRY = re.compile(r"^\s*(?:[-*]\s*)?\*{0,2}(?:19|20)\d\d-\d\d(?:-\d\d)?\*{0,2}\b")


def check_notes_seed(name, folder):
    seed = os.path.join(folder, "notes.seed")
    if not os.path.isdir(seed):
        err("%s: no notes.seed/ directory" % name)
        return 0
    for need in ("learnings.md", "contacts.md", "decisions.md"):
        if not os.path.isfile(os.path.join(seed, need)):
            err("%s: notes.seed/%s missing" % (name, need))
    journal = os.path.join(seed, "journal")
    months = [f for f in os.listdir(journal) if re.match(r"^\d{4}-\d\d\.md$", f)] if os.path.isdir(journal) else []
    if len(months) != 1:
        err("%s: notes.seed/journal must hold exactly one YYYY-MM.md seed, found %d" % (name, len(months)))
    for dirpath, _, filenames in os.walk(seed):
        for f in filenames:
            if not f.endswith(".md"):
                continue
            path = os.path.join(dirpath, f)
            for n, line in enumerate(read(path).splitlines(), 1):
                if DATE_ENTRY.match(line):
                    err("%s: notes.seed/%s:%d carries a dated entry - seeds are schema only, never experience"
                        % (name, os.path.relpath(path, seed), n))
    return 1


def check_scripts(name, folder):
    scripts = os.path.join(folder, "scripts")
    if not os.path.isdir(scripts):
        err("%s: no scripts/ directory - no deterministic check to run" % name)
        return 0
    pys = sorted(f for f in os.listdir(scripts) if f.endswith(".py"))
    if not pys:
        err("%s: scripts/ holds no python file" % name)
        return 0
    tested = 0
    for f in pys:
        path = os.path.join(scripts, f)
        body = read(path)
        if "--self-test" not in body:
            err("%s: scripts/%s does not implement --self-test" % (name, f))
            continue
        r = subprocess.run([sys.executable, path, "--self-test"],
                           capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            err("%s: scripts/%s --self-test failed:\n%s" % (name, f, (r.stdout + r.stderr).strip()[-500:]))
        else:
            tested += 1
    return tested


def check_registry_entry(entry):
    name = entry.get("name")
    level = entry.get("level")
    if level not in LEVELS:
        err("%s: registry level %r is not one of %s" % (name, level, "/".join(LEVELS)))
    if entry.get("category") not in CATEGORIES:
        err("%s: registry category %r is not one of %s" % (name, entry.get("category"), ", ".join(CATEGORIES)))
    perms = entry.get("permissions")
    if not isinstance(perms, list) or not perms or not all(isinstance(p, str) and p for p in perms):
        err("%s: registry permissions must be a non-empty list of strings" % name)
    cost = entry.get("cost")
    if not isinstance(cost, dict):
        err("%s: registry cost must be an object" % name)
    else:
        if cost.get("band") not in COST_BANDS:
            err("%s: cost band %r is not one of %s" % (name, cost.get("band"), "/".join(COST_BANDS)))
        if not str(cost.get("driver", "")).strip():
            err("%s: cost has no driver - a band with no reason is a guess" % name)
    conn = entry.get("connectors")
    if not isinstance(conn, dict):
        err("%s: registry connectors must be an object" % name)
        return
    available = conn.get("available") or []
    required = conn.get("required") or []
    if not available:
        err("%s: connectors.available is empty" % name)
    if not required:
        err("%s: connectors.required is empty" % name)
    for item in available:
        if not isinstance(item, dict) or not item.get("name"):
            err("%s: connectors.available entries need a name" % name)
            continue
        if item.get("status") not in CONNECTOR_STATES:
            err("%s: connector %r status %r is not one of %s"
                % (name, item.get("name"), item.get("status"), "/".join(CONNECTOR_STATES)))
    if not any(i.get("status") == "connected" for i in available if isinstance(i, dict)):
        err("%s: no connector marked connected - the employee cannot work on day one" % name)
    if entry.get("status") != "probation":
        err("%s: new employee must ship with status 'probation', got %r" % (name, entry.get("status")))
    if entry.get("reliability") != "unverified":
        err("%s: new employee must ship with reliability 'unverified', got %r" % (name, entry.get("reliability")))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="warnings fail the gate too")
    args = ap.parse_args()

    check_v1()

    registry = json.loads(read(os.path.join(ROOT, "registry.json")))
    employees = registry.get("employees", [])
    by_name = {e["name"]: e for e in employees}
    changelog = read(os.path.join(ROOT, "CHANGELOG.md"))
    backlog = read(os.path.join(ROOT, "BACKLOG.md"))
    router = read(os.path.join(SKILLS, "employee-hub-router", "references", "role-map.md"))

    new = [e for e in employees if e.get("schema") == 2]
    if not new:
        err("registry holds no schema-2 employee - nothing to gate")

    for entry in new:
        check_registry_entry(entry)

    batch = [e for e in new if e.get("added") == TODAY]
    mix = {}
    for e in batch:
        mix[e.get("category")] = mix.get(e.get("category"), 0) + 1
    if len(batch) != 5:
        err("today's batch is %d employees, the drop is five" % len(batch))
    if mix.get("revenue-facing") != 2 or mix.get("operations") != 2 or mix.get("founder-leverage") != 1:
        err("today's batch breaks the 2-2-1 mix: %s" % json.dumps(mix, sort_keys=True))
    levels = [e.get("level") for e in batch]
    info("batch mix: %s | levels: %s" % (json.dumps(mix, sort_keys=True), ", ".join(map(str, levels))))

    total_evals = 0
    total_refs = 0
    total_scripts = 0
    for entry in new:
        name = entry["name"]
        folder = os.path.join(SKILLS, name)
        if not os.path.isdir(folder):
            err("%s: folder missing" % name)
            continue
        text = read(os.path.join(folder, "SKILL.md"))
        fm, body = parse_frontmatter(text)
        if fm is None:
            err("%s: no frontmatter" % name)
            fm, body = {}, text
        check_description(name, fm.get("description", ""))
        check_section_order(name, body)
        total_refs += check_references(name, folder, body)
        check_assets(name, folder)
        total_evals += check_evals(name, folder)
        check_notes_seed(name, folder)
        total_scripts += check_scripts(name, folder)
        lines = len(body.splitlines())
        if lines < 100:
            warn("%s: SKILL.md body is %d lines - too thin to be operational" % (name, lines))
        if "`%s`" % name not in backlog:
            err("%s: not in BACKLOG.md" % name)
        elif ("| `%s` |" % name) in backlog and ("shipped %s" % entry.get("added")) not in backlog:
            err("%s: backlog row is not marked shipped %s" % (name, entry.get("added")))
        if name not in changelog:
            err("%s: no CHANGELOG entry" % name)
        if name not in router:
            err("%s: missing from employee-hub-router's role map" % name)

    if ("## %s" % TODAY) not in changelog:
        err("CHANGELOG has no block for %s" % TODAY)

    # the 1024 character limit is enforced on every schema-2 employee. Entries
    # written before the limit existed are listed here as debt, so the next
    # description edit clears them rather than the gate hiding them.
    legacy = []
    for folder_name in sorted(os.listdir(SKILLS)):
        path = os.path.join(SKILLS, folder_name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        fm, _ = parse_frontmatter(read(path))
        if not fm:
            continue
        length = len(fm.get("description", ""))
        if length <= DESC_LIMIT:
            continue
        if folder_name in by_name and by_name[folder_name].get("schema") == 2:
            err("%s: description is %d characters, limit is %d"
                % (folder_name, length, DESC_LIMIT))
        else:
            legacy.append("%s (%d)" % (folder_name, length))
    if legacy:
        info("legacy descriptions over %d chars, trimmed at the next edit: %s"
             % (DESC_LIMIT, ", ".join(legacy)))

    # manifests must agree with the registry
    for rel, key_path in ((".claude-plugin/plugin.json", ["version"]),
                          (".claude-plugin/marketplace.json", ["version"]),
                          (".claude-plugin/marketplace.json", ["metadata", "version"])):
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            err("manifest missing: %s" % rel)
            continue
        data = json.loads(read(path))
        for key in key_path:
            data = data.get(key, {}) if isinstance(data, dict) else {}
        if data != registry.get("version"):
            err("%s %s is %r, registry is %r" % (rel, ".".join(key_path), data, registry.get("version")))

    print("v2 gate | %s | registry %s | employees %d | schema-2 %d | batch %d"
          % (TODAY, registry.get("version"), len(employees), len(new), len(batch)))
    for i in infos:
        print("  info    " + i)
    for e in errors:
        print("  ERROR   " + e)
    for w in warnings:
        print("  warning " + w)
    failed = len(errors) + (len(warnings) if args.strict else 0)
    print("checked: %d references, %d eval cases, %d self-tests"
          % (total_refs, total_evals, total_scripts))
    print("RESULT: %s (%d errors, %d warnings%s)"
          % ("PASS" if failed == 0 else "FAIL", len(errors), len(warnings),
             ", strict" if args.strict else ""))
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
