#!/usr/bin/env python3
"""Check a listing sheet against one marketplace's real rules before anything is uploaded.

Marketplaces reject on attributes, not on prose. This checks the rejectable things -
title length, mandatory attributes, image count, price, HSN/GSTIN format and the
claims that get a listing suppressed - and prints a fix list per SKU.

Deterministic: the rules are a table in this file, applied in a fixed order.

CSV columns:
  sku, channel, title, attributes, images, price, hsn, gstin

  channel     one of amazon, flipkart, indiamart, gem
  attributes  semicolon-separated key=value pairs, e.g. "brand=Acme;material=Cotton"

Usage:
  python3 listing_qa.py --self-test
  python3 listing_qa.py listings.csv [--gate]

  --gate exits 1 if any SKU fails, which is what a pre-upload check should do.

Exit 0 = checked (or all pass with --gate). Exit 1 = failures with --gate, or bad input.
"""
import csv
import re
import sys

# Title limits and mandatory attributes per channel. These are the rules that
# reject a listing at upload; category-specific attributes are added by the
# channel's own template and are listed under `references/` in the skill.
CHANNELS = {
    "amazon": {"title_min": 30, "title_max": 200, "min_images": 3,
               "required": ("brand", "material", "size", "colour"), "hsn": True, "gstin": True},
    "flipkart": {"title_min": 20, "title_max": 120, "min_images": 3,
                 "required": ("brand", "model", "colour"), "hsn": True, "gstin": True},
    "indiamart": {"title_min": 15, "title_max": 100, "min_images": 1,
                  "required": ("brand", "material", "moq"), "hsn": False, "gstin": True},
    "gem": {"title_min": 20, "title_max": 150, "min_images": 1,
            "required": ("brand", "model", "warranty"), "hsn": True, "gstin": True},
}

BANNED = ("best seller", "no.1", "number 1", "guaranteed cure", "100% cure", "cheapest in india", "free gift")
GSTIN_RE = re.compile(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9A-Z]Z[0-9A-Z]$")


def parse_attributes(text):
    attrs = {}
    for part in (text or "").split(";"):
        if "=" in part:
            key, _, value = part.partition("=")
            attrs[key.strip().lower()] = value.strip()
    return attrs


def check_row(row):
    channel = (row.get("channel") or "").strip().lower()
    issues = []
    rules = CHANNELS.get(channel)
    if not rules:
        return {"sku": row.get("sku", ""), "channel": channel,
                "status": "FAIL", "issues": ["unknown channel %r - not checked" % channel]}

    title = (row.get("title") or "").strip()
    if len(title) < rules["title_min"]:
        issues.append("title is %d characters, %s needs at least %d" % (len(title), channel, rules["title_min"]))
    if len(title) > rules["title_max"]:
        issues.append("title is %d characters, %s cuts off at %d" % (len(title), channel, rules["title_max"]))
    low = title.lower()
    for word in BANNED:
        if word in low:
            issues.append("title contains a suppressed claim: %r" % word)

    attrs = parse_attributes(row.get("attributes"))
    for key in rules["required"]:
        if not attrs.get(key):
            issues.append("missing mandatory attribute: %s" % key)

    try:
        images = int(float(str(row.get("images") or "0").strip() or 0))
    except ValueError:
        images = 0
        issues.append("image count is not a number")
    if images < rules["min_images"]:
        issues.append("%d image(s), %s requires %d" % (images, channel, rules["min_images"]))

    price_text = str(row.get("price") or "").replace(",", "").replace("₹", "").strip()
    try:
        price = float(price_text)
    except ValueError:
        price = 0.0
    if price <= 0:
        issues.append("price is missing or zero")

    if rules["hsn"]:
        hsn = str(row.get("hsn") or "").strip()
        if not hsn:
            issues.append("HSN missing")
        elif not (hsn.isdigit() and len(hsn) in (4, 6, 8)):
            issues.append("HSN must be 4, 6 or 8 digits, got %r" % hsn)

    if rules["gstin"]:
        gstin = str(row.get("gstin") or "").strip().upper()
        if not GSTIN_RE.match(gstin):
            issues.append("GSTIN does not match the 15-character format")

    return {"sku": (row.get("sku") or "").strip(), "channel": channel,
            "status": "PASS" if not issues else "FAIL", "issues": issues}


