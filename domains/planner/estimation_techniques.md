---
key: planner-estimation
summary: 5 estimation techniques - Planning Poker, Wideband Delphi, T-Shirt Sizing, Story Points, Analogy
---

# Domain 5: Estimation Techniques

## Planning Poker (Modified Delphi)
- Uses Fibonacci sequence: 1, 2, 3, 5, 8, 13, 21
- Team simultaneously reveals estimates (avoids anchoring bias)
- Discuss outliers: highest and lowest estimators explain their reasoning
- Re-estimate until convergence (typically 2-3 rounds)
- **Best for:** Sprint-level stories, teams of 3-9 people

The simultaneous reveal is critical -- if estimates are shared sequentially, the first number anchors everyone else's judgment.

## Wideband Delphi (Boehm, 1970s)
- Anonymous multi-round estimation with expert panel
- Coordinator shares anonymous distribution of estimates after each round
- Focus discussion on wide divergences between experts
- Typically converges in 3 rounds
- **Best for:** High-stakes estimates, complex technical work, cross-team estimation

## T-Shirt Sizing

| Size | Story Point Range | Duration Range |
|---|---|---|
| XS | 1-2 | < 1 day |
| S | 3-5 | 1-3 days |
| M | 8-13 | 3-5 days |
| L | 20-40 | 1-2 weeks |
| XL | 40-100 | 2-4 weeks |
| XXL | 100+ | Needs decomposition |

**Best for:** Roadmap planning, initial backlog grooming, portfolio-level decisions where relative sizing matters more than precision.

**Rule:** Any item sized XXL MUST be decomposed further before it enters a sprint or implementation plan.

## Story Points vs. Hours

| Dimension | Story Points | Hours |
|---|---|---|
| Measures | Relative complexity, risk, effort | Absolute calendar time |
| Team agreement | Senior and junior agree on same value | Diverges by skill level |
| Forecasting | Via velocity (points per sprint) | Via capacity (available hours) |
| **Best for** | Long-term forecasting, Agile teams | Short-term tasks, billing contexts |

Story points measure the SIZE of work (complexity + uncertainty + effort), not the TIME. A senior developer and a junior developer should assign the same story point value to a task, even though the junior will take longer in hours.

## Estimation by Analogy
1. Find similar past projects or tasks
2. Compare characteristics (scope, technology, team, complexity)
3. Adjust for differences (more complex = scale up, simpler = scale down)
4. Arrive at estimate grounded in actual historical data

**Best for:** Project initiation, feasibility studies, when detailed requirements are unavailable but comparable past work exists.
