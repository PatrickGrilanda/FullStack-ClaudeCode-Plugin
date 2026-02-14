---
name: identify-stack
description: Identifies the project's technology stack with versions by running the identify_stack.py script, and annotates CLAUDE.md with documentation links for Context7 consultation.
---

# Identify Stack Skill

Identifies the complete technology stack of a project including languages, frameworks, databases, infrastructure, and testing tools — with emphasis on **versions**. Maps all detected technologies to their Context7 documentation IDs for agent consultation.

## Usage

Run the identification script pointing to the target project:

```bash
python3 scripts/identify_stack.py /path/to/target/project
```

Or set the `PROJECT_ROOT` environment variable:

```bash
PROJECT_ROOT=/path/to/target/project python3 scripts/identify_stack.py
```

## What the script analyzes

| File | Language/Framework |
|---|---|
| `package.json` | Node.js, React, Vue, Next.js, Angular, Svelte, NestJS, etc. |
| `composer.json` | PHP, Laravel, Symfony, etc. |
| `requirements.txt` / `pyproject.toml` | Python, Django, Flask, FastAPI, etc. |
| `Gemfile` | Ruby, Rails, etc. |
| `go.mod` | Go, Gin, Echo, Fiber, etc. |
| `Cargo.toml` | Rust, Actix, Tokio, Axum, etc. |
| `docker-compose.yml` | PostgreSQL, MySQL, MongoDB, Redis (with versions from image tags) |
| `tsconfig.json` | TypeScript |
| `tailwind.config.*` | TailwindCSS |
| `vite.config.*` | Vite |
| `*lock*` files | Package manager detection (npm, yarn, pnpm, bun, poetry) |

## Output format

The script returns JSON with:

```json
{
  "languages": [{"name": "PHP", "version": "^8.2"}],
  "frameworks": [],
  "databases": [{"name": "PostgreSQL", "version": "16"}],
  "infrastructure": [{"name": "Docker Compose", "services": {...}}],
  "all_dependencies": {"npm": {...}, "composer": {...}},
  "documentation_links": [
    {
      "technology": "laravel",
      "detected_as": "laravel/framework",
      "context7_id": "/laravel/framework",
      "documentation_url": "https://laravel.com/docs"
    }
  ]
}
```

## MANDATORY: Annotate CLAUDE.md after identification

After running the script, the agent MUST update the `### Development Environment Quirks` section in `CLAUDE.md` with:

1. **Detected stack summary** with exact versions.
2. **Context7 documentation links** for every detected technology, formatted as:

```markdown
### Development Environment Quirks

#### Technology Stack
- **PHP:** ^8.2
- **Laravel:** ^11.0
- **PostgreSQL:** 16
- **Node.js:** ^20
- **React:** ^18.2.0
- **TailwindCSS:** ^3.4

#### Context7 Documentation References
Use these IDs with the `resolve-library-id` and `query-docs` Context7 tools:
- Laravel: `/laravel/framework` — https://laravel.com/docs
- React: `/facebook/react` — https://react.dev
- TailwindCSS: `/tailwindlabs/tailwindcss` — https://tailwindcss.com/docs
- PostgreSQL: `/postgres/postgres` — https://www.postgresql.org/docs
```

This ensures all agents can consult the correct documentation via Context7 during any workflow step.

## Rules

1. ALWAYS run the script — never guess the stack manually.
2. ALWAYS emphasize **versions** in the output.
3. ALWAYS annotate `CLAUDE.md` with the documentation links after identification.
4. If the script finds no config files, inform the user that the project root may be incorrect.
5. The Context7 IDs in `documentation_links` should be used with `mcp__plugin_context7_context7__resolve-library-id` and `mcp__plugin_context7_context7__query-docs` tools.
