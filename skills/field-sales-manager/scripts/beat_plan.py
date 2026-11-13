#!/usr/bin/env python3
"""Deterministic beat plan for field-sales-manager.

    python3 scripts/beat_plan.py --csv outlets.csv --reps 3 --working-days 24 --max-calls 10
    python3 scripts/beat_plan.py --self-test

CSV columns required: outlet_id, name, zone, priority, visits_per_month, last_visit
  priority is A, B, C or D (A is the most important)
  last_visit is YYYY-MM-DD, or blank for never visited

The plan fills days in zone order, most-visited zone first, and inside a zone by priority then by the
oldest last visit, up to `reps x max_calls` calls a day. It never invents an outlet, a visit or a
date: it schedules what the file says and reports what it could not place.

Output: the day-by-day plan, coverage against the frequency policy, and the outlets the month cannot
reach. Coverage below 100% is a capacity finding, not a planning failure - the script says so.

Exit 0 on success, 1 on a data error, 2 on bad usage.
"""
import csv
import datetime
import io
import sys

PRIORITY_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}
REQUIRED = ["outlet_id", "name", "zone", "priority", "visits_per_month", "last_visit"]


def load_outlets(text):
    reader = csv.DictReader(io.StringIO(text.strip()))
    if reader.fieldnames is None:
        raise ValueError("empty CSV")
    fields = [f.strip() for f in reader.fieldnames]
    missing = [c for c in REQUIRED if c not in fields]
    if missing:
        raise ValueError("missing columns: %s" % ", ".join(missing))
    outlets = []
    for i, raw in enumerate(reader, start=2):
        row = {k.strip(): (v or "").strip() for k, v in raw.items() if k}
        if not row.get("outlet_id") or not row.get("name"):
            raise ValueError("row %d: outlet_id and name are required" % i)
        pri = (row.get("priority") or "C").upper()
        if pri not in PRIORITY_ORDER:
            raise ValueError("row %d: priority must be A, B, C or D" % i)
        try:
            visits = int(float(row.get("visits_per_month") or 1))
        except ValueError:
            raise ValueError("row %d: visits_per_month must be a number" % i)
        if visits < 0:
            raise ValueError("row %d: negative visits_per_month" % i)
        last = row.get("last_visit") or ""
        if last:
            try:
                datetime.date.fromisoformat(last)
            except ValueError:
                raise ValueError("row %d: last_visit must be YYYY-MM-DD" % i)
        outlets.append({"id": row["outlet_id"], "name": row["name"],
                        "zone": row.get("zone") or "unassigned", "priority": pri,
                        "visits": visits, "last_visit": last})
    if not outlets:
        raise ValueError("no outlets in the file")
    return outlets


def build_visits(outlets):
    """One entry per required visit, ordered by zone size, priority, then oldest last visit."""
    zone_weight = {}
    for o in outlets:
        zone_weight[o["zone"]] = zone_weight.get(o["zone"], 0) + o["visits"]
    visits = []
    for o in outlets:
        for n in range(o["visits"]):
            visits.append({"outlet": o, "visit_no": n + 1})
    visits.sort(key=lambda v: (-zone_weight[v["outlet"]["zone"]],
                               PRIORITY_ORDER[v["outlet"]["priority"]],
                               v["outlet"]["last_visit"] or "0000-00-00",
                               v["outlet"]["id"]))
    return visits, zone_weight


def plan(outlets, reps, working_days, max_calls):
    if reps < 1 or working_days < 1 or max_calls < 1:
        raise ValueError("reps, working_days and max_calls must be at least 1")
    visits, zone_weight = build_visits(outlets)
    per_day = reps * max_calls
    days, current, current_count = [], [], 0
    for v in visits:
        if current_count >= per_day:
            days.append(current)
            current, current_count = [], 0
        current.append(v)
        current_count += 1
    if current:
        days.append(current)

    placed = sum(len(d) for d in days[:working_days])
    unplaced = [v for d in days[working_days:] for v in d]
    scheduled = days[:working_days]

    required = sum(o["visits"] for o in outlets)
    covered_ids = {v["outlet"]["id"] for d in scheduled for v in d}
    all_ids = {o["id"] for o in outlets}
    return {"days": scheduled, "required": required, "placed": placed,
            "coverage": round(placed / required, 3) if required else 1.0,
            "capacity": reps * working_days * max_calls,
            "unplaced": unplaced,
            "outlets_never_visited": sorted(all_ids - covered_ids),
            "zone_weight": zone_weight}


