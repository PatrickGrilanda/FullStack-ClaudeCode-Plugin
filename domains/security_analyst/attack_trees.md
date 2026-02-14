---
key: security-attack-trees
summary: Bruce Schneier attack tree methodology with OR/AND nodes and attribute calculation rules
---

## Attack Trees (Bruce Schneier, 1999)

Hierarchical model of possible attacks against a system.

### Structure
- **Root node:** The attacker's goal (e.g., "Exfiltrate customer PII")
- **OR nodes:** Alternative ways to achieve the parent (ANY child succeeds = parent succeeds)
- **AND nodes:** All children must succeed for the parent to succeed
- **Leaf nodes:** Atomic attack steps

### Construction Process
1. Define the root goal (attacker's objective)
2. Decompose into sub-goals (OR = alternatives, AND = required steps)
3. Continue until leaf nodes are atomic, actionable attack steps
4. Annotate with attributes: Cost, Skill Level, Detection Risk, Success Probability
5. Calculate path feasibility

### Attribute Calculation Rules

| Node Type | Cost | Time | Skill | Detection | Probability |
|---|---|---|---|---|---|
| **OR** | MIN of children | MIN of children | MIN of children | MIN of children | MAX of children |
| **AND** | SUM of children | SUM of children | MAX of children | MAX of children | PRODUCT of children |
