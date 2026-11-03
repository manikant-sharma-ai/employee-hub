#!/usr/bin/env python3
"""Lint an email sequence for the failures that are mechanical, not creative.

Checks every email for the things that must never be missing (unsubscribe,
sender identity), the things that are almost always wrong (subject length,
spam-trigger words, broken merge tags), and the things that are wrong in
aggregate (cadence, duplicate subjects, two sends in 24 hours).

Deterministic: same JSON in, same report out. No network, no model.

Input: JSON
{
  "sequence": {"name": "welcome", "audience": "new signups", "exit": "first purchase"},
  "emails": [
    {"day": 0, "subject": "...", "preview": "...", "body": "...",
     "links": 1, "merge_tags": ["first_name"], "unsubscribe": true,
     "sender_identity": true}
  ]
}

Usage:
    python3 sequence_linter.py sequence.json          # exit 1 on errors
    python3 sequence_linter.py sequence.json --json
    python3 sequence_linter.py --self-test
"""
import argparse
import json
import re
import sys

MAX_SUBJECT = 60
SOFT_SUBJECT = 50
MAX_PREVIEW = 100
MIN_PREVIEW = 30
MAX_LINKS = 3
MIN_BODY_WORDS = 60
MAX_BODY_WORDS = 450
MAX_PER_DAY = 1
ALLOWED_TAGS = {"first_name", "last_name", "company", "city", "product",
                "order_id", "unsubscribe_url", "store_name"}

SPAM_WORDS = ["free money", "guaranteed", "risk-free", "act now", "limited time only",
              "100% free", "no cost", "cash bonus", "winner", "claim your",
              "urgent", "buy now", "cheap", "lowest price", "!!!", "$$$"]


def _words(text):
    return len(re.findall(r"[A-Za-z0-9\u0900-\u097F]+", text or ""))


def lint_email(i, e):
    errs, warns = [], []
    tag = "email %d (day %s)" % (i + 1, e.get("day", "?"))
    subj = e.get("subject", "") or ""
    prev = e.get("preview", "") or ""
    body = e.get("body", "") or ""

    if not subj.strip():
        errs.append(tag + ": subject is empty")
    elif len(subj) > MAX_SUBJECT:
        errs.append(tag + ": subject is %d chars, over the %d limit" % (len(subj), MAX_SUBJECT))
    elif len(subj) > SOFT_SUBJECT:
        warns.append(tag + ": subject is %d chars - mobile truncates near 40" % len(subj))

    if not prev.strip():
        warns.append(tag + ": preview is empty - the inbox will show body text instead")
    elif len(prev) > MAX_PREVIEW:
        warns.append(tag + ": preview is %d chars, over %d" % (len(prev), MAX_PREVIEW))
    elif len(prev) < MIN_PREVIEW:
        warns.append(tag + ": preview is only %d chars - it is the second half of the subject" % len(prev))
    if prev and subj and prev.strip().lower().startswith(subj.strip().lower()[:20]):
        warns.append(tag + ": preview repeats the subject")

    if not e.get("unsubscribe", False):
        errs.append(tag + ": no unsubscribe line - required on every marketing email")
    if not e.get("sender_identity", False):
        errs.append(tag + ": no sender identity / postal address block")

    links = e.get("links", 0)
    try:
        links = int(links)
    except (TypeError, ValueError):
        links = 0
    if links < 1:
        errs.append(tag + ": no link - the email has no action")
    elif links > MAX_LINKS:
        warns.append(tag + ": %d links - a newsletter with this many has no primary action" % links)

    wc = _words(body)
    if wc < MIN_BODY_WORDS:
        warns.append(tag + ": body is %d words - thin for a marketing email" % wc)
    elif wc > MAX_BODY_WORDS:
        warns.append(tag + ": body is %d words - cut it or split it" % wc)

    low = (subj + " " + prev + " " + body).lower()
    for w in SPAM_WORDS:
        if w in low:
            warns.append(tag + ": spam-trigger phrase %r" % w)
    letters = [c for c in subj if c.isalpha()]
    if letters and sum(1 for c in letters if c.isupper()) / len(letters) > 0.5 and len(letters) > 8:
        warns.append(tag + ": subject is mostly capitals")

    for m in re.findall(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}", subj + prev + body):
        if m not in ALLOWED_TAGS:
            errs.append(tag + ": unknown merge tag {{%s}}" % m)
    for m in e.get("merge_tags", []) or []:
        if m not in ALLOWED_TAGS:
            errs.append(tag + ": declared merge tag %r is not in the platform vocabulary" % m)

    return errs, warns


