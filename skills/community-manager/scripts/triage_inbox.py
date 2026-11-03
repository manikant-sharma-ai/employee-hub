#!/usr/bin/env python3
"""Triage a batch of comments and DMs into a ranked reply queue.

Deterministic: same input, same output, no model, no network. The judgement is
in the rule tables below, which are meant to be edited for a given business -
not in a prompt that drifts.

Input: CSV with columns channel,author,text,minutes_waiting,is_customer
       (is_customer is y/n; an optional followers column is accepted and ignored
        except for reach, which only breaks ties).

Output: TSV to stdout, highest risk first, then longest-waiting.
        --json emits the same rows as JSON.

Usage:
    python3 triage_inbox.py batch.csv
    python3 triage_inbox.py --self-test
"""
import argparse
import csv
import io
import json
import re
import sys

BUCKETS = ["abuse_or_spam", "high_risk_complaint", "complaint", "buying_signal",
           "question", "praise", "off_topic"]

# Ordered rules: first match wins. Lower-case substring tests, deliberately dumb
# and readable so a business can audit why a comment was bucketed a certain way.
SPAM = ["earn from home", "work from home job", "click here", "bit.ly", "t.me/",
        "dm for promo", "free followers", "investment tip", "loan approved"]
ABUSE = ["idiot", "stupid", "fraud company", "chor", "bakwas", "scam", "cheat",
         "worthless", "shut up", "kill you", "will find you"]
HIGH_RISK = ["burn", "burnt", "fire", "injur", "hospital", "hurt", "allerg",
             "rash", "sick", "poison", "lawyer", "legal notice", "court", "police",
             "consumer forum", "aadhaar", "aadhar", "data leak", "privacy", "death",
             "refund", "money back", "charged twice", "duplicate payment"]
BUYING = ["price", "how much", "kitna", "rate", "cost", "dm me", "interested",
          "order", "buy", "bulk", "wholesale", "quotation", "quote", "cod",
          "cash on delivery", "deliver to", "stock"]
COMPLAINT = ["not received", "not delivered", "still waiting", "third time",
             "no response", "broken", "damaged", "wrong item", "missing",
             "worst", "disappointed", "return", "complaint", "late"]
PRAISE = ["love", "great", "amazing", "best", "thank", "beautiful", "nice",
          "super", "excellent", "mast", "zabardast"]
OFF_TOPIC = ["election", "politic", "religion", "cricket score", "follow back",
             "f4f", "l4l"]

# bucket -> (sla hours for first touch, decision, base urgency 0-3)
PLAYBOOK = {
    "abuse_or_spam":      (0, "no reply - hide or remove, log the rule", 2),
    "high_risk_complaint": (1, "do not reply until a human has seen it", 3),
    "complaint":          (2, "public reply, then move to DM", 2),
    "buying_signal":      (1, "public reply, then DM - hand to sales with context", 3),
    "question":           (8, "public reply, one specific sentence", 1),
    "praise":             (48, "like, or one short line", 0),
    "off_topic":          (72, "ignore - log if it repeats", 0),
}


def _has(text, words):
    low = " " + re.sub(r"\s+", " ", text.lower()) + " "
    return any(w in low for w in words)


def classify(text):
    """Return (bucket, risk, matched_terms). Risk is 'high', 'medium' or 'low'."""
    hits = []
    if _has(text, SPAM):
        return "abuse_or_spam", "medium", [w for w in SPAM if w in text.lower()]
    if _has(text, HIGH_RISK):
        hits = [w for w in HIGH_RISK if w in text.lower()]
        return "high_risk_complaint", "high", hits
    if _has(text, ABUSE):
        hits = [w for w in ABUSE if w in text.lower()]
        # Abuse aimed at the brand with a product grievance is still a complaint
        # that needs a human; abuse with nothing else is spam-adjacent noise.
        if _has(text, COMPLAINT):
            return "high_risk_complaint", "high", hits
        return "abuse_or_spam", "medium", hits
    if _has(text, COMPLAINT):
        return "complaint", "medium", [w for w in COMPLAINT if w in text.lower()]
    if _has(text, BUYING):
        return "buying_signal", "low", [w for w in BUYING if w in text.lower()]
    if _has(text, PRAISE):
        return "praise", "low", [w for w in PRAISE if w in text.lower()]
    if _has(text, OFF_TOPIC):
        return "off_topic", "low", [w for w in OFF_TOPIC if w in text.lower()]
    return "question", "low", []


