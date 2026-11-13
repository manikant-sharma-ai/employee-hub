#!/usr/bin/env python3
"""Deterministic lead scoring for lead-qualifier.

    python3 scripts/score_lead.py --lead lead.json --icp icp.json
    python3 scripts/score_lead.py --json '{"company":"Acme","industry":"retail",...}' --icp icp.json
    python3 scripts/score_lead.py --self-test

One rubric, one arithmetic, every lead. The script never guesses a field: anything missing is scored
zero and reported as missing, and a missing factor that could change the band downgrades the lead to
band D (one question) instead of a C (decline).

Lead fields (all optional, unknown is a valid state):
    company, industry, employees, city, state, role, enquiry, budget_signal,
    timeline_days, is_competitor, is_student, is_existing_customer, is_agency

ICP fields:
    industries, adjacent_industries, size_min, size_max, cities, states,
    decision_roles, influencer_roles

Exit 0 on success, 1 on a data error, 2 on bad usage.
"""
import json
import sys

WEIGHTS = {"industry": 20, "size": 20, "geography": 15, "problem": 15,
           "authority": 10, "budget": 10, "timing": 10}

BANDS = ((75, "A"), (50, "B"), (0, "C"))

TIMELINE_WORDS = ("urgent", "asap", "this month", "immediately", "next week", "before")
IMPACT_WORDS = ("lose", "cost", "waste", "delay", "manual", "hours", "per month", "every day")


def band_for(score):
    for floor, name in BANDS:
        if score >= floor:
            return name
    return "C"


def _text(lead, key):
    v = lead.get(key)
    return v.strip() if isinstance(v, str) else v


def _num(lead, key):
    v = lead.get(key)
    if v in (None, ""):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        raise ValueError("%s must be a number, got %r" % (key, v))


def disqualify(lead):
    """Checked before any scoring. Returns (code, line) or None."""
    if lead.get("is_competitor"):
        return ("NOT-BUYER", "a competitor enquiring about the product")
    if lead.get("is_student"):
        return ("NOT-BUYER", "a student or researcher, not a buyer")
    if lead.get("is_agency"):
        return ("NOT-BUYER", "an agency or reseller, not an end customer")
    if lead.get("is_existing_customer"):
        return ("ALREADY-SERVED", "an existing customer - route to customer success")
    return None


