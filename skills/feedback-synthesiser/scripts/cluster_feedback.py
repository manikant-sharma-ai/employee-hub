#!/usr/bin/env python3
"""Deterministic theme counts for feedback-synthesiser.

    python3 scripts/cluster_feedback.py --csv feedback.csv --themes themes.json
    python3 scripts/cluster_feedback.py --self-test

CSV columns required: id, source, text. Optional: date, rating, segment.
Themes file: {"theme-id": {"label": "...", "include": ["phrase", ...], "exclude": ["phrase", ...],
                           "severity": "S1|S2|S3|S4"}}

Counting rules, fixed and stated in the output:
  - a record is counted once per theme, no matter how many phrases it matches
  - a record may carry at most TWO themes (the two with the most phrase hits, then file order)
  - shares are records-mentioning / records-total, so they do not sum to 100
  - a record matching nothing goes to `other`, and an `other` share above 15% is reported as a finding

No network, no model call. The same file always produces the same counts.
Exit 0 on success, 1 on a data error, 2 on bad usage.
"""
import csv
import io
import json
import sys

MAX_THEMES_PER_RECORD = 2
OTHER_ALERT_SHARE = 0.15

STARTER_THEMES = {
    "onboarding-slow": {"label": "Onboarding takes more than a day", "severity": "S2",
                        "include": ["took days", "could not finish setup", "setup took",
                                    "import failed", "onboarding took", "couldn't set up"],
                        "exclude": ["onboarding was easy"]},
    "payment-failed": {"label": "Payment or invoice failed", "severity": "S1",
                       "include": ["payment failed", "card declined", "invoice did not match",
                                   "double charged", "charged twice", "refund not received"],
                       "exclude": []},
    "delivery-late": {"label": "Delivery arrived late", "severity": "S3",
                      "include": ["arrived late", "delivered late", "delayed by", "still waiting",
                                  "not delivered", "late delivery"],
                      "exclude": []},
    "support-unsolved": {"label": "Support replied but did not solve it", "severity": "S2",
                         "include": ["no response", "did not solve", "still not fixed",
                                     "no reply", "kept asking me", "told me to restart"],
                         "exclude": []},
    "pricing-value": {"label": "Price does not match the value", "severity": "S3",
                      "include": ["too expensive", "not worth", "price increased",
                                  "overpriced", "cheaper alternative"],
                      "exclude": []},
    "missing-feature": {"label": "A needed feature is missing", "severity": "S3",
                        "include": ["no option to", "wish it had", "cannot export",
                                    "missing feature", "does not support"],
                        "exclude": []},
    "quality-defect": {"label": "The product arrived defective", "severity": "S2",
                       "include": ["broken", "damaged", "does not work", "stopped working",
                                   "crashes", "defective"],
                       "exclude": []},
}


def load_themes(path=None):
    if not path:
        return STARTER_THEMES
    data = json.load(open(path, encoding="utf-8"))
    if not isinstance(data, dict) or not data:
        raise ValueError("themes file must be a non-empty object")
    for key, spec in data.items():
        if "include" not in spec or not spec["include"]:
            raise ValueError("theme %r has no include phrases" % key)
        if spec.get("severity") not in (None, "S1", "S2", "S3", "S4"):
            raise ValueError("theme %r has an invalid severity" % key)
    return data


def load_records(text):
    reader = csv.DictReader(io.StringIO(text.strip()))
    if reader.fieldnames is None:
        raise ValueError("empty CSV")
    fields = [f.strip() for f in reader.fieldnames]
    for need in ("id", "source", "text"):
        if need not in fields:
            raise ValueError("missing column: %s" % need)
    records = []
    for i, raw in enumerate(reader, start=2):
        row = {k.strip(): (v or "").strip() for k, v in raw.items() if k}
        text_body = row.get("text", "")
        if not text_body:
            continue  # empty records are excluded and counted
        records.append({"id": row["id"], "source": row.get("source", "unknown").lower(),
                        "text": text_body, "date": row.get("date", ""),
                        "segment": row.get("segment", ""),
                        "rating": row.get("rating", "")})
    if not records:
        raise ValueError("no records with text")
    return records


def match_themes(record, themes):
    """Return the themes a record carries, at most MAX_THEMES_PER_RECORD, deterministic."""
    body = record["text"].lower()
    scored = []
    for order, (key, spec) in enumerate(themes.items()):
        if any(x.lower() in body for x in spec.get("exclude", [])):
            continue
        hits = sum(1 for phrase in spec["include"] if phrase.lower() in body)
        if hits:
            scored.append((-hits, order, key))
    scored.sort()
    return [k for _, _, k in scored[:MAX_THEMES_PER_RECORD]]


def cluster(records, themes):
    counts = {k: 0 for k in themes}
    per_source = {k: {} for k in themes}
    quotes = {k: [] for k in themes}
    other = []
    for r in records:
        keys = match_themes(r, themes)
        if not keys:
            other.append(r)
            continue
        for k in keys:
            counts[k] += 1
            per_source[k][r["source"]] = per_source[k].get(r["source"], 0) + 1
            if len(quotes[k]) < 3:
                quotes[k].append(r)
    total = len(records)
    rows = []
    for k, spec in themes.items():
        n = counts[k]
        if not n:
            continue
        rows.append({"theme": k, "label": spec.get("label", k), "severity": spec.get("severity", ""),
                     "records": n, "share": round(n / total, 3),
                     "sources": per_source[k], "quotes": quotes[k]})
    rows.sort(key=lambda r: (-r["records"], r["theme"]))
    return {"total": total, "rows": rows, "other": other,
            "other_share": round(len(other) / total, 3)}


