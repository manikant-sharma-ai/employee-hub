#!/usr/bin/env python3
"""Validate the whole employee-hub repo.

Checks: core standard present, registry parses and matches folders, every skill
passes validate_skill.py, changelog coverage, backlog runway for the daily
cadence, and no obvious secrets committed.

Usage: python3 scripts/validate_repo.py
Exit 0 = pass.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []

CORE_FILES = [
    "core/employee-standard.md",
    "core/connector-preflight.md",
    "core/connector-catalog.md",
    "core/memory-and-notes.md",
    "core/performance-tracking.md",
]
for c in CORE_FILES:
    if not os.path.isfile(os.path.join(ROOT, c)):
        errors.append("core standard incomplete: missing %s" % c)

reg_path = os.path.join(ROOT, "registry.json")
if not os.path.isfile(reg_path):
    print("ERROR: registry.json missing")
    sys.exit(1)
registry = json.load(open(reg_path, encoding="utf-8"))
employees = registry.get("employees", [])
names = [e.get("name") for e in employees]
if len(names) != len(set(names)):
    errors.append("duplicate names in registry")

skills_dir = os.path.join(ROOT, "skills")
on_disk = sorted(d for d in os.listdir(skills_dir)
                 if os.path.isdir(os.path.join(skills_dir, d))) if os.path.isdir(skills_dir) else []

for n in names:
    if n not in on_disk:
        errors.append("registry lists %r but skills/%s does not exist" % (n, n))
for d in on_disk:
    if d not in names:
        errors.append("skills/%s exists but is not in registry.json" % d)

changelog = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read() if os.path.isfile(os.path.join(ROOT, "CHANGELOG.md")) else ""
for n in names:
    if n not in changelog:
        warnings.append("skill %r has no CHANGELOG entry" % n)

for d in on_disk:
    folder = os.path.join(skills_dir, d)
    v = os.path.join(folder, "scripts", "validate_skill.py")
    if not os.path.isfile(v):
        v = os.path.join(ROOT, "scripts", "validate_skill.py")
    if not os.path.isfile(v):
        warnings.append("%s has no validate_skill.py" % d)
        continue
    r = subprocess.run([sys.executable, v, folder], capture_output=True, text=True)
    if r.returncode != 0:
        errors.append("%s failed validation:\n%s" % (d, r.stdout.strip()))

backlog = open(os.path.join(ROOT, "BACKLOG.md"), encoding="utf-8").read() if os.path.isfile(os.path.join(ROOT, "BACKLOG.md")) else ""
for n in names:
    if "`%s`" % n not in backlog:
        warnings.append("skill %r not listed in BACKLOG.md" % n)

queued = backlog.count("| queued |")
if queued < 50:
    warnings.append("only %d queued roles - under 10 days of runway at 5 per day" % queued)

SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{20,}", "possible API key"),
    (r"AKIA[0-9A-Z]{16}", "possible AWS key"),
    (r"ghp_[A-Za-z0-9]{30,}", "possible GitHub token"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
]
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
                    errors.append("%s: %s" % (os.path.relpath(p, ROOT), label))

print("repo: %s | employees: %d | folders: %d | queued in backlog: %d" % (
    registry.get("name"), len(names), len(on_disk), queued))
print("employees: " + ", ".join(names))
for e in errors:
    print("  ERROR   " + e)
for w in warnings:
    print("  warning " + w)
print("RESULT: %s (%d errors, %d warnings)" % ("PASS" if not errors else "FAIL", len(errors), len(warnings)))
sys.exit(0 if not errors else 1)
