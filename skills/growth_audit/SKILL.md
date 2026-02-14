---
name: growth-audit
description: Performs a complete AARRR funnel audit with unit economics health check, growth loop identification, and ICE-scored opportunity prioritization.
---

# Growth Audit Skill

Performs a comprehensive product growth audit. Used by the `product-growth` agent during Business Analysis Workflow (Step 4: Business Context Analysis) or when explicitly requested.

## Usage

1. Run `python3 scripts/frontmatter_content_evaluation.py` to acquire existing project knowledge.
2. Read relevant `app_knowledge/` themes to understand the product context, business model, and current metrics (if documented).
3. Execute the audit following the process below.

## Process

### Phase 1: Product Classification
- Identify the **business model** (SaaS, Marketplace, E-commerce, Consumer App, API/Infrastructure).
- Determine the **growth stage** (Pre-PMF, Early Growth, Scale-up, Mature).
- Define or validate the **North Star Metric** and its 3-5 input metrics.

### Phase 2: AARRR Funnel Assessment
For each stage (Acquisition → Activation → Retention → Referral → Revenue):
- Document the **current metric** (if available) or the **recommended metric to track**.
- Compare against **industry benchmarks**:
  - Acquisition: SaaS signup rate 2-5%, organic CAC < paid CAC
  - Activation: 20-40% for SaaS, time-to-value < 5 minutes ideal
  - Retention: D1 25-40%, D7 10-20%, D30 5-15% (consumer); monthly churn < 5% (SaaS)
  - Referral: K-factor > 0.5 meaningful, > 1.0 viral; NPS > 50 excellent
  - Revenue: Freemium conversion 2-5%, top performers 6-8%
- Calculate the **gap** between current and benchmark.
- Assign **priority** (High/Medium/Low) based on gap severity and business impact.

### Phase 3: Unit Economics Health Check
Calculate and assess:
- **LTV:** ARPU × Gross Margin % × (1 / Churn Rate)
- **CAC:** Total acquisition spend / New customers
- **LTV:CAC ratio:** Must be ≥ 3:1 (warning at 2:1, critical below 2:1)
- **CAC Payback Period:** Must be < 12 months (warning at 12-18, critical above 18)
- **Net Revenue Retention:** Target > 110%

If unit economics are unhealthy, this MUST be flagged as the #1 priority before any scaling recommendations.

### Phase 4: Growth Loop Identification
Analyze the product to identify:
- **Primary growth loop** (the one loop that, if working, drives most growth):
  - Viral Loop: products with sharing/invitation mechanics
  - UGC Loop: products where users create discoverable content
  - Engagement Loop: products with personalization/recommendation engines
  - Collaborative Loop: products where team usage increases value
- **Secondary loops** that complement the primary.
- **Broken loops:** loops that should work but aren't completing the cycle — identify the breakage point.

### Phase 5: Opportunity Prioritization
Identify the top 3-5 growth opportunities and score each using **ICE Scoring**:
- **Impact** (1-10): How much will this move the target metric?
- **Confidence** (1-10): How confident are we it will work?
- **Ease** (1-10): How easy is it to implement?
- **ICE Score = Impact × Confidence × Ease** (max 1000)

Priority rules:
- 700-1000: Execute immediately
- 400-699: Schedule in next sprint
- 100-399: Backlog
- < 100: Skip

## Output Format

The audit MUST follow this exact structure:

```
## Growth Audit: [Product/Feature Name]

### Current State
- **Business model:** [type]
- **Stage:** [stage]
- **North Star Metric:** [metric] — current value: [X]
- **Input metrics:** [list 3-5]

### AARRR Funnel Assessment
| Stage | Current Metric | Benchmark | Gap | Priority |
|---|---|---|---|---|
| Acquisition | [value] | [benchmark] | [delta] | [H/M/L] |
| Activation | [value] | [benchmark] | [delta] | [H/M/L] |
| Retention | [value] | [benchmark] | [delta] | [H/M/L] |
| Referral | [value] | [benchmark] | [delta] | [H/M/L] |
| Revenue | [value] | [benchmark] | [delta] | [H/M/L] |

### Unit Economics Health Check
| Metric | Current | Target | Status |
|---|---|---|---|
| LTV | [value] | [target] | [Healthy/Warning/Critical] |
| CAC | [value] | [target] | [Healthy/Warning/Critical] |
| LTV:CAC | [ratio] | ≥ 3:1 | [Healthy/Warning/Critical] |
| Payback Period | [months] | < 12 mo | [Healthy/Warning/Critical] |
| NRR | [%] | > 110% | [Healthy/Warning/Critical] |

### Growth Loop Analysis
- **Primary loop:** [type] — [how it works for this product]
- **Secondary loops:** [type] — [description]
- **Broken loops:** [description of breakage points, if any]

### Top Opportunities (ICE Scored)
| # | Opportunity | Impact | Confidence | Ease | ICE Score | AARRR Stage |
|---|---|---|---|---|---|---|
| 1 | [description] | [1-10] | [1-10] | [1-10] | [score] | [stage] |
| 2 | [description] | [1-10] | [1-10] | [1-10] | [score] | [stage] |
| 3 | [description] | [1-10] | [1-10] | [1-10] | [score] | [stage] |

### Recommendations
[Specific, actionable recommendations tied to the findings — ordered by priority]

### Persisted To
[Which app_knowledge file(s) were updated]
```

## Rules

- NEVER produce an audit without benchmarks — every metric must have a reference point **with its source cited**.
- NEVER recommend scaling when unit economics are unhealthy (LTV:CAC < 3:1).
- NEVER present unsorted opportunity lists — always ICE-score and rank.
- NEVER deduce or fabricate any metric value. If the data is unavailable, propose a structured question to the user with options. Use the format from CLAUDE.md's Zero Deduction Policy.
- NEVER present a calculation without showing the formula, inputs, and result. Example: "LTV = ARPU ($X) × Margin (Y%) × (1 / Churn (Z%)) = $Result"
- ALWAYS identify the AARRR stage of each opportunity.
- ALWAYS persist findings in the relevant `app_knowledge/` theme folder.
- ALWAYS tag data points not confirmed by the user or real research as `[UNVERIFIED]`.
