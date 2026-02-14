---
key: review-code-smells
summary: Martin Fowler's code smell taxonomy organized in 5 categories with detection thresholds
---

# Domain 1: Code Smell Taxonomy (Martin Fowler)

Code smells are surface indicators of deeper design problems. Organized by category:

## Bloaters (Code that has grown too large)

| Smell | Detection | Threshold |
|---|---|---|
| **Long Method** | Method exceeds readable size | > 20 lines (flag), > 50 lines (critical) |
| **Large Class** | Class has too many responsibilities | > 200 lines or > 10 methods or > 7 fields |
| **Long Parameter List** | Too many parameters | > 3 parameters |
| **Primitive Obsession** | Using primitives instead of small objects | Money as float, phone as string, ZIP as int |
| **Data Clumps** | Same group of fields/parameters appearing together | 3+ fields that always travel together |

## Object-Orientation Abusers

| Smell | Detection |
|---|---|
| **Switch Statements** | switch/if-else chains dispatching on type (should use polymorphism) |
| **Refused Bequest** | Subclass inherits but doesn't use most parent methods/properties |
| **Feature Envy** | Method uses more features of another class than its own |
| **Inappropriate Intimacy** | Two classes access each other's private details excessively |

## Change Preventers

| Smell | Detection |
|---|---|
| **Divergent Change** | One class is changed for multiple unrelated reasons (violates SRP) |
| **Shotgun Surgery** | One change requires edits across many classes |
| **Parallel Inheritance Hierarchies** | Creating a subclass in one hierarchy requires creating one in another |

## Dispensables

| Smell | Detection |
|---|---|
| **Dead Code** | Unreachable code, unused variables/parameters/methods |
| **Speculative Generality** | Abstractions created "just in case" with only one implementation |
| **Lazy Class** | Class does too little to justify its existence |
| **Duplicate Code** | Same or very similar code in 2+ places |
| **Comments (as smell)** | Comments explaining WHAT code does instead of code being self-explanatory |

## Couplers

| Smell | Detection |
|---|---|
| **Message Chains** | `a.getB().getC().doSomething()` -- Law of Demeter violation |
| **Middle Man** | Class that delegates almost everything to another class |