def lint(doc):
    errs, warns = [], []
    seq = doc.get("sequence", {}) or {}
    emails = doc.get("emails", []) or []

    if not emails:
        errs.append("sequence has no emails")
        return errs, warns
    for key in ("name", "audience", "exit"):
        if not str(seq.get(key, "")).strip():
            errs.append("sequence.%s is missing - a sequence without it has no boundary" % key)

    days = []
    for i, e in enumerate(emails):
        if not isinstance(e.get("day"), (int, float)):
            errs.append("email %d: day must be a number" % (i + 1))
            days.append(None)
        else:
            days.append(e["day"])
        a, b = lint_email(i, e)
        errs += a
        warns += b

    numeric = [d for d in days if d is not None]
    if numeric != sorted(numeric):
        errs.append("days are not in ascending order: %s" % numeric)
    for prev, cur in zip(numeric, numeric[1:]):
        if cur - prev < 1:
            errs.append("gap between day %s and day %s is under a day - two marketing emails in 24 hours" % (prev, cur))
        elif cur - prev > 14:
            warns.append("gap between day %s and day %s is %s days - the thread goes cold" % (prev, cur, cur - prev))

    per_day = {}
    for d in numeric:
        per_day[d] = per_day.get(d, 0) + 1
    for d, n in per_day.items():
        if n > MAX_PER_DAY:
            errs.append("day %s has %d emails - one per day per sequence" % (d, n))

    subs = [(e.get("subject", "") or "").strip().lower() for e in emails]
    dups = {s for s in subs if s and subs.count(s) > 1}
    for s in sorted(dups):
        errs.append("duplicate subject across the sequence: %r" % s)

    return errs, warns


GOOD = {
    "sequence": {"name": "welcome", "audience": "new signups, D2C", "exit": "first purchase"},
    "emails": [
        {"day": 0, "subject": "Your 10% code, and how to use it",
         "preview": "One code, three products it actually works on, expires in 14 days.",
         "body": "Here is the code: WELCOME10. It works on the 500ml and the 1L, and on "
                 "the sampler. It does not work on the gift box, because the gift box is "
                 "already discounted. Use it at checkout - the field is under the total. "
                 "If it does not apply, reply to this email and a person will fix it "
                 "within a working day. That is the whole email. See the three products "
                 "it covers, or read why we cold-press instead of refine.",
         "links": 2, "merge_tags": ["first_name"], "unsubscribe": True, "sender_identity": True},
        {"day": 2, "subject": "Why our oil costs more than the shop's",
         "preview": "Cold-pressed, 90 days shelf life, and the one thing we will not do.",
         "body": "The oil on the shelf is usually refined: heated, deodorised, and stable "
                 "for a year. Ours is pressed and bottled, which is why it costs more and "
                 "why it tastes of something. It also means a 90 day shelf life, and a "
                 "batch date on every bottle. We will not add preservatives to extend it. "
                 "If that trade is not worth it to you, the cheaper bottle is genuinely "
                 "the right buy. If it is, the range is here and the code still works.",
         "links": 2, "merge_tags": [], "unsubscribe": True, "sender_identity": True},
        {"day": 9, "subject": "What 40 customers said after a month",
         "preview": "Three quotes, one complaint, and what we changed because of it.",
         "body": "We asked 40 customers what changed after a month. Most said the same "
                 "thing: they used less oil per dish. Three said the bottle drips, which "
                 "is true of the old cap - we changed it in September. One said it was too "
                 "expensive and went back to the shop, which is a fair answer. The new cap "
                 "is on every bottle shipped this month. The code expires on Sunday.",
         "links": 1, "merge_tags": [], "unsubscribe": True, "sender_identity": True},
    ],
}

