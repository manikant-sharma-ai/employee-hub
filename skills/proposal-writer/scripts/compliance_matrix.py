#!/usr/bin/env python3
"""Build the compliance matrix for an RFP response, and score it honestly.

Every requirement in the buyer's document becomes one row: is it mandatory, who
answers it, what is the status. The score is mandatory coverage, not word count,
because a proposal that misses one mandatory requirement is a disqualified proposal
however well it reads.

Deterministic: same CSV in, same matrix and same score out.

CSV columns:
  req_id, requirement, mandatory, section, owner, status

  mandatory   Y/N (or 1/0, true/false)
  status      answered | partial | gap | todo   (anything else is treated as todo)

Usage:
  python3 compliance_matrix.py --self-test
  python3 compliance_matrix.py requirements.csv [--gate]

  --gate exits 1 if any mandatory requirement is not answered, which is the
  check to run before the proposal leaves the building.

Exit 0 = matrix produced. Exit 1 = unusable file, or --gate with gaps.
"""
import csv
import sys

STATUSES = ("answered", "partial", "gap", "todo")
COUNTED_AS_ANSWERED = ("answered",)


def _truthy(value):
    return str(value or "").strip().lower() in ("y", "yes", "1", "true", "mandatory", "m")


def build(rows):
    matrix, problems = [], []
    for i, row in enumerate(rows, start=2):
        req_id = (row.get("req_id") or "").strip()
        text = (row.get("requirement") or "").strip()
        if not req_id or not text:
            problems.append("line %d: missing req_id or requirement text - skipped" % i)
            continue
        status = (row.get("status") or "todo").strip().lower()
        if status not in STATUSES:
            problems.append("%s: unknown status %r - counted as todo" % (req_id, status))
            status = "todo"
        owner = (row.get("owner") or "").strip()
        if not owner:
            problems.append("%s: no owner - an unowned requirement is nobody's deadline" % req_id)
        matrix.append({
            "req_id": req_id,
            "requirement": text,
            "mandatory": _truthy(row.get("mandatory")),
            "section": (row.get("section") or "General").strip() or "General",
            "owner": owner or "UNASSIGNED",
            "status": status,
        })
    return matrix, problems


def score(matrix):
    mandatory = [r for r in matrix if r["mandatory"]]
    answered = [r for r in mandatory if r["status"] in COUNTED_AS_ANSWERED]
    partial = [r for r in mandatory if r["status"] == "partial"]
    open_mandatory = [r for r in mandatory if r["status"] not in COUNTED_AS_ANSWERED]
    optional = [r for r in matrix if not r["mandatory"]]
    coverage = (len(answered) / len(mandatory) * 100.0) if mandatory else 0.0
    return {
        "total": len(matrix),
        "mandatory": len(mandatory),
        "answered": len(answered),
        "partial": len(partial),
        "open_mandatory": open_mandatory,
        "optional": len(optional),
        "coverage_pct": coverage,
        "ready": bool(mandatory) and not open_mandatory,
    }


def render(matrix, problems):
    s = score(matrix)
    lines = ["# Compliance matrix", ""]
    lines.append("Mandatory coverage: %d/%d answered (%.0f%%). %d mandatory open, %d partial." % (
        s["answered"], s["mandatory"], s["coverage_pct"], len(s["open_mandatory"]), s["partial"]))
    lines.append("Verdict: %s" % ("READY to send" if s["ready"] else "NOT READY - mandatory requirements open"))
    lines.append("")
    sections = []
    for r in matrix:
        if r["section"] not in sections:
            sections.append(r["section"])
    for section in sections:
        lines.append("## %s" % section)
        lines.append("")
        lines.append("| Req | Requirement | M | Owner | Status |")
        lines.append("|---|---|---|---|---|")
        for r in matrix:
            if r["section"] == section:
                lines.append("| %s | %s | %s | %s | %s |" % (
                    r["req_id"], r["requirement"], "M" if r["mandatory"] else "-",
                    r["owner"], r["status"]))
        lines.append("")
    if s["open_mandatory"]:
        lines.append("## Open mandatory requirements")
        for r in s["open_mandatory"]:
            lines.append("- **%s** (%s) - %s - owner %s" % (
                r["req_id"], r["section"], r["requirement"], r["owner"]))
        lines.append("")
    if problems:
        lines.append("## Data problems")
        for p in problems:
            lines.append("- " + p)
    return "\n".join(lines).rstrip() + "\n"


def _fixture():
    text = (
        "req_id,requirement,mandatory,section,owner,status\n"
        "M1,ISO 27001 certificate or equivalent,Y,Compliance,security-reviewer,answered\n"
        "M2,Three reference customers in India,Y,Experience,proposal-writer,partial\n"
        "M3,Implementation within 45 days,Y,Delivery,ops-automator,todo\n"
        "M4,Annual price in INR,Y,Pricing,finance-ops,answered\n"
        "O1,Optional training package,N,Pricing,,gap\n"
        "O2,Case study on sustainability,N,Experience,proposal-writer,answered\n"
    )
    return list(csv.DictReader(__import__("io").StringIO(text)))


def self_test():
    checks = []

    def check(label, got, want):
        checks.append((label, got == want, got, want))

    matrix, problems = build(_fixture())
    s = score(matrix)

    check("six requirements parsed", s["total"], 6)
    check("four are mandatory", s["mandatory"], 4)
    check("two mandatory answered", s["answered"], 2)
    check("one mandatory partial", s["partial"], 1)
    check("two mandatory open", len(s["open_mandatory"]), 2)
    check("coverage is 50 percent", s["coverage_pct"], 50.0)
    check("not ready with mandatory open", s["ready"], False)
    check("unowned requirement flagged", any("O1" in p for p in problems), True)
    check("mandatory parsing accepts Y", matrix[0]["mandatory"], True)
    check("mandatory parsing rejects N", matrix[4]["mandatory"], False)

    out = render(matrix, problems)
    check("verdict line present", "NOT READY" in out, True)
    check("gaps listed with owners", "M3" in out.split("## Open mandatory requirements")[-1], True)
    check("sections preserved in order", out.index("## Compliance") < out.index("## Experience"), True)
    check("output reproducible", render(matrix, problems) == out, True)

    clean = [r for r in matrix if not r["mandatory"]]
    s2 = score(clean)
    check("optional-only sheet is not called ready", s2["ready"], False)
    check("unknown status becomes todo", build([{"req_id": "X", "requirement": "y", "status": "done"}])[0][0]["status"], "todo")

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
        print("usage: compliance_matrix.py <requirements.csv> [--gate] | --self-test")
        return 2
    try:
        with open(args[0], encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            missing = [c for c in ("req_id", "requirement") if c not in (reader.fieldnames or [])]
            if missing:
                print("ERROR: CSV is missing required column(s): %s" % ", ".join(missing))
                return 1
            rows = list(reader)
    except OSError as exc:
        print("ERROR: cannot read %s: %s" % (args[0], exc))
        return 1
    matrix, problems = build(rows)
    if not matrix:
        print("ERROR: no usable requirement rows in %s" % args[0])
        return 1
    print(render(matrix, problems))
    if "--gate" in argv:
        s = score(matrix)
        if not s["ready"]:
            print("%d mandatory requirement(s) still open - do not send." % len(s["open_mandatory"]))
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
