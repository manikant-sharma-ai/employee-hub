#!/usr/bin/env python3
"""Deterministic eligibility matching for the govt-scheme-finder employee.

This script compares a business profile against a rules file built by hand from
scheme guidelines. It does not know, store or guess any scheme parameter - the
rules file carries them, with the source and the date each was read.

Rules file format (JSON list):
[
  {"id": "S1", "name": "example scheme", "authority": "ministry",
   "level": "central", "family": "capital subsidy",
   "benefit": "formula as written in the guideline",
   "source": "url or notification number", "read_on": "YYYY-MM-DD",
   "requires": {"entity_type": ["private_limited"], "udyam": true,
                "max_turnover": 50000000, "min_years": 1, "max_years": 10,
                "states": ["Maharashtra"], "sectors": ["manufacturing"],
                "max_employees": 100, "exports": true, "min_capex": 1000000}}
]
Every key in "requires" is optional. Unknown keys are reported, not ignored.

Usage:
    python3 scheme_match.py --self-test
    python3 scheme_match.py profile.json rules.json
"""
import json
import sys

STATUS_ORDER = {"eligible": 0, "needs_check": 1, "not_eligible": 2}
KNOWN_KEYS = {"entity_type", "udyam", "max_turnover", "min_turnover", "min_years",
              "max_years", "states", "sectors", "max_employees", "exports",
              "min_capex", "requires_gst", "requires_iec", "dpiit"}

# rule field -> profile field
PROFILE_KEY = {
    "entity_type": "entity_type", "udyam": "udyam",
    "max_turnover": "turnover", "min_turnover": "turnover",
    "min_years": "years", "max_years": "years",
    "max_employees": "employees", "min_capex": "capex",
    "states": "state", "sectors": "sector", "exports": "exports",
    "requires_gst": "gst", "requires_iec": "iec", "dpiit": "dpiit",
}
BOOL_FIELDS = ("udyam", "exports", "requires_gst", "requires_iec", "dpiit")


def match(profile, rules):
    """Run every rule against the profile and return a ranked matrix.

    A rule is "eligible" when every clause passes, "not_eligible" when any clause
    fails, and "needs_check" when a clause could not be tested because the profile
    does not carry that field.
    """
    rows = []
    for rule in rules:
        req = rule.get("requires", {})
        unknown = set(req) - KNOWN_KEYS
        reasons, missing = [], []
        failed = False
        for field in sorted(req):
            if field in unknown:
                continue
            key = PROFILE_KEY[field]
            have = profile.get(key)
            want = req[field]
            if have is None:
                missing.append(key)
                continue
            if field in ("entity_type", "states", "sectors"):
                wanted = want if isinstance(want, list) else [want]
                values = have if isinstance(have, list) else [have]
                if not any(v in wanted for v in values):
                    reasons.append("%s %r not in %r" % (key, have, wanted))
                    failed = True
            elif field in BOOL_FIELDS:
                if bool(have) != bool(want):
                    reasons.append("%s is %r, scheme needs %r" % (key, have, want))
                    failed = True
            elif field == "max_turnover" and have > want:
                reasons.append("turnover %.0f exceeds %.0f" % (have, want))
                failed = True
            elif field == "min_turnover" and have < want:
                reasons.append("turnover %.0f below %.0f" % (have, want))
                failed = True
            elif field == "min_years" and have < want:
                reasons.append("years operating %.1f below %.1f" % (have, want))
                failed = True
            elif field == "max_years" and have > want:
                reasons.append("years operating %.1f above %.1f" % (have, want))
                failed = True
            elif field == "max_employees" and have > want:
                reasons.append("headcount %.0f above %.0f" % (have, want))
                failed = True
            elif field == "min_capex" and have < want:
                reasons.append("planned capex %.0f below %.0f" % (have, want))
                failed = True
        if unknown:
            reasons.append("unrecognised rule keys: %s" % ", ".join(sorted(unknown)))
            failed = True
        if failed:
            status = "not_eligible"
        elif missing:
            status = "needs_check"
        else:
            status = "eligible"
        rows.append({
            "id": rule.get("id"), "name": rule.get("name"),
            "authority": rule.get("authority"), "level": rule.get("level"),
            "family": rule.get("family"), "status": status,
            "reason": "; ".join(reasons) if reasons else "all clauses satisfied on the profile",
            "missing_fields": missing,
            "benefit": rule.get("benefit"),
            "source": rule.get("source"), "read_on": rule.get("read_on"),
            "verified": bool(rule.get("source") and rule.get("read_on")),
        })
    rows.sort(key=lambda r: (STATUS_ORDER[r["status"]], r["name"] or ""))
    return rows


