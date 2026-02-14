---
name: push
description: Pushes committed changes to the remote repository after validating branch state and remote tracking.
---

# Push Skill

Handles pushing committed changes to the remote repository during `Step 14: Push to Remote Repository` of the Development Workflow.

## Usage

1. Verify the current branch and its remote tracking status.
2. Check for unpushed commits.
3. Push to the remote with appropriate flags.

## Process

```bash
# 1. Check current branch
git branch --show-current

# 2. Check remote tracking
git status -sb

# 3. Push (with -u if no upstream is set)
git push -u origin <branch-name>
```

## Rules

- NEVER force push (`--force`) unless explicitly requested by the user.
- NEVER push directly to `main` or `master` without user confirmation.
- Always verify there are commits to push before attempting.
- If the branch has no upstream, use `-u` to set tracking.
- If push fails due to diverged history, inform the user and ask how to proceed.
