#!/usr/bin/env python3
"""Turn a month's actuals into the one-page variance table the owner reads on Monday.

Reads a CSV with one row per metric and writes a fixed-layout table: actual, target,
last period, variance against each, and a RAG flag computed by one stated rule.
Deterministic - no clock, no network, no rounding drift.

CSV columns (header required, order free):
  metric, unit, actual, target, prior, higher_is_better

  higher_is_better: 1 or 0. Revenue is 1, refund rate is 0.

RAG rule (the only one used, so nobody argues about colour):
  deviation = (actual - target) / |target| * (+1 if higher_is_better else -1)
  deviation >= -0.05  -> ON TRACK
  deviation >= -0.15  -> WATCH
  otherwise           -> OFF TRACK
  target == 0         -> NOT SET (no ratio exists; say so instead of inventing one)

Usage:
  python3 mis_variance.py --self-test
  python3 mis_variance.py metrics.csv [--csv]

Exit 0 = table produced. Exit 1 = the file is unusable.
"""
import csv
import io
import sys

COLUMNS = ("metric", "unit", "actual", "target", "prior", "higher_is_better")
ON_TRACK = -0.05
WATCH = -0.15


def _num(value):
    """Parse a number, tolerating thousands separators, currency marks and blanks."""
    if value is None:
        return None
    text = str(value).strip().replace(",", "").replace("₹", "").replace("$", "")
    if text in ("", "-", "na", "NA", "n/a", "None"):
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _pct(new, base):
    if base is None or base == 0 or new is None:
        return None
    return (new - base) / abs(base)


def flag(actual, target, higher_is_better):
    if actual is None or target is None or target == 0:
        return "NOT SET", None
    deviation = _pct(actual, target) * (1 if higher_is_better else -1)
    if deviation >= ON_TRACK:
        return "ON TRACK", deviation
    if deviation >= WATCH:
        return "WATCH", deviation
    return "OFF TRACK", deviation


def build(rows):
    """Return (table_rows, problems). table_rows are dicts in input order."""
    table, problems = [], []
    for i, row in enumerate(rows, start=2):
        metric = (row.get("metric") or "").strip()
        if not metric:
            problems.append("line %d: no metric name - skipped" % i)
            continue
        actual = _num(row.get("actual"))
        target = _num(row.get("target"))
        prior = _num(row.get("prior"))
        hib_raw = (row.get("higher_is_better") or "1").strip()
        higher_is_better = hib_raw not in ("0", "false", "False", "no")
        if actual is None:
            problems.append("line %d (%s): actual is blank - reported as not measured" % (i, metric))
        rag, deviation = flag(actual, target, higher_is_better)
        table.append({
            "metric": metric,
            "unit": (row.get("unit") or "").strip(),
            "actual": actual,
            "target": target,
            "prior": prior,
            "higher_is_better": higher_is_better,
            "vs_target": _pct(actual, target),
            "vs_prior": _pct(actual, prior),
            "rag": rag,
            "deviation": deviation,
        })
    return table, problems


def _fmt(value, unit, pct=False):
    if value is None:
        return "not measured"
    if pct:
        return "%+.1f%%" % (value * 100)
    if unit == "INR":
        return "%.2f lakh" % (value / 100000.0) if abs(value) >= 100000 else "%.0f" % value
    if unit == "%":
        return "%.1f%%" % value
    return ("%.2f" % value).rstrip("0").rstrip(".")


