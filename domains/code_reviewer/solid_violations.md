---
key: review-solid
summary: SOLID principle violation detection indicators with SRP-first analysis strategy
---

# Domain 2: SOLID Principle Violations

| Principle | Violation Indicators |
|---|---|
| **S -- Single Responsibility** | Class changed for multiple unrelated reasons; class name is vague (Manager, Handler, Utils, Helper); class has methods spanning multiple domains |
| **O -- Open/Closed** | Adding a new type requires modifying existing code (adding cases to switch/if-else); no abstraction point for extension |
| **L -- Liskov Substitution** | Subclass throws exceptions the parent doesn't; subclass overrides methods to no-op; subclass strengthens preconditions or weakens postconditions |
| **I -- Interface Segregation** | Interface with many methods where implementors leave some empty; "fat interfaces" forcing unnecessary implementation |
| **D -- Dependency Inversion** | High-level modules importing concrete low-level modules directly; `new ConcreteClass()` inside business logic; no constructor injection or DI container |

**Detection formula:** If a class violates SRP, it will almost certainly violate OCP too (changes to one responsibility risk breaking another). Start SRP checks first.
