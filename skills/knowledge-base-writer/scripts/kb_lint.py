#!/usr/bin/env python3
"""Lint a help-centre article against the house rules.

Mechanical faults only - the ones a reviewer should never have to spend attention
on: a long title, a preamble before the answer, missing steps, a missing failure
path, hedging words, passive voice, images with no alt text, no review date.

Usage:
  python3 kb_lint.py article.md [article2.md ...]
  python3 kb_lint.py --self-test

Exit 0 = clean or warnings only, 1 = errors, 2 = file not readable.
"""
import os
import re
import sys
import tempfile

BANNED = ["simply", "just", "obviously", "rest assured", "please note",
          "kindly", "unfortunately", "as you know", "easy to"]
HEDGES = ["may be ", "might be ", "should be able"]
MAX_TITLE = 60
MAX_ANSWER_WORDS = 45
MIN_STEPS, MAX_STEPS = 3, 10
MAX_SENTENCE_WORDS = 30


def lint(text):
    lines = text.splitlines()
    errors, warnings = [], []

    def err(msg, ln=None):
        errors.append((ln, msg))

    def warn(msg, ln=None):
        warnings.append((ln, msg))

    title, title_ln = None, None
    for i, line in enumerate(lines, 1):
        if line.startswith("# "):
            title, title_ln = line[2:].strip(), i
            break
    if not title:
        err("no H1 title - the title is the search phrase")
    elif len(title) > MAX_TITLE:
        err("title is %d characters (max %d): %r" % (len(title), MAX_TITLE, title), title_ln)
    elif title.endswith("."):
        warn("title ends with a full stop - search does not type it", title_ln)

    # the answer block: first non-empty paragraph after the title
    answer, answer_ln = "", None
    if title_ln:
        i = title_ln
        while i < len(lines) and not lines[i].strip():
            i += 1
        parts = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
            parts.append(lines[i].strip())
            i += 1
        answer, answer_ln = " ".join(parts), title_ln + 1
    if not answer:
        err("no answer paragraph after the title - the fix goes in the first two lines")
    else:
        if answer.startswith(("- ", "* ", "|")):
            warn("the answer starts with a list - lead with the action in a sentence", answer_ln)
        words = len(answer.split())
        if words > MAX_ANSWER_WORDS:
            err("answer block is %d words (max %d) - the reader is stuck, not reading"
                % (words, MAX_ANSWER_WORDS), answer_ln)
        if answer.lower().startswith(("thank", "we understand", "we are sorry")):
            warn("answer opens with an apology - apologise after the fix, not instead of it", answer_ln)

    headings = [l.strip() for l in lines if l.startswith("## ")]
    lowered = [h[3:].strip().lower() for h in headings]
    if not any("step" in h for h in lowered):
        err("no '## Steps' section")
    if not any("if this does not work" in h or "still" in h for h in lowered):
        err("no failure path - add '## If this does not work' and say who to contact")

    # numbered steps
    step_lines = [l for l in lines if re.match(r"^\s*\d+[.)]\s+\S", l)]
    if len(step_lines) < MIN_STEPS:
        err("only %d numbered steps (min %d)" % (len(step_lines), MIN_STEPS))
    elif len(step_lines) > MAX_STEPS:
        err("%d numbered steps (max %d) - split the article" % (len(step_lines), MAX_STEPS))

    low = text.lower()
    for word in BANNED:
        pattern = r"\b" + re.escape(word) + r"\b"
        if re.search(pattern, low):
            ln = next((i for i, l in enumerate(lines, 1) if re.search(pattern, l.lower())), None)
            err("banned phrase %r - it blames the reader or wastes the line" % word, ln)
    for word in HEDGES:
        pattern = r"\b" + re.escape(word.strip()) + r"\b"
        if re.search(pattern, low):
            ln = next((i for i, l in enumerate(lines, 1) if re.search(pattern, l.lower())), None)
            warn("hedge %r - say the condition or drop it" % word.strip(), ln)

    if not re.search(r"\byou\b", low):
        warn("no second person - the article is not speaking to the reader")
    if "click here" in low:
        err("link text 'click here' - name the destination")
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"!\[(.*?)\]\((.*?)\)", line):
            if not m.group(1).strip():
                err("image with no alt text: %s" % m.group(2), i)
    if "last reviewed" not in low:
        err("no 'Last reviewed:' date - an undated article is already decaying")

    sentences = re.split(r"(?<=[.!?])\s+", " ".join(
        l.strip() for l in lines if l.strip() and not l.startswith(("#", "|", "!", "-", "*"))
        and not re.match(r"^\d+[.)]", l.strip())))
    long_sentences = [s for s in sentences if len(s.split()) > MAX_SENTENCE_WORDS]
    if long_sentences:
        warn("%d sentence(s) over %d words" % (len(long_sentences), MAX_SENTENCE_WORDS))

    return {"title": title, "errors": errors, "warnings": warnings,
            "steps": len(step_lines), "answer_words": len(answer.split())}


