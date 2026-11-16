#!/usr/bin/env python3
"""Validate the whole employee-hub repo against the v2 employee standard.

Two layers, on purpose:

* **Layer 1 - the 2026-11-01 standard, unchanged.** Every skill must still pass
  `scripts/validate_skill.py`, the registry must match the folders on disk, the
  changelog must mention every employee, the backlog must keep runway, and no
  secret may be committed. Nothing that shipped before this gate existed is
  asked to meet a rule it was never written against.

* **Layer 2 - the v2 drop contract.** An employee whose registry entry carries
  `"standard_revision": "v2"` must also ship the full tree: a SKILL.md with the
  fixed section order, 3-6 reference files, at least one deterministic script
  that passes its own `--self-test`, one asset template, `evals.json` with the
  five required cases, and a `notes.seed/` that is schema only - no fabricated
  experience. Its registry entry must declare level, category, permissions,
  cost, connector availability, `status: probation` and `reliability:
  unverified`, and its frontmatter description must stay under 1024 characters.

`--strict` turns every warning into an error. Warnings raised about pre-v2
employees stay advisory even under `--strict`, because a rule added today
cannot retroactively fail a skill written three weeks ago - those are printed
in a separate advisory block and counted separately.

Usage:
    python3 scripts/validate_repo_v2.py             # gate, warnings advisory
    python3 scripts/validate_repo_v2.py --strict    # gate, zero tolerance
    python3 scripts/validate_repo_v2.py --skill skills/billing-support

Exit 0 = pass.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

CORE_FILES = [
    "core/employee-standard.md",
    "core/connector-preflight.md",
    "core/connector-catalog.md",
    "core/memory-and-notes.md",
    "core/performance-tracking.md",
]

# The fixed section order. Same headings, same sequence, in every v2 skill.
SECTION_ORDER = [
    "What you are accountable for",
    "What you must be handed before you start",
    "Tools it assumes",
    "Routing: read the request, load the craft",
    "The workflow",
    "Standards you hold yourself to",
    "Notes and self-tracking",
    "Output contract",
    "Guardrails",
    "Trigger test",
]

STANDARD_LINKS = [
    ("core/connector-preflight.md", "connector preflight"),
    ("core/memory-and-notes.md", "notes protocol"),
    ("core/performance-tracking.md", "performance tracking"),
]

EVAL_KINDS = ["happy_path", "thin_brief", "missing_connector", "wrong_tool", "handoff"]
LEVELS = ["L0", "L1", "L2", "L3", "L4"]
CATEGORIES = ["revenue", "operations", "founder-leverage"]
AVAILABILITY = ["core", "recommended", "optional", "rare"]
DESCRIPTION_CAP = 1024

SEED_FILES = ["learnings.md", "contacts.md", "decisions.md"]

SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{20,}", "possible API key"),
    (r"AKIA[0-9A-Z]{16}", "possible AWS key"),
    (r"ghp_[A-Za-z0-9]{30,}", "possible GitHub token"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
]

errors = []
warnings = []      # v2 scope - fatal under --strict
advisory = []      # pre-v2 scope - never fatal

STRICT = "--strict" in sys.argv
ONLY = None
if "--skill" in sys.argv:
    ONLY = sys.argv[sys.argv.index("--skill") + 1].rstrip("/")


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def note(msg):
    advisory.append(msg)


def parse_frontmatter(text):
    """Same tolerant parser validate_skill.py uses: flat keys, folded lines."""
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


def h2_headings(body):
    out = []
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m and not line.startswith("###"):
            out.append(m.group(1))
    return out


def is_schema_only(path):
    """A seed note is schema only if every line is a heading, a comment, a table
    header/rule, or carries a <placeholder>. Prose about things that happened is
    exactly what this rejects."""
    bad = []
    in_comment = False
    for i, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        if in_comment:
            if "-->" in s:
                in_comment = False
            continue
        if s.startswith("<!--"):
            in_comment = "-->" not in s
            continue
        if s.startswith("#"):
            continue
        if s.startswith("|") and set(s.replace("|", "").strip()) <= set("-: "):
            continue  # table rule
        if s.startswith("|") and ("Who" in s or "Date" in s or "Rule" in s or "Question" in s
                                  or "When" in s or "What" in s or "Where" in s):
            continue  # table header row
        if "<" in s and ">" in s:
            continue  # carries a placeholder
        bad.append((i, s[:90]))
    return bad


def check_skill_script(path):
    """Run `python3 <script> --self-test` and insist on exit 0."""
    r = subprocess.run([sys.executable, path, "--self-test"],
                       capture_output=True, text=True, timeout=120)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def check_determinism(path):
    body = open(path, encoding="utf-8").read()
    problems = []
    for mod in ("requests", "urllib", "socket", "httpx", "random"):
        if re.search(r"^\s*(import|from)\s+%s\b" % mod, body, re.M):
            problems.append("imports %s" % mod)
    if re.search(r"datetime\.now\(|time\.time\(|date\.today\(", body):
        problems.append("reads the wall clock")
    if not body.lstrip().startswith("#!") and not re.search(r'^"""', body, re.M):
        problems.append("no module docstring")
    return problems