def render(results):
    ready = [r for r in results if r["status"] == "PASS"]
    lines = ["# Listing pre-upload check", ""]
    lines.append("%d of %d SKUs are ready to upload." % (len(ready), len(results)))
    lines.append("")
    for r in results:
        lines.append("## %s (%s) - %s" % (r["sku"], r["channel"], r["status"]))
        if r["issues"]:
            for issue in r["issues"]:
                lines.append("- " + issue)
        else:
            lines.append("- title, attributes, images, price and statutory fields all pass")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _fixture():
    text = (
        "sku,channel,title,attributes,images,price,hsn,gstin\n"
        "A-100,amazon,Cotton straight kurta for women block print daily wear,brand=Acme;material=Cotton;size=M;colour=Indigo,5,899,6205,27AABCU9603R1ZM\n"
        "A-200,flipkart,Stole,brand=Acme;colour=Red,1,499,6214,27AABCU9603R1ZM\n"
        "A-300,indiamart,Cotton kurta wholesale lot of 50 pieces,brand=Acme;material=Cotton,2,275,,\n"
        "A-400,amazon,Best seller premium silk saree with zari border,brand=Acme;material=Silk;size=Free;colour=Maroon,4,2499,5007,27AABCU9603R1ZM\n"
    )
    return list(csv.DictReader(__import__("io").StringIO(text)))


def self_test():
    checks = []

    def check(label, got, want):
        checks.append((label, got == want, got, want))

    results = [check_row(r) for r in _fixture()]
    by = {r["sku"]: r for r in results}

    check("all four rows checked", len(results), 4)
    check("A-100 passes amazon", by["A-100"]["status"], "PASS")
    check("A-200 fails: short title", any("title is" in i for i in by["A-200"]["issues"]), True)
    check("A-200 fails: missing model", any("model" in i for i in by["A-200"]["issues"]), True)
    check("A-200 fails: too few images", any("requires 3" in i for i in by["A-200"]["issues"]), True)
    check("A-200 has exactly three issues", len(by["A-200"]["issues"]), 3)
    check("A-300 fails: missing MOQ", any("moq" in i for i in by["A-300"]["issues"]), True)
    check("A-300 does not demand HSN on IndiaMART", any("HSN" in i for i in by["A-300"]["issues"]), False)
    check("A-300 fails: bad GSTIN", any("GSTIN" in i for i in by["A-300"]["issues"]), True)
    check("A-400 fails: suppressed claim", any("best seller" in i for i in by["A-400"]["issues"]), True)
    check("A-400 otherwise complete", len(by["A-400"]["issues"]), 1)
    check("unknown channel is a failure, not a pass", check_row({"sku": "X", "channel": "meesho"})["status"], "FAIL")

    check("GSTIN regex accepts a valid number", bool(GSTIN_RE.match("27AABCU9603R1ZM")), True)
    check("GSTIN regex rejects a 14-character number", bool(GSTIN_RE.match("27AABCU9603R1Z")), False)
    check("attribute parsing lowercases keys", parse_attributes("Brand=Acme;Size=M"), {"brand": "Acme", "size": "M"})

    out = render(results)
    check("summary counts ready SKUs", "1 of 4 SKUs are ready" in out, True)
    check("output reproducible", render(results) == out, True)

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
        print("usage: listing_qa.py <listings.csv> [--gate] | --self-test")
        return 2
    try:
        with open(args[0], encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            missing = [c for c in ("sku", "channel", "title") if c not in (reader.fieldnames or [])]
            if missing:
                print("ERROR: CSV is missing required column(s): %s" % ", ".join(missing))
                return 1
            rows = list(reader)
    except OSError as exc:
        print("ERROR: cannot read %s: %s" % (args[0], exc))
        return 1
    if not rows:
        print("ERROR: no listing rows in %s" % args[0])
        return 1
    results = [check_row(r) for r in rows]
    print(render(results))
    failures = [r for r in results if r["status"] == "FAIL"]
    if "--gate" in argv and failures:
        print("%d SKU(s) failed the pre-upload check." % len(failures))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
