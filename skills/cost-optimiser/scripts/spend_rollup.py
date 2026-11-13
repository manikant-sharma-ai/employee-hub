#!/usr/bin/env python3
"""Deterministic roll-up for cost-optimiser.

    python3 scripts/spend_rollup.py --csv inventory.csv --fx-usd 88.4 --target 20
    python3 scripts/spend_rollup.py --self-test

Reads a CSV with these columns (extra columns are ignored):

    vendor, product, seats, unit_price, currency, billing_period, seats_active, owner

billing_period is `monthly` or `annual`; unit_price is per seat per period. Prints the annualised
inventory in INR, the total, the duplicate candidates, the unused-seat saving, and a ranked cut list
that reaches the target percentage.

No network, no model call, no invented price. Every number comes from the file you were given.
Exit 0 on success, 1 on a data error, 2 on bad usage.
"""
import csv
import io
import sys

REQUIRED = ["vendor", "product", "seats", "unit_price", "currency", "billing_period",
            "seats_active", "owner"]

# Payment-processor and legal noise that makes the same vendor look like four vendors.
STRIP_PREFIX = ("google*", "google *", "sp *", "sp*", "paypal *", "paypal*", "razorpay*",
                "razorpay *", "stripe*", "stripe *", "amazon web services", "aws emea")
STRIP_SUFFIX = ("pvt ltd", "private limited", "ltd", "limited", "inc", "llc", "gmbh",
                "ireland", "technologies", "technology", "software", "india")


def normalise_vendor(raw):
    """'GOOGLE *GSUITE_Ireland Ltd' -> 'gsuite'. One vendor, one line."""
    s = (raw or "").strip().lower()
    for p in STRIP_PREFIX:
        if s.startswith(p.strip()):
            s = s[len(p.strip()):]
    s = s.replace("_", " ").replace("-", " ")
    for suf in STRIP_SUFFIX:
        if s.endswith(" " + suf) or s == suf:
            s = s[: len(s) - len(suf)].strip()
    out = "".join(ch for ch in s if ch.isalnum() or ch == " ").strip()
    return " ".join(out.split())


def parse_rows(text):
    """CSV text -> list of dicts with numeric fields coerced. Raises ValueError on bad data."""
    reader = csv.DictReader(io.StringIO(text.strip()))
    if reader.fieldnames is None:
        raise ValueError("empty CSV")
    missing = [c for c in REQUIRED if c not in [f.strip() for f in reader.fieldnames]]
    if missing:
        raise ValueError("missing columns: %s" % ", ".join(missing))
    rows = []
    for i, raw in enumerate(reader, start=2):
        row = {k.strip(): (v or "").strip() for k, v in raw.items() if k}
        try:
            seats = int(float(row["seats"]))
            active = int(float(row["seats_active"]))
            price = float(row["unit_price"])
        except (TypeError, ValueError):
            raise ValueError("row %d: seats, unit_price and seats_active must be numbers" % i)
        period = row["billing_period"].lower()
        if period not in ("monthly", "annual"):
            raise ValueError("row %d: billing_period must be monthly or annual" % i)
        if seats < 0 or active < 0 or price < 0:
            raise ValueError("row %d: negative value" % i)
        if active > seats:
            raise ValueError("row %d: seats_active exceeds seats" % i)
        rows.append({"row": i, "vendor": row["vendor"], "vendor_key": normalise_vendor(row["vendor"]),
                     "product": row["product"], "seats": seats, "seats_active": active,
                     "unit_price": price, "currency": row["currency"].upper() or "INR",
                     "billing_period": period, "owner": row["owner"]})
    if not rows:
        raise ValueError("no data rows")
    return rows


def annualise(rows, fx_usd=1.0, fx_other=1.0):
    """Fill annual_inr per row. Foreign currency is converted at the rate supplied, never assumed."""
    for r in rows:
        per_seat_year = r["unit_price"] * (12 if r["billing_period"] == "monthly" else 1)
        if r["currency"] == "INR":
            fx = 1.0
        elif r["currency"] == "USD":
            fx = fx_usd
        else:
            fx = fx_other
        r["per_seat_year_inr"] = round(per_seat_year * fx, 2)
        r["annual_inr"] = round(per_seat_year * fx * r["seats"], 2)
        r["unused_seats"] = r["seats"] - r["seats_active"]
        r["unused_saving_inr"] = round(r["unused_seats"] * per_seat_year * fx, 2)
    return rows


def find_duplicates(rows):
    """Same product sold by the same normalised vendor on more than one line = duplicate billing."""
    seen = {}
    for r in rows:
        key = (r["vendor_key"], r["product"].strip().lower())
        seen.setdefault(key, []).append(r)
    return {k: v for k, v in seen.items() if len(v) > 1}


def summarise(rows, target_pct=0.0):
    total = round(sum(r["annual_inr"] for r in rows), 2)
    unused = round(sum(r["unused_saving_inr"] for r in rows), 2)
    ranked = sorted(rows, key=lambda r: r["unused_saving_inr"], reverse=True)
    target = round(total * target_pct / 100.0, 2)
    picked, running = [], 0.0
    for r in ranked:
        if running >= target or r["unused_saving_inr"] <= 0:
            continue
        picked.append(r)
        running = round(running + r["unused_saving_inr"], 2)
    return {"total_inr": total, "unused_saving_inr": unused, "target_inr": target,
            "cut_list": picked, "cut_total_inr": running,
            "unused_share": round(unused / total * 100, 1) if total else 0.0}


