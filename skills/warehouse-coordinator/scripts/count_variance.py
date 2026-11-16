#!/usr/bin/env python3
"""Reconcile a physical stock count against the system, and say what to do.

Joins two CSVs - the system stock report and the counted sheet - on SKU, and
produces per SKU: the variance in units, its value at cost, the ABC class, and
an action drawn from a tolerance that is set per class. Then it summarises by
cause bucket and by action, so the recount list and the adjustment proposal
fall out of the same run.

Deterministic: no network, no randomness, no wall clock. The count date and the
cost are inputs, never looked up.

System CSV:  sku, description, unit, qty, unit_cost
Count  CSV:  sku, counted_qty

Usage:
    python3 count_variance.py --system system.csv --count counted.csv
    python3 count_variance.py --system system.csv --count counted.csv --abc abc.csv
    python3 count_variance.py --self-test

abc.csv is optional: sku, class (A/B/C). Without it, class is assigned by value
share in this file - A for the SKUs that make up the first 70% of stock value,
B to 90%, C for the rest.
"""
import csv
import sys

# Tolerance by class, from references/stock-count-and-variance.md.
TOLERANCE = {"A": 0.01, "B": 0.05, "C": 0.10}


def read_csv(path, required):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing = [c for c in required if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("%s missing columns: %s" % (path, ", ".join(missing)))
        for raw in reader:
            rows.append({k: (v or "").strip() for k, v in raw.items() if k})
    return rows


def load(system_path, count_path, abc_path=None):
    system = {}
    for r in read_csv(system_path, ["sku", "description", "unit", "qty", "unit_cost"]):
        system[r["sku"]] = {
            "sku": r["sku"],
            "description": r["description"],
            "unit": r["unit"],
            "qty": float(r["qty"]),
            "unit_cost": float(r["unit_cost"]),
        }
    counted = {}
    for r in read_csv(count_path, ["sku", "counted_qty"]):
        counted[r["sku"]] = float(r["counted_qty"])
    abc = {}
    if abc_path:
        for r in read_csv(abc_path, ["sku", "class"]):
            cls = r["class"].upper()
            if cls not in TOLERANCE:
                raise ValueError("unknown ABC class %r for %s" % (cls, r["sku"]))
            abc[r["sku"]] = cls
    return system, counted, abc


def assign_abc(rows):
    """A: the SKUs that make up the first 70% of value, B: to 90%, C: the rest.

    The share is measured *before* the row is added, so the single largest SKU
    is always A even when it is 80% of the stock on its own.
    """
    total = sum(r["value"] for r in rows) or 1.0
    running = 0.0
    for r in sorted(rows, key=lambda x: (-x["value"], x["sku"])):
        share_before = running / total
        r["class"] = "A" if share_before < 0.70 else ("B" if share_before < 0.90 else "C")
        running += r["value"]


def reconcile(system, counted, abc=None):
    rows = []
    for sku, s in system.items():
        if sku not in counted:
            continue  # not counted: reported separately, never assumed zero
        diff = counted[sku] - s["qty"]
        value = abs(diff) * s["unit_cost"]
        rows.append({
            "sku": sku,
            "description": s["description"],
            "unit": s["unit"],
            "system": s["qty"],
            "physical": counted[sku],
            "variance": diff,
            "value": value,
            # A SKU with no class in the abc file is treated as C, the loosest
            # tolerance, so an unclassed item is never quietly tightened.
            "class": (abc or {}).get(sku) or "C",
        })
    if not abc:
        assign_abc(rows)
    for r in rows:
        tol = TOLERANCE[r["class"]] * max(abs(r["system"]), 1.0)
        if r["variance"] == 0:
            r["action"], r["cause"] = "clear", "none"
        elif abs(r["variance"]) <= tol:
            r["action"], r["cause"] = "clear", "within tolerance"
        elif abs(r["variance"]) <= tol * 3:
            r["action"], r["cause"] = "recount", "unconfirmed"
        else:
            r["action"], r["cause"] = "investigate", "unexplained"
    rows.sort(key=lambda r: (-r["value"], r["sku"]))
    uncounted = sorted(set(system) - set(counted))
    extra = sorted(set(counted) - set(system))
    return rows, uncounted, extra


def summarise(rows, uncounted, extra):
    short = sum(r["value"] for r in rows if r["variance"] < 0)
    excess = sum(r["value"] for r in rows if r["variance"] > 0)
    return {
        "skus": len(rows),
        "short_value": short,
        "excess_value": excess,
        "net_value": excess - short,
        "by_action": {a: [r for r in rows if r["action"] == a]
                      for a in ("clear", "recount", "investigate")},
        "uncounted": uncounted,
        "extra": extra,
    }


def render(rows, summary, stock_value, as_of=""):
    def money(x):
        return "%.0f" % x
    out = []
    head = "# Stock count variance"
    if as_of:
        head += " - as of %s" % as_of
    out += [head, ""]
    share = (summary["short_value"] / stock_value * 100.0) if stock_value else 0.0
    out.append("SKUs reconciled: **%d** | short: ₹%s | excess: ₹%s | net: ₹%s"
               % (summary["skus"], money(summary["short_value"]),
                  money(summary["excess_value"]), money(summary["net_value"])))
    out.append("Short value as share of stock value: **%.2f%%**" % share)
    out.append("")
    out.append("| Action | SKUs | Value at cost |")
    out.append("|---|---|---|")
    for action in ("recount", "investigate", "clear"):
        items = summary["by_action"][action]
        out.append("| %s | %d | ₹%s |" % (action, len(items),
                                          money(sum(v["value"] for v in items))))
    out.append("")
    out.append("## Top ten by value")
    out.append("")
    out.append("| SKU | Description | Unit | System | Physical | Variance | Value | Class | Action |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    for r in rows[:10]:
        out.append("| %s | %s | %s | %g | %g | %+g | ₹%s | %s | %s |"
                   % (r["sku"], r["description"].replace("|", "/"), r["unit"], r["system"],
                      r["physical"], r["variance"], money(r["value"]), r["class"], r["action"]))
    out.append("")
    if summary["uncounted"]:
        out.append("**Not counted (not assumed zero):** " + ", ".join(summary["uncounted"][:20])
                   + (" ..." if len(summary["uncounted"]) > 20 else ""))
    if summary["extra"]:
        out.append("**Counted but not in the system (needs a SKU, not an adjustment):** "
                   + ", ".join(summary["extra"][:20]))
    out.append("")
    out.append("_Computed by scripts/count_variance.py. Adjustments are a proposal: "
               "bookkeeper posts them after approval. Counted-by and recount evidence are not in this file._")
    return "\n".join(out)


SYSTEM = """sku,description,unit,qty,unit_cost
SKU-1001,Motor 1.5kW,piece,40,18500
SKU-1002,Bolt M8,piece,4000,6
SKU-1003,Cable 2.5mm,metre,1200,42
SKU-1004,Bearing 6203,piece,150,120
SKU-1005,Gasket set,set,60,950
SKU-1006,Label roll,roll,80,180
"""

COUNT = """sku,counted_qty
SKU-1001,38
SKU-1002,3960
SKU-1003,1195
SKU-1004,150
SKU-1005,52
"""


def self_test():
    import tempfile
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("FAIL %s: got %r, want %r" % (label, got, want))

    def tmp(body):
        fh = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False)
        fh.write(body)
        fh.close()
        return fh.name

    system, counted, abc = load(tmp(SYSTEM), tmp(COUNT))
    check("system rows", len(system), 6)
    rows, uncounted, extra = reconcile(system, counted, abc)
    check("reconciled rows", len(rows), 5)
    check("uncounted", uncounted, ["SKU-1006"])
    check("extra", extra, [])

    by_sku = {r["sku"]: r for r in rows}
    check("motor variance", by_sku["SKU-1001"]["variance"], -2.0)
    check("motor value", by_sku["SKU-1001"]["value"], 37000.0)
    check("motor class", by_sku["SKU-1001"]["class"], "A")
    check("motor action", by_sku["SKU-1001"]["action"], "investigate")
    check("gasket class", by_sku["SKU-1005"]["class"], "B")
    check("gasket action", by_sku["SKU-1005"]["action"], "recount")
    check("bearing clear", by_sku["SKU-1004"]["action"], "clear")
    check("bolt class", by_sku["SKU-1002"]["class"], "C")
    check("unclassed defaults to C", _unclassed_defaults(tmp(SYSTEM), tmp(COUNT), tmp("sku,class\nSKU-1002,A\n")), "C")
    check("sorted by value", [r["sku"] for r in rows][0], "SKU-1001")

    stock_value = sum(s["qty"] * s["unit_cost"] for s in system.values())
    summary = summarise(rows, uncounted, extra)
    check("skus", summary["skus"], 5)
    check("short value", summary["short_value"], 37000.0 + 240.0 + 210.0 + 7600.0)
    check("recount count", len(summary["by_action"]["recount"]), 1)
    check("investigate count", len(summary["by_action"]["investigate"]), 1)
    check("clear count", len(summary["by_action"]["clear"]), 3)

    text = render(rows, summary, stock_value, "2026-11-16")
    check("report names motor", "| SKU-1001 |" in text, True)
    check("report flags uncounted", "SKU-1006" in text, True)
    check("determinism", render(*reconcile(system, counted, abc)[:1] + (summary, stock_value), "2026-11-16") == text, True)
    check("abc file wins", _abc_file_wins(tmp(SYSTEM), tmp(COUNT), tmp("sku,class\nSKU-1002,A\n")), "A")
    check("bad abc rejected", _bad_abc_rejected(tmp(SYSTEM), tmp(COUNT), tmp("sku,class\nSKU-1002,Z\n")), True)

    print("self-test: %s" % ("PASS (24 checks)" if ok else "FAIL"))
    return 0 if ok else 1


def _unclassed_defaults(system_path, count_path, abc_path):
    system, counted, abc = load(system_path, count_path, abc_path)
    rows, _, _ = reconcile(system, counted, abc)
    return {r["sku"]: r["class"] for r in rows}["SKU-1001"]


def _abc_file_wins(system_path, count_path, abc_path):
    system, counted, abc = load(system_path, count_path, abc_path)
    rows, _, _ = reconcile(system, counted, abc)
    return {r["sku"]: r["class"] for r in rows}["SKU-1002"]


def _bad_abc_rejected(system_path, count_path, abc_path):
    try:
        load(system_path, count_path, abc_path)
    except ValueError:
        return True
    return False


def main(argv):
    if "--self-test" in argv:
        return self_test()
    args = {}
    for flag in ("--system", "--count", "--abc", "--as-of"):
        if flag in argv:
            args[flag] = argv[argv.index(flag) + 1]
    if "--system" not in args or "--count" not in args:
        print(__doc__)
        return 2
    try:
        system, counted, abc = load(args["--system"], args["--count"], args.get("--abc"))
    except (ValueError, KeyError) as exc:
        print("cannot read input: %s" % exc)
        return 2
    rows, uncounted, extra = reconcile(system, counted, abc)
    summary = summarise(rows, uncounted, extra)
    stock_value = sum(s["qty"] * s["unit_cost"] for s in system.values())
    print(render(rows, summary, stock_value, args.get("--as-of", "")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
