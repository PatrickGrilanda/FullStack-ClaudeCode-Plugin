---
key: review-cognitive-complexity
summary: SonarSource cognitive complexity scoring rules with nesting penalties and thresholds
---

# Domain 3: Cognitive Complexity (SonarSource)

A metric measuring how difficult code is to **understand** (not just test). More accurate than cyclomatic complexity for human readability.

## Scoring Rules

| Structure | Increment | Nesting Penalty |
|---|---|---|
| `if`, `else if`, `else` | +1 per branch | +1 per nesting level |
| `switch` | +1 per case | +1 per nesting level |
| `for`, `while`, `do-while` | +1 per loop | +1 per nesting level |
| `catch` | +1 | +1 per nesting level |
| Ternary `? :` | +1 | +1 per nesting level |
| Logical operators (sequence break) | +1 per change between `&&` and `||` | — |
| `break`, `continue` with label | +1 | — |
| Recursion | +1 | — |

**Key insight:** Nesting is penalized incrementally. A `for` inside an `if` inside a `try` scores much higher than the same constructs at the same level.

## Thresholds

| Score | Assessment | Action |
|---|---|---|
| 0-7 | Simple, easy to understand | Acceptable |
| 8-15 | Moderate complexity | Consider refactoring |
| 16-24 | High complexity | Should be refactored |
| 25+ | Very high complexity | MUST be refactored -- unacceptable in review |
