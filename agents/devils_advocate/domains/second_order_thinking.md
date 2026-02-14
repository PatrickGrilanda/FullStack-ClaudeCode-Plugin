---
key: advocate-second-order
summary: Consequences analysis, Chesterton's Fence, Goodhart's Law, unintended consequences
---

# Domain 6: Second-Order Thinking & Consequences Analysis

Second-order thinking (Howard Marks, "The Most Important Thing," 2011) asks "And then what?" repeatedly to trace cascading consequences.

- **First-order:** "If we add this feature, users will be happy."
- **Second-order:** "AND THEN users request more → roadmap becomes request-driven → we become a feature factory → we lose differentiation."

## Consequences Analysis Template

```
DECISION: [State the decision]

1ST ORDER (Immediate, direct):
  - [Effect 1] → 2ND ORDER: [Consequence] → 3RD ORDER: [Cascade]
  - [Effect 2] → 2ND ORDER: [Consequence] → 3RD ORDER: [Cascade]

TIME HORIZONS:
  - 10 minutes from now: [effects]
  - 10 months from now: [effects]
  - 10 years from now: [effects]
```

## Chesterton's Fence (G.K. Chesterton, 1929)

**Principle:** Before removing, refactoring, or replacing ANY existing system, process, code, or rule, you MUST first understand **WHY it exists**. The fact that you don't understand its purpose does NOT mean it has none.

**Steps:**
1. Before changing anything, ask: "Why does this exist?"
2. If you cannot answer, research until you can (commit history, design docs, post-mortems, ask the creator).
3. Only after understanding the original purpose should you decide whether to remove it.

## Unintended Consequences

- **Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure." (Measuring lines of code → verbose code)
- **Cobra Effect:** Incentives producing the opposite result. (Bug bounty incentivizing bug creation)
- **Streisand Effect:** Attempting to suppress information increases its spread.

## Application Rule

For every significant decision, trace at least 2 levels of consequences AND check for Goodhart's Law on any proposed metrics.
