---
name: wireframing
description: Creates wireframe specifications for UI components and pages based on requirements and design decisions.
---

# Wireframing Skill

Handles wireframe creation during `Step 8: Wireframe Creation` of the Development Workflow.

## Usage

1. Run `python3 scripts/frontmatter_content_evaluation.py` to acquire design context from project knowledge.
2. Read the **Layout Concepts** section from the theme's `design.md` in `app_knowledge/`. This section is produced by Step 7 (Design Reference Research) and is the mandatory foundation for wireframe creation.
3. Read the relevant `requirements.md` from the theme in `app_knowledge/`.
4. Create wireframe specifications based on the layout concepts AND the requirements.

## Output Format

For each wireframe, provide:

### Layout Structure
- Component hierarchy and nesting
- Grid/flex layout specifications
- Spacing and alignment rules

### Component Specifications
- Component type and purpose
- Content placeholders
- Interactive states (default, hover, active, disabled)

### Responsive Behavior
- Breakpoints and layout changes
- Component visibility per viewport
- Stacking and reflow behavior

### Interaction Details
- User actions and expected responses
- Navigation flows
- Form validation feedback

## Rules

- NEVER create wireframes without first reading the Layout Concepts from `design.md` — the concepts produced in Step 7 are mandatory input.
- Always start from requirements — never design without understanding the need.
- Follow existing design system patterns if one exists.
- Document accessibility considerations for each component.
- Persist wireframe specs in the theme's `design.md` file in `app_knowledge/` (after the Layout Concepts section).
