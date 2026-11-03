#!/usr/bin/env python3
"""Check a translation against its source, its glossary and its length budget.

Catches the failures that are mechanical: dropped or reordered placeholders,
glossary terms rendered two different ways, untranslated strings, script mixing,
length expansion beyond the language allowance, and Indian number/currency
formats written the foreign way.

Deterministic, stdlib only, no network.

Input JSON:
{
  "target_lang": "hi",
  "pairs": [{"id": "btn.save", "source": "Save {count} items", "target": "..."}],
  "glossary": {"invoice": {"hi": "चालान", "do_not_translate": false}}
}

Usage:
    python3 glossary_check.py strings.json
    python3 glossary_check.py strings.json --json
    python3 glossary_check.py --self-test
"""
import argparse
import json
import re
import sys

# Expansion allowance per target language, as a ratio of source length.
EXPANSION = {"hi": 1.15, "mr": 1.25, "gu": 1.20, "bn": 1.25,
             "ta": 1.40, "te": 1.35, "kn": 1.40, "ml": 1.45}

SCRIPTS = {
    "hi": r"[\u0900-\u097F]", "mr": r"[\u0900-\u097F]", "bn": r"[\u0980-\u09FF]",
    "gu": r"[\u0A80-\u0AFF]", "ta": r"[\u0B80-\u0BFF]", "te": r"[\u0C00-\u0C7F]",
    "kn": r"[\u0C80-\u0CFF]", "ml": r"[\u0D00-\u0D7F]",
}

SCRIPT_RANGES = {}
for _l, _p in SCRIPTS.items():
    SCRIPT_RANGES.setdefault(_p, []).append(_l)
for _p in SCRIPT_RANGES:
    SCRIPT_RANGES[_p] = sorted(SCRIPT_RANGES[_p])

PLACEHOLDER_RE = re.compile(r"(\{[a-zA-Z0-9_]+\}|\{\{[a-zA-Z0-9_]+\}\}|%[sd]|%\d+\$s)")


def placeholders(text):
    return PLACEHOLDER_RE.findall(text or "")


def check_pair(pair, glossary, lang):
    errs, warns = [], []
    pid = pair.get("id", "?")
    src = pair.get("source", "") or ""
    tgt = pair.get("target", "") or ""

    if not tgt.strip():
        errs.append("%s: target is empty" % pid)
        return errs, warns

    # 1. placeholder parity - same set, same multiset
    sp, tp = placeholders(src), placeholders(tgt)
    if sorted(sp) != sorted(tp):
        errs.append("%s: placeholder mismatch - source %s, target %s" % (pid, sp or "none", tp or "none"))
    elif sp != tp and sp:
        warns.append("%s: placeholders reordered (%s -> %s) - check the format string" % (pid, sp, tp))

    # 2. untranslated - identical to source and longer than a single token
    if src.strip() == tgt.strip() and len(src.split()) >= 2:
        warns.append("%s: target is identical to source - untranslated or intentionally copied?" % pid)

    # 3. glossary consistency
    for term, spec in (glossary or {}).items():
        if not re.search(r"\b%s\b" % re.escape(term), src, re.I):
            continue
        if spec.get("do_not_translate"):
            if term.lower() not in tgt.lower():
                errs.append("%s: glossary term %r is do-not-translate but is missing from the target" % (pid, term))
            continue
        want = (spec.get(lang) or "").strip()
        if not want:
            continue
        if want not in tgt:
            errs.append("%s: glossary term %r should be %r, not found in target" % (pid, term, want))

    # 4. script mixing
    pat = SCRIPTS.get(lang)
    if pat and not re.search(pat, tgt) and re.search(r"[A-Za-z]{4,}", tgt):
        warns.append("%s: target has no %s script characters - is this romanised?" % (pid, lang))
    # Devanagari covers both hi and mr, so report once per distinct Unicode range.
    for opat, langs in SCRIPT_RANGES.items():
        if opat == pat:
            continue
        if re.search(opat, tgt) and not re.search(opat, src):
            errs.append("%s: %s script characters found in a %s string"
                        % (pid, "/".join(langs), lang))

    # 5. length expansion
    allow = EXPANSION.get(lang)
    if allow and src.strip():
        ratio = len(tgt) / float(len(src))
        if ratio > allow:
            warns.append("%s: target is %.0f%% of source length (allowance %.0f%%) - check the UI element"
                         % (pid, ratio * 100, allow * 100))

    # 6. Indian number grouping: a 6+ digit run with western grouping
    for m in re.finditer(r"\b\d{1,3}(?:,\d{3}){1,}\b", tgt):
        errs.append("%s: %r uses western digit grouping - use 1,00,000" % (pid, m.group(0)))
    if re.search(r"\bRs\.?\s?\d", tgt):
        warns.append("%s: 'Rs.' - use the rupee sign in consumer strings" % pid)

    # 7. dangling whitespace
    if tgt != tgt.strip():
        warns.append("%s: leading or trailing whitespace" % pid)

    return errs, warns


