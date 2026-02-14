---
key: review-severity
summary: 5-level severity classification with blocking behavior and bug vs quality differentiation
---

# Domain 7: Severity Classification

## Severity Levels

| Level | Criteria | Examples | Action |
|---|---|---|---|
| **CRITICAL** | Security vulnerabilities, data loss/corruption, system crash, breaking API changes | SQL injection, race conditions corrupting state, exposed secrets | MUST fix. Blocks merge. |
| **HIGH** | Bugs in common cases, significant performance degradation, missing auth checks | N+1 on main page, incorrect business logic for normal flows | MUST fix. Blocks merge. |
| **MEDIUM** | Edge case errors, architectural violations, missing tests for new code, SOLID violations | Missing null check on optional field, no tests for happy path | Should fix. May block merge. |
| **LOW** | Code smells not affecting correctness, minor naming issues, documentation gaps | Long method (but correct), missing JSDoc on internal function | Should address. Does not block. |
| **NIT** | Style preferences, alternative names, import ordering | Prefer `userId` over `uid` | Optional. Author decides. |

## Bug vs. Code Quality Differentiation

| | Bug | Code Quality Issue |
|---|---|---|
| Impact | Incorrect behavior at runtime | Maintainability/readability |
| Urgency | Must fix before release | Can address iteratively |
| Testing | Caught by tests | Often not caught by tests |
| Typical severity | Critical/High | Medium/Low/Nit |
