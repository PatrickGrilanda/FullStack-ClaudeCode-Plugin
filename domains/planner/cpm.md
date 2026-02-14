---
key: planner-cpm
summary: Critical Path Method with forward/backward pass formulas and schedule compression
---

# Domain 2: Critical Path Method (CPM)

## Forward Pass (Earliest Start/Finish)
```
ES (first task) = 0
EF = ES + Duration
ES (successor) = MAX(EF of all predecessors)
```

The forward pass calculates the earliest possible start and finish for each activity by moving left-to-right through the network diagram. When an activity has multiple predecessors, its earliest start is the MAXIMUM of all predecessor earliest finishes.

## Backward Pass (Latest Start/Finish)
```
LF (last task) = EF of project
LS = LF - Duration
LF (predecessor) = MIN(LS of all successors)
```

The backward pass calculates the latest allowable start and finish for each activity by moving right-to-left. When an activity has multiple successors, its latest finish is the MINIMUM of all successor latest starts.

## Float Calculation
```
Total Float = LF - EF = LS - ES
Free Float = MIN(ES of successors) - EF
```

- **Total Float:** How much an activity can be delayed without delaying the project end date.
- **Free Float:** How much an activity can be delayed without delaying any successor activity.

**Critical Path = the path where Total Float = 0.** This is the longest path through the network and determines the minimum project duration.

## Key Properties
- Delaying ANY critical path activity delays the entire project
- Multiple critical paths can exist simultaneously (all have float = 0)
- Adding resources to a critical path activity CAN shorten the project (crashing)
- The critical path can CHANGE as the project progresses -- always recalculate after significant schedule changes

## Schedule Compression Techniques

| Technique | Description | Risk |
|---|---|---|
| **Crashing** | Add resources to critical path activities to reduce their duration | Increased cost; diminishing returns after a point (Brooks's Law for software) |
| **Fast-Tracking** | Run sequential activities in parallel (overlap them) | Increased risk of rework; only works for activities with discretionary dependencies |

**When to use which:**
- **Crashing:** When budget is flexible but deadline is fixed. Start with activities that have the lowest crash cost per unit of time saved.
- **Fast-Tracking:** When budget is fixed but schedule needs compression. Only possible for activities with discretionary (soft) dependencies.