def _selftest():
    checks = 0
    sample = """outlet_id,name,zone,priority,visits_per_month,last_visit
1,Sharma Stores,kothrud,A,4,2026-10-02
2,Patil Kirana,kothrud,B,2,2026-10-20
3,New Mart,baner,A,4,
4,Deccan Traders,deccan,C,1,2026-09-01
5,Sunrise Shop,baner,C,1,2026-11-01
"""
    outlets = load_outlets(sample)
    assert len(outlets) == 5
    assert sum(o["visits"] for o in outlets) == 12
    checks += 2

    r = plan(outlets, reps=1, working_days=6, max_calls=4)
    assert r["required"] == 12 and r["placed"] == 12
    assert r["coverage"] == 1.0
    assert r["capacity"] == 24
    assert r["outlets_never_visited"] == []
    checks += 4

    # the largest zone is planned first
    first_zone = r["days"][0][0]["outlet"]["zone"]
    assert first_zone == "kothrud", first_zone
    checks += 1

    # inside a zone, A priority comes before B
    kothrud = [v["outlet"]["priority"] for d in r["days"] for v in d
               if v["outlet"]["zone"] == "kothrud"]
    assert kothrud[0] == "A" and kothrud[-1] == "B", kothrud
    checks += 1

    # capacity shortfall is reported, not hidden
    tight = plan(outlets, reps=1, working_days=1, max_calls=3)
    assert tight["placed"] == 3 and tight["coverage"] == 0.25
    assert len(tight["unplaced"]) == 9
    assert len(tight["outlets_never_visited"]) >= 2
    checks += 3

    # every day respects the calls cap
    for d in r["days"]:
        assert len(d) <= 4, len(d)
    checks += 1

    # a never-visited outlet sorts ahead of a recently visited one at the same priority
    same = """outlet_id,name,zone,priority,visits_per_month,last_visit
10,Recent,zone1,C,1,2026-11-10
11,Never,zone1,C,1,
"""
    rs = plan(load_outlets(same), 1, 2, 5)
    assert rs["days"][0][0]["outlet"]["id"] == "11", rs["days"][0][0]
    checks += 1

    for bad in ("outlet_id,name,zone,priority,visits_per_month,last_visit\n1,x,z,E,2,\n",
                "outlet_id,name,zone,priority,visits_per_month,last_visit\n1,x,z,A,2,10/11/2026\n",
                "outlet_id,name\n1,x\n"):
        try:
            load_outlets(bad)
        except ValueError:
            checks += 1
        else:
            raise AssertionError("accepted bad outlet data: %r" % bad[:40])

    try:
        plan(outlets, 0, 24, 10)
    except ValueError:
        checks += 1
    else:
        raise AssertionError("accepted zero reps")

    print("self-test: %d checks passed" % checks)
    return 0


def main(argv):
    if "--self-test" in argv:
        return _selftest()

    def arg(flag, default=None):
        return argv[argv.index(flag) + 1] if flag in argv and argv.index(flag) + 1 < len(argv) else default

    if not arg("--csv"):
        print(__doc__)
        return 2
    try:
        outlets = load_outlets(open(arg("--csv"), encoding="utf-8").read())
        r = plan(outlets, int(arg("--reps", "1")), int(arg("--working-days", "24")),
                 int(arg("--max-calls", "10")))
    except (OSError, ValueError) as e:
        print("ERROR: %s" % e)
        return 1

    print("outlets: %d | required visits: %d | capacity: %d | planned: %d | coverage: %.1f%%" % (
        len(outlets), r["required"], r["capacity"], r["placed"], r["coverage"] * 100))
    print("zones by required visits: %s" % ", ".join(
        "%s %d" % (z, n) for z, n in sorted(r["zone_weight"].items(), key=lambda kv: -kv[1])))
    for i, day in enumerate(r["days"], start=1):
        zones = sorted({v["outlet"]["zone"] for v in day})
        print("\nday %d - %s (%d calls)" % (i, "/".join(zones), len(day)))
        for v in day:
            o = v["outlet"]
            print("   %-12s %-20s %s  visits %d/%d  last %s" % (
                o["id"], o["name"][:20], o["priority"], v["visit_no"], o["visits"],
                o["last_visit"] or "never"))
    if r["unplaced"]:
        print("\nFINDING: %d required visits do not fit in the working days at this capacity." % len(r["unplaced"]))
        print("  Either add capacity, lower the frequency policy for C and D outlets, or accept the gap in writing.")
    if r["outlets_never_visited"]:
        print("  outlets not reached this month: %s" % ", ".join(r["outlets_never_visited"][:20]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
