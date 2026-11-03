#!/usr/bin/env python3
"""Unit economics, price floor and discount arithmetic for one SKU or plan.

Deterministic, stdlib only, no network. The model is arithmetic on stated
inputs - it is not a forecast, and it prints the inputs next to the answer so
someone else can check it.

Input JSON (all money in rupees, per unit unless noted):
{
  "name": "500ml cold-pressed",
  "price_incl_gst": 899,
  "gst_rate_pct": 5,
  "discount_pct": 0,
  "cogs": 310,
  "packaging": 28,
  "freight_out": 65,
  "return_rate_pct": 6,
  "freight_back": 55,
  "payment_fee_pct": 2.0,
  "marketplace_fee_pct": 0,
  "fixed_cost_month": 250000,
  "units_month": 1800
}

Usage:
    python3 margin_model.py model.json
    python3 margin_model.py model.json --json
    python3 margin_model.py --self-test
"""
import argparse
import json
import sys


def _f(doc, key, default=0.0):
    v = doc.get(key, default)
    if v is None:
        return float(default)
    if isinstance(v, str):
        v = v.replace(",", "").replace("₹", "").strip() or 0
    return float(v)


def model(doc):
    price = _f(doc, "price_incl_gst")
    gst_pct = _f(doc, "gst_rate_pct")
    disc_pct = _f(doc, "discount_pct")
    cogs = _f(doc, "cogs")
    pack = _f(doc, "packaging")
    fwd = _f(doc, "freight_out")
    ret_pct = _f(doc, "return_rate_pct")
    back = _f(doc, "freight_back")
    pay_pct = _f(doc, "payment_fee_pct")
    mp_pct = _f(doc, "marketplace_fee_pct")
    fixed = _f(doc, "fixed_cost_month")
    units = _f(doc, "units_month")

    if price <= 0:
        raise ValueError("price_incl_gst must be greater than zero")

    gross = price
    discount = gross * disc_pct / 100.0
    net_incl = gross - discount
    gst = net_incl - net_incl / (1 + gst_pct / 100.0) if gst_pct else 0.0
    net_rev = net_incl - gst

    pay_fee = net_incl * pay_pct / 100.0
    mp_fee = net_incl * mp_pct / 100.0
    # A returned unit still costs the forward leg, the return leg and the
    # packaging, and loses the sale - so the allowance is per unit sold.
    ret_cost = (ret_pct / 100.0) * (cogs + pack + fwd + back)
    variable = cogs + pack + fwd + pay_fee + mp_fee + ret_cost
    contribution = net_rev - variable
    cm_pct = (contribution / net_rev * 100.0) if net_rev else 0.0

    breakeven_units = (fixed / contribution) if contribution > 0 else None
    breakeven_revenue = (breakeven_units * net_rev) if breakeven_units else None

    # Price floor: solve net_rev(p) - variable(p) = 0 where the variable parts
    # that scale with price are the percentage fees. Costs that do not scale
    # with price stay as they are.
    fixed_var = cogs + pack + fwd + ret_cost
    pct_var = (pay_pct + mp_pct) / 100.0
    # net_incl * (1 - pct_var) - gst_component - fixed_var = 0
    # with net_rev = net_incl / (1 + gst) and fees on net_incl:
    # net_incl * (1/(1+g) - pct_var) = fixed_var
    denom = (1.0 / (1 + gst_pct / 100.0)) - pct_var
    floor_incl = (fixed_var / denom) if denom > 0 else None

    uplift = (1.0 / (1 - disc_pct / 100.0) - 1) * 100.0 if disc_pct < 100 else None
    price_up_5 = None
    if contribution > 0:
        p2 = price * 1.05
        d2 = p2 * disc_pct / 100.0
        n2 = p2 - d2
        g2 = n2 - n2 / (1 + gst_pct / 100.0) if gst_pct else 0.0
        rev2 = n2 - g2
        var2 = cogs + pack + fwd + n2 * (pay_pct + mp_pct) / 100.0 + ret_cost
        price_up_5 = {
            "new_price_incl_gst": round(p2, 2),
            "new_contribution": round(rev2 - var2, 2),
            "contribution_change_pct": round(((rev2 - var2) - contribution) / contribution * 100.0, 1),
        }

    # What the discount itself costs, against the same model at full price.
    lost = 0.0
    if disc_pct:
        base = model(dict(doc, discount_pct=0))
        lost = base["per_unit"]["contribution"] - contribution

    monthly_contribution = contribution * units - fixed
    return {
        "name": doc.get("name", "unnamed"),
        "inputs": {
            "price_incl_gst": price, "gst_rate_pct": gst_pct, "discount_pct": disc_pct,
            "cogs": cogs, "packaging": pack, "freight_out": fwd,
            "return_rate_pct": ret_pct, "freight_back": back,
            "payment_fee_pct": pay_pct, "marketplace_fee_pct": mp_pct,
            "fixed_cost_month": fixed, "units_month": units,
        },
        "per_unit": {
            "gross_price": round(gross, 2),
            "discount": round(discount, 2),
            "net_price_incl_gst": round(net_incl, 2),
            "gst_component": round(gst, 2),
            "net_revenue_ex_gst": round(net_rev, 2),
            "payment_fee": round(pay_fee, 2),
            "marketplace_fee": round(mp_fee, 2),
            "returns_allowance": round(ret_cost, 2),
            "variable_cost": round(variable, 2),
            "contribution": round(contribution, 2),
            "contribution_margin_pct": round(cm_pct, 1),
        },
        "breakeven": {
            "units_per_month": round(breakeven_units, 0) if breakeven_units else None,
            "revenue_ex_gst": round(breakeven_revenue, 2) if breakeven_revenue else None,
            "price_floor_incl_gst": round(floor_incl, 2) if floor_incl else None,
            "headroom_over_floor": round(price - floor_incl, 2) if floor_incl else None,
        },
        "discount_effect": {
            "volume_uplift_needed_pct": round(uplift, 1) if uplift is not None else None,
            "contribution_lost": round(lost, 2),
        },
        "price_up_5pct": price_up_5,
        "month": {
            "contribution_at_volume": round(contribution * units, 2),
            "profit_after_fixed": round(monthly_contribution, 2),
            "verdict": "profitable" if monthly_contribution > 0 else "losing money",
        },
    }