def _selftest():
    checks = 0
    assert normalise_vendor("GOOGLE *GSUITE_Ireland Ltd") == "gsuite"
    assert normalise_vendor("Zoho Corporation Pvt Ltd") == "zoho corporation"
    assert normalise_vendor("  Freshdesk  ") == "freshdesk"
    checks += 3

    sample = """vendor,product,seats,unit_price,currency,billing_period,seats_active,owner
GOOGLE *Workspace,Workspace Business,25,720,INR,monthly,18,ops@
GOOGLE *Workspace,Workspace Business,5,720,INR,monthly,5,founder@
Zoho Corporation Pvt Ltd,Books,3,9000,INR,annual,3,accounts@
Notion Labs Inc,Team,10,12,USD,monthly,4,product@
"""
    rows = parse_rows(sample)
    assert len(rows) == 4
    checks += 1
    rows = annualise(rows, fx_usd=88.0)

    ws = rows[0]
    assert ws["per_seat_year_inr"] == 8640.0, ws["per_seat_year_inr"]
    assert ws["annual_inr"] == 216000.0, ws["annual_inr"]
    assert ws["unused_seats"] == 7 and ws["unused_saving_inr"] == 60480.0
    checks += 3

    zoho = rows[2]
    assert zoho["annual_inr"] == 27000.0, "annual plan must not be multiplied by twelve"
    assert zoho["vendor_key"] == "zoho corporation"
    checks += 2

    notion = rows[3]
    assert notion["per_seat_year_inr"] == 12672.0, notion["per_seat_year_inr"]
    assert notion["annual_inr"] == 126720.0
    checks += 2

    dups = find_duplicates(rows)
    assert list(dups) == [("workspace", "workspace business")], list(dups)
    checks += 1

    s = summarise(rows, target_pct=10)
    assert s["total_inr"] == 412920.0, s["total_inr"]
    assert s["unused_saving_inr"] == 136512.0, s["unused_saving_inr"]
    assert s["cut_list"][0]["owner"] == "product@", "biggest unused saving must rank first"
    assert s["cut_total_inr"] >= s["target_inr"]
    checks += 4

    for bad, why in ((sample.replace("monthly,18", "weekly,18"), "bad period"),
                     (sample.replace("25,720", "25,abc"), "non-numeric price"),
                     (sample.replace(",18,ops@", ",30,ops@"), "active above seats")):
        try:
            parse_rows(bad)
        except ValueError:
            checks += 1
        else:
            raise AssertionError("accepted bad data: %s" % why)

    try:
        parse_rows("vendor,product,seats\nx,y,1\n")
    except ValueError:
        checks += 1
    else:
        raise AssertionError("accepted a CSV missing columns")

    print("self-test: %d checks passed" % checks)
    return 0


def main(argv):
    if "--self-test" in argv:
        return _selftest()
    if "--csv" not in argv:
        print(__doc__)
        return 2

    def arg(flag, default=None):
        if flag in argv and argv.index(flag) + 1 < len(argv):
            return argv[argv.index(flag) + 1]
        return default

    try:
        text = open(arg("--csv"), encoding="utf-8").read()
        rows = annualise(parse_rows(text),
                         fx_usd=float(arg("--fx-usd", "1")),
                         fx_other=float(arg("--fx-other", "1")))
        s = summarise(rows, float(arg("--target", "0")))
    except (OSError, ValueError) as e:
        print("ERROR: %s" % e)
        return 1

    print("lines: %d | annualised total: %.0f INR | unused-seat saving: %.0f INR (%.1f%%)" % (
        len(rows), s["total_inr"], s["unused_saving_inr"], s["unused_share"]))
    print("\nranked by unused-seat saving:")
    for r in sorted(rows, key=lambda r: r["unused_saving_inr"], reverse=True):
        print("  %-22s %-18s seats %2d/%-2d  annual %9.0f  unused %8.0f  %s" % (
            r["vendor_key"][:22], r["product"][:18], r["seats_active"], r["seats"],
            r["annual_inr"], r["unused_saving_inr"], r["owner"]))
    dups = find_duplicates(rows)
    if dups:
        print("\nduplicate candidates (same vendor and product on more than one line):")
        for (v, p), group in dups.items():
            print("  %s / %s - %d lines, owners: %s" % (v, p, len(group),
                                                        ", ".join(sorted({g["owner"] for g in group}))))
    if s["target_inr"]:
        print("\ncut list to reach %.0f INR:" % s["target_inr"])
        for r in s["cut_list"]:
            print("  remove %d seat(s) of %s / %s - saves %.0f INR/yr, owner %s" % (
                r["unused_seats"], r["vendor_key"], r["product"], r["unused_saving_inr"], r["owner"]))
        print("  total from unused seats: %.0f INR against a target of %.0f INR" % (
            s["cut_total_inr"], s["target_inr"]))
        if s["cut_total_inr"] < s["target_inr"]:
            print("  short by %.0f INR - the rest needs a duplicate, a downgrade or a renegotiation"
                  % (s["target_inr"] - s["cut_total_inr"]))
    print("\nwrite the source and the read date beside every figure before it goes in a pack")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
