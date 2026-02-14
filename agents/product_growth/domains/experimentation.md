---
key: growth-experimentation
summary: ICE and RICE scoring frameworks with experiment design rules
---

# Experimentation Frameworks

All growth recommendations must be prioritized using a scoring framework. Unsorted lists of ideas are unacceptable — every initiative must be scored and ranked.

## ICE Scoring (Sean Ellis / GrowthHackers)

Each experiment is scored 1-10 on three dimensions:

- **Impact:** If it works, how much will it move the target metric? (1 = negligible, 10 = transformative)
- **Confidence:** How confident are we it will work? Based on data, research, or analogies. (1 = pure guess, 10 = near-certain)
- **Ease:** How easy is it to implement? Considers time, resources, and complexity. (1 = months of work, 10 = hours)

**Score = Impact x Confidence x Ease** (out of 1000)

### Priority Ranges

| Score Range | Priority | Action |
|---|---|---|
| 700-1000 | **High** | Execute immediately |
| 400-699 | **Medium** | Schedule in next sprint |
| 100-399 | **Low** | Backlog — revisit quarterly |
| < 100 | **Skip** | Not worth the investment |

### When to Use ICE
- Early-stage products with limited data
- Quick prioritization sessions
- Smaller teams with fast execution cycles
- When gut feeling + directional data is acceptable

## RICE Scoring (Intercom)

For more rigorous prioritization when team capacity is constrained:

- **Reach:** How many users will this affect per quarter? (concrete number)
- **Impact:** Per-user impact on the target metric
  - 3 = massive
  - 2 = high
  - 1 = medium
  - 0.5 = low
  - 0.25 = minimal
- **Confidence:** Percentage confidence in estimates
  - 100% = high confidence (backed by data)
  - 80% = medium confidence (based on research/analogies)
  - 50% = low confidence (hypothesis-driven)
- **Effort:** Person-months required to implement

**Score = (Reach x Impact x Confidence) / Effort**

### When to Use RICE
- Scale-ups with historical data to estimate reach
- Larger teams where effort estimation is critical
- Resource-constrained environments requiring precise trade-offs
- When multiple teams compete for engineering capacity

## Experiment Design Rules

Every experiment MUST follow these 5 rules:

### 1. Clear Hypothesis
Every experiment MUST have a hypothesis in the format:

**"We believe [specific change] will [expected outcome] because [rationale backed by data or framework]."**

Examples:
- "We believe reducing the signup form from 6 fields to 3 will increase signup completion by 20% because industry data shows each additional form field reduces conversion by 5-10%."
- "We believe adding a progress bar to onboarding will increase activation by 15% because the Zeigarnik effect drives completion of visible progress."

### 2. Pre-defined Success Metric
Define the primary success metric BEFORE running the experiment. This prevents post-hoc rationalization. Also define guardrail metrics that must NOT degrade.

### 3. Minimum Sample Size
Calculate minimum sample size for statistical significance:
- **p-value threshold:** < 0.05 (95% confidence)
- **Statistical power:** > 0.8 (80% chance of detecting a true effect)
- Use standard sample size calculators based on baseline conversion rate and minimum detectable effect

### 4. Maximum Duration
Set a maximum experiment duration before starting:
- Typical duration: 2-4 weeks
- Shorter for high-traffic experiments
- Longer for low-traffic or B2B contexts
- NEVER let experiments run indefinitely

### 5. Expected Lift
Document the expected lift percentage before running:
- Forces realistic expectations
- Enables post-experiment evaluation of prediction accuracy
- Example: "+15% activation rate" or "+8% free-to-paid conversion"