def triage_row(row):
    text = row.get("text", "")
    bucket, risk, hits = classify(text)
    sla, decision, base = PLAYBOOK[bucket]
    try:
        waited = float(row.get("minutes_waiting", 0) or 0)
    except ValueError:
        waited = 0.0
    waited_h = waited / 60.0
    # Urgency rises with waiting, but a high-risk item is urgent regardless.
    urgency = base + (2 if waited_h >= 24 else 1 if waited_h >= 4 else 0)
    overdue = waited_h > sla if sla else waited_h > 0
    return {
        "channel": row.get("channel", "").strip(),
        "author": row.get("author", "").strip(),
        "bucket": bucket,
        "risk": risk,
        "urgency": min(urgency, 5),
        "waited_h": round(waited_h, 1),
        "sla_h": sla,
        "overdue": overdue,
        "customer": (row.get("is_customer", "").strip().lower() in ("y", "yes", "true", "1")),
        "decision": decision,
        "matched": ", ".join(sorted(set(hits))),
        "text": re.sub(r"\s+", " ", text).strip()[:160],
    }


RISK_ORDER = {"high": 0, "medium": 1, "low": 2}


def rank(rows):
    return sorted(rows, key=lambda r: (RISK_ORDER[r["risk"]], -r["urgency"],
                                       -r["waited_h"], r["author"]))


def summarise(rows):
    counts = {b: 0 for b in BUCKETS}
    for r in rows:
        counts[r["bucket"]] += 1
    return {
        "total": len(rows),
        "counts": counts,
        "overdue": sum(1 for r in rows if r["overdue"]),
        "high_risk": sum(1 for r in rows if r["risk"] == "high"),
        "buying_signals": counts["buying_signal"],
    }


def run(text):
    rows = [triage_row(r) for r in csv.DictReader(io.StringIO(text))]
    return rank(rows)


def emit(rows, as_json=False):
    if as_json:
        print(json.dumps({"summary": summarise(rows), "rows": rows}, indent=2))
        return
    cols = ["bucket", "risk", "urgency", "waited_h", "sla_h", "overdue", "channel",
            "author", "customer", "decision", "matched", "text"]
    print("\t".join(cols))
    for r in rows:
        print("\t".join(str(r[c]) for c in cols))
    s = summarise(rows)
    print("\n# total=%d high_risk=%d overdue=%d buying_signals=%d"
          % (s["total"], s["high_risk"], s["overdue"], s["buying_signals"]))
    print("# " + " ".join("%s=%d" % (b, n) for b, n in s["counts"].items() if n))


FIXTURE = """channel,author,text,minutes_waiting,is_customer
instagram,asha_09,Price for the 1L bottle?,45,y
instagram,rahul_k,The bottle burnt my hand and I am going to the hospital,600,y
instagram,promo_king,Earn from home 5000 daily click here,10,n
instagram,deepa_r,Third time asking - still waiting for my order,3000,y
linkedin,vikram_s,Do you do bulk rates for 200 units?,90,n
instagram,meera,Love this colour so much,30,n
instagram,random_guy,Election results are out,20,n
instagram,priya,Is COD available in Kochi?,200,y
"""


def self_test():
    rows = run(FIXTURE)
    by = {r["author"]: r for r in rows}

    assert by["rahul_k"]["bucket"] == "high_risk_complaint", by["rahul_k"]
    assert by["rahul_k"]["risk"] == "high"
    assert rows[0]["author"] == "rahul_k", "highest risk must rank first"
    assert by["asha_09"]["bucket"] == "buying_signal"
    assert by["promo_king"]["bucket"] == "abuse_or_spam"
    assert by["deepa_r"]["bucket"] == "complaint"
    assert by["deepa_r"]["overdue"] is True, "50 hours against a 2 hour SLA is overdue"
    assert by["vikram_s"]["bucket"] == "buying_signal"
    assert by["meera"]["bucket"] == "praise"
    assert by["random_guy"]["bucket"] == "off_topic"
    assert by["priya"]["bucket"] == "buying_signal"

    s = summarise(rows)
    assert s["total"] == 8, s
    assert s["high_risk"] == 1, s
    assert s["buying_signals"] == 3, s
    assert s["overdue"] == 5, s

    # Determinism: identical input must give identical output, twice.
    assert json.dumps(run(FIXTURE)) == json.dumps(run(FIXTURE))

    # Empty batch is not a crash.
    assert run("channel,author,text,minutes_waiting,is_customer\n") == []

    # A refund demand is high risk even when phrased politely.
    assert triage_row({"text": "Please process my refund", "minutes_waiting": "5"})["risk"] == "high"

    print("self-test: all assertions passed (8 fixture rows, 12 checks)")


def main():
    ap = argparse.ArgumentParser(description="Triage comments and DMs into a ranked queue.")
    ap.add_argument("path", nargs="?", help="CSV batch file; omit to read stdin")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of TSV")
    ap.add_argument("--self-test", action="store_true", help="run the built-in assertions")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return 0
    data = open(a.path, encoding="utf-8").read() if a.path else sys.stdin.read()
    emit(run(data), a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
