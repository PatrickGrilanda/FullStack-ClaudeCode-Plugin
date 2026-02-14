---
key: review-refactoring
summary: 8 refactoring patterns with detection triggers and application steps
---

# Domain 5: Refactoring Patterns

| Pattern | When to Apply | Detection |
|---|---|---|
| **Extract Method** | Code block is too long, has a clear logical purpose, or appears in multiple places | Comments explaining "what this block does"; deeply nested code |
| **Inline Method** | Method body is as clear as its name; just a simple delegation | One-line methods that wrap another call without adding clarity |
| **Extract Class** | Class has too many responsibilities; a subset of fields/methods form a cohesive group | Class > 200 lines; fields cluster into groups; vague class name |
| **Move Method** | Method uses more features of another class than its own (Feature Envy) | Count field/method accesses across classes |
| **Replace Conditional with Polymorphism** | Multiple if/else or switch dispatching behavior based on type | `switch(type)`, `if(obj instanceof X)`, repeated type-checking |
| **Introduce Parameter Object** | Same 3+ parameters appear in multiple method signatures | Methods with 4+ parameters; same parameter groups recurring |
| **Replace Magic Number with Named Constant** | Numeric literal without explanation; same magic number in multiple places | Any non-obvious literal that isn't 0 or 1 |
| **Decompose Conditional** | Complex conditional logic hard to follow | Long if-condition spanning multiple lines; nested conditionals |
