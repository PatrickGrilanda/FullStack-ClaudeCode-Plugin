---
key: review-performance
summary: 7 performance anti-patterns with detection methods and fixes
---

# Domain 8: Performance Anti-Patterns

| Anti-Pattern | Detection in Review | Fix |
|---|---|---|
| **N+1 Queries** | Loop executing DB queries; ORM lazy-loading inside iterations | Eager loading (JOIN, INCLUDE), batch loading (DataLoader) |
| **Unnecessary Re-renders (React)** | Components without `React.memo`; new object/array/function refs on every render; missing dependency arrays | `React.memo`, `useMemo`, `useCallback`, state colocation |
| **Memory Leaks** | `setInterval`/`setTimeout` without cleanup; event listeners without removal; `useEffect` without cleanup; growing collections without bounds | Cleanup functions, `WeakRef`/`WeakMap`, listener removal on unmount |
| **Sync I/O in Async Context** | `fs.readFileSync` in Express handler; blocking HTTP calls in event loop; `time.sleep()` in `async def` | Async alternatives (`fs.promises`, `aiohttp`, async DB drivers) |
| **Excessive Object Creation** | Object creation in tight loops; string concatenation in loops; repeated Regex/Date creation | Object pooling, pre-allocation, caching, `StringBuilder`/`join` |
| **Missing Indexes** | New queries with WHERE on non-indexed columns; ORDER BY on non-indexed columns; JOINs on non-indexed FKs | Add indexes for frequently queried columns; composite indexes |
| **Unbounded Queries** | `SELECT *` without LIMIT; API endpoints without pagination; `findAll()` without size constraint | Always enforce pagination; set maximum page sizes |