def check_v2_employee(entry, folder):
    """Layer 2 for one v2 employee."""
    name = entry["name"]
    skill_md = os.path.join(folder, "SKILL.md")

    # --- frontmatter and description cap ---------------------------------
    text = open(skill_md, encoding="utf-8").read()
    fm, body = parse_frontmatter(text)
    if fm is None:
        err("%s: no YAML frontmatter" % name)
        return 0, 0
    desc = fm.get("description", "")
    if len(desc) >= DESCRIPTION_CAP:
        err("%s: description is %d chars, cap is %d" % (name, len(desc), DESCRIPTION_CAP))
    for need in ("Use when", "Trigger phrases", "Not for"):
        if need.lower() not in desc.lower():
            err("%s: description missing %r clause" % (name, need))
    if not fm.get("version"):
        err("%s: frontmatter version missing" % name)
    if not fm.get("license"):
        warn("%s: frontmatter license missing" % name)

    # --- fixed section order ---------------------------------------------
    found = h2_headings(body)
    if found != SECTION_ORDER:
        if set(found) != set(SECTION_ORDER):
            missing = [s for s in SECTION_ORDER if s not in found]
            extra = [s for s in found if s not in SECTION_ORDER]
            err("%s: section set wrong (missing %s; unexpected %s)" % (name, missing, extra))
        else:
            err("%s: sections out of order - got %s" % (name, " > ".join(found)))

    # --- standard wiring --------------------------------------------------
    for link, label in STANDARD_LINKS:
        if link not in body:
            err("%s: standard not wired - no %s (%s)" % (name, label, link))
    if "references/" not in body:
        err("%s: no reference is routed to from SKILL.md" % name)

    # --- references: 3 to 6, each real and routed ------------------------
    refs_dir = os.path.join(folder, "references")
    refs = sorted(f for f in os.listdir(refs_dir) if f.endswith(".md")) if os.path.isdir(refs_dir) else []
    if not 3 <= len(refs) <= 6:
        err("%s: %d reference files, the contract is 3-6" % (name, len(refs)))
    for f in refs:
        p = os.path.join(refs_dir, f)
        if os.path.getsize(p) < 1200:
            err("%s: reference %s is %d bytes - under the 1200-byte floor"
                % (name, f, os.path.getsize(p)))
        if ("references/" + f) not in body:
            err("%s: reference %s is never routed to" % (name, f))

    # --- scripts: deterministic, self-tested -----------------------------
    scr_dir = os.path.join(folder, "scripts")
    scripts = sorted(f for f in os.listdir(scr_dir) if f.endswith(".py")) if os.path.isdir(scr_dir) else []
    if not scripts:
        err("%s: no scripts/ - a v2 employee ships at least one deterministic script" % name)
    for f in scripts:
        p = os.path.join(scr_dir, f)
        if "--self-test" not in open(p, encoding="utf-8").read():
            err("%s: script %s has no --self-test" % (name, f))
            continue
        ok, out = check_skill_script(p)
        if not ok:
            err("%s: %s --self-test FAILED\n%s" % (name, f, out[-600:]))
        for problem in check_determinism(p):
            err("%s: script %s is not deterministic - %s" % (name, f, problem))
        if f not in body:
            warn("%s: script %s is never mentioned in SKILL.md" % (name, f))

    # --- assets: at least one template -----------------------------------
    ast_dir = os.path.join(folder, "assets")
    assets = sorted(os.listdir(ast_dir)) if os.path.isdir(ast_dir) else []
    if not assets:
        err("%s: no assets/ template" % name)
    for f in assets:
        if ("assets/" + f) not in body:
            err("%s: asset %s is never routed to from SKILL.md" % (name, f))

    # --- evals.json: five cases, five kinds ------------------------------
    evals_path = os.path.join(folder, "evals.json")
    passed = total = 0
    corpus = text
    for sub in ("references", "assets"):
        d = os.path.join(folder, sub)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith((".md", ".json")):
                    corpus += "\n" + open(os.path.join(d, f), encoding="utf-8").read()
    if not os.path.isfile(evals_path):
        err("%s: no evals.json" % name)
    else:
        try:
            ev = json.load(open(evals_path, encoding="utf-8"))
        except ValueError as e:
            err("%s: evals.json does not parse (%s)" % (name, e))
            ev = {}
        cases = ev.get("cases", [])
        total = len(cases)
        if total != 5:
            err("%s: %d eval cases, the contract is exactly 5" % (name, total))
        kinds = [c.get("kind") for c in cases]
        for k in EVAL_KINDS:
            if kinds.count(k) != 1:
                err("%s: eval kind %r appears %d times, expected once" % (name, k, kinds.count(k)))
        seen = set()
        for c in cases:
            cid = c.get("id", "")
            if not cid or cid in seen:
                err("%s: eval case with missing or duplicate id %r" % (name, cid))
            seen.add(cid)
            for field in ("kind", "prompt", "expect", "must_include", "must_not_claim"):
                if not c.get(field):
                    err("%s: eval %r has empty %s" % (name, cid, field))
            ok_case = True
            for phrase in c.get("must_include", []):
                if phrase.lower() not in corpus.lower():
                    ok_case = False
                    err("%s: eval %r requires %r, which the skill text never states"
                        % (name, cid, phrase))
            if ok_case and c.get("must_include"):
                passed += 1

    # --- notes.seed: schema only, no fabricated experience ---------------
    seed_dir = os.path.join(folder, "notes.seed")
    if not os.path.isdir(seed_dir):
        err("%s: no notes.seed/ - the schema a fresh employee starts from" % name)
    else:
        for f in SEED_FILES:
            p = os.path.join(seed_dir, f)
            if not os.path.isfile(p):
                err("%s: notes.seed/%s missing" % (name, f))
                continue
            bad = is_schema_only(p)
            if bad:
                err("%s: notes.seed/%s carries fabricated experience at line(s) %s"
                    % (name, f, ", ".join(str(i) for i, _ in bad[:3])))
        jdir = os.path.join(seed_dir, "journal")
        journals = sorted(os.listdir(jdir)) if os.path.isdir(jdir) else []
        if not journals:
            err("%s: notes.seed/journal/ has no YYYY-MM.md" % name)
        for f in journals:
            if not re.match(r"^\d{4}-\d{2}\.md$", f):
                err("%s: notes.seed/journal/%s is not YYYY-MM.md" % (name, f))
            bad = is_schema_only(os.path.join(jdir, f))
            if bad:
                err("%s: notes.seed/journal/%s carries fabricated experience at line(s) %s"
                    % (name, f, ", ".join(str(i) for i, _ in bad[:3])))

    # --- the live notes/ folder, also seeded clean ------------------------
    live = os.path.join(folder, "notes")
    for f in ("learnings.md", "contacts.md"):
        p = os.path.join(live, f)
        if not os.path.isfile(p):
            err("%s: notes/%s missing" % (name, f))
            continue
        bad = is_schema_only(p)
        if bad:
            err("%s: notes/%s ships with invented entries at line(s) %s"
                % (name, f, ", ".join(str(i) for i, _ in bad[:3])))
    for f in sorted(os.listdir(live)) if os.path.isdir(live) else []:
        if f in ("learnings.md", "contacts.md"):
            continue
        p = os.path.join(live, f)
        if os.path.isfile(p):
            bad = is_schema_only(p)
            if bad:
                err("%s: notes/%s ships with invented entries at line(s) %s"
                    % (name, f, ", ".join(str(i) for i, _ in bad[:3])))
    jdir = os.path.join(live, "journal")
    for f in sorted(os.listdir(jdir)) if os.path.isdir(jdir) else []:
        bad = is_schema_only(os.path.join(jdir, f))
        if bad:
            err("%s: notes/journal/%s ships with invented entries at line(s) %s"
                % (name, f, ", ".join(str(i) for i, _ in bad[:3])))

    # --- registry declaration --------------------------------------------
    lvl = entry.get("level")
    if lvl not in LEVELS:
        err("%s: registry level %r not in %s" % (name, lvl, LEVELS))
    cat = entry.get("category")
    if cat not in CATEGORIES:
        err("%s: registry category %r not in %s" % (name, cat, CATEGORIES))
    if entry.get("status") != "probation":
        err("%s: new employees enter at status 'probation', got %r" % (name, entry.get("status")))
    if entry.get("reliability") != "unverified":
        err("%s: reliability must be 'unverified' until graded, got %r"
            % (name, entry.get("reliability")))
    perm = entry.get("permissions") or {}
    for key in ("read", "draft", "send", "spend", "approval_required_for"):
        if key not in perm:
            err("%s: permissions.%s not declared" % (name, key))
    if perm.get("send") not in ([], None) and not isinstance(perm.get("send"), list):
        err("%s: permissions.send must be a list" % name)
    cost = entry.get("cost") or {}
    for key in ("class", "minutes_per_task", "paid_api"):
        if key not in cost:
            err("%s: cost.%s not declared" % (name, key))
    conns = entry.get("connectors") or []
    if len(conns) < 3:
        err("%s: %d connectors declared, a v2 employee names at least 3" % (name, len(conns)))
    for c in conns:
        for key in ("name", "availability", "unlocks", "fallback"):
            if not c.get(key):
                err("%s: connector %r missing %s" % (name, c.get("name"), key))
        if c.get("availability") not in AVAILABILITY:
            err("%s: connector %r availability %r not in %s"
                % (name, c.get("name"), c.get("availability"), AVAILABILITY))
    prob = entry.get("probation") or {}
    for key in ("since", "exit_criteria"):
        if not prob.get(key):
            err("%s: probation.%s not declared" % (name, key))
    for key in ("tagline", "skills_inside", "tools_required", "outputs", "best_for"):
        if not entry.get(key):
            err("%s: registry %s missing" % (name, key))

    return passed, total


