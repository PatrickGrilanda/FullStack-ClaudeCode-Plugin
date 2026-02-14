---
name: diagnosis
description: Diagnoses problems by analyzing data structures, consulting project memory, and examining the codebase.
---

# Diagnosis Skill

Performs problem diagnosis during `Step 3: Problem Diagnosis` of the Development Workflow. Combines data structure analysis, project memory consultation, and code examination.

## Usage

This skill executes three sub-steps that can run simultaneously:

### 3.1 Data Structure Analysis
- Examine relevant data models, schemas, and relationships.
- Identify structural issues that may cause the reported problem.

### 3.2 Consult Memory
- Run `python3 scripts/frontmatter_content_evaluation.py` to check existing knowledge.
- Read relevant theme files from `app_knowledge/` and `memory/`.
- Identify if this problem or similar issues have been documented before.

### 3.3 Problem Analysis
- Trace the issue through the codebase.
- Identify root cause vs. symptoms.
- Determine the scope of impact.

## Output

Provide a structured diagnosis with:
- **Root cause** — what is actually causing the problem.
- **Impact scope** — what parts of the system are affected.
- **Evidence** — specific code references and data supporting the diagnosis.
- **Recommended approach** — high-level direction for the fix.
