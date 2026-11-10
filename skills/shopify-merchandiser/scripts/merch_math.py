#!/usr/bin/env python3
"""Deterministic merchandising arithmetic for the shopify-merchandiser employee.

Three decisions that must never be done by feel:
  - what a bundle should cost, priced up from the margin floor
  - how much volume a discount needs to hold gross profit
  - what an add-on is actually worth at a given attachment rate

Usage:
    python3 merch_math.py --self-test
    python3 merch_math.py --demo
"""
import json
import math
import sys


def bundle_price(components, margin_floor):
    """Price a bundle up from component cost.

    components: [{"name": str, "cost": number, "price": number}]
    margin_floor: minimum gross margin the bundle may run at, 0..1
    """
    if not 0 <= margin_floor < 1:
        raise ValueError("margin_floor must be in [0, 1)")
    cost = sum(c["cost"] for c in components)
    list_value = sum(c["price"] for c in components)
    if list_value <= 0:
        raise ValueError("component list prices must be positive")
    floor = cost / (1 - margin_floor)
    suggested = math.ceil(floor / 10.0) * 10
    return {
        "component_cost": round(cost, 2),
        "list_value": round(list_value, 2),
        "floor_price": round(floor, 2),
        "max_discount_pct": round((1 - floor / list_value) * 100, 2),
        "suggested_price": float(suggested),
        "gross_margin_pct": round((1 - cost / suggested) * 100, 2),
        "viable": floor <= list_value,
    }


def discount_break_even(price, unit_cost, discount_pct):
    """Units and volume lift needed to hold gross profit at a discount."""
    if price <= 0:
        raise ValueError("price must be positive")
    if not 0 <= discount_pct < 100:
        raise ValueError("discount_pct must be in [0, 100)")
    gp_before = price - unit_cost
    new_price = price * (1 - discount_pct / 100.0)
    gp_after = new_price - unit_cost
    if gp_before <= 0:
        raise ValueError("unit cost already exceeds price")
    if gp_after <= 0:
        return {"new_price": round(new_price, 2), "gp_before": round(gp_before, 2),
                "gp_after": round(gp_after, 2), "multiple": None,
                "lift_pct": None, "sustainable": False}
    multiple = gp_before / gp_after
    return {
        "new_price": round(new_price, 2),
        "gp_before": round(gp_before, 2),
        "gp_after": round(gp_after, 2),
        "multiple": round(multiple, 3),
        "lift_pct": round((multiple - 1) * 100, 2),
        "sustainable": (multiple - 1) <= 1.0,  # needs no more than a doubling
    }


def ladder(price, unit_cost, depths=(10, 20, 30, 40, 50)):
    """The discount ladder for one product, as a list of rows."""
    rows = []
    for d in depths:
        rows.append(dict(discount_pct=d, **discount_break_even(price, unit_cost, d)))
    return rows


def addon_value(orders, attached_orders, addon_price, addon_cost):
    """Gross profit an add-on contributes at its real attachment rate."""
    if orders <= 0:
        raise ValueError("orders must be positive")
    rate = attached_orders / float(orders)
    gp_per_attach = addon_price - addon_cost
    return {
        "attachment_rate_pct": round(rate * 100, 2),
        "gp_per_attached_order": round(gp_per_attach, 2),
        "gp_per_100_orders": round(rate * 100 * gp_per_attach, 2),
    }


def threshold_setting(avg_order_value, delivery_cost, multiplier=1.6):
    """A free-delivery threshold derived from AOV, not from a round number."""
    if avg_order_value <= 0:
        raise ValueError("avg_order_value must be positive")
    threshold = avg_order_value * multiplier
    rounded = math.ceil(threshold / 50.0) * 50
    margin_cost = delivery_cost / (avg_order_value * multiplier) if avg_order_value else None
    return {
        "threshold": float(rounded),
        "aov_multiple": round(rounded / avg_order_value, 2),
        "delivery_cost": delivery_cost,
        "cost_as_pct_of_threshold": round(100.0 * delivery_cost / rounded, 2),
        "note": "delivery is paid on every order below the threshold; count RTO too",
    }


def _self_test():
    b = bundle_price([{"name": "a", "cost": 400, "price": 1000},
                      {"name": "b", "cost": 300, "price": 800}], 0.35)
    assert b["component_cost"] == 700.0
    assert b["floor_price"] == 1076.92
    assert b["suggested_price"] == 1080.0
    assert b["max_discount_pct"] == 40.17
    assert b["viable"] is True
    assert b["gross_margin_pct"] == 35.19

    d = discount_break_even(1000, 400, 20)
    assert d["new_price"] == 800.0 and d["gp_after"] == 400.0
    assert d["multiple"] == 1.5 and d["lift_pct"] == 50.0

    deep = discount_break_even(1000, 400, 40)
    assert deep["sustainable"] is False
    assert deep["lift_pct"] == 200.0

    dead = discount_break_even(1000, 700, 40)
    assert dead["sustainable"] is False and dead["lift_pct"] is None

    a = addon_value(1000, 80, 400, 150)
    assert a["attachment_rate_pct"] == 8.0
    assert a["gp_per_100_orders"] == 2000.0

    t = threshold_setting(1850, 110)
    assert t["threshold"] == 3000.0
    assert t["cost_as_pct_of_threshold"] == 3.67
    print("self-test: 13 assertions passed")


def _demo():
    print("bundle: " + json.dumps(bundle_price(
        [{"name": "kurta", "cost": 420, "price": 1290},
         {"name": "stole", "cost": 300, "price": 890}], 0.35)))
    for row in ladder(1290, 520):
        print("  %2d%% -> price %.0f | gp/unit %.0f | lift needed %s%%"
              % (row["discount_pct"], row["new_price"], row["gp_after"],
                 "impossible" if row["lift_pct"] is None else "%.0f" % row["lift_pct"]))
    print("addon: " + json.dumps(addon_value(4200, 310, 450, 180)))
    print("threshold: " + json.dumps(threshold_setting(1850, 110)))


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        _self_test()
    elif "--demo" in sys.argv:
        _demo()
    else:
        print(__doc__)