GOOD = {"name": "500ml", "price_incl_gst": 899, "gst_rate_pct": 5, "discount_pct": 0,
        "cogs": 310, "packaging": 28, "freight_out": 65, "return_rate_pct": 6,
        "freight_back": 55, "payment_fee_pct": 2.0, "marketplace_fee_pct": 0,
        "fixed_cost_month": 250000, "units_month": 1800}

DISC = dict(GOOD, discount_pct=10)

MP = dict(GOOD, marketplace_fee_pct=18, discount_pct=0)


def self_test():
    r = model(GOOD)
    pu = r["per_unit"]
    # net_rev = 899 / 1.05 = 856.19
    assert abs(pu["net_revenue_ex_gst"] - 856.19) < 0.01, pu
    assert abs(pu["gst_component"] - 42.81) < 0.01, pu
    # returns allowance = 6% * (310+28+65+55) = 27.48
    assert abs(pu["returns_allowance"] - 27.48) < 0.01, pu
    # payment fee = 2% of 899 = 17.98
    assert abs(pu["payment_fee"] - 17.98) < 0.01, pu
    # variable = 310+28+65+17.98+0+27.48 = 448.46
    assert abs(pu["variable_cost"] - 448.46) < 0.01, pu
    # contribution = 856.19 - 448.46 = 407.73
    assert abs(pu["contribution"] - 407.73) < 0.01, pu
    assert abs(pu["contribution_margin_pct"] - 47.6) < 0.1, pu

    be = r["breakeven"]
    assert abs(be["units_per_month"] - 613) < 1, be       # 250000 / 407.73
    assert be["price_floor_incl_gst"] is not None, be
    assert be["price_floor_incl_gst"] < 899, be
    assert abs(be["headroom_over_floor"] - (899 - be["price_floor_incl_gst"])) < 0.01

    # A 10% discount costs more than a tenth of contribution.
    d = model(DISC)["per_unit"]
    assert d["contribution"] < pu["contribution"] * 0.9, d
    assert abs(model(DISC)["discount_effect"]["volume_uplift_needed_pct"] - 11.1) < 0.1
    assert model(DISC)["discount_effect"]["contribution_lost"] > 0, "a discount must cost contribution"
    assert model(GOOD)["discount_effect"]["contribution_lost"] == 0, "no discount, nothing lost"

    # Marketplace fees can push an order below the floor.
    m = model(MP)
    assert m["per_unit"]["contribution"] < pu["contribution"], m["per_unit"]

    # A price above the floor must have positive contribution; below it, negative.
    floor = be["price_floor_incl_gst"]
    assert model(dict(GOOD, price_incl_gst=floor))["per_unit"]["contribution"] > -1
    assert model(dict(GOOD, price_incl_gst=floor * 0.8))["per_unit"]["contribution"] < 0

    # Determinism.
    assert json.dumps(model(GOOD)) == json.dumps(model(GOOD))

    # Guardrails.
    try:
        model(dict(GOOD, price_incl_gst=0))
        assert False, "zero price should raise"
    except ValueError:
        pass

    # String money with commas and a rupee sign is accepted.
    assert model(dict(GOOD, cogs="₹310"))["per_unit"]["contribution"] == pu["contribution"]

    print("self-test: all assertions passed (unit economics, floor, discount uplift, marketplace, guards)")


