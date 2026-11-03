#!/usr/bin/env python3
"""Validate this skill against the v2 standard.

Thin wrapper so the v1 repo validator and a human both get one command. The
checks live in scripts/validate_repo_v2.py - one implementation, not two that
drift apart.

Usage: python3 validate_skill.py <skill-folder>
Exit 0 = pass.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
name = os.path.basename(os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)))
returncode = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate_repo_v2.py"),
                             "--strict", "--skill", name]).returncode
sys.exit(returncode)
