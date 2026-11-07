#!/usr/bin/env python3
"""Turn a stock sheet into a reorder plan: cover, reorder point, quantity, dead stock.

One arithmetic, stated once, applied to every SKU - so two people get the same
answer and the argument is about the inputs, not the method. No clock, no network,
no randomness.

CSV columns (header required):
  sku, name, on_hand, on_order, avg_daily, lead_days, safety_days, review_days, unit_cost

Definitions used (write them on the sheet, not just in the code):
  position        = on_hand + on_order
  cover_days      = position / avg_daily          (blank if avg_daily is 0)
  reorder_point   = avg_daily * (lead_days + safety_days)
  order_up_to     = avg_daily * (lead_days + safety_days + review_days)
  order_qty       = max(0, ceil(order_up_to - position))   when position <= reorder_point
  days_to_stockout= on_hand / avg_daily
  DEAD            = avg_daily == 0 and on_hand > 0         (value at cost reported)

Usage:
  python3 reorder_plan.py --self-test
  python3 reorder_plan.py stock.csv [--csv]

Exit 0 = plan produced. Exit 1 = the file is unusable.
"""
import csv
import math
import sys

NUMERIC = ("on_hand", "on_order", "avg_daily", "lead_days", "safety_days", "review_days", "unit_cost")


def _num(value, default=0.0):
    if value is None:
        return default
    text = str(value).strip().replace(",", "").replace("₹", "")
    if text in ("", "-", "na", "NA", "n/a"):
        return default
    try:
        return float(text)
    except ValueError:
        return default


def plan_row(row):
    sku = (row.get("sku") or "").strip()
    on_hand = _num(row.get("on_hand"))
    on_order = _num(row.get("on_order"))
    avg_daily = _num(row.get("avg_daily"))
    lead = _num(row.get("lead_days"))
    safety = _num(row.get("safety_days"))
    review = _num(row.get("review_days"))
    cost = _num(row.get("unit_cost"))

    position = on_hand + on_order
    cover = (position / avg_daily) if avg_daily > 0 else None
    stockout = (on_hand / avg_daily) if avg_daily > 0 else None
    rop = avg_daily * (lead + safety)
    up_to = avg_daily * (lead + safety + review)

    if avg_daily == 0 and on_hand > 0:
        action, qty = "DEAD", 0
    elif avg_daily == 0:
        action, qty = "NO SALES", 0
    elif position <= rop:
        action = "ORDER"
        qty = max(0, int(math.ceil(up_to - position)))
    else:
        action, qty = "HOLD", 0

    return {
        "sku": sku,
        "name": (row.get("name") or "").strip(),
        "position": position,
        "cover_days": cover,
        "days_to_stockout": stockout,
        "reorder_point": rop,
        "order_qty": qty,
        "action": action,
        "dead_value": on_hand * cost if action == "DEAD" else 0.0,
        "order_value": qty * cost,
    }


def build(rows):
    plan, problems = [], []
    for i, row in enumerate(rows, start=2):
        sku = (row.get("sku") or "").strip()
        if not sku:
            problems.append("line %d: no SKU - skipped" % i)
            continue
        if _num(row.get("avg_daily")) == 0 and _num(row.get("on_hand")) > 0:
            problems.append("%s: no sales in the period - classified DEAD, confirm before writing off" % sku)
        if _num(row.get("lead_days")) == 0:
            problems.append("%s: lead time is 0 - reorder point assumes next-day supply" % sku)
        plan.append(plan_row(row))
    return plan, problems


def _f(value, digits=1):
    if value is None:
        return "n/a"
    return ("%." + str(digits) + "f") % value


