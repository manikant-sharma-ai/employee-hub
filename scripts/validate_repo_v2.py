#!/usr/bin/env python3
"""Validate the employee-hub repo against the v2 employee standard.

v1 asked whether a skill was wired to the Employee Standard. v2 asks whether the
employee is shippable: does it declare what it may touch, what it costs and how far
it has been checked; does it carry the full tree (references, a deterministic
script, an asset, evals, a notes schema); and do the evals actually resolve against
the files on disk.

Checks, in order:

  A  core standard present, including the v2 levels document
  B  registry parses, folders match, v2 profile fields complete and in range
  C  every skill: frontmatter, description under 1024 characters, fixed section
     order, 3-6 routed references, an asset, a script whose --self-test passes,
     evals.json with the five case types, notes.seed/ schema only, notes/ seeded
  D  the legacy validators (skill, repo, manifests, capability audit) still pass
  E  changelog and backlog reflect every registered employee
  F  no secrets committed
  G  the eval harness: each case's expectations resolve against the skill corpus

Usage:
  python3 scripts/validate_repo_v2.py            # errors fail, warnings do not
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
errors, warnings, notes = [], [], []

LEVELS = ["L0", "L1", "L2", "L3", "L4"]
CATEGORIES = ["revenue", "operations", "founder-leverage", "product", "infrastructure"]
STATUSES = ["probation", "stable", "retired"]
RELIABILITY = ["unverified", "measured", "degraded"]
MODEL_TIERS = ["small", "standard", "frontier"]
PERMISSION_KEYS = ["read", "write", "send", "spend", "delete"]
CASE_TYPES = ["happy_path", "thin_brief", "missing_connector", "wrong_tool", "handoff"]
MAX_DESCRIPTION = 1024
SECTION_ORDER = [
    "what you are accountable for",
    "what you must be handed before you start",
    "tools it assumes",
    "routing: read the request, load the craft",
    "the workflow",
    "standards you hold yourself to",
    "notes and self-tracking",
    "output contract",
    "guardrails",
    "trigger test",
]
SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{20,}", "possible API key"),
    (r"AKIA[0-9A-Z]{16}", "possible AWS key"),
    (r"ghp_[A-Za-z0-9]{30,}", "possible GitHub token"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
]


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------- A: core files
CORE_FILES = [
    "core/employee-standard.md",
    "core/connector-preflight.md",
    "core/connector-catalog.md",
    "core/memory-and-notes.md",
    "core/performance-tracking.md",
    "docs/levels-and-permissions.md",
]
for c in CORE_FILES:
    if not os.path.isfile(os.path.join(ROOT, c)):
        err("core standard incomplete: missing %s" % c)

# ---------------------------------------------------------------- B: registry
registry = json.loads(read(os.path.join(ROOT, "registry.json")))
employees = registry.get("employees", [])
names = [e.get("name") for e in employees]
if len(names) != len(set(names)):
    err("duplicate names in registry.json")

skills_dir = os.path.join(ROOT, "skills")
backlog_text = read(os.path.join(ROOT, "BACKLOG.md"))
on_disk = sorted(d for d in os.listdir(skills_dir)
                 if os.path.isdir(os.path.join(skills_dir, d)))
for n in names:
    if n not in on_disk:
        err("registry lists %r but skills/%s does not exist" % (n, n))
for d in on_disk:
    if d not in names:
        err("skills/%s exists but is not in registry.json" % d)


def check_profile(emp):
    """v2 profile fields. Required for employees that declare profile_version >= 2."""
    n = emp["name"]
    if emp.get("profile_version", 1) < 2:
        notes.append("%s: legacy profile (v1) - no level, permissions or cost declared" % n)
        return
    level = emp.get("level")
    if level not in LEVELS:
        err("%s: level %r is not one of %s" % (n, level, ", ".join(LEVELS)))
    if emp.get("category") not in CATEGORIES:
        err("%s: category %r is not one of %s" % (n, emp.get("category"), ", ".join(CATEGORIES)))
    if emp.get("status") not in STATUSES:
        err("%s: status %r is not one of %s" % (n, emp.get("status"), ", ".join(STATUSES)))
    if emp.get("reliability") not in RELIABILITY:
        err("%s: reliability %r is not one of %s"
            % (n, emp.get("reliability"), ", ".join(RELIABILITY)))
    if emp.get("status") == "probation" and emp.get("reliability") == "measured":
        err("%s: probation with measured reliability - one of the two is wrong" % n)

    perms = emp.get("permissions")
    if not isinstance(perms, dict):
        err("%s: permissions missing or not an object" % n)
        perms = {}
    for key in PERMISSION_KEYS:
        if not isinstance(perms.get(key), list):
            err("%s: permissions.%s missing or not a list" % (n, key))
    if level in ("L0", "L1"):
        for key in ("send", "spend"):
            if perms.get(key):
                err("%s: %s may not have permissions.%s - drafts, never sends or spends"
                    % (n, level, key))
    if level == "L0" and (perms.get("write") or perms.get("send")):
        err("%s: L0 may not write or send" % n)
    if perms.get("delete"):
        err("%s: no employee in this hub holds delete" % n)

    cost = emp.get("cost")
    if not isinstance(cost, dict):
        err("%s: cost missing or not an object" % n)
    else:
        if cost.get("model_tier") not in MODEL_TIERS:
            err("%s: cost.model_tier %r is not one of %s"
                % (n, cost.get("model_tier"), ", ".join(MODEL_TIERS)))
        band = cost.get("est_cost_inr_per_task")
        if not (isinstance(band, list) and len(band) == 2
                and all(isinstance(x, (int, float)) for x in band) and band[0] <= band[1]):
            err("%s: cost.est_cost_inr_per_task must be [low, high] in rupees" % n)
        if not isinstance(cost.get("est_tokens_per_task"), int):
            err("%s: cost.est_tokens_per_task must be an integer" % n)
        if not isinstance(cost.get("paid_tools"), list):
            err("%s: cost.paid_tools must be a list, empty if none" % n)
        if not cost.get("basis"):
            err("%s: cost.basis missing - a range with no basis is a guess" % n)

    conn = emp.get("connectors")
    if not isinstance(conn, dict):
        err("%s: connectors missing or not an object" % n)
    else:
        if not isinstance(conn.get("available"), list) or not conn.get("available"):
            err("%s: connectors.available must list at least one connector" % n)
        if not isinstance(conn.get("needs_setup"), list):
            err("%s: connectors.needs_setup must be a list, empty if none" % n)
        if not isinstance(conn.get("usable_on_day_one"), bool):
            err("%s: connectors.usable_on_day_one must be true or false" % n)
        if conn.get("usable_on_day_one") is False:
            err("%s: usable_on_day_one is false - a skill nobody can start is not shippable" % n)
        if not conn.get("fallback"):
            err("%s: connectors.fallback missing - say what works without the connector" % n)


for emp in employees:
    check_profile(emp)

# ---------------------------------------------------------------- C: each skill
corpus_cache = {}
eval_total = 0
eval_passed = 0
eval_failures = []


def corpus(folder):
    if folder in corpus_cache:
        return corpus_cache[folder]
    parts = []
    for base in ("SKILL.md", "references", "assets"):
        path = os.path.join(folder, base)
        if os.path.isfile(path):
            parts.append(read(path))
        elif os.path.isdir(path):
            for fn in sorted(os.listdir(path)):
                if fn.endswith(".md"):
                    parts.append(read(os.path.join(path, fn)))
    text = "\n".join(parts).lower()
    corpus_cache[folder] = text
    return text


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    data, key = {}, None
    for line in text[3:end].strip().splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            data[key] = m.group(2).strip()
        elif key and line.strip():
            data[key] = (data[key] + " " + line.strip()).strip()
    return data, text[end + 4:]


v2_skills = 0
for emp in employees:
    n = emp["name"]
    folder = os.path.join(skills_dir, n)
    if not os.path.isdir(folder):
        continue
    is_v2 = emp.get("profile_version", 1) >= 2
    if not is_v2:
        # Legacy employees are held to v1 (validate_repo.py + validate_skill.py).
        # The v2 tree is required from the drop that introduced the standard, and
        # backfilled one employee at a time - see docs/levels-and-permissions.md.
        continue
    v2_skills += 1
    skill_path = os.path.join(folder, "SKILL.md")
    if not os.path.isfile(skill_path):
        err("%s: SKILL.md missing" % n)
        continue
    text = read(skill_path)
    fm = frontmatter(text)
    if fm is None:
        err("%s: missing YAML frontmatter" % n)
        fm, body = {}, text
    else:
        fm, body = fm
    if fm.get("name") != n:
        err("%s: frontmatter name %r does not match the folder" % (n, fm.get("name")))
    desc = fm.get("description", "")
    if not desc:
        err("%s: description missing" % n)
    elif len(desc) > MAX_DESCRIPTION:
        err("%s: description is %d characters (max %d)"
            % (n, len(desc), MAX_DESCRIPTION))
    if not fm.get("version"):
        warn("%s: frontmatter version missing" % n)

    lowered = body.lower()
    positions = []
    for heading in SECTION_ORDER:
        idx = lowered.find("## " + heading)
        if idx == -1:
            idx = lowered.find("### " + heading)
        if idx == -1:
            err("%s: missing section %r" % (n, heading))
        positions.append((idx, heading))
    found = [h for i, h in positions if i >= 0]
    found_idx = [i for i, _ in positions if i >= 0]
    if found_idx != sorted(found_idx):
        err("%s: sections are out of the fixed order - %s" % (n, " > ".join(found)))

    refs_dir = os.path.join(folder, "references")
    refs = sorted(f[:-3] for f in os.listdir(refs_dir) if f.endswith(".md")) \
        if os.path.isdir(refs_dir) else []
    if not 3 <= len(refs) <= 6:
        err("%s: %d references (must be 3-6)" % (n, len(refs)))
    for stem in refs:
        rel = "references/%s.md" % stem
        if rel not in body:
            err("%s: %s is never routed from SKILL.md" % (n, rel))
        if os.path.getsize(os.path.join(refs_dir, stem + ".md")) < 1500:
            warn("%s: %s is thin (<1500 bytes)" % (n, rel))

    assets_dir = os.path.join(folder, "assets")
    assets = [f for f in os.listdir(assets_dir)] if os.path.isdir(assets_dir) else []
    if not assets:
        err("%s: no assets/ template - the role produces a document" % n)
    else:
        if not any(a in body for a in assets):
            err("%s: no asset template is referenced from SKILL.md" % n)

    scripts_dir = os.path.join(folder, "scripts")
    scripts = sorted(f for f in os.listdir(scripts_dir) if f.endswith(".py")) \
        if os.path.isdir(scripts_dir) else []
    if not scripts:
        err("%s: no deterministic script - the arithmetic must not be improvised" % n)
    selftested = False
    for s in scripts:
        path = os.path.join(scripts_dir, s)
        body_py = read(path)
        if "--self-test" not in body_py:
            continue
        selftested = True
        r = subprocess.run([sys.executable, path, "--self-test"],
                           capture_output=True, text=True, cwd=folder)
        if r.returncode != 0:
            err("%s: scripts/%s --self-test failed\n%s"
                % (n, s, (r.stdout + r.stderr).strip()[:600]))
    if not selftested:
        err("%s: no script exposes a passing --self-test" % n)

    evals_path = os.path.join(folder, "evals.json")
    if not os.path.isfile(evals_path):
        err("%s: evals.json missing" % n)
    else:
        try:
            evals = json.loads(read(evals_path))
        except ValueError as exc:
            err("%s: evals.json does not parse: %s" % (n, exc))
            evals = {}
        cases = evals.get("cases", [])
        if len(cases) != 5:
            err("%s: %d eval cases (must be exactly 5)" % (n, len(cases)))
        types = [c.get("type") for c in cases]
        for t in CASE_TYPES:
            if t not in types:
                err("%s: eval case type %r missing" % (n, t))
        text_corpus = corpus(folder)
        for case in cases:
            eval_total += 1
            cid = case.get("id", "?")
            problems = []
            if not case.get("input") or len(case["input"]) < 20:
                problems.append("input missing or too thin to be a test")
            if not case.get("pass_criteria"):
                problems.append("pass_criteria missing")
            exp = case.get("expects", {})
            terms = exp.get("must_include_any", [])
            if not terms:
                problems.append("expects.must_include_any missing")
            elif not any(t.lower() in text_corpus for t in terms):
                problems.append("none of the expected terms appear in the skill")
            for banned in exp.get("must_not", []):
                if banned.lower() in text_corpus:
                    problems.append("the skill contains the forbidden phrase %r" % banned)
            route = exp.get("routes_to")
            if route and not os.path.isfile(os.path.join(folder, route)):
                if route.startswith("core/"):
                    if not os.path.isfile(os.path.join(ROOT, route)):
                        problems.append("routes_to %r does not exist" % route)
                else:
                    problems.append("routes_to %r does not exist" % route)
            for key in ("handoff", "wrong_owner"):
                target = exp.get(key)
                if target and target == n:
                    problems.append("%s target is the skill itself" % key)
                elif target and target not in names:
                    if "`%s`" % target in backlog_text:
                        notes.append("%s/%s: %s target %r is queued, not shipped - the eval "
                                     "must name its backlog number" % (n, cid, key, target))
                    else:
                        problems.append("%s target %r is neither a registered employee nor a "
                                        "backlog role" % (key, target))
            connector = exp.get("connector")
            if connector:
                declared = (emp.get("connectors") or {}).get("needs_setup", [])
                if not any(connector.lower() in c.lower() for c in declared):
                    problems.append("eval names connector %r that the registry does not list "
                                    "under connectors.needs_setup" % connector)
            if problems:
                eval_failures.append("%s/%s: %s" % (n, cid, "; ".join(problems)))
            else:
                eval_passed += 1

    seed_dir = os.path.join(folder, "notes.seed")
    if not os.path.isdir(seed_dir):
        err("%s: notes.seed/ missing - there is no schema for what the employee learns" % n)
    else:
        for need in ("learnings.md", "contacts.md", "decisions.md"):
            if not os.path.isfile(os.path.join(seed_dir, need)):
                err("%s: notes.seed/%s missing" % (n, need))
        journal = os.path.join(seed_dir, "journal")
        if not os.path.isdir(journal) or not any(f.endswith(".md") for f in os.listdir(journal)):
            err("%s: notes.seed/journal/ missing or empty" % n)
        for dirpath, _, filenames in os.walk(seed_dir):
            for fn in filenames:
                p = os.path.join(dirpath, fn)
                rel = os.path.relpath(p, folder)
                body_seed = read(p)
                if fn == "README.md":
                    continue  # documents the schema; it is not a note
                if re.search(r"\b20\d\d-\d\d-\d\d\b", body_seed):
                    err("%s: %s contains a dated entry - the seed must be schema only" % (n, rel))
                seed_lines = body_seed.splitlines()
                for idx, line in enumerate(seed_lines):
                    s = line.strip()
                    if not s.startswith("|") or re.match(r"^\|[\s|:-]+\|$", s):
                        continue
                    nxt = seed_lines[idx + 1].strip() if idx + 1 < len(seed_lines) else ""
                    if re.match(r"^\|[\s|:-]+\|$", nxt):
                        continue  # header row, followed by the separator
                    cells = [c.strip() for c in s.strip("|").split("|")]
                    # A row is filled when a value column (anything after the label
                    # column) carries content. A metric name with an empty value is
                    # the schema, which is exactly what a seed file should contain.
                    values = [c for c in cells[1:]
                              if c and not c.startswith("<") and not re.match(r"^[#\d]$", c)]
                    if values:
                        err("%s: %s has a filled table row (%r) - no fabricated experience"
                            % (n, rel, s[:70]))
                        break

    notes_dir = os.path.join(folder, "notes")
    if not os.path.isdir(notes_dir):
        err("%s: notes/ missing" % n)
    else:
        for need in ("learnings.md", "contacts.md", "decisions.md"):
            if not os.path.isfile(os.path.join(notes_dir, need)):
                warn("%s: notes/%s missing" % (n, need))
        journal = os.path.join(notes_dir, "journal")
        if not os.path.isdir(journal) or not any(f.endswith(".md") for f in os.listdir(journal)):
            warn("%s: notes/journal/ has no month file" % n)

    for link in set(re.findall(r"`(references/[\w./-]+\.md)`", body)):
        if not os.path.isfile(os.path.join(folder, link)):
            err("%s: broken reference link %s" % (n, link))

# ---------------------------------------------------------------- D: legacy gates
for script, label in (("scripts/validate_repo.py", "repo"),
                      ("scripts/validate_manifests.py", "manifests"),
                      ("scripts/audit_capabilities.py", "capability audit")):
    r = subprocess.run([sys.executable, os.path.join(ROOT, script)],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        tail = [l for l in (r.stdout + r.stderr).splitlines()
                if "ERROR" in l or "GAP" in l or "RESULT" in l]
        err("%s validator failed: %s" % (label, " | ".join(tail[-4:]) or "see output"))
    else:
        notes.append("%s validator passed" % label)

# ---------------------------------------------------------------- E: changelog, backlog
changelog = read(os.path.join(ROOT, "CHANGELOG.md"))
backlog = read(os.path.join(ROOT, "BACKLOG.md"))
for emp in employees:
    n = emp["name"]
    if n not in changelog:
        warn("%s: no CHANGELOG entry" % n)
    if "`%s`" % n not in backlog:
        warn("%s: not listed in BACKLOG.md" % n)
    elif emp.get("status") in ("stable", "probation"):
        row = re.search(r"\|[^|\n]*`%s`[^|\n]*\|[^|\n]*\|\s*([^|\n]+)\|" % re.escape(n), backlog)
        if row and "shipped" not in row.group(1):
            err("%s: registered as %s but BACKLOG.md says %r"
                % (n, emp.get("status"), row.group(1).strip()))

queued = backlog.count("| queued |")
if queued < 40:
    warn("only %d queued roles in the backlog - under 8 days of runway" % queued)

# ---------------------------------------------------------------- F: secrets
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [x for x in dirnames if x not in (".git", "__pycache__", "node_modules")]
    for fn in filenames:
        if fn.endswith((".md", ".json", ".py", ".txt", ".yml", ".yaml")):
            p = os.path.join(dirpath, fn)
            body_file = read(p)
            for pat, label in SECRET_PATTERNS:
                if re.search(pat, body_file):
                    err("%s: %s" % (os.path.relpath(p, ROOT), label))

# ---------------------------------------------------------------- G: eval harness
for failure in eval_failures:
    err("eval failed - " + failure)
if eval_total and eval_passed != eval_total:
    err("eval harness: %d of %d cases failed" % (eval_total - eval_passed, eval_total))

# ---------------------------------------------------------------- report
v2_profiles = sum(1 for e in employees if e.get("profile_version", 1) >= 2)
print("employee-hub v2 | employees: %d | skills on disk: %d | v2 profiles: %d "
      "(legacy %d held to v1)" % (len(names), len(on_disk), v2_profiles,
                                  len(names) - v2_profiles))
print("references: %d | assets: %d | scripts: %d | queued in backlog: %d"
      % (sum(len(os.listdir(os.path.join(skills_dir, d, "references")))
             for d in on_disk if os.path.isdir(os.path.join(skills_dir, d, "references"))),
         sum(len(os.listdir(os.path.join(skills_dir, d, "assets")))
             for d in on_disk if os.path.isdir(os.path.join(skills_dir, d, "assets"))),
         sum(len([f for f in os.listdir(os.path.join(skills_dir, d, "scripts")) if f.endswith(".py")])
             for d in on_disk if os.path.isdir(os.path.join(skills_dir, d, "scripts"))),
         queued))
print("EVALS: %d/%d passed" % (eval_passed, eval_total))
for e in errors:
    print("  ERROR   " + e)
for w in warnings:
    print("  warning " + w)
for nt in notes:
    print("  note    " + nt)

if STRICT and warnings:
    errors.extend(warnings)
    warnings = []
print("RESULT: %s (%d errors, %d warnings%s)"
      % ("PASS" if not errors else "FAIL", len(errors), len(warnings),
         ", strict" if STRICT else ""))
sys.exit(0 if not errors else 1)
