---
name: experiment-design
description: Designs structured growth experiments with hypothesis, RICE/ICE scoring, statistical requirements, and clear decision criteria.
---

# Experiment Design Skill

Designs rigorous growth experiments for A/B testing and iterative optimization. Used by the `product-growth` agent when experiments are needed to validate growth hypotheses.

## Usage

1. Run `python3 scripts/frontmatter_content_evaluation.py` to acquire existing project knowledge.
2. Read relevant `app_knowledge/` themes to understand the product context and current metrics.
3. Review existing experiments (if documented in `decisions.md`) to avoid redundancy.
4. Design experiments following the process below.

## Process

### Phase 1: Hypothesis Formation
Every experiment starts with a structured hypothesis:

**Format:** "We believe [specific change] will [expected outcome with metric] because [rationale backed by data, framework, or user research]."

Examples of GOOD hypotheses:
- "We believe reducing the onboarding form from 6 fields to 3 will increase activation rate by 15% because Baymard Institute research shows each additional form field reduces completion by 7-10%."
- "We believe adding social proof (active user count) to the pricing page will increase trial-to-paid conversion by 8% because the current page has no trust signals and our NPS is 62."

Examples of BAD hypotheses (NEVER produce these):
- "We believe improving the UX will increase conversions." (Too vague — which UX change? Which conversion?)
- "We believe this will work because competitors do it." (No quantified expectation, no mechanism)

### Phase 2: Scoring

#### For quick prioritization — use ICE:
- **Impact** (1-10): How much will this move the target metric if successful?
- **Confidence** (1-10): How confident are we, based on data or analogies?
- **Ease** (1-10): How easy is it to implement? (1 = months of work, 10 = a config change)
- **Score = I × C × E**

#### For rigorous prioritization — use RICE:
- **Reach:** Number of users affected per quarter
- **Impact:** Per-user impact (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)
- **Confidence:** Percentage (100%=high data support, 80%=medium, 50%=low/intuition)
- **Effort:** Person-months required
- **Score = (R × I × C) / E**

**Selection guidance:**
- Use ICE for early-stage products or when data is limited
- Use RICE when team capacity is constrained and precise resource allocation matters

### Phase 3: Experiment Design

For each experiment, define:

1. **Control:** The current state (what users see today)
2. **Variant(s):** The proposed change(s) — be specific about what changes
3. **Primary success metric:** The ONE metric that determines success/failure
4. **Guardrail metrics:** Metrics that MUST NOT degrade (e.g., "revenue per user must not decrease by more than 5%")
5. **Sample size calculation:**
   - Significance level: p < 0.05
   - Statistical power: > 80%
   - Minimum detectable effect: the smallest lift that would be worth implementing
   - Use the formula: n = (Z_α/2 + Z_β)² × (p₁(1-p₁) + p₂(1-p₂)) / (p₁ - p₂)²
6. **Duration:** Estimated run time based on traffic and required sample size (typical: 2-4 weeks)
7. **Segmentation:** Which user segments to include/exclude

### Phase 4: Decision Criteria

Pre-define the decision BEFORE running the experiment:

| Result | Action |
|---|---|
| Lift ≥ [X%] with p < 0.05 | Ship to 100% of users |
| Lift between [Y%] and [X%] | Iterate on the variant and re-test |
| Lift < [Y%] or not significant | Kill the experiment, document learnings |
| Guardrail metric degraded | Kill immediately regardless of primary metric |

## Output Format

Each experiment MUST follow this structure:

```
## Experiment: [Descriptive Name]

### Hypothesis
We believe [specific change] will [expected outcome] because [rationale].

### Scoring
**Method:** [ICE or RICE]
- [Score breakdown]
- **Total Score:** [calculated]
- **Priority:** [High/Medium/Low/Skip]

### Design
- **Control:** [current state — be specific]
- **Variant:** [proposed change — be specific]
- **Primary metric:** [metric name and current baseline]
- **Guardrail metrics:** [list with acceptable degradation thresholds]
- **Expected lift:** +[X]% on [metric]

### Statistical Requirements
- **Significance level:** p < 0.05
- **Power:** 80%
- **Minimum detectable effect:** [X]%
- **Required sample size:** [N] per group
- **Estimated duration:** [weeks] at current traffic of [users/day]

### Decision Criteria
| Outcome | Action |
|---|---|
| ≥ [X]% lift, p < 0.05 | Ship |
| [Y-X]% lift | Iterate |
| < [Y]% or not significant | Kill |
| Guardrail breach | Kill immediately |

### Implementation Notes
[Any technical considerations for the engineering team]

### Persisted To
[Which app_knowledge file(s) were updated]
```

## Rules

- NEVER design an experiment without a quantified hypothesis (must include expected % lift).
- NEVER skip statistical requirements — every experiment needs a sample size calculation with the formula shown.
- NEVER forget guardrail metrics — success on the primary metric is meaningless if it degrades critical metrics.
- NEVER propose more than 5 experiments at once — focus beats breadth.
- NEVER invent baseline metrics. If you don't know the current conversion rate, activation rate, or any other baseline, ASK the user. Use the structured question format from CLAUDE.md's Zero Deduction Policy.
- NEVER fabricate expected lift percentages without justification. Every expected lift must reference either (a) a benchmark from a cited source, (b) results from a similar experiment, or (c) a calculation from known data.
- ALWAYS pre-define decision criteria — post-hoc rationalization of results is not allowed.
- ALWAYS show sample size calculations with the formula and inputs, not just the result.
- ALWAYS persist experiment designs in the theme's `design.md` file in `app_knowledge/`.
- ALWAYS tag any input value not confirmed by the user or real data as `[UNVERIFIED]`.
