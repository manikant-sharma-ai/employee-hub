#!/usr/bin/env python3
"""Audit a YouTube export and name the failure on each video.

Reads a CSV exported from YouTube Studio (or kept by hand) and reports, per
video: click-through, percentage viewed, and a named failure drawn from four
causes - `packaging`, `hook`, `body` or `fine`. The channel median is computed
from the file itself, so the audit is always relative to this channel.

Deterministic: no network, no randomness, no wall clock. Same file in, same
report out.

CSV columns (header required, order free):
    video_id, title, published, impressions, views,
    avg_view_duration_sec, length_sec

Usage:
    python3 packaging_audit.py videos.csv
    python3 packaging_audit.py videos.csv --min-impressions 500
    python3 packaging_audit.py --self-test
"""
import csv
import sys

COLUMNS = ["video_id", "title", "published", "impressions", "views",
           "avg_view_duration_sec", "length_sec"]

# Bands from references/retention-and-watch-time.md: percentage viewed worth
# having, by length. Below the band the video is losing people.
BANDS = [(60, 0.70), (480, 0.40), (1200, 0.30), (10 ** 9, 0.25)]

TITLE_CAP = 60


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("missing columns: %s" % ", ".join(missing))
        for raw in reader:
            length = int(raw["length_sec"])
            impressions = int(raw["impressions"])
            views = int(raw["views"])
            avd = float(raw["avg_view_duration_sec"])
            rows.append({
                "video_id": raw["video_id"].strip(),
                "title": raw["title"].strip(),
                "published": raw["published"].strip(),
                "impressions": impressions,
                "views": views,
                "avd": avd,
                "length": length,
                "ctr": (100.0 * views / impressions) if impressions else 0.0,
                "pct_viewed": (100.0 * avd / length) if length else 0.0,
            })
    return rows


def median(values):
    s = sorted(values)
    n = len(s)
    if not n:
        return 0.0
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2.0


def band_for(length):
    for cap, floor in BANDS:
        if length <= cap:
            return floor
    return BANDS[-1][1]


def classify(row, ctr_median, pct_median, min_impressions):
    """Four causes, in the order they should be fixed."""
    if row["impressions"] < min_impressions:
        return "untested", "too few impressions to judge"
    if row["ctr"] < ctr_median:
        return "packaging", "click-through %.1f%% is under the channel median %.1f%%" % (
            row["ctr"], ctr_median)
    band = band_for(row["length"]) * 100
    if row["pct_viewed"] < band:
        return "hook", "clicked, then left: %.0f%% viewed against a %.0f%% band for %ds" % (
            row["pct_viewed"], band, row["length"])
    if row["length"] > 480 and row["pct_viewed"] < band * 1.25:
        return "body", ("long video only just clearing its band: %.0f%% viewed against %.0f%%, "
                        "so the promise is being paid out too slowly" % (row["pct_viewed"], band))
    return "fine", "packaging and retention both hold"


def audit(rows, min_impressions=500):
    judged = [r for r in rows if r["impressions"] >= min_impressions]
    ctr_median = median([r["ctr"] for r in judged]) if judged else 0.0
    pct_median = median([r["pct_viewed"] for r in judged]) if judged else 0.0
    out = []
    for r in rows:
        verdict, reason = classify(r, ctr_median, pct_median, min_impressions)
        item = dict(r)
        item["verdict"] = verdict
        item["reason"] = reason
        item["title_over"] = len(r["title"]) > TITLE_CAP
        out.append(item)
    order = {"packaging": 0, "hook": 1, "body": 2, "fine": 3, "untested": 4}
    out.sort(key=lambda x: (order[x["verdict"]], -x["impressions"]))
    return out, ctr_median, pct_median


