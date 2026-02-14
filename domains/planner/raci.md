---
key: planner-raci
summary: RACI Matrix with validation rules ensuring exactly one Accountable per task
---

# Domain 7: RACI Matrix

## Role Definitions

| Role | Definition | Rule |
|---|---|---|
| **R** (Responsible) | Does the work -- the person or team who performs the task | One or more per task |
| **A** (Accountable) | Ultimate decision-maker and sign-off authority -- the person who answers for the outcome | **Exactly ONE per task** (non-negotiable) |
| **C** (Consulted) | Provides input before or during the work (two-way communication) | Limit to 2-3 per task |
| **I** (Informed) | Kept updated after the fact (one-way communication) | As needed |

## Validation Rules

These rules MUST be checked for every RACI matrix before it is considered complete:

1. **Every task must have exactly one A (Accountable) and at least one R (Responsible).** A task without an Accountable has no decision-maker. A task without a Responsible has no one doing the work.

2. **No single person should be A on everything.** This is a bottleneck signal -- one person being accountable for all tasks means they become the single point of failure and decision bottleneck.

3. **No column should be all I's.** If a person is only Informed on every task, they are unnecessarily involved in the project and should be removed from the matrix.

4. **Too many C's per task = decision paralysis.** Every Consulted person adds communication overhead and can slow down decisions. Limit to 2-3 per task. If more input is needed, consider a workshop rather than individual consultation.

5. **A can also be R, but this must be explicit.** The Accountable person may also do the work (common in small teams), but this should be a conscious choice, not an accident. Mark as "A/R" in the matrix.

## Anti-patterns to Watch For
- **Everyone is R:** No clear ownership -- work falls through cracks
- **Multiple A's per task:** Diffused accountability means no accountability
- **No one is C on complex tasks:** Decisions made without necessary expertise
- **Stakeholder listed but no role assigned:** Remove them or assign a role