def main():
    # ---------------------------------------------------------------- core
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

    on_disk = sorted(d for d in os.listdir(SKILLS)
                     if os.path.isdir(os.path.join(SKILLS, d))) if os.path.isdir(SKILLS) else []
    for n in names:
        if n not in on_disk:
            err("registry lists %r but skills/%s does not exist" % (n, n))
    for d in on_disk:
        if d not in names:
            err("skills/%s exists but is not in registry.json" % d)

    changelog = ""
    cl_path = os.path.join(ROOT, "CHANGELOG.md")
    if os.path.isfile(cl_path):
        changelog = open(cl_path, encoding="utf-8").read()
    backlog = ""
    bl_path = os.path.join(ROOT, "BACKLOG.md")
    if os.path.isfile(bl_path):
        backlog = open(bl_path, encoding="utf-8").read()

    v2_entries = [e for e in employees if e.get("standard_revision") == "v2"]

    # ------------------------------------------------------- layer 1: v1
    for d in on_disk:
        if ONLY and d != os.path.basename(ONLY):
            continue
        folder = os.path.join(SKILLS, d)
        v = os.path.join(folder, "scripts", "validate_skill.py")
        if not os.path.isfile(v):
            v = os.path.join(ROOT, "scripts", "validate_skill.py")
        if not os.path.isfile(v):
            warn("%s has no validate_skill.py" % d)
            continue
        r = subprocess.run([sys.executable, v, folder], capture_output=True, text=True)
        if r.returncode != 0:
            err("%s failed the v1 skill check:\n%s" % (d, r.stdout.strip()))

    for n in names:
        if n not in changelog:
            warn("skill %r has no CHANGELOG entry" % n)
        if "`%s`" % n not in backlog:
            warn("skill %r not listed in BACKLOG.md" % n)

    queued = backlog.count("| queued |")
    if queued < 50:
        warn("only %d queued roles - under 10 days of runway at 5 per day" % queued)

    # ------------------------------------------------------- layer 2: v2
    eval_passed = eval_total = 0
    if not ONLY:
        for entry in v2_entries:
            folder = os.path.join(SKILLS, entry["name"])
            if not os.path.isdir(folder):
                continue
            p, t = check_v2_employee(entry, folder)
            eval_passed += p
            eval_total += t

        # the drop itself: probation employees dated today must be in the changelog
        for entry in v2_entries:
            added = entry.get("added", "")
            if added and ("## %s" % added) not in changelog:
                err("%s: added %s but CHANGELOG.md has no block for that date" % (entry["name"], added))
            if entry.get("status") == "probation" and "shipped %s" % added not in backlog:
                err("%s: BACKLOG.md does not mark it shipped %s" % (entry["name"], added))

        mix = [e.get("category") for e in v2_entries if e.get("added") == (v2_entries[-1].get("added") if v2_entries else "")]
        if mix:
            if mix.count("revenue") != 2 or mix.count("operations") != 2 or mix.count("founder-leverage") != 1:
                err("the drop's mix is %s - the rule is 2 revenue, 2 operations, 1 founder-leverage"
                    % {k: mix.count(k) for k in CATEGORIES})

    # --------------------------------------------------- description cap
    over = []
    for entry in employees:
        folder = os.path.join(SKILLS, entry["name"])
        p = os.path.join(folder, "SKILL.md")
        if not os.path.isfile(p):
            continue
        fm, _ = parse_frontmatter(open(p, encoding="utf-8").read())
        if not fm:
            continue
        n = len(fm.get("description", ""))
        if n >= DESCRIPTION_CAP:
            over.append((entry["name"], n, entry.get("standard_revision") == "v2"))
    for n, ln, is_v2 in over:
        if is_v2:
            err("%s: description %d chars over the %d cap" % (n, ln, DESCRIPTION_CAP))
        else:
            note("%s: description %d chars, over the v2 cap of %d (pre-v2, advisory)"
                 % (n, ln, DESCRIPTION_CAP))

    # ------------------------------------------------------------ secrets
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [x for x in dirnames if x not in (".git", "__pycache__", "node_modules")]
        for fn in filenames:
            if fn.endswith((".md", ".json", ".py", ".txt", ".yml", ".yaml")):
                p = os.path.join(dirpath, fn)
                try:
                    body = open(p, encoding="utf-8", errors="ignore").read()
                except OSError:
                    continue
                for pat, label in SECRET_PATTERNS:
                    if re.search(pat, body):
                        err("%s: %s" % (os.path.relpath(p, ROOT), label))

    # -------------------------------------------------------------- report
    fatal = errors + (warnings if STRICT else [])
    print("repo: %s | version: %s | employees: %d | v2: %d | queued: %d"
          % (registry.get("name"), registry.get("version"), len(names), len(v2_entries), queued))
    if v2_entries:
        print("v2 employees: " + ", ".join("%s (%s/%s)" % (e["name"], e.get("level"), e.get("category"))
                                           for e in v2_entries))
        print("eval cases resolving against shipped text: %d/%d" % (eval_passed, eval_total))
    for e in errors:
        print("  ERROR   " + e)
    for w in warnings:
        print("  %s %s" % ("ERROR  " if STRICT else "warning", w))
    if advisory:
        print("  advisory (pre-v2, not fatal under --strict):")
        for a in advisory:
            print("    - " + a)
    print("RESULT: %s (%d errors, %d warnings%s)"
          % ("PASS" if not fatal else "FAIL", len(fatal), len(advisory),
             ", strict" if STRICT else ""))
    return 0 if not fatal else 1


if __name__ == "__main__":
    sys.exit(main())
