---
key: planner-moscow
summary: MoSCoW prioritization with 60% Rule and challenge test for Must Haves
---

# Domain 8: MoSCoW Prioritization

## Categories

| Category | Definition | Consequence if Missing |
|---|---|---|
| **Must Have** | Non-negotiable. Without these, the release fails or is unusable. | System is unusable or non-compliant |
| **Should Have** | Important but not vital. Solution works without them, but with pain or workarounds. | Significant value loss but system functions |
| **Could Have** | Desirable. "Nice to have." Less impact if left out. | Minor value loss |
| **Won't Have (this time)** | Explicitly out of scope for this iteration. May be reconsidered in future. | None (intentionally excluded) |

## The 60% Rule

**Must Haves MUST NOT exceed 60% of total effort** for the timeboxed period. This leaves a 40% buffer distributed across Should Haves (~20%) and Could Haves (~20%).

The 40% buffer serves two purposes:
1. **Schedule protection:** If Must Haves take longer than estimated (which they often do -- see Planning Fallacy), the buffer absorbs the overrun without missing the deadline.
2. **Value maximization:** If Must Haves finish on time, Should Haves and Could Haves deliver additional value within the same timebox.

## Challenge Test for Must Haves

Ask: **"What happens if we don't deliver this?"**

| Answer | Classification |
|---|---|
| "The system is unusable" | **Must Have** |
| "We face legal or contractual consequences" | **Must Have** |
| "It's inconvenient but users can work around it" | **Should Have** |
| "Users would like it but won't miss it much" | **Could Have** |
| "We want it eventually but not now" | **Won't Have** |

## Red Flag

**If >60% of items are classified as Must Have, the prioritization has failed.**

This typically means:
- Stakeholders are inflating priority to ensure their items get built
- The team has not pushed back hard enough on "everything is critical"
- The scope needs renegotiation

Action: Push back, re-apply the challenge test rigorously, and escalate to the user if consensus cannot be reached.
