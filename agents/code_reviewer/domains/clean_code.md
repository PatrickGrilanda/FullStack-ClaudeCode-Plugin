---
key: review-clean-code
summary: Robert C. Martin clean code principles covering functions, naming, Law of Demeter, YAGNI
---

# Domain 6: Clean Code Principles (Robert C. Martin)

## Function Rules

| Rule | Threshold |
|---|---|
| **Size** | Max ~20 lines, ideally 5-10 |
| **Do One Thing** | Functions do one thing, do it well, do it only |
| **One Level of Abstraction** | Don't mix high-level business logic with low-level string manipulation |
| **Arguments** | 0 (ideal), 1-2 (acceptable), 3 (questionable), >3 (never) |
| **No Side Effects** | Don't do hidden things (mutate global state, modify args unexpectedly) |
| **Command-Query Separation** | Functions either DO something or ANSWER something, never both |

## Naming Rules

| Rule | Example |
|---|---|
| Intention-Revealing | `elapsedTimeInDays` NOT `d` |
| Avoid Disinformation | Don't use `accountList` if it's not a List |
| Meaningful Distinctions | Never `a1`, `a2`, `data`, `info` as distinguishers |
| Searchable Names | Single-letter names only for short-scope loop counters |
| Class Names = Nouns | `Customer`, `Account`, `AddressParser` |
| Method Names = Verbs | `save`, `deletePage`, `postPayment` |
| One Word Per Concept | Pick `fetch` or `retrieve` or `get` -- not all three |

## Law of Demeter
A method should only call methods on: the object itself (`this`), objects passed as parameters, objects it creates, its direct component objects (fields).

**Violation:** `a.getB().getC().doSomething()` -- "train wreck" / message chain.

## YAGNI (You Aren't Gonna Need It)
- Don't add functionality until needed
- Don't create abstractions "just in case"
- Delete speculative code immediately
- Build the simplest thing that works today