def emit(r, as_json=False):
    if as_json:
        print(json.dumps(r, indent=2))
        return
    pu, be, mo = r["per_unit"], r["breakeven"], r["month"]
    print("model: %s" % r["name"])
    print("  gross price            %10.2f" % pu["gross_price"])
    print("  discount               %10.2f" % pu["discount"])
    print("  GST component          %10.2f" % pu["gst_component"])
    print("  net revenue (ex-GST)   %10.2f" % pu["net_revenue_ex_gst"])
    print("  variable cost          %10.2f" % pu["variable_cost"])
    print("    of which returns     %10.2f" % pu["returns_allowance"])
    print("  contribution           %10.2f  (%.1f%%)" % (pu["contribution"], pu["contribution_margin_pct"]))
    print("  price floor (incl GST) %s" % ("%.2f" % be["price_floor_incl_gst"] if be["price_floor_incl_gst"] else "n/a - contribution is negative at any price"))
    print("  break-even units/month %s" % (be["units_per_month"] if be["units_per_month"] else "n/a"))
    if r["discount_effect"]["contribution_lost"]:
        print("  contribution lost to the discount: %.2f" % r["discount_effect"]["contribution_lost"])
    if r["discount_effect"]["volume_uplift_needed_pct"] is not None:
        print("  volume needed to hold contribution after discount: +%.1f%%"
              % r["discount_effect"]["volume_uplift_needed_pct"])
    print("  month at %d units: contribution %.2f, after fixed cost %.2f (%s)"
          % (r["inputs"]["units_month"], mo["contribution_at_volume"],
             mo["profit_after_fixed"], mo["verdict"]))


def main():
    ap = argparse.ArgumentParser(description="Unit economics and price floor for one SKU or plan.")
    ap.add_argument("path", nargs="?", help="model JSON; omit to read stdin")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return 0
    raw = open(a.path, encoding="utf-8").read() if a.path else sys.stdin.read()
    emit(model(json.loads(raw)), a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
