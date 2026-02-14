---
key: planner-risk
summary: 5x5 P*I matrix, EMV calculation, risk register, PMBOK response strategies
---

# Domain 6: Risk Quantification

## Probability x Impact Matrix (5x5)

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---|---|---|---|---|
| **Prob 5 (>80%)** | 5 | 10 | 15 | 20 | 25 |
| **Prob 4 (60-80%)** | 4 | 8 | 12 | 16 | 20 |
| **Prob 3 (40-60%)** | 3 | 6 | 9 | 12 | 15 |
| **Prob 2 (20-40%)** | 2 | 4 | 6 | 8 | 10 |
| **Prob 1 (<20%)** | 1 | 2 | 3 | 4 | 5 |

**Risk Score = Probability Rating x Impact Rating**

### Risk Zones
- **Red (15-25):** Immediate response needed. These risks require active mitigation or avoidance strategies before the plan can proceed.
- **Amber (6-14):** Mitigation plan required. These risks must have documented response strategies and assigned owners.
- **Green (1-5):** Monitor. Track these risks but no immediate action required beyond awareness.

## Expected Monetary Value (EMV)
```
EMV = Probability x Impact (in monetary terms or schedule days)
Project Risk Exposure = SUM(all EMVs)
```

EMV converts qualitative risk assessment into quantitative terms, enabling cost-benefit analysis of risk responses. The total Project Risk Exposure should inform the contingency reserve.

## Risk Response Strategies (PMBOK)

| For Threats | Action |
|---|---|
| **Avoid** | Eliminate the threat by changing the plan (remove scope, change approach) |
| **Mitigate** | Reduce probability and/or impact (add testing, use proven technology, prototype first) |
| **Transfer** | Shift impact to third party (insurance, fixed-price contract, SLA with vendor) |
| **Accept (Active)** | Establish contingency reserve (time and/or budget buffer allocated specifically for this risk) |
| **Accept (Passive)** | Deal with it if it occurs (no proactive action, only reactive) |
| **Escalate** | Outside team's authority -- escalate to higher-level decision maker |

## Risk Register Structure
Every identified risk must include:

| Field | Description |
|---|---|
| Risk ID | Unique identifier (R-001, R-002, etc.) |
| Description | Clear statement of what could happen |
| Category | Technical, Schedule, Resource, External, etc. |
| Probability (1-5) | Likelihood rating |
| Impact (1-5) | Consequence rating |
| Score | P x I |
| Priority | H/M/L based on score zones |
| Risk Owner | Person responsible for monitoring and response |
| Response Strategy | Avoid / Mitigate / Transfer / Accept / Escalate |
| Response Plan | Specific actions to implement the strategy |
| Trigger / Early Warning | Observable indicator that the risk is materializing |
| EMV | Quantified expected value (when calculable) |
| Status | Open / Mitigating / Closed / Occurred |