def render(items, ctr_median, pct_median):
    counts = {}
    for i in items:
        counts[i["verdict"]] = counts.get(i["verdict"], 0) + 1
    lines = ["# Packaging and retention audit", ""]
    lines.append("Channel median click-through **%.1f%%**, median percentage viewed **%.0f%%**."
                 % (ctr_median, pct_median))
    lines.append("")
    lines.append("| Verdict | Videos |")
    lines.append("|---|---|")
    for k in ("packaging", "hook", "body", "fine", "untested"):
        if counts.get(k):
            lines.append("| %s | %d |" % (k, counts[k]))
    lines.append("")
    lines.append("## Fix in this order")
    lines.append("")
    lines.append("| Video | Title | CTR | Viewed | Verdict | Evidence |")
    lines.append("|---|---|---|---|---|---|")
    for i in items:
        flag = " (title over %d chars)" % TITLE_CAP if i["title_over"] else ""
        lines.append("| %s | %s%s | %.1f%% | %.0f%% | %s | %s |"
                     % (i["video_id"], i["title"].replace("|", "/"), flag, i["ctr"],
                        i["pct_viewed"], i["verdict"], i["reason"]))
    lines.append("")
    lines.append("_Computed by scripts/packaging_audit.py from the Studio export. "
                 "Click-through needs impressions; retention needs watch time. Neither is estimated._")
    return "\n".join(lines)


FIXTURE = """video_id,title,published,impressions,views,avg_view_duration_sec,length_sec
V-01,How to raise a GST invoice in 4 clicks,2026-10-02,12000,960,300,360
V-02,Our factory tour,2026-10-09,9000,180,90,600
V-03,Dead stock: what it really costs,2026-10-16,8000,640,90,540
V-04,Why your dispatch is slow,2026-10-23,300,15,60,300
V-05,The five-minute GST check,2026-10-30,6000,600,210,600
"""


def self_test():
    import tempfile
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("FAIL %s: got %r, want %r" % (label, got, want))

    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        fh.write(FIXTURE)
        path = fh.name
    rows = load(path)
    check("rows", len(rows), 5)
    check("ctr V-01", round(rows[0]["ctr"], 2), 8.0)
    check("pct V-01", round(rows[0]["pct_viewed"], 2), 83.33)
    check("pct V-05", round(rows[4]["pct_viewed"], 2), 35.0)
    check("zero impressions safe", _zero_impressions(), 0.0)

    items, ctr_med, pct_med = audit(rows)
    check("median ctr", round(ctr_med, 2), 8.0)
    check("median pct", round(pct_med, 2), 25.83)
    verdicts = {i["video_id"]: i["verdict"] for i in items}
    check("V-01 fine", verdicts["V-01"], "fine")
    check("V-02 packaging", verdicts["V-02"], "packaging")
    check("V-03 hook", verdicts["V-03"], "hook")
    check("V-04 untested", verdicts["V-04"], "untested")
    check("V-05 body", verdicts["V-05"], "body")
    check("fix order", [i["video_id"] for i in items],
          ["V-02", "V-03", "V-05", "V-01", "V-04"])
    check("band under 60s", band_for(45), 0.70)
    check("band 8 min", band_for(480), 0.40)
    check("band 20 min", band_for(1200), 0.30)
    check("band long", band_for(3600), 0.25)

    text = render(items, ctr_med, pct_med)
    check("report names packaging", "| V-02 |" in text and "packaging" in text, True)
    check("determinism", render(*audit(load(path))[:1] + (ctr_med, pct_med)) == text, True)
    print("self-test: %s" % ("PASS (19 checks)" if ok else "FAIL"))
    return 0 if ok else 1


def _zero_impressions():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as fh:
        fh.write("video_id,title,published,impressions,views,avg_view_duration_sec,length_sec\n"
                 "V-00,Zero,2026-10-01,0,0,0,300\n")
        path = fh.name
    return load(path)[0]["ctr"]


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    min_impressions = 500
    if "--min-impressions" in argv:
        min_impressions = int(argv[argv.index("--min-impressions") + 1])
    try:
        rows = load(path)
    except (ValueError, KeyError) as exc:
        print("cannot read %s: %s" % (path, exc))
        return 2
    items, ctr_med, pct_med = audit(rows, min_impressions)
    print(render(items, ctr_med, pct_med))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
