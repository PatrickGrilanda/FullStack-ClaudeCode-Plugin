---
key: planner-pert
summary: PERT three-point estimation with formulas, standard deviation, and confidence intervals
---

# Domain 3: PERT (Three-Point Estimation)

Developed for the US Navy Polaris missile program (1958). Accounts for uncertainty by using three estimates instead of a single-point guess.

## Formulas
```
Expected Duration (E) = (O + 4M + P) / 6
Standard Deviation (sigma) = (P - O) / 6
Variance = sigma^2 = ((P - O) / 6)^2
```

Where:
- **O** = Optimistic (best-case scenario, everything goes right)
- **M** = Most Likely (normal conditions, most frequent outcome)
- **P** = Pessimistic (worst-case scenario, everything that can go wrong does)

The formula weights the Most Likely estimate 4x because it represents the mode of the assumed beta distribution.

## Confidence Intervals (Normal Distribution)
```
68.3% confidence: E +/- 1 * sigma
95.4% confidence: E +/- 2 * sigma
99.7% confidence: E +/- 3 * sigma
```

For planning purposes, the **95.4% confidence interval (E +/- 2 sigma)** is the standard recommendation -- it provides high confidence without being overly conservative.

## Path Duration (Summing Activities)
```
Path Expected Duration = SUM(E of each activity on path)
Path Variance = SUM(Variance of each activity on path)
Path Standard Deviation = SQRT(Path Variance)
```

Note: Variances are additive (by the Central Limit Theorem), but standard deviations are NOT. Always sum variances first, then take the square root for the path standard deviation.

## Mandatory Presentation Rule

**ALWAYS present estimates as ranges, not single numbers.**

Example: "Task estimated at 5 days (E), range 3-7 days at 95% confidence."

A single-point estimate creates a false sense of precision. Ranges communicate uncertainty honestly and enable better decision-making by stakeholders.
