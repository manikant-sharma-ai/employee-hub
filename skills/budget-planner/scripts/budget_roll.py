#!/usr/bin/env python3
"""Deterministic budget arithmetic for the budget-planner employee.

Four things a budget needs and a spreadsheet gets subtly wrong by hand:
a driver-based monthly build, a price/volume variance decomposition, a
full-year reforecast, and the cash tied up in the working-capital cycle.

Usage:
    python3 budget_roll.py --self-test
    python3 budget_roll.py --demo
"""
import json
import sys

MONTHS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep",
          "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]


def monthly(driver):
    """Expand one driver into twelve monthly amounts.

    driver = {"name": str, "kind": "revenue"|"cost", "start_qty": number,
              "growth": monthly compounding rate (default 0),
              "rate": price or cost per unit,
              "seasonality": optional list of 12 multipliers}
    """
    season = driver.get("seasonality") or [1.0] * 12
    if len(season) != 12:
        raise ValueError("seasonality must have 12 values")
    out = []
    for m in range(12):
        qty = driver["start_qty"] * (1 + driver.get("growth", 0.0)) ** m
        out.append(round(qty * driver["rate"] * season[m], 2))
    return out


def rollup(lines):
    """Roll driver lines into revenue, cost and EBITDA by month."""
    rev = [0.0] * 12
    cost = [0.0] * 12
    for line in lines:
        series = monthly(line)
        target = rev if line.get("kind") == "revenue" else cost
        for m, v in enumerate(series):
            target[m] = round(target[m] + v, 2)
    ebitda = [round(rev[m] - cost[m], 2) for m in range(12)]
    return {"revenue": rev, "cost": cost, "ebitda": ebitda,
            "total_revenue": round(sum(rev), 2),
            "total_cost": round(sum(cost), 2),
            "total_ebitda": round(sum(ebitda), 2)}


def variance(plan, actual, kind="revenue"):
    """Absolute, percentage and favourability of a plan-versus-actual gap."""
    gap = round(actual - plan, 2)
    pct = round(gap / plan, 4) if plan else None
    favourable = gap >= 0 if kind == "revenue" else gap <= 0
    return {"plan": plan, "actual": actual, "gap": gap,
            "pct": pct, "kind": kind, "favourable": favourable}


def decompose(plan_price, plan_qty, actual_price, actual_qty):
    """Split a revenue gap into price effect, volume effect and residual."""
    total = actual_price * actual_qty - plan_price * plan_qty
    price_effect = (actual_price - plan_price) * actual_qty
    volume_effect = (actual_qty - plan_qty) * plan_price
    return {"total": round(total, 2),
            "price_effect": round(price_effect, 2),
            "volume_effect": round(volume_effect, 2),
            "residual": round(total - price_effect - volume_effect, 2)}


def reforecast(plan_year, ytd_actual, months_done, uplift=1.0):
    """Full-year landing point: YTD actual plus the remaining plan, re-driven."""
    if not 0 <= months_done <= 12:
        raise ValueError("months_done must be 0..12")
    remaining = sum(plan_year[months_done:]) * uplift
    landing = round(ytd_actual + remaining, 2)
    original = round(sum(plan_year), 2)
    return {"original": original, "landing": landing,
            "gap": round(landing - original, 2),
            "gap_pct": round((landing - original) / original, 4) if original else None,
            "remaining_months": 12 - months_done}


def working_capital(monthly_revenue, monthly_cost,
                    debtor_days, creditor_days, inventory_days):
    """Cash tied up in the trading cycle, in the currency of the inputs."""
    receivables = monthly_revenue * debtor_days / 30.0
    payables = monthly_cost * creditor_days / 30.0
    inventory = monthly_cost * inventory_days / 30.0
    return {"receivables": round(receivables, 2),
            "payables": round(payables, 2),
            "inventory": round(inventory, 2),
            "cash_tied": round(receivables - payables + inventory, 2)}


def _self_test():
    d = {"start_qty": 100, "rate": 50, "growth": 0.1}
    assert monthly(d)[0] == 5000.0
    assert monthly(d)[1] == 5500.0
    season = {"start_qty": 10, "rate": 100,
              "seasonality": [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
    assert monthly(season)[1] == 2000.0

    r = rollup([{"name": "rev", "kind": "revenue", "start_qty": 10, "rate": 100},
                {"name": "cogs", "kind": "cost", "start_qty": 10, "rate": 40}])
    assert r["total_revenue"] == 12000.0 and r["total_cost"] == 4800.0
    assert r["total_ebitda"] == 7200.0

    assert variance(1000, 1100, "revenue")["favourable"] is True
    assert variance(1000, 1100, "revenue")["pct"] == 0.1
    assert variance(1000, 1100, "cost")["favourable"] is False

    dec = decompose(50, 100, 45, 120)
    assert dec["price_effect"] == -600.0
    assert dec["volume_effect"] == 1000.0
    assert dec["total"] == 400.0
    assert dec["residual"] == 0.0

    rf = reforecast([1000] * 12, 3300, 3)
    assert rf["landing"] == 12300.0 and rf["gap"] == 300.0
    assert rf["remaining_months"] == 9

    wc = working_capital(1000000, 700000, 45, 30, 60)
    assert wc["cash_tied"] == 2200000.0
    print("self-test: 12 assertions passed")


def _demo():
    lines = [
        {"name": "D2C revenue", "kind": "revenue", "start_qty": 4200, "rate": 1900,
         "growth": 0.015,
         "seasonality": [0.85, 0.9, 0.95, 1.0, 1.0, 1.05, 1.4, 1.5, 1.6, 0.9, 0.85, 0.8]},
        {"name": "COGS", "kind": "cost", "start_qty": 4200, "rate": 950,
         "growth": 0.015,
         "seasonality": [0.85, 0.9, 0.95, 1.0, 1.0, 1.05, 1.4, 1.5, 1.6, 0.9, 0.85, 0.8]},
        {"name": "Ad spend", "kind": "cost", "start_qty": 1, "rate": 850000,
         "growth": 0.01},
    ]
    r = rollup(lines)
    print("revenue total: %.0f | cost total: %.0f | ebitda: %.0f"
          % (r["total_revenue"], r["total_cost"], r["total_ebitda"]))
    print("lowest ebitda month: %s %.0f"
          % (MONTHS[r["ebitda"].index(min(r["ebitda"]))], min(r["ebitda"])))
    print("variance: " + json.dumps(variance(r["total_revenue"], r["total_revenue"] * 0.94,
                                             "revenue")))
    print("decomposition: " + json.dumps(decompose(1900, 50400, 1840, 53500)))
    print("reforecast: " + json.dumps(reforecast(r["revenue"], sum(r["revenue"][:3]) * 0.95, 3)))
    print("working capital: " + json.dumps(working_capital(r["total_revenue"] / 12,
                                                          r["total_cost"] / 12,
                                                          45, 30, 60)))


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        _self_test()
    elif "--demo" in sys.argv:
        _demo()
    else:
        print(__doc__)