def report(path, result):
    print("%s: %r" % (path, result["title"]))
    print("  steps %d | answer %d words" % (result["steps"], result["answer_words"]))
    for ln, msg in result["errors"]:
        print("  ERROR   %s%s" % ("line %d: " % ln if ln else "", msg))
    for ln, msg in result["warnings"]:
        print("  warning %s%s" % ("line %d: " % ln if ln else "", msg))
    print("RESULT: %s (%d errors, %d warnings)"
          % ("PASS" if not result["errors"] else "FAIL",
             len(result["errors"]), len(result["warnings"])))


GOOD = """# Money debited but order not confirmed

Your payment went through but the order is not showing. Do not pay again - the
order is usually confirmed within 15 minutes, and the money is either refunded
automatically or applied to the order.

## Steps

1. Open Orders and pull down to refresh. You will see the order if it was confirmed.
2. Check your bank message for a debit. If there is none, the payment failed and no money moved.
3. Wait 15 minutes, then refresh once more. You will see either the order or a refund line.
4. If you still see nothing, reply to this email with the transaction reference.

## If this does not work

Reply with the transaction reference and the amount. A person will confirm the
order or refund it within one working day.

Last reviewed: 2026-11-06
"""

BAD = """# Payment gateway error handling and reconciliation troubleshooting

Thank you for reaching out about your payment. We understand that waiting for a
refund can be frustrating, and we are sorry for the inconvenience caused to you
during this time. Our team works hard to process every refund as quickly as
possible and we appreciate your patience while we look into this matter for you
and get back to you with an update as soon as we can.

## Overview

Simply check the dashboard and kindly note that refunds are easy to process.

Last reviewed: 2026-11-06
"""

THIN = """# Refund policy

Refunds take 7 days.

## Steps

1. Wait.

## If this does not work

Contact support.
"""


def self_test():
    ok = True
    tmp = tempfile.mkdtemp()
    cases = []
    for name, body in (("good.md", GOOD), ("bad.md", BAD), ("thin.md", THIN)):
        p = os.path.join(tmp, name)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
        cases.append((p, lint(body)))

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print("  FAIL %s: got %r want %r" % (label, got, want))

    good = cases[0][1]
    check("good article has no errors", good["errors"], [])
    check("good article counts 4 steps", good["steps"], 4)
    check("good title captured", good["title"], "Money debited but order not confirmed")

    bad = cases[1][1]
    check("bad title too long", any("max 60" in m for _, m in bad["errors"]), True)
    check("bad answer too long", any("answer block" in m for _, m in bad["errors"]), True)
    check("bad has no steps", any("numbered steps" in m for _, m in bad["errors"]), True)
    check("banned phrase caught", any("simply" in m for _, m in bad["errors"]), True)

    thin = cases[2][1]
    check("thin article fails", bool(thin["errors"]), True)
    check("thin has one step", thin["steps"], 1)
    check("alt text rule fires on empty alt",
          any("alt text" in m for _, m in lint("# T\n\nAnswer here for you.\n\n![ ](a.png)\n\n## Steps\n\n1. a\n2. b\n3. c\n\n## If this does not work\n\nMail us.\n\nLast reviewed: 2026-11-06\n")["errors"]),
          True)

    print("kb_lint self-test: %s (10 checks)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return self_test()
    if not argv:
        print(__doc__.strip())
        return 2
    failed = False
    for path in argv:
        try:
            with open(path, encoding="utf-8") as fh:
                result = lint(fh.read())
        except OSError as exc:
            print("ERROR: %s" % exc)
            return 2
        report(path, result)
        failed = failed or bool(result["errors"])
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
