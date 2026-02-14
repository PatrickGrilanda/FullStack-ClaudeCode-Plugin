---
key: planner-reference-class
summary: Kahneman's reference-class forecasting combating Planning Fallacy with outside view
---

# Domain 4: Reference-Class Forecasting (Kahneman & Tversky)

Combats the **Planning Fallacy** -- the systematic tendency to underestimate time, cost, and risks of planned actions while overestimating benefits.

## Evidence
- Daniel Kahneman's Nobel Prize research showed people instinctively use the **"inside view"** (focus on specifics of the current project, its unique features, and optimistic scenarios) rather than the **"outside view"** (look at how similar projects actually performed regardless of their initial plans).
- Bent Flyvbjerg's research across thousands of projects: **9 out of 10 infrastructure projects** had cost overruns. Average overrun: **28%**. IT projects fare even worse, with average schedule overruns of 33% and cost overruns of 27%.

## The Method
1. **Identify the reference class:** Find a set of similar past projects (same type, similar scope, comparable technology, similar team size)
2. **Establish the distribution:** What were the actual outcomes (durations, costs, defect rates) of those projects?
3. **Position the current project:** Where does the current project sit in that distribution? Is it simpler or more complex than average?
4. **Apply the adjustment:** Adjust your initial estimate based on the reference class data

## Practical Application
```
Your initial estimate: 6 weeks
Reference class of 10 similar projects:
  Average actual duration: 9.2 weeks
  Median: 8.5 weeks
  Range: 5-16 weeks
  % that finished within initial estimate: 20%

Adjusted estimate: 8.5-10 weeks (using median to average of reference class)
Buffer: 2.5-4 weeks above naive estimate
```

The adjustment uses the median-to-average range because:
- The **median** resists outlier influence (one 16-week disaster does not skew it)
- The **average** captures the full distribution including the common overruns

## Key Insight

The outside view is statistically superior to the inside view in virtually all studied contexts.

**ALWAYS check: "What happened when others tried something similar?"**

When no formal reference class data exists, use informal baselines: previous sprints, past features of similar complexity, industry benchmarks with cited sources. The key is to anchor on actual outcomes rather than optimistic plans.
