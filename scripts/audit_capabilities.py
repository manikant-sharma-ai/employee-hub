#!/usr/bin/env python3
"""Audit every employee's capability coverage.

Checks four things the repo validator does not:

1. Declared capabilities (registry `skills_inside`) against references on disk.
2. Every shipped reference is routed from SKILL.md, so the employee can find it.
3. The capability baseline - the disciplines each role must keep shipping. This is
   what stops a capability quietly disappearing in a refactor.
4. Handoffs to employees that do not exist, which leave a reader with nowhere to go.

Usage: python3 scripts/audit_capabilities.py [--quiet]
Exit 0 = every employee is complete. Exit 1 = gaps found.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Disciplines each role must keep shipping, by reference stem. Adding a role to the
# hub means adding it here, or the audit will not know what "complete" means for it.
BASELINE = {
    "ai-engineer": ["prompt-engineering", "context-engineering", "loop-engineering",
                    "graph-engineering", "mcp-and-tools", "image-generation",
                    "model-selection-and-evals", "skill-authoring",
                    "rag-and-retrieval", "cost-latency-and-scaling", "agent-safety-and-guardrails"],
    "graphic-designer": ["brand-system-and-assets", "layout-and-typography", "social-and-thumbnail-craft",
                         "print-and-production", "creative-brief-and-feedback",
                         "indian-market-visual-conventions", "packaging-and-label-compliance",
                         "motion-and-animated-assets"],
    "content-writer": ["voice-and-tone", "long-form-structure", "short-form-and-hooks",
                       "editing-and-fact-check", "humanizer-pass", "distribution-and-repurposing",
                       "landing-page-and-conversion-copy"],
    "research-analyst": ["research-design", "source-quality-and-verification",
                         "competitor-and-market-mapping", "company-and-people-diligence",
                         "synthesis-and-decision-memo", "india-market-sources",
                         "interviews-and-surveys"],
    "support-agent": ["triage-and-priority", "reply-patterns", "tone-and-de-escalation",
                      "escalation-and-refund-authority", "knowledge-and-macros", "indian-channel-norms"],
    "data-analyst": ["data-cleaning", "metric-definitions", "analysis-patterns",
                     "charting-and-readout", "spreadsheet-to-answer", "statistical-honesty",
                     "sql-and-queries", "forecasting-and-scenarios"],
    "sales-outreach": ["icp-and-list-building", "cold-email-craft", "follow-up-sequences",
                       "objection-handling", "crm-hygiene", "india-outbound-norms",
                       "discovery-calls-and-demos"],
    "video-editor": ["footage-intake-and-organising", "edit-and-cut-craft", "short-form-structure",
                     "captions-and-subtitles", "audio-and-music", "platform-delivery-specs",
                     "long-form-and-youtube", "colour-and-finishing"],
    "finance-ops": ["invoicing-and-billing", "reconciliation", "expense-categorisation",
                    "monthly-close", "gst-and-statutory-readiness", "controls-and-fraud-checks",
                    "cash-flow-and-runway", "payroll-and-tds"],
    "hr-recruiter": ["role-scorecard", "jd-writing", "screening-and-shortlisting", "interview-kit",
                     "candidate-comms-and-offers", "india-hiring-norms", "onboarding-handoff"],
    "brand-strategist": ["positioning", "messaging-hierarchy", "naming", "tone-of-voice",
                         "category-and-competitor-framing", "brand-audit-and-testing",
                         "brand-architecture"],
    "seo-specialist": ["keyword-and-intent-mapping", "serp-and-competitor-gap", "on-page-fixes",
                       "content-briefs-that-rank", "measuring-seo", "india-search-behaviour",
                       "technical-seo-crawl-and-index", "local-seo-and-maps"],
    "presentation-designer": ["narrative-arc", "deck-types-and-standards", "slide-by-slide-craft",
                              "data-slides-and-charts", "speaker-notes-and-delivery", "reviewing-a-deck"],
    "bookkeeper": ["double-entry-basics", "chart-of-accounts-and-coding", "voucher-entry",
                   "documents-and-supporting", "vendor-and-payment-tracking", "common-entry-errors",
                   "payroll-and-statutory-entries"],
    "legal-drafter": ["contract-anatomy", "service-agreements", "nda-and-confidentiality",
                      "policy-drafting", "review-boundary-and-risk-flags", "india-contract-basics",
                      "employment-and-consultant-agreements", "ip-and-brand-protection"],
    "product-manager": ["discovery-and-evidence", "prd-and-specs", "prioritisation",
                        "story-slicing", "scope-and-saying-no", "launch-and-after"],
    "employee-hub-router": ["role-map", "brief-and-handover", "scheduling-and-cadence"],
    "social-media-manager": ["content-calendar-and-cadence", "platform-mechanics",
                             "repurposing-and-formats", "engagement-and-community",
                             "india-social-norms", "analytics-and-reporting"],
    "ui-designer": ["flow-and-screens", "states-and-edge-cases", "spacing-and-type-scale",
                    "handoff-and-specs", "accessibility-and-inclusive-design",
                    "responsive-and-mobile-patterns"],
    "email-marketer": ["subject-lines-and-open-rate", "sequence-design",
                       "list-hygiene-and-consent", "deliverability-and-compliance",
                       "newsletter-and-curation"],
    "qa-tester": ["test-plan-and-scope", "edge-case-matrix", "bug-report-craft",
                  "release-call-and-severity", "api-and-integration-testing"],
    "translator-localiser": ["indic-language-craft", "tone-and-formality",
                             "formats-numbers-and-dates", "glossary-and-consistency",
                             "ui-strings-and-translation-memory"],
    "pr-writer": ["news-hooks-and-angles", "press-release-craft", "founder-story-and-pitch",
                  "media-list-and-outreach", "measurement-and-coverage"],
    "partnerships": ["partner-types-and-fit", "partner-one-pager", "partner-outreach",
                     "deal-terms-and-economics", "partner-activation-and-scorecard"],
    "procurement": ["specification-and-rfq", "quote-comparison-and-tco", "vendor-due-diligence",
                    "negotiation-prep", "purchase-to-pay-and-controls"],
    "analytics-instrumenter": ["event-taxonomy", "tracking-plan", "funnel-and-metric-definitions",
                               "dashboard-spec", "qa-and-data-quality"],
    "pricing-analyst": ["willingness-to-pay", "packaging-and-plans", "margin-and-unit-economics",
                        "discount-and-leakage", "price-testing-and-rollout"],
}

HANDOFF = re.compile(r"\((?:use|see) ([a-z][a-z0-9]+(?:-[a-z0-9]+)+)\)")

def main():
    quiet = "--quiet" in sys.argv
    reg = json.load(open(os.path.join(ROOT, "registry.json"), encoding="utf-8"))
    skills_dir = os.path.join(ROOT, "skills")
    shipped = {e["name"] for e in reg["employees"]}
    gaps, warns = [], []

    for e in reg["employees"]:
        name = e["name"]
        folder = os.path.join(skills_dir, name)
        ref_dir = os.path.join(folder, "references")
        on_disk = {f[:-3] for f in os.listdir(ref_dir) if f.endswith(".md")} if os.path.isdir(ref_dir) else set()
        skill_md = open(os.path.join(folder, "SKILL.md"), encoding="utf-8").read()

        declared = set(e.get("skills_inside", []))
        for missing in sorted(declared - on_disk):
            gaps.append("%s: declared %r but references/%s.md does not exist" % (name, missing, missing))

        for cap in BASELINE.get(name, []):
            if cap not in on_disk:
                gaps.append("%s: MISSING CAPABILITY %r (baseline requires it)" % (name, cap))

        for stem in sorted(on_disk):
            if ("references/%s.md" % stem) not in skill_md:
                warns.append("%s: references/%s.md is never routed from SKILL.md" % (name, stem))

        for target in sorted(set(HANDOFF.findall(skill_md))):
            if target not in shipped and target not in ("core", "references"):
                warns.append("%s: hands off to %r, which is not an employee in skills/" % (name, target))

    if not BASELINE.get("_silent"):
        for name in sorted(shipped - set(BASELINE)):
            warns.append("%s: no capability baseline declared in audit_capabilities.py" % name)

    print("capability audit: %d employees | %d baselines" % (len(shipped), len(BASELINE)))
    for g in gaps:
        print("  GAP     " + g)
    for w in warns:
        print("  warning " + w)
    print("RESULT: %s (%d gaps, %d warnings)" % ("PASS" if not gaps else "FAIL", len(gaps), len(warns)))
    return 0 if not gaps else 1

if __name__ == "__main__":
    sys.exit(main())
