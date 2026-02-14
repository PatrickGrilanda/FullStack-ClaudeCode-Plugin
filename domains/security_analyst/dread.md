---
key: security-dread
summary: DREAD quick risk scoring model with 1-10 factors and action thresholds
---

## DREAD Risk Scoring

Quick risk assessment model for prioritizing threats.

| Factor | 1-3 (Low) | 4-6 (Medium) | 7-10 (High) |
|---|---|---|---|
| **D -- Damage** | Minor inconvenience | Significant data loss | Complete system compromise |
| **R -- Reproducibility** | Hard to reproduce | Reproducible with specific conditions | Always reproducible |
| **E -- Exploitability** | Requires deep expertise + custom tools | Requires some skill + available tools | Novice with browser can exploit |
| **A -- Affected Users** | Isolated individual users | Significant subset of users | All users |
| **D -- Discoverability** | Extremely difficult to find | Requires dedicated effort | Publicly known or easily findable |

### Calculation
```
DREAD Score = D + R + E + A + D (sum of all 5 factors)
Max Score = 50
```

| Score Range | Severity | Action |
|---|---|---|
| 40-50 | Critical | Fix immediately (within 24-48 hours) |
| 25-39 | High | Fix within current sprint |
| 12-24 | Medium | Schedule for next sprint |
| 5-11 | Low | Add to backlog |
