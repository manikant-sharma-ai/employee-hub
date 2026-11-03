#!/usr/bin/env python3
"""Check the plugin manifests agree with registry.json.

Three files carry a version and a name: registry.json, .claude-plugin/plugin.json
and .claude-plugin/marketplace.json. They drift silently because nothing reads
them together. This does.

Usage: python3 scripts/validate_manifests.py
Exit 0 = pass.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return json.load(f)


errors = []
registry = load("registry.json")
plugin = load(".claude-plugin/plugin.json")
market = load(".claude-plugin/marketplace.json")

reg_version = registry.get("version")
if plugin.get("version") != reg_version:
    errors.append("plugin.json version %r != registry.json %r" % (plugin.get("version"), reg_version))
if market.get("version") != reg_version:
    errors.append("marketplace.json version %r != registry.json %r" % (market.get("version"), reg_version))
for p in market.get("plugins", []):
    if p.get("version") != reg_version:
        errors.append("marketplace plugin %r version %r != registry %r"
                      % (p.get("name"), p.get("version"), reg_version))
    if p.get("source") != "./":
        errors.append("marketplace plugin %r source must be './' so skills resolve" % p.get("name"))
if market.get("name") != plugin.get("name"):
    errors.append("marketplace name %r != plugin name %r" % (market.get("name"), plugin.get("name")))
if plugin.get("skills") != "./skills/":
    errors.append("plugin.json skills must point at ./skills/")
if market.get("owner", {}).get("name") != plugin.get("author", {}).get("name"):
    errors.append("author/owner mismatch: plugin author %r vs marketplace owner %r"
                  % (plugin.get("author", {}).get("name"), market.get("owner", {}).get("name")))
if len(registry.get("employees", [])) < 1:
    errors.append("registry has no employees")

print("registry %s | plugin %s | marketplace %s | employees %d"
      % (reg_version, plugin.get("version"), market.get("version"), len(registry.get("employees", []))))
for e in errors:
    print("  ERROR   " + e)
print("RESULT: %s (%d errors)" % ("PASS" if not errors else "FAIL", len(errors)))
sys.exit(0 if not errors else 1)