def score_factors(lead, icp):
    """Returns dict factor -> (fraction or None, evidence). None means unknown."""
    out = {}

    industry = (_text(lead, "industry") or "").lower()
    industries = [i.lower() for i in icp.get("industries", [])]
    adjacent = [i.lower() for i in icp.get("adjacent_industries", [])]
    if not industry:
        out["industry"] = (None, "industry not given")
    elif industry in industries:
        out["industry"] = (1.0, "industry %r is in the ICP list" % industry)
    elif industry in adjacent:
        out["industry"] = (0.5, "industry %r is adjacent to the ICP list" % industry)
    else:
        out["industry"] = (0.0, "industry %r is outside the ICP list" % industry)

    employees = _num(lead, "employees")
    lo, hi = icp.get("size_min"), icp.get("size_max")
    if employees is None:
        out["size"] = (None, "employee count not given")
    elif lo is None or hi is None:
        out["size"] = (None, "ICP has no size band - fix the ICP before scoring")
    elif lo <= employees <= hi:
        out["size"] = (1.0, "%d employees is inside the %d-%d band" % (employees, lo, hi))
    elif lo / 2 <= employees <= hi * 2:
        out["size"] = (0.5, "%d employees is one band away from %d-%d" % (employees, lo, hi))
    else:
        out["size"] = (0.0, "%d employees is outside the %d-%d band" % (employees, lo, hi))

    city = (_text(lead, "city") or "").lower()
    state = (_text(lead, "state") or "").lower()
    cities = [c.lower() for c in icp.get("cities", [])]
    states = [s.lower() for s in icp.get("states", [])]
    if not city and not state:
        out["geography"] = (None, "city and state not given")
    elif city and city in cities:
        out["geography"] = (1.0, "%s is in the service area" % city)
    elif state and state in states:
        out["geography"] = (0.5, "%s is serviceable at distance" % state)
    else:
        out["geography"] = (0.0, "no service coverage for %s" % (city or state))

    enquiry = (_text(lead, "enquiry") or "")
    words = enquiry.split()
    if not enquiry:
        out["problem"] = (None, "no enquiry text - unqualifiable as it stands")
    else:
        detail = len(words) >= 25
        impact = any(w in enquiry.lower() for w in IMPACT_WORDS)
        urgency = any(w in enquiry.lower() for w in TIMELINE_WORDS)
        hits = sum((detail, impact, urgency))
        frac = {3: 1.0, 2: 0.5, 1: 0.0, 0: 0.0}[hits]
        out["problem"] = (frac, "%d words, impact %s, timing %s" % (
            len(words), "stated" if impact else "not stated", "stated" if urgency else "not stated"))

    role = (_text(lead, "role") or "").lower()
    decision = [r.lower() for r in icp.get("decision_roles", [])]
    influence = [r.lower() for r in icp.get("influencer_roles", [])]
    if not role:
        out["authority"] = (None, "role not given")
    elif role in decision:
        out["authority"] = (1.0, "%r is a decision role" % role)
    elif role in influence:
        out["authority"] = (0.5, "%r is an influencer role" % role)
    else:
        out["authority"] = (0.0, "%r has no path to the decision" % role)

    budget = (_text(lead, "budget_signal") or "").lower()
    if budget in ("stated", "spending"):
        out["budget"] = (1.0, "budget %s" % budget)
    elif budget == "implied":
        out["budget"] = (0.5, "budget only implied")
    elif budget == "none":
        out["budget"] = (0.0, "no budget stated or available")
    else:
        out["budget"] = (None, "budget signal not given")

    days = _num(lead, "timeline_days")
    if days is None:
        out["timing"] = (None, "timeline not given")
    elif days <= 30:
        out["timing"] = (1.0, "needs it in %d days" % days)
    elif days <= 90:
        out["timing"] = (0.5, "needs it in %d days, inside the quarter" % days)
    else:
        out["timing"] = (0.0, "needs it in %d days - a B at best" % days)

    return out


def evaluate(lead, icp):
    dq = disqualify(lead)
    if dq:
        return {"band": "DQ", "code": dq[0], "score": 0,
                "reasons_for": [], "reasons_against": [dq[1]],
                "missing": [], "questions": [], "factors": {}}

    factors = score_factors(lead, icp)
    score = sum(WEIGHTS[k] * (v[0] or 0.0) for k, v in factors.items())
    score = int(round(score))
    band = band_for(score)

    missing = [k for k, v in factors.items() if v[0] is None]
    unknown_weight = sum(WEIGHTS[k] for k in missing)
    # A score built mostly on unknowns is not a decision. Ask before banding.
    if unknown_weight >= 40:
        band = "D"
    # One unknown factor that could lift the lead a band makes it a D, not a C.
    elif band in ("B", "C"):
        for k in missing:
            lifted = score + WEIGHTS[k]
            if band_for(int(round(lifted))) != band:
                band = "D"
                break

    ordered = sorted(factors.items(), key=lambda kv: WEIGHTS[kv[0]] * (kv[1][0] or 0), reverse=True)
    reasons_for = ["%s: %s" % (k, v[1]) for k, v in ordered if v[0]]
    reasons_against = ["%s: %s" % (k, v[1]) for k, v in ordered
                       if v[0] is not None and v[0] < 1.0]
    return {"band": band, "code": None, "score": score, "reasons_for": reasons_for,
            "reasons_against": reasons_against, "missing": missing,
            "questions": questions_for(missing), "factors": factors}


QUESTIONS = {
    "size": "How many people are in the business, and who would use this day to day?",
    "industry": "What exactly does the business sell, and to whom?",
    "geography": "Where would the work be delivered from, and in which locations?",
    "problem": "What are you using today, and what made you look at this now?",
    "authority": "Who else is involved in the decision, and what is your timeline?",
    "budget": "Is there a budget set aside for this, or would it need one?",
    "timing": "When would you want this live, and what happens if it slips?",
}


def questions_for(missing):
    return [QUESTIONS[m] for m in missing][:3]


