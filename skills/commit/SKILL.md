---
name: commit
description: Creates a well-structured git commit with conventional commit messages based on staged changes.
---

# Commit Skill

Creates a git commit following conventional commit standards. Analyzes staged changes to generate an appropriate commit message.

## Usage

1. Run `git status` to identify changed files.
2. Run `git diff --staged` to understand the staged changes.
3. Run `git log --oneline -5` to follow the repository's commit message style.
4. Draft a commit message that summarizes the **why** rather than the **what**.
5. Stage relevant files by name (avoid `git add .` or `git add -A`).
6. Create the commit.

## Commit Message Format

```
<type>(<scope>): <short description>

<optional body explaining why the change was made>

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

### Types
- `feat`: new feature
- `fix`: bug fix
- `refactor`: code refactoring without behavior change
- `docs`: documentation changes
- `test`: adding or updating tests
- `chore`: maintenance tasks, dependency updates
- `style`: formatting, whitespace changes

## Rules

- NEVER commit files that may contain secrets (`.env`, credentials, keys).
- NEVER use `git add .` or `git add -A` — always stage files by name.
- NEVER amend previous commits unless explicitly requested.
- NEVER skip pre-commit hooks unless explicitly requested.
- Always use a HEREDOC to pass the commit message.
