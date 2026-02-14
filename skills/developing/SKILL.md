---
name: developing
description: Executes the implementation phase of the development workflow, writing code based on an approved plan.
---

# Developing Skill

Handles the code implementation phase of the development workflow. Receives an approved plan and translates it into working code.

## Usage

This skill is invoked during `Step 6: Planning Execution` of the Development Workflow.

## Process

1. Read the approved plan to understand scope and requirements.
2. Run `python3 scripts/frontmatter_content_evaluation.py` to acquire project knowledge.
3. Identify the files that need to be created or modified.
4. Implement changes following the project's code style and patterns.
5. Ensure backward compatibility unless the plan explicitly requires breaking changes.
6. Validate that all changes align with the approved plan.

## Rules

- Follow the project's existing code style and conventions.
- Prefer editing existing files over creating new ones.
- Do not over-engineer — implement only what the plan specifies.
- Do not add features, refactoring, or improvements beyond scope.
- Always read a file before modifying it.