def render(table, problems, period=""):
    lines = ["# MIS variance%s" % (" - " + period if period else ""), ""]
    lines.append("| Metric | Actual | Target | Last period | vs target | vs last | Flag |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in table:
        lines.append("| %s | %s | %s | %s | %s | %s | %s |" % (
            r["metric"],
            _fmt(r["actual"], r["unit"]),
            _fmt(r["target"], r["unit"]),
            _fmt(r["prior"], r["unit"]),
            _fmt(r["vs_target"], r["unit"], pct=True),
            _fmt(r["vs_prior"], r["unit"], pct=True),
            r["rag"],
        ))
    counts = {}
    for r in table:
        counts[r["rag"]] = counts.get(r["rag"], 0) + 1
    lines.append("")
    lines.append("Flags: " + ", ".join("%s %d" % (k, counts[k]) for k in sorted(counts)))
    movers = [r for r in table if r["vs_prior"] is not None]
    if movers:
        top = max(movers, key=lambda r: abs(r["vs_prior"]))
        lines.append("Biggest move since last period: %s (%s)." % (
            top["metric"], _fmt(top["vs_prior"], top["unit"], pct=True)))
    off = [r["metric"] for r in table if r["rag"] == "OFF TRACK"]
    if off:
        lines.append("Needs a decision this week: " + ", ".join(off) + ".")
    if problems:
        lines.append("")
        lines.append("Data problems:")
        for p in problems:
            lines.append("- " + p)
    return "\n".join(lines)


def _fixture():
    text = (
        "metric,unit,actual,target,prior,higher_is_better\n"
        "Revenue,INR,4120000,4500000,3980000,1\n"
        "Gross margin,%,31.5,34.0,33.2,1\n"
        "Refund rate,%,4.2,2.0,3.1,0\n"
        "Orders,count,1820,1700,1740,1\n"
        "New dealers,count,,12,9,1\n"
    )
    return list(csv.DictReader(io.StringIO(text)))


def self_test():
    checks = []

    def check(label, got, want):
        checks.append((label, got == want, got, want))

    rows = _fixture()
    table, problems = build(rows)
    check("all five rows parsed", len(table), 5)
    by = {r["metric"]: r for r in table}

    check("revenue inside the watch band", by["Revenue"]["rag"], "WATCH")
    check("revenue deviation computed", round(by["Revenue"]["deviation"], 4), round((4120000 - 4500000) / 4500000, 4))
    check("margin inside watch band", by["Gross margin"]["rag"], "WATCH")
    check("refund rate inverted for a lower-is-better metric", by["Refund rate"]["rag"], "OFF TRACK")
    check("orders beat target and are ON TRACK", by["Orders"]["rag"], "ON TRACK")
    check("orders vs prior is positive", by["Orders"]["vs_prior"] > 0, True)
    check("blank actual is NOT SET", by["New dealers"]["rag"], "NOT SET")
    check("blank actual is not silently zero", by["New dealers"]["actual"], None)
    check("blank actual is reported as a data problem", any("New dealers" in p for p in problems), True)

    check("zero target does not divide by zero", flag(10, 0, 1)[0], "NOT SET")
    check("blank prior leaves vs_prior empty", _pct(10, None), None)
    check("currency marks are tolerated", _num("₹1,23,456"), 123456.0)

    out = render(table, problems, period="October 2026")
    check("table header present", out.startswith("# MIS variance - October 2026"), True)
    check("biggest mover named", "Biggest move since last period:" in out, True)
    check("off-track metrics listed for a decision", "Refund rate" in out.split("Needs a decision this week:")[-1], True)
    check("output reproducible", render(table, problems, period="October 2026") == out, True)
    check("flag count line present", "Flags:" in out, True)

    failed = [c for c in checks if not c[1]]
    for label, ok, got, want in checks:
        print("%-52s %s" % (label, "ok" if ok else "FAIL (got %r, want %r)" % (got, want)))
    print("SELF-TEST: %s (%d/%d)" % ("PASS" if not failed else "FAIL", len(checks) - len(failed), len(checks)))
    return 0 if not failed else 1


def main(argv):
    if "--self-test" in argv:
        return self_test()
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: mis_variance.py <metrics.csv> [--csv] | --self-test")
        return 2
    try:
        with open(args[0], encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            missing = [c for c in ("metric", "actual", "target") if c not in (reader.fieldnames or [])]
            if missing:
                print("ERROR: CSV is missing required column(s): %s" % ", ".join(missing))
                return 1
            rows = list(reader)
    except OSError as exc:
        print("ERROR: cannot read %s: %s" % (args[0], exc))
        return 1
    table, problems = build(rows)
    if not table:
        print("ERROR: no usable metric rows in %s" % args[0])
        return 1
    if "--csv" in argv:
        writer = csv.writer(sys.stdout)
        writer.writerow(["metric", "unit", "actual", "target", "prior", "vs_target", "vs_prior", "flag"])
        for r in table:
            writer.writerow([r["metric"], r["unit"], r["actual"], r["target"], r["prior"],
                             r["vs_target"], r["vs_prior"], r["rag"]])
    else:
        print(render(table, problems))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