def _selftest():
    checks = 0
    icp = {"industries": ["retail", "d2c"], "adjacent_industries": ["wholesale"],
           "size_min": 11, "size_max": 200, "cities": ["pune", "mumbai"],
           "states": ["maharashtra"], "decision_roles": ["founder", "ceo", "head of ops"],
           "influencer_roles": ["manager", "analyst"]}
    assert sum(WEIGHTS.values()) == 100
    checks += 1

    good = {"company": "Acme", "industry": "retail", "employees": 40, "city": "Pune",
            "state": "maharashtra", "role": "founder", "budget_signal": "stated",
            "timeline_days": 20,
            "enquiry": "We run four stores and reconcile stock by hand every night, which costs us "
                       "about six hours a week and delays the morning report. We want this live "
                       "before Diwali."}
    r = evaluate(good, icp)
    assert r["band"] == "A", r
    assert r["score"] == 100, r["score"]
    assert not r["missing"]
    checks += 3

    thin = {"company": "Beta", "enquiry": "Please share pricing."}
    r = evaluate(thin, icp)
    assert r["band"] == "D", r["band"]
    assert set(r["missing"]) == {"industry", "size", "geography", "authority", "budget", "timing"}
    assert len(r["questions"]) == 3
    checks += 3

    bad_fit = {"company": "Gamma", "industry": "mining", "employees": 5, "city": "Chennai",
               "role": "student", "budget_signal": "none", "timeline_days": 400,
               "enquiry": "Just looking."}
    r = evaluate(bad_fit, icp)
    assert r["band"] == "C", r["band"]
    assert r["score"] == 0, r["score"]
    checks += 2

    competitor = {"company": "Rival", "industry": "retail", "is_competitor": True}
    r = evaluate(competitor, icp)
    assert r["band"] == "DQ" and r["code"] == "NOT-BUYER", r
    checks += 1

    existing = dict(good, is_existing_customer=True)
    r = evaluate(existing, icp)
    assert r["band"] == "DQ" and r["code"] == "ALREADY-SERVED", r
    checks += 1

    # One unknown factor that could lift a B to an A must produce a D, not a B.
    near = dict(good, employees=5, role="manager", budget_signal=None)
    r = evaluate(near, icp)
    assert r["score"] == 65 and r["band"] == "D", (r["score"], r["band"])
    checks += 2

    # A B that no single unknown can lift stays a B.
    mid = dict(good, employees=5, role="manager", budget_signal="implied", timeline_days=60)
    r = evaluate(mid, icp)
    assert r["score"] == 65 and r["band"] == "B", (r["score"], r["band"])
    checks += 2

    try:
        evaluate({"employees": "many"}, icp)
    except ValueError:
        checks += 1
    else:
        raise AssertionError("accepted a non-numeric employee count")

    print("self-test: %d checks passed" % checks)
    return 0


def main(argv):
    if "--self-test" in argv:
        return _selftest()

    def arg(flag):
        if flag in argv and argv.index(flag) + 1 < len(argv):
            return argv[argv.index(flag) + 1]
        return None

    icp_path = arg("--icp")
    if not icp_path:
        print("ERROR: --icp is required - a score without an ICP is a preference")
        return 2
    try:
        icp = json.load(open(icp_path, encoding="utf-8"))
        raw = arg("--json")
        lead = json.loads(raw) if raw else json.load(open(arg("--lead"), encoding="utf-8"))
        r = evaluate(lead, icp)
    except (OSError, ValueError, TypeError) as e:
        print("ERROR: %s" % e)
        return 1

    print("lead: %s | band: %s | score: %d/100" % (lead.get("company", "unnamed"), r["band"], r["score"]))
    if r["code"]:
        print("disqualified: %s - %s" % (r["code"], r["reasons_against"][0]))
        return 0
    print("\nfor:")
    for line in r["reasons_for"][:4]:
        print("  + " + line)
    print("against:")
    for line in r["reasons_against"][:3]:
        print("  - " + line)
    if r["missing"]:
        print("\nunknown (scored zero, not guessed): %s" % ", ".join(r["missing"]))
        print("ask:")
        for q in r["questions"]:
            print("  ? " + q)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
