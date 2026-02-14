---
key: security-cvss
summary: CVSS v3.1 full scoring formula with metric weights, severity thresholds, and v4.0 changes
---

## CVSS v3.1 Scoring

Common Vulnerability Scoring System -- industry standard for quantifying vulnerability severity.

### Base Metrics

| Metric | Values | Description |
|---|---|---|
| **Attack Vector (AV)** | Network (0.85), Adjacent (0.62), Local (0.55), Physical (0.20) | How the vulnerability can be exploited |
| **Attack Complexity (AC)** | Low (0.77), High (0.44) | Conditions beyond attacker's control |
| **Privileges Required (PR)** | None (0.85), Low (0.62/0.68), High (0.27/0.50) | Level of privileges needed (values differ with/without Scope change) |
| **User Interaction (UI)** | None (0.85), Required (0.62) | Whether a user must take action |
| **Scope (S)** | Unchanged, Changed | Whether the vulnerability can affect resources beyond its security scope |
| **Confidentiality (C)** | None (0), Low (0.22), High (0.56) | Impact on information confidentiality |
| **Integrity (I)** | None (0), Low (0.22), High (0.56) | Impact on information integrity |
| **Availability (A)** | None (0), Low (0.22), High (0.56) | Impact on system availability |

### Calculation Formula
```
ISCBase = 1 - [(1 - C) x (1 - I) x (1 - A)]

If Scope Unchanged:
  Impact = 6.42 x ISCBase
  BaseScore = RoundUp(min(Impact + Exploitability, 10))

If Scope Changed:
  Impact = 7.52 x [ISCBase - 0.029] - 3.25 x [ISCBase - 0.02]^15
  BaseScore = RoundUp(min(1.08 x (Impact + Exploitability), 10))

Exploitability = 8.22 x AV x AC x PR x UI
```

### Severity Thresholds

| Score | Severity |
|---|---|
| 0.0 | None |
| 0.1-3.9 | Low |
| 4.0-6.9 | Medium |
| 7.0-8.9 | High |
| 9.0-10.0 | Critical |

### CVSS v4.0 Key Changes
- New **Attack Requirements (AT)** metric replacing some AC nuances
- **Dual impact assessment:** Vulnerable System vs. Subsequent System (replaces Scope)
- Temporal group renamed to **Threat** group
- New **Supplemental** metrics (Safety, Automatable, Recovery, Value Density, Vulnerability Response Effort, Provider Urgency)
