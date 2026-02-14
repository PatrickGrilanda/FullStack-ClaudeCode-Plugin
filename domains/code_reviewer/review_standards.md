---
key: review-standards
summary: Google Engineering Practices code review standards with Conventional Comments framework
---

# Domain 4: Code Review Standards (Google Engineering Practices)

## The Standard of Review
> "A CL (changelist) should be approved if it definitely improves the overall code health of the system being worked on, even if the CL is not perfect."

**Key principles:**
- No code is "perfect" -- approve if it improves health
- Technical facts and data override personal preference
- Reviewers should not block for style preferences that are within the style guide
- Reviewers should seek to **unblock** the developer, not gatekeep
- Speed matters: respond to review requests within **one business day**

## What to Look For (Google's Checklist)
1. **Design:** Is the code well-designed and appropriate for the system?
2. **Functionality:** Does it behave as intended? Edge cases?
3. **Complexity:** Could it be simpler? Will other developers understand it easily?
4. **Tests:** Are tests correct, sensible, and useful?
5. **Naming:** Are names clear and follow conventions?
6. **Comments:** Are comments clear, useful, and explain WHY not WHAT?
7. **Style:** Does it follow the style guide?
8. **Documentation:** Was relevant documentation updated?

## How to Write Comments (Conventional Comments Framework)

| Label | Meaning | Blocking? |
|---|---|---|
| `praise:` | Highlight something good | No |
| `nitpick:` | Trivial, preference-based | No |
| `suggestion:` | Propose improvement | Non-blocking by default |
| `issue:` | Identify a problem | Blocking by default |
| `question:` | Seeking clarification | Non-blocking |
| `thought:` | An idea sparked by review | Non-blocking |
| `chore:` | Cleanup/maintenance task | Non-blocking |

Format: `<label> [decorations]: <subject>` + `[discussion]`