def _selftest():
    checks = 0
    sample = """id,source,date,segment,text
1,ticket,2026-11-01,smb,"Setup took two days, the import failed twice"
2,ticket,2026-11-01,smb,"Payment failed at checkout and then it double charged"
3,review,2026-11-02,smb,"Delivery arrived late by three days"
4,review,2026-11-02,ent,"Arrived late and the box was damaged"
5,survey,2026-11-03,smb,"Too expensive for what it does"
6,survey,2026-11-03,ent,""
7,whatsapp,2026-11-04,smb,"Thank you, all good"
8,ticket,2026-11-04,ent,"No response for four days, still not fixed"
"""
    records = load_records(sample)
    assert len(records) == 7, "the empty record must be excluded"
    checks += 1

    themes = load_themes()
    assert len(themes) == 7
    checks += 1

    r = cluster(records, themes)
    assert r["total"] == 7
    assert r["other_share"] == round(1 / 7, 3), r["other_share"]
    assert [o["id"] for o in r["other"]] == ["7"]
    checks += 3

    by = {row["theme"]: row for row in r["rows"]}
    assert by["onboarding-slow"]["records"] == 1
    assert by["payment-failed"]["records"] == 1
    assert by["delivery-late"]["records"] == 2, "two records mention a late delivery"
    assert by["support-unsolved"]["records"] == 1
    assert by["pricing-value"]["records"] == 1
    checks += 5

    assert by["delivery-late"]["sources"] == {"review": 2}
    assert by["delivery-late"]["share"] == round(2 / 7, 3)
    assert len(by["delivery-late"]["quotes"]) == 2
    checks += 3

    # ranking: delivery-late (2) must come first
    assert r["rows"][0]["theme"] == "delivery-late", r["rows"][0]
    checks += 1

    # a record carrying three matches keeps only two themes
    multi = [{"id": "9", "source": "ticket", "text": "payment failed, delivery arrived late, "
                                                      "and support gave no response", "date": "",
              "segment": "", "rating": ""}]
    keys = match_themes(multi[0], themes)
    assert len(keys) == MAX_THEMES_PER_RECORD, keys
    checks += 1

    # exclude wins over include
    custom = {"x": {"label": "X", "include": ["slow"], "exclude": ["not slow"]}}
    rec = [{"id": "10", "source": "t", "text": "the app is not slow at all", "date": "",
            "segment": "", "rating": ""}]
    assert match_themes(rec[0], custom) == [], "exclude must override include"
    checks += 1

    # theme with no hits is dropped from the output, not printed at zero
    r2 = cluster([{"id": "11", "source": "t", "text": "broken hinge", "date": "",
                   "segment": "", "rating": ""}], themes)
    assert [row["theme"] for row in r2["rows"]] == ["quality-defect"], r2["rows"]
    checks += 1

    for bad in ("id,source\ntext,x\n", "id,source,text\n"):
        try:
            load_records(bad)
        except ValueError:
            checks += 1
        else:
            raise AssertionError("accepted a CSV without required columns or rows")

    try:
        load_themes("/nonexistent/themes.json")
    except OSError:
        checks += 1
    else:
        raise AssertionError("accepted a missing themes file")

    print("self-test: %d checks passed" % checks)
    return 0


def main(argv):
    if "--self-test" in argv:
        return _selftest()

    def arg(flag):
        return argv[argv.index(flag) + 1] if flag in argv and argv.index(flag) + 1 < len(argv) else None

    if not arg("--csv"):
        print(__doc__)
        return 2
    try:
        records = load_records(open(arg("--csv"), encoding="utf-8").read())
        themes = load_themes(arg("--themes"))
        r = cluster(records, themes)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print("ERROR: %s" % e)
        return 1

    print("records read: %d | themes matched: %d | unmatched: %d (%.1f%%)" % (
        r["total"], len(r["rows"]), len(r["other"]), r["other_share"] * 100))
    print("counting rule: one record counts once per theme, max two themes per record, "
          "shares are records/total and do not sum to 100\n")
    for row in r["rows"]:
        srcs = ", ".join("%s %d" % (s, n) for s, n in sorted(row["sources"].items()))
        print("%-20s %-45s %3d  %5.1f%%  %-3s  %s" % (
            row["theme"], row["label"][:45], row["records"], row["share"] * 100,
            row["severity"], srcs))
        for q in row["quotes"][:1]:
            print("    \"%s\" (%s, %s)" % (q["text"][:90], q["source"], q["date"] or "no date"))
    if r["other_share"] > OTHER_ALERT_SHARE:
        print("\nFINDING: %.1f%% of records matched no theme - re-read them before publishing, "
              "the theme list is probably missing the newest problem" % (r["other_share"] * 100))
    if r["other"]:
        print("\nunmatched record ids: %s" % ", ".join(o["id"] for o in r["other"][:20]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
