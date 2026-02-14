---
key: review-error-handling
summary: Exception hierarchy, 6 anti-patterns with detection, retry and circuit breaker patterns
---

# Domain 9: Error Handling Patterns

## Proper Exception Hierarchy
```
ApplicationError (base)
+-- ValidationError (400)
+-- AuthenticationError (401)
+-- AuthorizationError (403)
+-- NotFoundError (404)
+-- ConflictError (409)
+-- InfrastructureError (500)
    +-- DatabaseError
    +-- ExternalServiceError
```

## Error Handling Anti-Patterns to Flag

| Anti-Pattern | Detection | Severity |
|---|---|---|
| **Empty Catch (Swallowing)** | Catch block with only `pass`, `return`, or `continue` | HIGH -- silent failures are dangerous |
| **Catching Too Broadly** | `catch (Exception)`, bare `except:`, `catch (Throwable)` | MEDIUM -- catches programming errors too |
| **Log and Throw** | Catch that both logs AND re-throws the same exception | LOW -- duplicate logging, polluted logs |
| **Exceptions as Flow Control** | try/catch for expected, non-exceptional cases | MEDIUM -- use `if` check instead |
| **Destructive Wrapping** | New exception thrown without passing original as cause | HIGH -- loses original stack trace |
| **Returning Null on Error** | Catch that returns null/empty without distinguishing error from "not found" | MEDIUM -- caller can't differentiate |

## Retry & Circuit Breaker Patterns
- **Retry:** Max 3-5 attempts. Only idempotent operations. Only transient errors (timeouts, 503s), NOT client errors (400, 422). Exponential backoff with jitter.
- **Circuit Breaker:** Closed (normal) -> Open (fail fast) -> Half-Open (testing). Params: failureThreshold, successThreshold, timeout.
