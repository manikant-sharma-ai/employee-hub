#!/usr/bin/env python3
"""Deterministic POC arithmetic for the sales-engineer employee.

Three things that must not be done by feel:
  - the weighted scorecard against criteria agreed before the POC
  - the go / conditional / no-go call from that score
  - what the POC costs us against the gross profit of one won deal

Usage:
    python3 poc_plan.py --self-test
    python3 poc_plan.py --demo
"""
import json
import math
import sys

DEFAULT_THRESHOLDS = {"go": 85.0, "conditional": 70.0}


def score(criteria, thresholds=None):
    """Weighted scorecard.

    criteria: [{"name": str, "weight": number, "target": number,
                "actual": number, "direction": "higher"|"lower"}]
    Returns the weighted score out of 100, per-criterion rows and the decision.
    """
    thresholds = thresholds or DEFAULT_THRESHOLDS
    total_weight = sum(c["weight"] for c in criteria)
    if total_weight <= 0:
        raise ValueError("weights must sum to more than zero")
    rows = []
    weighted = 0.0
    for c in criteria:
        target, actual = float(c["target"]), float(c["actual"])
        direction = c.get("direction", "higher")
        if target == 0:
            ratio = 1.0 if actual == 0 else 0.0
        elif direction == "lower":
            ratio = min(target / actual, 1.0) if actual > 0 else 1.0
        else:
            ratio = min(actual / target, 1.0)
        contribution = c["weight"] * ratio
        weighted += contribution
        rows.append({
            "name": c["name"], "target": target, "actual": actual,
            "direction": direction, "score": round(ratio * 100, 1),
            "weight": c["weight"],
            "weighted": round(contribution / total_weight * 100, 2),
        })
    final = round(weighted / total_weight * 100, 2)
    return {"score": final, "rows": rows,
            "decision": decide(final, thresholds), "thresholds": thresholds}


def decide(final_score, thresholds=None):
    thresholds = thresholds or DEFAULT_THRESHOLDS
    if final_score >= thresholds["go"]:
        return "go"
    if final_score >= thresholds["conditional"]:
        return "conditional"
    return "no-go"


def poc_cost(days, hours_per_day, blended_rate, infra_cost=0.0):
    """What the POC costs us in money."""
    hours = days * hours_per_day
    return {"engineer_days": days, "engineer_hours": hours,
            "engineering_cost": round(hours * blended_rate, 2),
            "infra_cost": round(infra_cost, 2),
            "total": round(hours * blended_rate + infra_cost, 2)}


def payback(deal_value, gross_margin_pct, cost):
    """The POC cost against the gross profit of one won deal."""
    if deal_value <= 0:
        raise ValueError("deal_value must be positive")
    gp = deal_value * gross_margin_pct / 100.0
    if gp <= 0:
        raise ValueError("gross profit must be positive")
    return {"gross_profit_per_deal": round(gp, 2),
            "poc_cost": round(cost, 2),
            "cost_as_pct_of_gp": round(100.0 * cost / gp, 2),
            "deals_to_cover": int(math.ceil(cost / gp)) if cost > 0 else 0,
            "verdict": ("marketing expense" if cost / gp <= 0.25 else
                        "needs approval as a project" if cost / gp <= 0.5 else
                        "too expensive for a POC")}


def _self_test():
    crit = [{"name": "recon", "weight": 3, "target": 200, "actual": 250},
            {"name": "latency", "weight": 1, "target": 800, "actual": 1600,
             "direction": "lower"}]
    s = score(crit)
    assert s["score"] == 87.5, s["score"]
    assert s["decision"] == "go"
    assert s["rows"][0]["score"] == 100.0
    assert s["rows"][1]["score"] == 50.0

    weak = score([{"name": "a", "weight": 1, "target": 100, "actual": 50},
                  {"name": "b", "weight": 1, "target": 100, "actual": 100}])
    assert weak["score"] == 75.0
    assert weak["decision"] == "conditional"

    bad = score([{"name": "a", "weight": 1, "target": 100, "actual": 20},
                 {"name": "b", "weight": 1, "target": 100, "actual": 100}])
    assert bad["score"] == 60.0 and bad["decision"] == "no-go"

    slow = score([{"name": "p95", "weight": 1, "target": 800, "actual": 1000,
                   "direction": "lower"}])
    assert slow["score"] == 80.0

    c = poc_cost(10, 6, 3000, 20000)
    assert c["engineering_cost"] == 180000.0
    assert c["total"] == 200000.0

    p = payback(1200000, 65, 200000)
    assert p["gross_profit_per_deal"] == 780000.0
    assert p["cost_as_pct_of_gp"] == 25.64
    assert p["deals_to_cover"] == 1
    assert p["verdict"] == "needs approval as a project"
    print("self-test: 14 assertions passed")


def _demo():
    crit = [
        {"name": "reconciliation at volume", "weight": 50, "target": 5000, "actual": 5000},
        {"name": "ERP fields mapped", "weight": 25, "target": 40, "actual": 40},
        {"name": "users unassisted", "weight": 15, "target": 2, "actual": 1.4},
        {"name": "p95 latency ms", "weight": 10, "target": 800, "actual": 940,
         "direction": "lower"},
    ]
    s = score(crit)
    print("score %.2f -> %s" % (s["score"], s["decision"]))
    for r in s["rows"]:
        print("  %-28s score %5.1f  weighted %5.2f" % (r["name"], r["score"], r["weighted"]))
    c = poc_cost(12, 6, 3000, 25000)
    print("cost: " + json.dumps(c))
    print("payback: " + json.dumps(payback(1800000, 62, c["total"])))


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        _self_test()
    elif "--demo" in sys.argv:
        _demo()
    else:
        print(__doc__)
