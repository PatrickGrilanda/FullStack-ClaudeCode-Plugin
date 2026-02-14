---
key: planner-agile
summary: Three horizons, velocity forecasting with ranges, Cone of Uncertainty, burndown vs burnup
---

# Domain 10: Agile Planning

## Three Horizons

| Horizon | Timeframe | Artifact | Detail Level |
|---|---|---|---|
| Strategic | 6-24 months | Product Roadmap | Themes, epics, goals (coarse) |
| Tactical | 1-6 months | Release Plan | Features estimated in story points (medium) |
| Operational | 1-4 weeks | Sprint Backlog | Stories broken into tasks (high detail) |

Each horizon uses progressively more precise estimation techniques. Strategic uses T-shirt sizing or analogies. Tactical uses story points and velocity. Operational uses task-hour breakdowns.

## Velocity-Based Forecasting
```
Sprints Needed = Remaining Story Points / Average Velocity
Calendar Time = Sprints Needed x Sprint Length

Example:
  Remaining: 150 story points
  Velocity (avg last 6 sprints): 39 points/sprint
  Sprint length: 2 weeks

  Optimistic (max velocity 45): 150/45 = 3.3 sprints = 7 weeks
  Average (39): 150/39 = 3.8 sprints = 8 weeks
  Pessimistic (min velocity 35): 150/35 = 4.3 sprints = 9 weeks
  Forecast: 7-9 weeks (most likely ~8 weeks)
```

**ALWAYS present velocity forecasts as ranges** using optimistic (max observed velocity), average, and pessimistic (min observed velocity) scenarios. A single-point forecast based on average velocity alone hides significant uncertainty.

## Cone of Uncertainty (Steve McConnell, 1997)

| Project Phase | Estimate Accuracy Range |
|---|---|
| Initial Concept | 0.25x to 4.0x (factor of 16 total range) |
| Approved Product Definition | 0.5x to 2.0x |
| Requirements Complete | 0.67x to 1.5x |
| ~30% Complete | 0.8x to 1.25x |
| ~50% Complete | 0.9x to 1.1x |

### Key Implications
- **Do NOT make hard commitments at Initial Concept stage.** With a 16x range, any commitment is essentially a guess.
- **Defer firm commitments until at least 30% complete** (when the range narrows to 0.8x-1.25x).
- **Use ranges, not single numbers, for ALL estimates.** The range width should reflect the current phase in the cone.
- **The cone narrows only through DECISIONS that eliminate variability** -- simply waiting does not narrow it. Each design decision, technology choice, or requirement clarification reduces uncertainty.
- **Re-estimate at every phase gate.** As the cone narrows, estimates should become more precise. If they don't, something is wrong.

## Burndown vs. Burnup Charts

| Chart Type | Shows | Strengths | Weaknesses |
|---|---|---|---|
| **Burndown** | Remaining work over time | Simple, intuitive, shows progress toward zero | HIDES scope changes -- if scope increases while work is completed, the line stays flat and masks both |
| **Burnup** | Completed work AND total scope over time | Makes scope creep visible as the total line moves up; clearly shows both progress and scope changes | Slightly more complex to read |

**Prefer burnup for release tracking.** The ability to see scope changes is critical for honest stakeholder communication. Burndown charts are acceptable for sprint-level tracking where scope is fixed.
