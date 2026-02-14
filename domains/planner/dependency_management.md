---
key: planner-dependencies
summary: 4 logical relationships, dependency nature types, leads and lags, validation rules
---

# Domain 9: Dependency Management

## Four Logical Relationships

| Type | Code | Definition | Frequency |
|---|---|---|---|
| **Finish-to-Start** | FS | B cannot start until A finishes | ~90% of dependencies |
| **Start-to-Start** | SS | B cannot start until A starts (can run in parallel after) | Common for parallel work |
| **Finish-to-Finish** | FF | B cannot finish until A finishes | Moderately common |
| **Start-to-Finish** | SF | B cannot finish until A starts | Very rare (avoid unless truly necessary) |

**Default assumption:** If the relationship type is not specified, assume **Finish-to-Start (FS)** as it is by far the most common.

## Dependency Nature

| Type | Flexibility | Example |
|---|---|---|
| **Mandatory (Hard)** | None -- cannot be changed without violating logic or regulations | Must get regulatory approval before launch; must compile before testing |
| **Discretionary (Soft)** | Flexible -- can be modified based on best practices or preferences | Prefer design before development (could overlap with risk) |
| **External** | Uncontrollable -- depends on factors outside the team | Waiting for vendor delivery, third-party API availability, client feedback |

## Leads and Lags
- **Lead:** Successor starts before predecessor finishes (negative lag). Example: Start testing a module when coding is 80% complete. Saves time but increases rework risk.
- **Lag:** Forced delay between predecessor and successor. Example: Wait 24 hours after deployment before running load tests (environment stabilization).

## Validation Rules

These MUST be verified for every dependency graph:

1. **No circular dependencies** -- A topological sort must be possible. If activities form a cycle (A depends on B, B depends on C, C depends on A), the schedule is invalid. Use topological sorting to detect and break cycles.

2. **Every activity (except first and last) has both a predecessor AND a successor.** An activity without a predecessor is a "dangling start" (may start at wrong time). An activity without a successor is a "dangling end" (its completion does not contribute to project finish).

3. **Review discretionary dependencies for fast-tracking opportunities.** Before finalizing the schedule, examine every discretionary (soft) dependency and ask: "Could these overlap partially?" This is the primary source of schedule compression via fast-tracking.
