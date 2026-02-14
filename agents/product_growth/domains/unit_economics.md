---
key: growth-unit-economics
summary: LTV and CAC calculations with critical ratios and health benchmarks
---

# Unit Economics

No growth strategy is valid without sustainable unit economics. Every growth recommendation must be validated against unit economics — scaling with broken economics only accelerates losses.

## LTV (Lifetime Value)

### Calculation Methods

**Basic formula:**
LTV = ARPU x Average Customer Lifespan

**With gross margin:**
LTV = ARPU x Gross Margin % x (1 / Churn Rate)

**Cohort-based (most accurate):**
Track revenue per cohort over time for more accurate LTV curves. This method accounts for changing retention patterns and expansion revenue.

### LTV by Business Model

| Business Model | LTV Calculation Focus |
|---|---|
| **Subscription SaaS** | Monthly revenue x expected months retained |
| **Marketplace** | Transaction commission x transactions per month x retention months |
| **E-commerce** | AOV (Average Order Value) x Purchase frequency x Retention period |
| **Freemium** | (Free user conversion rate x Paid ARPU x Paid lifespan) + Ad revenue |

### LTV Improvement Levers
- Increase ARPU (upselling, cross-selling, pricing optimization)
- Reduce churn (retention improvements, engagement loops)
- Increase purchase frequency (habit-forming features, triggers)
- Expand revenue per account (seat expansion, usage growth)

## CAC (Customer Acquisition Cost)

### Calculation Methods

**Blended CAC:**
Total marketing + sales spend / New customers acquired

**Channel CAC:**
Channel-specific spend / Customers acquired from that channel

**Fully-loaded CAC:**
Include salaries, tools, and overhead — not just ad spend. This gives the true cost of acquiring a customer.

### CAC Reduction Levers
- Improve conversion rates at each funnel stage
- Shift spend to lower-CAC channels (organic, referral)
- Increase viral coefficient to reduce paid dependency
- Optimize ad targeting and creative performance

## Critical Ratios and Benchmarks

| Metric | Healthy Benchmark | Warning Sign | Critical |
|---|---|---|---|
| **LTV:CAC ratio** | >= 3:1 | 2:1 - 3:1 | < 2:1 |
| **CAC Payback Period** | 5-12 months | 12-18 months | > 18 months |
| **Gross Margin** | > 70% (SaaS), > 40% (marketplace) | 50-70% | < 50% |
| **Monthly Churn** | < 2% (B2B SaaS), < 5% (B2C) | 5-7% | > 7% |
| **Net Revenue Retention** | > 110% | 90-110% | < 90% |

### Interpreting the Ratios

**LTV:CAC >= 3:1** means the customer generates at least 3x what it costs to acquire them. This provides margin for operational costs and profit.

**CAC Payback 5-12 months** means the company recovers acquisition costs within a year, enabling reinvestment in growth.

**Net Revenue Retention > 110%** means existing customers are spending more over time (through expansion), offsetting any churn within the cohort.

## Analysis Rule

**NEVER recommend a growth strategy that worsens LTV:CAC below 3:1 or extends CAC payback beyond 18 months.**

If current unit economics are unhealthy (LTV:CAC < 3:1, payback > 18 months, churn > 7%), the FIRST recommendation must always be to fix unit economics before scaling. Scaling with broken economics only amplifies losses.

### Priority Order When Economics Are Broken
1. Reduce churn (improves LTV directly)
2. Improve activation (increases proportion of paying users)
3. Optimize pricing (improves ARPU and LTV)
4. Reduce CAC (improve conversion rates, shift to organic channels)
5. THEN scale acquisition
