---
key: business-bpmn
summary: BPMN key elements, gateway types, and As-Is to To-Be process mapping methodology
---

## BPMN (Business Process Model and Notation)

### Key Elements

| Element | Symbol | Purpose |
|---|---|---|
| **Start Event** | Thin circle | Triggers the process |
| **End Event** | Thick circle | Concludes the process |
| **Task** | Rounded rectangle | Single unit of work |
| **Exclusive Gateway (XOR)** | Diamond with X | Decision -- only ONE path taken (if/else) |
| **Parallel Gateway (AND)** | Diamond with + | ALL paths taken simultaneously (fork/join) |
| **Inclusive Gateway (OR)** | Diamond with circle | ONE OR MORE paths taken |
| **Sequence Flow** | Solid arrow | Order of activities within a process |
| **Message Flow** | Dashed arrow | Messages between separate participants (across pools) |
| **Pool/Lane** | Container | Participant/role responsible for activities |

### As-Is to To-Be Process Mapping

1. **As-Is:** Map what ACTUALLY happens (not what should happen). Validate with process participants. Mark bottlenecks, redundancies, handoff problems.
2. **To-Be:** Eliminate unnecessary steps, automate manual tasks, parallelize sequential activities, reduce handoffs.
3. **Gap Analysis:** Compare side by side. Document what changes, what stays, what resources are needed for transition.
