#!/usr/bin/env python3
"""Deterministic helper for ip-researcher.

    python3 scripts/tm_class_tool.py --check 9,35,42
    python3 scripts/tm_class_tool.py --fee --classes 3 --applicant startup --mode efile \
        --rates '{"individual":4500,"startup":4500,"small":4500,"other":9000}'
    python3 scripts/tm_class_tool.py --self-test

No network, no model call, no invented fee. Rates are never hardcoded: you pass the schedule you
read from the portal today, so a stale figure cannot leak into a client pack.

Exit 0 on success, 1 on a validation error, 2 on bad usage.
"""
import json
import sys

# Nice classification, 1-34 goods and 35-45 services. Headings only - the class heading is the
# minimum an examiner reads, and quoting one from memory is how a brief gets the goods wrong.
NICE = {
    1: "Chemicals used in industry, science, agriculture",
    2: "Paints, varnishes, lacquers, preservatives against rust",
    3: "Bleaching preparations, cleaning preparations, cosmetics, dentifrices",
    4: "Industrial oils and greases, lubricants, fuels, candles, wicks",
    5: "Pharmaceuticals, veterinary preparations, dietetic food, plasters, disinfectants",
    6: "Common metals and alloys, metal building materials, metal containers, hardware of metal",
    7: "Machines, machine tools, motors, agricultural implements",
    8: "Hand tools and implements, cutlery",
    9: "Scientific, electrical and electronic apparatus, recorded and downloadable software",
    10: "Surgical, medical, dental apparatus, artificial limbs, orthopaedic articles",
    11: "Apparatus for lighting, heating, cooking, refrigerating, drying, ventilating, water supply",
    12: "Vehicles, apparatus for locomotion by land, air or water",
    13: "Firearms, ammunition, explosives, fireworks",
    14: "Precious metals and their alloys, jewellery, precious stones, watches",
    15: "Musical instruments",
    16: "Paper, cardboard, printed matter, bookbinding material, stationery, plastic packaging",
    17: "Rubber, gutta-percha, plastics in extruded form, packing, insulating materials",
    18: "Leather and imitations of leather, bags, trunks, umbrellas",
    19: "Building materials of non-metal, rigid pipes, asphalt, monuments of non-metal",
    20: "Furniture, mirrors, picture frames, articles of wood, cork, reed, plastic",
    21: "Household or kitchen utensils, containers, combs, brushes, cleaning instruments",
    22: "Ropes, string, nets, tents, awnings, sails, sacks, padding materials",
    23: "Yarns and threads for textile use",
    24: "Textiles and textile goods, bed covers, table covers",
    25: "Clothing, footwear, headgear",
    26: "Lace and embroidery, ribbons, buttons, pins, needles, artificial flowers",
    27: "Carpets, rugs, mats, linoleum, wall hangings of textile",
    28: "Games, toys, playthings, sporting and gymnastic articles, decorations for trees",
    29: "Meat, fish, poultry, preserved and cooked fruits and vegetables, dairy, edible oils",
    30: "Coffee, tea, cocoa, sugar, rice, flour, bread, pastry, spices, condiments",
    31: "Agricultural, horticultural products, fresh fruits and vegetables, seeds, live animals",
    32: "Beers, mineral and aerated waters, non-alcoholic drinks, fruit drinks, syrups",
    33: "Alcoholic beverages except beers",
    34: "Tobacco, smokers' articles, matches",
    35: "Advertising, business management, retail and wholesale services, office functions",
    36: "Insurance, financial affairs, monetary affairs, real estate affairs",
    37: "Building construction, repair, installation services",
    38: "Telecommunications",
    39: "Transport, packaging and storage of goods, travel arrangement",
    40: "Treatment of materials",
    41: "Education, providing of training, entertainment, sporting and cultural activities",
    42: "Scientific and technological services, software design and development, hosting, SaaS",
    43: "Services for providing food and drink, temporary accommodation",
    44: "Medical services, veterinary services, hygiene and beauty care",
    45: "Legal services, security services, personal and social services",
}

# Pairs an examiner or an opponent will cross-cite even when the goods look different.
RELATED = [
    (9, 42), (35, 42), (35, 41), (25, 35), (29, 30), (29, 43), (30, 43), (5, 44), (3, 44),
    (16, 41), (36, 45), (41, 42), (12, 37), (6, 40), (7, 40), (1, 5), (20, 35), (24, 25),
    (31, 29), (28, 41), (38, 42), (39, 37), (32, 33),
]

APPLICANTS = ("individual", "startup", "small", "other")
MODES = ("efile", "physical")


class UsageError(Exception):
    pass


