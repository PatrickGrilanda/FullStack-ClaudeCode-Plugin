---
name: pricing-analysis
description: Evaluates pricing models, competitive positioning, freemium strategy, and monetization optimization with unit economics impact analysis.
---

# Pricing Analysis Skill

Performs structured pricing and monetization analysis. Used by the `product-growth` agent when evaluating or designing pricing strategies.

## Usage

1. Run `python3 scripts/frontmatter_content_evaluation.py` to acquire existing project knowledge.
2. Read relevant `app_knowledge/` themes to understand the product context, business model, and current pricing (if documented).
3. Execute the analysis following the process below.

## Process

### Phase 1: Current Pricing Assessment
Document the current state:
- **Current pricing model:** [Freemium/Free Trial/Usage-Based/Tiered/Per-Seat/Hybrid/None yet]
- **Current price points:** [specific prices per tier/plan]
- **Current conversion rate:** [free-to-paid or trial-to-paid]
- **Revenue per user (ARPU):** [monthly and annual]
- **Pricing page conversion:** [visitor-to-signup or visitor-to-trial rate]

### Phase 2: Pricing Model Evaluation
Evaluate which pricing model best fits the product using this decision matrix:

| Factor | Freemium | Free Trial | Usage-Based | Tiered | Per-Seat | Hybrid |
|---|---|---|---|---|---|---|
| **Best for** | High volume, low marginal cost | Complex products | Variable consumption | Diverse segments | Team tools | Complex value |
| **Marginal cost** | Must be near-zero | Can be higher | Scales with usage | Fixed tiers | Per-user cost | Mixed |
| **Sales motion** | Self-serve | Self-serve + sales | Self-serve | Sales-assisted | Sales | Sales-assisted |
| **Viral potential** | High (free users spread) | Medium | Low | Medium | High (seat expansion) | Medium |
| **Revenue predictability** | Low (depends on conversion) | Medium | Low (variable) | High | High | Medium |

For each viable model, assess:
- **Alignment with value metric:** Does the pricing scale with the value users receive?
- **Competitive positioning:** How does this compare to alternatives in the market?
- **Expansion revenue potential:** Can users naturally grow into higher tiers/spend?
- **Friction points:** Where might pricing create adoption barriers?

### Phase 3: Freemium Strategy (if applicable)
If recommending or evaluating freemium:

1. **Feature gate analysis:** Identify the feature that creates the upgrade trigger
   - The gate must be at the **value threshold** — the point where users have experienced enough value to justify payment
   - Apply the 80/20 rule: 80% of core value available free, the 20% that drives power use is gated
   - NEVER gate basic functionality — that creates frustration, not desire

2. **Conversion benchmarks:**
   - Average freemium conversion: 2-5%
   - Top performers (Slack, Dropbox, Spotify): 6-8%
   - If current conversion < 2%: the free tier gives too much OR the upgrade value prop is unclear
   - If current conversion > 8%: the free tier might be too restrictive — potential growth left on table

3. **Free-to-paid journey:**
   - **Time-to-upgrade:** Median days from signup to first payment
   - **Upgrade triggers:** What user actions correlate with conversion
   - **Expansion path:** How do paying users increase their spend over time

### Phase 4: Competitive Pricing Analysis
For the top 3-5 competitors or alternatives:

| Competitor | Model | Entry Price | Mid-Tier | Enterprise | Key Differentiator |
|---|---|---|---|---|---|
| [Name] | [model] | [price] | [price] | [price] | [what they emphasize] |

Analyze positioning options:
- **Premium positioning:** Price 20-50% above market — requires clear differentiation
- **Parity positioning:** Match market pricing — compete on features/experience
- **Penetration positioning:** Price 20-40% below market — gain market share fast (risk: race to bottom)

### Phase 5: Unit Economics Impact
Every pricing recommendation MUST include its impact on unit economics:

| Metric | Current | After Change | Delta |
|---|---|---|---|
| ARPU | [current] | [projected] | [+/- %] |
| LTV | [current] | [projected] | [+/- %] |
| CAC (if affected) | [current] | [projected] | [+/- %] |
| LTV:CAC | [current ratio] | [projected ratio] | [improvement/degradation] |
| Payback Period | [current months] | [projected months] | [improvement/degradation] |

**Hard constraint:** Never recommend a pricing change that degrades LTV:CAC below 3:1 or extends payback beyond 18 months.

### Phase 6: Price Sensitivity (if data is available)
If user/market data supports it, apply:
- **Van Westendorp PSM:** 4 price-perception questions to find the acceptable price range
  - Too cheap (quality concern) → Bargain → Getting expensive → Too expensive
  - Optimal Price Point (OPP): intersection of "too cheap" and "too expensive"
  - Indifference Price Point (IDP): intersection of "bargain" and "getting expensive"
- **Willingness-to-pay interviews:** "What are you currently paying for [alternative]?"
- **Price anchoring:** Use the highest tier to make the recommended tier feel reasonable

## Output Format

The analysis MUST follow this structure:

```
## Pricing Analysis: [Product Name]

### Current State
- **Model:** [current pricing model]
- **Price points:** [current tiers/prices]
- **ARPU:** [monthly/annual]
- **Conversion rate:** [free-to-paid or trial-to-paid]

### Model Evaluation
| Model Considered | Fit Score (1-5) | Pros | Cons |
|---|---|---|---|
| [model] | [score] | [pros] | [cons] |

**Recommended model:** [model] because [justification tied to product characteristics]

### Competitive Landscape
| Competitor | Model | Entry Price | Mid-Tier | Differentiator |
|---|---|---|---|---|
| [name] | [model] | [price] | [price] | [differentiator] |

**Positioning recommendation:** [Premium/Parity/Penetration] because [justification]

### Pricing Recommendation
- **Tier structure:** [recommended tiers with prices]
- **Feature gates:** [what is free vs. paid and why]
- **Upgrade triggers:** [what drives conversion]
- **Expansion levers:** [how revenue grows per customer]

### Unit Economics Impact
| Metric | Current | Projected | Delta |
|---|---|---|---|
| ARPU | [value] | [value] | [+/- %] |
| LTV | [value] | [value] | [+/- %] |
| LTV:CAC | [ratio] | [ratio] | [change] |
| Payback | [months] | [months] | [change] |

### Risks & Mitigations
| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [risk] | [H/M/L] | [H/M/L] | [mitigation] |

### Persisted To
[Which app_knowledge file(s) were updated]
```

## Rules

- NEVER recommend pricing changes without unit economics impact analysis **with calculations shown**.
- NEVER evaluate pricing in isolation — always include competitive context **researched via WebSearch**.
- NEVER recommend a freemium model without specifying the feature gate and conversion benchmark **with source cited**.
- NEVER recommend penetration pricing without a clear path to price increases.
- NEVER invent competitor pricing. Research actual prices via `WebSearch` or ask the user. If competitor pricing is not publicly available, state "Competitor pricing not publicly available" and ask the user.
- NEVER fabricate ARPU, LTV, or revenue projections. Calculate from known inputs with formula shown, or ask the user for the inputs.
- ALWAYS quantify the projected impact of pricing recommendations (ARPU, LTV, conversion rate) **with formulas and inputs visible**.
- ALWAYS persist pricing analysis in the theme's `decisions.md` file in `app_knowledge/`.
- ALWAYS tag any data point not confirmed by research or user input as `[UNVERIFIED]`.