BAD = {
    "sequence": {"name": "blast", "audience": "", "exit": ""},
    "emails": [
        {"day": 0, "subject": "URGENT!!! BUY NOW - LIMITED TIME ONLY - GUARANTEED RESULTS FROM OUR AMAZING PRODUCT TODAY",
         "preview": "", "body": "Buy now.", "links": 6, "merge_tags": ["firstname"],
         "unsubscribe": False, "sender_identity": False},
        {"day": 0, "subject": "URGENT!!! BUY NOW - LIMITED TIME ONLY - GUARANTEED RESULTS FROM OUR AMAZING PRODUCT TODAY",
         "preview": "Same subject again", "body": "Hi {{customer_name}}, buy now. " * 40,
         "links": 1, "merge_tags": [], "unsubscribe": True, "sender_identity": True},
        {"day": 1, "subject": "One more thing", "preview": "A short note about delivery.",
         "body": "Delivery is free above 999. " * 10, "links": 1, "merge_tags": [],
         "unsubscribe": True, "sender_identity": True},
    ],
}


def self_test():
    e, w = lint(GOOD)
    assert e == [], "good sequence should have no errors, got %s" % e
    assert len(w) <= 3, "good sequence should be near-clean, got %s" % w

    e2, w2 = lint(BAD)
    joined = " | ".join(e2)
    assert any("over the 60 limit" in x for x in e2), joined
    assert any("no unsubscribe" in x for x in e2), joined
    assert any("no sender identity" in x for x in e2), joined
    assert any("sequence.audience" in x for x in e2), joined
    assert any("sequence.exit" in x for x in e2), joined
    assert any("unknown merge tag {{customer_name}}" in x for x in e2), joined
    assert any("day 0 has 2 emails" in x for x in e2), joined
    assert any("duplicate subject" in x for x in e2), joined
    assert any("under a day" in x for x in e2), joined
    assert any("no link" in x for x in e2) is False, "the bad fixture does have links"

    # Determinism and idempotence.
    assert json.dumps(lint(GOOD)) == json.dumps(lint(GOOD))
    assert json.dumps(lint(BAD)) == json.dumps(lint(BAD))

    # An empty sequence is an error, not a crash.
    assert lint({"sequence": {}, "emails": []})[0] == ["sequence has no emails"]

    # A single well-formed email with no preview warns but does not fail.
    one = {"sequence": {"name": "x", "audience": "y", "exit": "z"},
           "emails": [{"day": 0, "subject": "Short one", "preview": "", "body": "word " * 70,
                       "links": 1, "merge_tags": [], "unsubscribe": True, "sender_identity": True}]}
    oe, ow = lint(one)
    assert oe == [], oe
    assert any("preview is empty" in x for x in ow), ow

    print("self-test: all assertions passed (1 clean sequence, 1 broken sequence, 2 edge cases)")


def main():
    ap = argparse.ArgumentParser(description="Lint an email sequence JSON.")
    ap.add_argument("path", nargs="?", help="sequence JSON; omit to read stdin")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return 0
    raw = open(a.path, encoding="utf-8").read() if a.path else sys.stdin.read()
    doc = json.loads(raw)
    errs, warns = lint(doc)
    if a.json:
        print(json.dumps({"errors": errs, "warnings": warns,
                          "result": "FAIL" if errs else "PASS"}, indent=2))
    else:
        for x in errs:
            print("ERROR   " + x)
        for x in warns:
            print("warning " + x)
        print("RESULT: %s (%d errors, %d warnings)" % ("FAIL" if errs else "PASS", len(errs), len(warns)))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