def parse_classes(raw):
    """'9, 35,42' -> [9, 35, 42]. Raises ValueError on anything not a Nice class."""
    if raw is None or not str(raw).strip():
        raise ValueError("no classes given")
    out = []
    for token in str(raw).replace(" ", "").split(","):
        if not token:
            continue
        if not token.isdigit():
            raise ValueError("not a class number: %r" % token)
        n = int(token)
        if n < 1 or n > 45:
            raise ValueError("class %d is outside 1-45" % n)
        if n not in out:
            out.append(n)
    if not out:
        raise ValueError("no classes given")
    return sorted(out)


def related_pairs(classes):
    s = set(classes)
    return [(a, b) for (a, b) in RELATED if a in s and b in s]


def is_related(a, b):
    return (a, b) in RELATED or (b, a) in RELATED


def fee_total(classes, applicant, mode, rates, professional_per_class=0):
    """Official fee for the classes plus optional professional fee. Rates are supplied, not assumed."""
    if applicant not in APPLICANTS:
        raise ValueError("applicant must be one of %s" % (APPLICANTS,))
    if mode not in MODES:
        raise ValueError("mode must be one of %s" % (MODES,))
    if not isinstance(rates, dict) or applicant not in rates:
        raise ValueError("rates must be a dict containing %r" % applicant)
    official = int(rates[applicant]) * len(classes)
    professional = int(professional_per_class) * len(classes)
    return {"classes": len(classes), "official": official,
            "professional": professional, "total": official + professional}


def _selftest():
    checks = 0

    assert len(NICE) == 45, "Nice table must cover all 45 classes"
    assert sorted(NICE) == list(range(1, 46)), "Nice table must be 1-45 with no gaps"
    checks += 2

    assert parse_classes("9,35,42") == [9, 35, 42]
    assert parse_classes(" 42 , 9 , 9 ") == [9, 42], "duplicates must collapse"
    checks += 2

    for bad in ("0", "46", "abc", "", "9,,x"):
        try:
            parse_classes(bad)
        except ValueError:
            checks += 1
        else:
            raise AssertionError("parse_classes accepted %r" % bad)

    assert is_related(9, 42) and is_related(42, 9), "9/42 is the classic pair"
    assert not is_related(9, 25), "9/25 is not a related pair"
    assert related_pairs([9, 42, 25]) == [(9, 42)], "only the filed pair counts"
    checks += 3

    rates = {"individual": 4500, "startup": 4500, "small": 4500, "other": 9000}
    r = fee_total([3, 5, 30], "other", "efile", rates, professional_per_class=2500)
    assert r["official"] == 27000, r
    assert r["professional"] == 7500, r
    assert r["total"] == 34500, r
    checks += 3

    r2 = fee_total([35], "startup", "efile", rates)
    assert r2["total"] == 4500, r2
    checks += 1

    try:
        fee_total([9], "company", "efile", rates)
    except ValueError:
        checks += 1
    else:
        raise AssertionError("unknown applicant category accepted")

    try:
        fee_total([9], "startup", "efile", {"other": 9000})
    except ValueError:
        checks += 1
    else:
        raise AssertionError("missing rate accepted - a fee must never be guessed")

    print("self-test: %d checks passed" % checks)
    return 0


def main(argv):
    if "--self-test" in argv:
        return _selftest()
    if "--check" in argv:
        raw = argv[argv.index("--check") + 1] if len(argv) > argv.index("--check") + 1 else ""
        try:
            classes = parse_classes(raw)
        except ValueError as e:
            print("ERROR: %s" % e)
            return 1
        print("classes: %s" % ", ".join(str(c) for c in classes))
        for c in classes:
            print("  %2d  %s" % (c, NICE[c]))
        pairs = related_pairs(classes)
        if pairs:
            print("related pairs inside this filing: %s" % ", ".join("%d/%d" % p for p in pairs))
            print("  expect a cross-citation in an opposition on these pairs")
        else:
            print("related pairs inside this filing: none")
        if len(classes) > 4:
            print("note: %d classes is %d official fees - confirm each one covers goods actually sold"
                  % (len(classes), len(classes)))
        return 0
    if "--fee" in argv:
        def arg(flag):
            if flag not in argv:
                raise UsageError("missing %s" % flag)
            i = argv.index(flag)
            if i + 1 >= len(argv):
                raise UsageError("%s needs a value" % flag)
            return argv[i + 1]
        try:
            classes = parse_classes(arg("--classes"))
            rates = json.loads(arg("--rates"))
            r = fee_total(classes, arg("--applicant"), arg("--mode"), rates,
                          int(arg("--professional") or 0) if "--professional" in argv else 0)
        except (UsageError, ValueError) as e:
            print("ERROR: %s" % e)
            return 2
        print("classes: %d | applicant: %s | mode: %s" % (r["classes"], arg("--applicant"), arg("--mode")))
        print("official fee: %d" % r["official"])
        print("professional fee: %d" % r["professional"])
        print("total: %d" % r["total"])
        print("write the portal and the date beside this figure before it goes in a pack")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
