---
name: frontmatter-evaluation
description: Evaluates and returns frontmatters from memory/ and app_knowledge/ files so agents can select the correct theme without reading full contents.
---

# Frontmatter Evaluation Skill

This skill scans `memory/` and `app_knowledge/` directories and returns the frontmatter metadata (`key` + `summary`) of all knowledge files.

## Usage

Run the evaluation script:

```bash
python3 scripts/frontmatter_content_evaluation.py
```

To filter by directory:

```bash
python3 scripts/frontmatter_content_evaluation.py memory
python3 scripts/frontmatter_content_evaluation.py app_knowledge
```

## Directory Structures

### memory/ (flat files)

```
memory/
  project_stack.md
  architecture_overview.md
```

Each file has a frontmatter with `key` and `summary`.

### app_knowledge/ (theme folders with 3 files each)

```
app_knowledge/
  authentication/
    requirements.md    ← what is needed and why
    design.md          ← how it will be built
    decisions.md       ← what was decided and the impact
  payment_flow/
    requirements.md
    design.md
    decisions.md
```

Each theme is a folder. Inside each folder there are EXACTLY 3 files — no more, no less:

| File | Purpose |
|---|---|
| `requirements.md` | Business and technical requirements for the theme. What is needed and why. |
| `design.md` | Architecture, UI/UX, and technical design for the theme. How it will be built. |
| `decisions.md` | Decisions made, alternatives considered, trade-offs, and their impact on the project. |

## Output Format

```json
{
  "memory": {
    "directory": "/path/to/memory",
    "total_files": 2,
    "files": [
      {
        "file": "project_stack.md",
        "path": "/full/path/project_stack.md",
        "key": "stack",
        "summary": "Technology stack and framework choices",
        "has_frontmatter": true
      }
    ]
  },
  "app_knowledge": {
    "directory": "/path/to/app_knowledge",
    "total_themes": 1,
    "themes": [
      {
        "theme": "authentication",
        "path": "/full/path/authentication",
        "files": {
          "requirements": {
            "path": "/full/path/authentication/requirements.md",
            "key": "auth-requirements",
            "summary": "Authentication requirements and user stories",
            "has_frontmatter": true
          },
          "design": {
            "path": "/full/path/authentication/design.md",
            "key": "auth-design",
            "summary": "JWT-based auth architecture and flow diagrams",
            "has_frontmatter": true
          },
          "decisions": {
            "path": "/full/path/authentication/decisions.md",
            "key": "auth-decisions",
            "summary": "Why JWT over sessions, token refresh strategy",
            "has_frontmatter": true
          }
        }
      }
    ]
  }
}
```

## Frontmatter Format

Every `.md` file in `memory/` and `app_knowledge/` MUST have this frontmatter:

```yaml
---
key: unique-theme-identifier
summary: A concise one-line description of what this file contains
---
```

## Rules

1. Agents MUST call this skill BEFORE reading any file in `memory/` or `app_knowledge/`.
2. Use the `key`, `summary`, and `theme` fields to identify the correct content for the current topic.
3. Only after identifying the correct theme should the agent read the specific files it needs.
4. When creating a new theme, the agent MUST create the folder AND all 3 files with proper frontmatter.
5. A theme folder can ONLY contain `requirements.md`, `design.md`, and `decisions.md`.