def summary(rows):
    out = {"eligible": 0, "needs_check": 0, "not_eligible": 0, "unverified_parameters": 0}
    for r in rows:
        out[r["status"]] += 1
        if not r["verified"]:
            out["unverified_parameters"] += 1
    return out


def _self_test():
    # Synthetic fixture. These are NOT real scheme parameters - they exist only
    # to exercise the comparison logic.
    profile = {"entity_type": "private_limited", "udyam": True, "turnover": 40000000,
               "years": 4.0, "employees": 24, "state": "Maharashtra",
               "sector": "manufacturing", "exports": False, "capex": 5000000}
    rules = [
        {"id": "T1", "name": "guarantee", "requires": {"udyam": True, "max_turnover": 50000000},
         "source": "fixture", "read_on": "2026-11-10"},
        {"id": "T2", "name": "capital", "requires": {"sector": "manufacturing", "min_capex": 10000000},
         "source": "fixture", "read_on": "2026-11-10"},
        {"id": "T3", "name": "export", "requires": {"exports": True},
         "source": "fixture", "read_on": "2026-11-10"},
        {"id": "T4", "name": "unverified", "requires": {"entity_type": "private_limited"}},
        {"id": "T5", "name": "state", "requires": {"states": "Karnataka"}},
    ]
    rows = match(profile, rules)
    by = {r["id"]: r for r in rows}
    assert by["T1"]["status"] == "eligible", by["T1"]
    assert by["T2"]["status"] == "not_eligible"
    assert "capex" in by["T2"]["reason"]
    assert by["T3"]["status"] == "not_eligible"
    assert by["T4"]["status"] == "eligible" and by["T4"]["verified"] is False
    assert by["T5"]["status"] == "not_eligible"
    assert rows[0]["status"] == "eligible"
    s = summary(rows)
    assert s["eligible"] == 2 and s["not_eligible"] == 3
    assert s["unverified_parameters"] == 2

    thin = {"entity_type": "private_limited"}
    rows2 = {r["id"]: r for r in match(thin, rules)}
    assert rows2["T1"]["status"] == "needs_check", rows2["T1"]
    assert "udyam" in rows2["T1"]["missing_fields"]
    assert "turnover" in rows2["T1"]["missing_fields"]
    assert rows2["T4"]["status"] == "eligible"
    print("self-test: 11 assertions passed")


def main():
    if "--self-test" in sys.argv:
        _self_test()
        return 0
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    profile = json.load(open(args[0], encoding="utf-8"))
    rules = json.load(open(args[1], encoding="utf-8"))
    rows = match(profile, rules)
    s = summary(rows)
    print("%-28s %-10s %-16s %s" % ("scheme", "status", "family", "reason"))
    for r in rows:
        print("%-28s %-10s %-16s %s" % ((r["name"] or "")[:28], r["status"],
                                        (r["family"] or "")[:16], r["reason"][:70]))
        if not r["verified"]:
            print("   ! parameter unverified - no source/date recorded")
    print("summary: " + json.dumps(s))
    return 0


if __name__ == "__main__":
    sys.exit(main())