def render(plan, problems, period=""):
    order = {"ORDER": 0, "DEAD": 1, "NO SALES": 2, "HOLD": 3}
    plan = sorted(plan, key=lambda r: (order.get(r["action"], 9), -(r["order_value"] or 0), r["sku"]))
    lines = ["# Reorder plan%s" % (" - " + period if period else ""), ""]
    lines.append("| SKU | Item | Position | Cover (days) | Reorder point | Order qty | Action | Value |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in plan:
        value = r["order_value"] if r["action"] == "ORDER" else r["dead_value"]
        lines.append("| %s | %s | %s | %s | %s | %d | %s | %s |" % (
            r["sku"], r["name"], _f(r["position"], 0), _f(r["cover_days"]),
            _f(r["reorder_point"], 0), r["order_qty"], r["action"],
            ("%.0f" % value) if value else "-"))
    orders = [r for r in plan if r["action"] == "ORDER"]
    dead = [r for r in plan if r["action"] == "DEAD"]
    lines.append("")
    lines.append("Orders to raise: %d, worth %.0f at cost." % (
        len(orders), sum(r["order_value"] for r in orders)))
    lines.append("Dead stock: %d SKUs, %.0f at cost." % (
        len(dead), sum(r["dead_value"] for r in dead)))
    soon = [r for r in plan if r["days_to_stockout"] is not None and r["days_to_stockout"] < 14]
    if soon:
        lines.append("Stocks out inside 14 days on current sales: " + ", ".join(
            "%s (%s days)" % (r["sku"], _f(r["days_to_stockout"], 0)) for r in soon) + ".")
    if problems:
        lines.append("")
        lines.append("Assumptions to confirm:")
        for p in problems:
            lines.append("- " + p)
    return "\n".join(lines)


def _fixture():
    text = (
        "sku,name,on_hand,on_order,avg_daily,lead_days,safety_days,review_days,unit_cost\n"
        "A-100,Cotton kurta,60,0,6,10,7,7,450\n"
        "A-200,Silk stole,900,0,2,21,14,7,1200\n"
        "A-300,Winter shawl,40,0,0,15,10,7,800\n"
        "A-400,Denim jacket,0,200,8,7,5,7,1500\n"
    )
    return list(csv.DictReader(__import__("io").StringIO(text)))


def self_test():
    checks = []

    def check(label, got, want):
        checks.append((label, got == want, got, want))

    plan, problems = build(_fixture())
    by = {r["sku"]: r for r in plan}

    check("all four SKUs planned", len(plan), 4)
    # A-100: position 120, cover 20d, rop = 6*17 = 102, up_to = 6*24 = 144 -> qty 24
    check("A-100 cover days", by["A-100"]["cover_days"], 10.0)
    check("A-100 reorder point", by["A-100"]["reorder_point"], 102.0)
    check("A-100 orders up to the cover target", by["A-100"]["order_qty"], 84)
    check("A-100 action", by["A-100"]["action"], "ORDER")
    # A-200: position 900, cover 450d, rop = 2*35 = 70 -> HOLD
    check("A-200 holds", by["A-200"]["action"], "HOLD")
    check("A-200 cover is long", by["A-200"]["cover_days"], 450.0)
    # A-300: no sales, stock on hand -> DEAD with value
    check("A-300 is dead stock", by["A-300"]["action"], "DEAD")
    check("A-300 dead value at cost", by["A-300"]["dead_value"], 40 * 800.0)
    check("A-300 cover is not a number", by["A-300"]["cover_days"], None)
    # A-400: on_order covers it -> position 200, rop 8*12=96 -> HOLD
    check("A-400 counts stock on order", by["A-400"]["position"], 200.0)
    check("A-400 holds because stock is in transit", by["A-400"]["action"], "HOLD")
    check("dead stock is flagged as an assumption", any("A-300" in p for p in problems), True)

    out = render(plan, problems, period="week 45")
    check("orders sorted before holds", out.index("A-100") < out.index("A-200"), True)
    check("total order value stated", "Orders to raise: 1" in out, True)
    check("dead stock value stated", "Dead stock: 1 SKUs" in out, True)
    check("output reproducible", render(plan, problems, period="week 45") == out, True)
    check("zero sales with no stock is not called dead", plan_row({"sku": "X", "on_hand": "0", "avg_daily": "0"})["action"], "NO SALES")

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
        print("usage: reorder_plan.py <stock.csv> [--csv] | --self-test")
        return 2
    try:
        with open(args[0], encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            missing = [c for c in ("sku", "on_hand", "avg_daily") if c not in (reader.fieldnames or [])]
            if missing:
                print("ERROR: CSV is missing required column(s): %s" % ", ".join(missing))
                return 1
            rows = list(reader)
    except OSError as exc:
        print("ERROR: cannot read %s: %s" % (args[0], exc))
        return 1
    plan, problems = build(rows)
    if not plan:
        print("ERROR: no usable SKU rows in %s" % args[0])
        return 1
    if "--csv" in argv:
        writer = csv.writer(sys.stdout)
        writer.writerow(["sku", "position", "cover_days", "reorder_point", "order_qty", "action"])
        for r in plan:
            writer.writerow([r["sku"], r["position"], r["cover_days"], r["reorder_point"],
                             r["order_qty"], r["action"]])
    else:
        print(render(plan, problems))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