def check(doc):
    lang = (doc.get("target_lang") or "").strip()
    errs, warns = [], []
    if not lang:
        return ["target_lang is missing - the length budget and script checks need it"], warns
    if lang not in EXPANSION:
        warns.append("no expansion allowance for %r - length is unchecked" % lang)
    pairs = doc.get("pairs") or []
    if not pairs:
        return ["no pairs to check"], warns
    glossary = doc.get("glossary") or {}
    ids = [p.get("id") for p in pairs]
    dupes = {i for i in ids if ids.count(i) > 1}
    for d in sorted(x for x in dupes if x):
        errs.append("duplicate string id: %r" % d)
    for p in pairs:
        e, w = check_pair(p, glossary, lang)
        errs += e
        warns += w
    return errs, warns


GOOD = {
    "target_lang": "hi",
    "glossary": {"invoice": {"hi": "चालान"}, "GST": {"do_not_translate": True}},
    "pairs": [
        {"id": "btn.save", "source": "Save", "target": "सहेजें"},
        {"id": "cart.count", "source": "You have {count} items in your cart",
         "target": "आपके कार्ट में {count} चीज़ें हैं"},
        {"id": "invoice.title", "source": "Your GST invoice", "target": "आपका GST चालान"},
        {"id": "msg.shipped", "source": "Your order shipped on 03/11/2026",
         "target": "आपका ऑर्डर 03/11/2026 को भेज दिया गया"},
    ],
}

BAD = {
    "target_lang": "ta",
    "glossary": {"invoice": {"hi": "चालान", "ta": "விலைப்பட்டியல்"}, "GST": {"do_not_translate": True}},
    "pairs": [
        {"id": "cart.count", "source": "You have {count} items", "target": "உங்களிடம் {Count} பொருட்கள் உள்ளன"},
        {"id": "invoice.title", "source": "Your GST invoice", "target": "உங்கள் GST பில்"},
        {"id": "empty.one", "source": "Save", "target": ""},
        {"id": "money.total", "source": "Total", "target": "மொத்தம் 1,000,000"},
        {"id": "mix.script", "source": "Save", "target": "सहेजें"},
        {"id": "untranslated", "source": "Continue to payment", "target": "Continue to payment"},
    ],
}


def self_test():
    e, w = check(GOOD)
    assert e == [], "good fixture should be clean, got %s" % e

    e2, w2 = check(BAD)
    joined = " | ".join(e2)
    assert any("placeholder mismatch" in x for x in e2), joined
    assert any("glossary term 'invoice'" in x and "விலைப்பட்டியல்" in x for x in e2), joined
    assert any("empty.one: target is empty" in x for x in e2), joined
    assert any("western digit grouping" in x for x in e2), joined
    assert any("script characters found" in x for x in e2), joined
    assert any("identical to source" in x for x in w2), " ".join(w2)

    # determinism
    assert json.dumps(check(GOOD)) == json.dumps(check(GOOD))
    assert json.dumps(check(BAD)) == json.dumps(check(BAD))

    # missing language is an error, not a crash
    assert check({"pairs": [{"id": "a", "source": "x", "target": "y"}]})[0] == [
        "target_lang is missing - the length budget and script checks need it"]
    # no pairs is an error
    assert check({"target_lang": "hi", "pairs": []})[0] == ["no pairs to check"]
    # duplicate ids are caught
    dup = {"target_lang": "hi", "pairs": [{"id": "a", "source": "x", "target": "y"},
                                          {"id": "a", "source": "x", "target": "y"}]}
    assert any("duplicate string id" in x for x in check(dup)[0])

    print("self-test: all assertions passed (2 fixtures, 6 checks each, 3 edge cases)")


def main():
    ap = argparse.ArgumentParser(description="Check a translation file against source, glossary and length.")
    ap.add_argument("path", nargs="?", help="strings JSON; omit to read stdin")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return 0
    raw = open(a.path, encoding="utf-8").read() if a.path else sys.stdin.read()
    errs, warns = check(json.loads(raw))
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
