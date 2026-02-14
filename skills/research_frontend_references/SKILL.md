---
name: research-frontend-references
description: Researches frontend design references, UI patterns, and component libraries for inspiration and best practices.
---

# Research Frontend References Skill

Researches frontend design references, UI patterns, and component inspiration to inform design and implementation decisions.

## Usage

1. Run `python3 scripts/frontmatter_content_evaluation.py` to check existing design knowledge.
2. Understand the requirements and design context for the feature being built.
3. Research relevant references.

## What to research

| Category | Examples |
|---|---|
| UI Patterns | Navigation, forms, data tables, dashboards, onboarding flows |
| Component Libraries | Shadcn, Radix, Material UI, Ant Design, Chakra UI |
| Design Systems | Design tokens, typography scales, color systems, spacing |
| Accessibility | WCAG patterns, ARIA roles, keyboard navigation |
| Responsive Patterns | Mobile-first, adaptive layouts, breakpoint strategies |
| Animation/Interaction | Micro-interactions, transitions, loading states |

## Output

Provide a structured research summary:
- **References found** — links and descriptions of relevant patterns.
- **Recommended approach** — which patterns best fit the project's needs.
- **Trade-offs** — pros and cons of each option.
- **Implementation notes** — practical considerations for the chosen approach.

## Rules

- Always relate research back to the project's specific requirements.
- Consider the existing tech stack when recommending component libraries.
- Persist research findings in the theme's `design.md` file in `app_knowledge/`.
