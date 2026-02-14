---
key: advocate-fmea
summary: FMEA with RPN calculation, S/O/D ratings 1-10, and risk level action thresholds
---

# Domain 10: FMEA (Failure Mode and Effects Analysis)

## Origins

- **U.S. Military:** MIL-P-1629 — original procedure for failure analysis.
- **NASA:** Apollo program — systematic reliability engineering.
- **Ford Motor Company:** Adopted for automotive quality and safety.

Proactively identifies failure modes before they occur.

## RPN Calculation

**RPN = Severity (S) x Occurrence (O) x Detection (D)**

Each rated 1-10. Range: 1 (lowest risk) to 1000 (highest risk).

## Rating Scales

| Rating | Severity (S) | Occurrence (O) | Detection (D) — INVERTED |
|---|---|---|---|
| 1 | No effect | Remote (<1 in 1M) | Almost certain to detect |
| 2-3 | Cosmetic/minor | Very low-Low | Very high-High detection |
| 4-5 | Functional impact, workaround exists | Moderately low-Moderate | Moderately high-Moderate detection |
| 6-7 | Feature degraded/inoperable | Moderately high-High | Low-Very low detection |
| 8 | System inoperable | Very high | Remote detection chance |
| 9 | Safety/security with warning | Very high | Very remote detection |
| 10 | Safety/security without warning | Almost certain failure | No detection capability |

## RPN Risk Levels and Action Thresholds

| RPN Range | Risk Level | Action |
|---|---|---|
| 1-50 | Low | Monitor |
| 51-100 | Medium | Plan corrective action this cycle |
| 101-200 | High | Priority corrective action |
| 201-500 | Very High | Immediate corrective action |
| 501-1000 | Critical | STOP and address before proceeding |

## Critical Note

Any individual Severity of 9-10 demands attention regardless of RPN. A catastrophic-but-rare failure (S=10, O=1, D=1, RPN=10) must NOT be ignored based on low RPN alone.
