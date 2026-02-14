---
key: planner-wbs
summary: Work Breakdown Structure with 100% Rule, 8/80 Rule, and decomposition process
---

# Domain 1: Work Breakdown Structure (WBS)

## The 100% Rule
The total scope of work at any level MUST equal 100% of the work represented by its parent. Nothing missing, nothing extra. This is the most important principle of WBS construction -- every child level must completely represent all the work of its parent, and no work should appear at a child level that is not represented in the parent.

## The 8/80 Rule
Work packages (lowest-level WBS elements) should be estimable between **8 and 80 hours** of effort. Smaller than 8h = over-decomposed (micro-management territory). Larger than 80h = needs further breakdown (too vague to estimate or assign reliably).

## Decomposition Process
1. Start with the project deliverable (Level 0)
2. Identify major deliverables (Level 1): what are the main outputs?
3. Break each deliverable into sub-deliverables (Level 2)
4. Continue decomposition until work packages fall within the 8-80 hour range
5. **Validate:** does the sum of children = 100% of parent at EVERY level?

At each level, ask: "Is this decomposed enough that a single person/team can own it and estimate it with confidence?" If no, decompose further. If yes, stop.

## WBS Numbering Convention
```
1.0 Project
  1.1 Deliverable A
    1.1.1 Sub-deliverable A1
    1.1.2 Sub-deliverable A2
  1.2 Deliverable B
    1.2.1 Sub-deliverable B1
    1.2.2 Sub-deliverable B2
```

The numbering scheme provides traceability -- every work package can be traced back to its parent deliverable and ultimately to the project objective.

## Common WBS Mistakes to Avoid
- **Listing activities instead of deliverables** -- WBS captures WHAT (deliverables/outcomes), not HOW (activities/tasks). Activities belong in the schedule, not the WBS.
- **Exceeding 5-7 levels of depth** -- Diminishing returns beyond this depth. If you need more levels, the project scope may need re-evaluation.
- **Work packages that can't be assigned** to a single team or person -- If a work package requires multiple unrelated teams, it needs further decomposition.
- **Missing the 100% rule** at any level -- The most common and most dangerous error. Always verify that children fully represent (and don't exceed) the parent scope.
