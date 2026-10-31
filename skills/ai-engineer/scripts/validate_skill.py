#!/usr/bin/env python3
"""Validate a skill folder: frontmatter, description quality, sections, reference links.

Usage: python validate_skill.py <path-to-skill-folder> [--quiet]
Exit code 0 = pass, 1 = errors found.
"""
import os
import re
import sys

REQUIRED_SECTIONS = [
    "Routing",          # symptom -> reference table
    "Guardrails",
]
RECOMMENDED = ["Standards", "Output", "Trigger test"]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    block = text[3:end].strip()
    body = text[end + 4:]
    data = {}
    key = None
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            data[key] = m.group(2).strip()
        elif key and line.strip():
            data[key] = (data[key] + " " + line.strip()).strip()
    return data, body


def main():
    if len(sys.argv) < 2:
        print("usage: validate_skill.py <skill-folder>")
        return 2
    folder = sys.argv[1].rstrip("/")
    path = os.path.join(folder, "SKILL.md")
    errors, warnings = [], []

    if not os.path.isfile(path):
        print("ERROR: SKILL.md not found in %s" % folder)
        return 1

    text = open(path, encoding="utf-8").read()
    fm, body = parse_frontmatter(text)
    if fm is None:
        errors.append("missing YAML frontmatter")
        fm = {}

    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        errors.append("frontmatter: name missing")
    elif not re.match(r"^[a-z0-9][a-z0-9-]*$", name):
        errors.append("frontmatter: name must be lowercase-hyphen, got %r" % name)
    elif name != os.path.basename(folder):
        warnings.append("name %r does not match folder %r" % (name, os.path.basename(folder)))

    if not desc:
        errors.append("frontmatter: description missing")
    else:
        words = len(desc.split())
        if words < 25:
            warnings.append("description is short (%d words) - weak triggering" % words)
        if words > 160:
            warnings.append("description is long (%d words) - trim" % words)
        if "use when" not in desc.lower():
            warnings.append("description lacks an explicit 'Use when' clause")
        if "trigger" not in desc.lower() and "when" not in desc.lower():
            warnings.append("description has no trigger phrasing")
        if "not for" not in desc.lower():
            warnings.append("description lacks a 'Not for' boundary")

    for sec in REQUIRED_SECTIONS:
        if sec.lower() not in body.lower():
            errors.append("missing required section: %s" % sec)
    for sec in RECOMMENDED:
        if sec.lower() not in body.lower():
            warnings.append("missing recommended section: %s" % sec)

    if len(body.splitlines()) > 600:
        warnings.append("SKILL.md body is %d lines - move depth to references/" % len(body.splitlines()))

    # reference links must resolve
    for link in set(re.findall(r"`(references/[\w./-]+\.md)`", body)):
        if not os.path.isfile(os.path.join(folder, link)):
            errors.append("broken reference link: %s" % link)

    refs_dir = os.path.join(folder, "references")
    if os.path.isdir(refs_dir):
        for fn in sorted(os.listdir(refs_dir)):
            if fn.endswith(".md"):
                p = os.path.join(refs_dir, fn)
                if os.path.getsize(p) < 400:
                    warnings.append("reference %s is very thin (<400 bytes)" % fn)
                if ("references/" + fn) not in body:
                    warnings.append("reference %s is never routed to from SKILL.md" % fn)
    else:
        warnings.append("no references/ directory")

    print("skill: %s" % (name or os.path.basename(folder)))
    print("lines: %d | description words: %d | references: %d" % (
        len(body.splitlines()), len(desc.split()),
        len(os.listdir(refs_dir)) if os.path.isdir(refs_dir) else 0))
    for e in errors:
        print("  ERROR   " + e)
    for w in warnings:
        print("  warning " + w)
    if not errors and not warnings:
        print("  clean")
    print("RESULT: %s (%d errors, %d warnings)" % ("PASS" if not errors else "FAIL", len(errors), len(warnings)))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
