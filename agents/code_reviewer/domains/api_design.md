---
key: review-api-design
summary: REST conventions, HTTP status code accuracy, pagination patterns, idempotency
---

# Domain 10: API Design Review

## RESTful Conventions Checklist

| Convention | Correct | Incorrect |
|---|---|---|
| Nouns, not verbs | `/users`, `/orders` | `/getUsers`, `/createOrder` |
| Plural resource names | `/users/123` | `/user/123` |
| Nested for relationships | `/users/123/orders` | `/getUserOrders?userId=123` |
| Hyphens for readability | `/user-profiles` | `/user_profiles` |
| Query params for filtering | `/users?role=admin` | `/users/role/admin` |

## HTTP Status Code Accuracy

| Common Mistake | Correct Usage |
|---|---|
| 200 for everything (hiding errors in body) | Use appropriate error codes (400, 401, 403, 404, 422, 500) |
| Confusing 401 vs 403 | 401 = "who are you?" (login required), 403 = "I know who you are, but no" |
| Using 404 for validation errors | 404 = resource doesn't exist, 422 = data is invalid |
| Not using 201 for POST creation | POST that creates -> 201 with Location header |
| 200 with error body | `{"status": 200, "error": "Failed"}` is an anti-pattern |

## Pagination Review
- Offset-based: Simple but degrades at high offsets. Check for max page size enforcement.
- Cursor-based: Scalable, consistent. Check for opaque cursors (base64). Check for `hasMore` indicator.
- Keyset-based: Efficient for time-series. Requires unique sequential key.

## Idempotency
- GET, PUT, DELETE are naturally idempotent
- POST is NOT -- check for `Idempotency-Key` header pattern on mutation endpoints
- PATCH is usually not idempotent -- depends on implementation
