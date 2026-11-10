#!/usr/bin/env python3
"""Deterministic expense tests for the expense-auditor employee.

Runs the tests that must never be eyeballed: exact and near duplicates, split
invoices, cap breaches, missing receipts, vendor concentration.

Input: a CSV with columns
    date,employee,vendor,category,amount,receipt,approver
    date    YYYY-MM-DD
    receipt yes/no/true/false/1/0
    amount  plain number, no currency symbol

Usage:
    python3 expense_check.py --self-test
    python3 expense_check.py claims.csv [--config rules.json] [--json]

Config (all optional, these are the defaults):
    {"receipt_threshold": 500, "dup_window_days": 7,
     "split_window_days": 14, "approval_threshold": 10000,
     "caps": {"lodging": 4500}, "concentration_pct": 30,
     "materiality": 2000}
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import date, timedelta

DEFAULTS = {
    "receipt_threshold": 500,
    "dup_window_days": 7,
    "split_window_days": 14,
    "approval_threshold": 10000,
    "caps": {},
    "concentration_pct": 30,
    "materiality": 2000,
}


def _norm(s):
    return " ".join(str(s or "").strip().lower().split())


def _day(s):
    y, m, d = [int(x) for x in str(s).strip().split("-")]
    return date(y, m, d)


def _truthy(s):
    return _norm(s) in ("yes", "y", "true", "1", "t")


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for i, raw in enumerate(csv.DictReader(fh), start=2):
            rows.append({
                "line": i,
                "date": _day(raw["date"]),
                "employee": _norm(raw.get("employee")),
                "vendor": _norm(raw.get("vendor")),
                "category": _norm(raw.get("category")),
                "amount": float(raw["amount"]),
                "receipt": _truthy(raw.get("receipt")),
                "approver": _norm(raw.get("approver")),
            })
    return rows


def _finding(rule, severity, rows, amount, evidence, recoverable=None):
    return {
        "rule": rule,
        "severity": severity,
        "lines": [r["line"] for r in rows],
        "amount_at_risk": round(amount, 2),
        "recoverable": round(amount if recoverable is None else recoverable, 2),
        "evidence": evidence,
    }


def find_duplicates(rows, cfg):
    out = []
    seen = defaultdict(list)
    for r in rows:
        seen[(r["vendor"], round(r["amount"], 2))].append(r)
    for (vendor, amount), group in seen.items():
        if len(group) < 2:
            continue
        group.sort(key=lambda r: r["date"])
        exact = [g for g in group if g["date"] == group[0]["date"]]
        if len(exact) > 1:
            out.append(_finding("exact_duplicate", "high", exact, amount * (len(exact) - 1),
                                "same vendor, same amount, same date"))
            continue
        for i in range(len(group) - 1):
            gap = (group[i + 1]["date"] - group[i]["date"]).days
            if gap <= cfg["dup_window_days"]:
                out.append(_finding("near_duplicate", "medium", [group[i], group[i + 1]], amount,
                                    "same vendor and amount within %d days" % gap))
    return out


def find_splits(rows, cfg):
    out = []
    threshold = cfg["approval_threshold"]
    buckets = defaultdict(list)
    for r in rows:
        if r["amount"] < threshold:
            buckets[(r["vendor"], r["employee"])].append(r)
    for (vendor, employee), group in buckets.items():
        group.sort(key=lambda r: r["date"])
        for i, start in enumerate(group):
            window = [g for g in group[i:]
                      if (g["date"] - start["date"]).days <= cfg["split_window_days"]]
            if len(window) >= 3 and sum(g["amount"] for g in window) >= threshold:
                out.append(_finding(
                    "split_invoice", "high", window, sum(g["amount"] for g in window),
                    "%d claims to one vendor by one person inside %d days, each under the "
                    "approval threshold of %d" % (len(window), cfg["split_window_days"], threshold),
                    recoverable=0))
                break
    return out


def find_cap_breaches(rows, cfg):
    out = []
    for r in rows:
        cap = cfg["caps"].get(r["category"])
        if cap and r["amount"] > cap:
            out.append(_finding("cap_breach", "medium", [r], r["amount"] - cap,
                                "%s claim of %.0f above the cap of %.0f"
                                % (r["category"], r["amount"], cap), recoverable=0))
    return out


def find_missing_receipts(rows, cfg):
    out = []
    flagged = [r for r in rows
               if not r["receipt"] and r["amount"] > cfg["receipt_threshold"]]
    if flagged:
        out.append(_finding("missing_receipt", "medium", flagged,
                            sum(r["amount"] for r in flagged),
                            "%d claims above %.0f with no receipt"
                            % (len(flagged), cfg["receipt_threshold"]), recoverable=0))
    return out


def find_concentration(rows, cfg):
    out = []
    by_cat = defaultdict(lambda: defaultdict(float))
    for r in rows:
        by_cat[r["category"]][r["vendor"]] += r["amount"]
    for category, vendors in by_cat.items():
        total = sum(vendors.values())
        if total <= 0:
            continue
        vendor, spend = max(vendors.items(), key=lambda kv: kv[1])
        share = 100.0 * spend / total
        if share >= cfg["concentration_pct"]:
            out.append({
                "rule": "concentration", "severity": "info", "lines": [],
                "amount_at_risk": 0.0, "recoverable": 0.0,
                "evidence": "%s is %.1f%% of %s spend (%.0f of %.0f)"
                            % (vendor, share, category, spend, total),
            })
    return out


def audit(rows, cfg=None):
    cfg = dict(DEFAULTS, **(cfg or {}))
    findings = (find_duplicates(rows, cfg) + find_splits(rows, cfg)
                + find_cap_breaches(rows, cfg) + find_missing_receipts(rows, cfg)
                + find_concentration(rows, cfg))
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
    findings.sort(key=lambda f: (order.get(f["severity"], 9), -f["amount_at_risk"]))
    material = [f for f in findings
                if f["amount_at_risk"] >= cfg["materiality"] or f["severity"] in ("high", "critical")]
    return {
        "rows": len(rows),
        "total_spend": round(sum(r["amount"] for r in rows), 2),
        "materiality": cfg["materiality"],
        "findings": findings,
        "material_findings": len(material),
        "at_risk": round(sum(f["amount_at_risk"] for f in findings), 2),
        "recoverable": round(sum(f["recoverable"] for f in findings), 2),
    }


def _self_test():
    import os
    import tempfile
    body = (
        "date,employee,vendor,category,amount,receipt,approver\n"
        "2026-09-01,ravi,amazon,workplace,4999,yes,anil\n"
        "2026-09-03,ravi,amazon,workplace,4999,yes,anil\n"
        "2026-09-02,sita,oyo,lodging,6200,no,anil\n"
        "2026-09-04,sita,oyo,lodging,2000,no,anil\n"
        "2026-09-05,sita,oyo,lodging,2000,no,anil\n"
        "2026-09-06,sita,oyo,lodging,2000,no,anil\n"
        "2026-09-07,sita,oyo,lodging,2000,no,anil\n"
        "2026-09-08,ravi,swiggy,client,800,yes,anil\n"
        "2026-09-09,sita,swiggy,client,300,no,anil\n"
    )
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, "claims.csv")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    rows = load(path)
    assert len(rows) == 9
    assert rows[0]["receipt"] is True and rows[2]["receipt"] is False

    cfg = dict(DEFAULTS, caps={"lodging": 4500}, receipt_threshold=500)
    res = audit(rows, cfg)
    rules = [f["rule"] for f in res["findings"]]
    assert "near_duplicate" in rules
    dup = [f for f in res["findings"] if f["rule"] == "near_duplicate"][0]
    assert dup["amount_at_risk"] == 4999.0
    assert "split_invoice" in rules
    split = [f for f in res["findings"] if f["rule"] == "split_invoice"][0]
    assert split["amount_at_risk"] == 14200.0
    assert "cap_breach" in rules
    assert "missing_receipt" in rules
    assert res["total_spend"] == 25298.0
    assert res["at_risk"] > res["recoverable"]
    print("self-test: 9 assertions passed")


def main():
    if "--self-test" in sys.argv:
        _self_test()
        return 0
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    cfg = DEFAULTS
    if "--config" in sys.argv:
        cfg = json.load(open(sys.argv[sys.argv.index("--config") + 1], encoding="utf-8"))
    res = audit(load(args[0]), cfg)
    if "--json" in sys.argv:
        print(json.dumps(res, indent=2, default=str))
    else:
        print("rows %d | spend %.0f | findings %d | at risk %.0f | recoverable %.0f"
              % (res["rows"], res["total_spend"], len(res["findings"]),
                 res["at_risk"], res["recoverable"]))
        for f in res["findings"]:
            print("  %-7s %-18s lines %-14s risk %8.0f  %s"
                  % (f["severity"].upper(), f["rule"],
                     ",".join(str(x) for x in f["lines"])[:14],
                     f["amount_at_risk"], f["evidence"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
