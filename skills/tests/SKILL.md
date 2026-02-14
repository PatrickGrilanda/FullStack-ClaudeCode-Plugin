---
name: tests
description: Creates and runs tests for the project based on the testing framework and conventions in use.
---

# Tests Skill

Handles test creation and execution during `Step 9: Test Creation` of the Development Workflow.

## Usage

1. Identify the project's testing framework and conventions.
2. Determine which code needs test coverage based on recent changes.
3. Write tests following existing patterns in the test suite.
4. Run the tests and report results.

## Process

1. Run `python3 scripts/frontmatter_content_evaluation.py` to check for existing testing conventions in project knowledge.
2. Examine existing test files to understand patterns, naming conventions, and structure.
3. Write tests covering:
   - Happy path scenarios
   - Edge cases and boundary conditions
   - Error handling paths
4. Run the test suite and verify all tests pass.

## Rules

- Follow the project's existing test patterns and naming conventions.
- Test behavior, not implementation details.
- Each test should be independent and not rely on execution order.
- Use descriptive test names that explain the scenario being tested.
- Do not mock what you don't own unless necessary.
