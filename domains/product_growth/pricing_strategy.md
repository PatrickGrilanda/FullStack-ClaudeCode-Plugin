---
key: growth-pricing
summary: 6 pricing models with freemium deep dive and price sensitivity analysis methods
---

# Pricing & Monetization Strategy

Pricing is the most impactful growth lever — a 1% pricing improvement yields 11% profit improvement (McKinsey). Understanding pricing models, their trade-offs, and how to analyze price sensitivity is critical to sustainable growth.

## Pricing Models

| Model | Best For | Key Consideration |
|---|---|---|
| **Freemium** | High volume, low marginal cost, viral potential | Feature gate at value threshold; 80/20 rule (80% value free, 20% premium) |
| **Free Trial** | High-touch products, complex onboarding | 14 days optimal for SMB; 30 days for enterprise; activation rate during trial is critical |
| **Usage-Based** | Variable consumption, API/infrastructure products | Align price with value delivered; provide cost predictability tools |
| **Tiered** | Diverse customer segments | 3 tiers optimal (Good/Better/Best); anchor with highest tier |
| **Per-Seat** | Collaboration tools, team products | Encourage seat expansion; avoid per-seat friction for small teams |
| **Hybrid** | Complex products with multiple value dimensions | Base + usage component; reduces barrier to entry while capturing growth |

### Model Selection Guidance

- **Freemium** works when free users serve as a marketing channel (viral/UGC loops) and marginal cost per user is near zero
- **Free Trial** works when the product requires time to demonstrate value and the "aha moment" takes more than a few minutes
- **Usage-Based** works when consumption varies widely across customers and price scales with value delivered
- **Tiered** works when customer segments have distinct needs and willingness to pay
- **Per-Seat** works when each additional user adds collaborative value and expansion is a natural motion
- **Hybrid** combines approaches to reduce entry friction while capturing value from heavy users

## Freemium Strategy Deep Dive

### Conversion Benchmarks
- **Average:** 2-5% free-to-paid conversion (Openview Partners)
- **Top performers:** 6-8% free-to-paid conversion
- **Elite:** >10% (rare, typically products with strong network effects or clear value gates)

### Feature Gating Strategy
Identify the feature that makes users say "I need to upgrade" — gate THAT specific feature, not random ones. The gate should be:
- Clearly visible to free users (they know what they're missing)
- Triggered by usage growth (as the user becomes more engaged, they hit the gate naturally)
- Aligned with the product's core value escalation

### Time-to-Upgrade Tracking
- Track median days from signup to first payment
- Identify the actions that precede conversion (leading indicators)
- Optimize the path from signup to those trigger actions

### Expansion Triggers
The most effective expansion triggers:
- **Usage limits:** Storage, API calls, team members, projects
- **Team size:** Collaboration features locked behind team plans
- **Advanced features:** Analytics, integrations, customization, automation
- **Priority support:** SLA guarantees, dedicated account management

## Price Sensitivity Analysis

### Van Westendorp Price Sensitivity Meter (PSM)

Uses 4 price-perception questions to identify the acceptable price range:
1. At what price would this be so cheap you'd question its quality? (Too Cheap)
2. At what price is this a bargain — a great buy for the money? (Cheap/Good Value)
3. At what price is this getting expensive but you'd still consider it? (Expensive/High)
4. At what price is this too expensive to consider? (Too Expensive)

Plot the cumulative distributions to find:
- **Point of Marginal Cheapness (PMC):** Intersection of "Too Cheap" and "Expensive"
- **Point of Marginal Expensiveness (PME):** Intersection of "Cheap" and "Too Expensive"
- **Acceptable price range:** Between PMC and PME
- **Optimal Price Point (OPP):** Intersection of "Too Cheap" and "Too Expensive"

### Conjoint Analysis

Quantifies willingness to pay for specific feature bundles:
- Decomposes product into attributes and levels
- Users evaluate trade-offs between feature combinations
- Statistical analysis reveals the value attributed to each feature
- Enables data-driven packaging and tiering decisions

### Competitive Anchoring

Position pricing relative to alternatives:
- **Premium positioning:** Price above competitors — requires clear differentiation and perceived superior value
- **Parity positioning:** Price at market level — competes on features, UX, or brand
- **Penetration positioning:** Price below competitors — captures market share, requires volume economics
