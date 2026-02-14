---
name: setup-project
description: Analyzes the target project and populates the empty sections of CLAUDE.md (Project Summary, Testing Instructions, Code Style, Architectural Decisions, Development Environment Quirks) with real, verified data.
---

# Setup Project Skill

Analyzes the target project's codebase to detect its technology stack, architecture, testing patterns, code style conventions, and development quirks — then populates the corresponding empty sections in `CLAUDE.md` with verified data.

This skill replaces the old `SessionStart` hooks. It is invoked **manually** by the user when setting up a new project or when `CLAUDE.md` sections need updating.

## Usage

```
/setup-project
```

Or with a specific project path:

```
/setup-project /path/to/target/project
```

If no path is provided, use the current working directory as the project root.

## Process

Execute the following 5 steps **in order**. Each step gathers data that the final step uses to write `CLAUDE.md`.

### Step 1: Identify Technology Stack

Run the stack identification script:

```bash
python3 scripts/identify_stack.py <project_root>
```

Capture the JSON output. This provides:
- Languages with versions
- Frameworks with versions
- Databases with versions
- Infrastructure (Docker, package managers)
- Context7 documentation links

### Step 2: Analyze Project Structure

Use `Glob`, `Read`, and `Grep` to detect:

**Project type:**
- Look for entry points: `src/index.*`, `app/Http/Kernel.php`, `main.*`, `server.*`, `index.html`
- Check for API routes: `routes/api.*`, `src/routes/*`, `app/api/*`
- Check for frontend: `src/App.*`, `pages/`, `views/`, `templates/`
- Determine: API-only, SPA, SSR, monolith, monorepo, CLI, library, etc.

**Architecture pattern:**
- Check directory structure for patterns:
  - `app/Models/`, `app/Controllers/`, `app/Views/` → MVC
  - `src/domain/`, `src/application/`, `src/infrastructure/` → Clean Architecture / DDD
  - `src/features/` or `src/modules/` → Feature-based
  - `packages/` or `apps/` → Monorepo
- Look for DI containers, service providers, middleware patterns
- Identify state management approach (Redux, Zustand, Context, Vuex, etc.)

**Key entry points:**
- Main application files
- Configuration files
- Route definitions
- Database migrations directory

### Step 3: Detect Testing Patterns

Search for test configuration and files:

**Config files to look for:**
- `jest.config.*`, `vitest.config.*`, `phpunit.xml*`, `pytest.ini`, `conftest.py`, `.rspec`, `cypress.config.*`, `playwright.config.*`

**Test directories:**
- `tests/`, `test/`, `__tests__/`, `spec/`, `cypress/`, `e2e/`

**Test scripts:**
- Read `package.json` → `scripts.test`, `scripts.test:*`
- Read `composer.json` → `scripts.test`
- Read `Makefile` or `Taskfile` for test targets

**Detect test types present:**
- Unit tests (files matching `*.test.*`, `*.spec.*`, `*Test.php`, `test_*.py`)
- Integration tests (files in `tests/integration/`, `tests/Feature/`)
- E2E tests (Cypress, Playwright, Selenium configs)

### Step 4: Detect Code Style

Search for linter and formatter configurations:

**Files to look for:**
- `.eslintrc.*`, `eslint.config.*` → ESLint rules
- `.prettierrc*`, `prettier.config.*` → Prettier config
- `biome.json`, `biome.jsonc` → Biome config
- `.editorconfig` → Editor conventions (indent style, size, charset)
- `pint.json`, `.php-cs-fixer.php` → PHP formatters
- `pyproject.toml` [tool.black], [tool.ruff] → Python formatters
- `.rubocop.yml` → Ruby linter
- `rustfmt.toml` → Rust formatter
- `.stylelintrc*` → CSS linter
- `tsconfig.json` → TypeScript strictness settings

**Extract from configs:**
- Indent style (tabs vs spaces) and size
- Quote style (single vs double)
- Semicolons (yes/no)
- Trailing commas
- Max line length
- Naming conventions (if configured in linter rules)

### Step 5: Populate CLAUDE.md

Read the current `CLAUDE.md` file. For each empty section, write **only verified data** gathered in Steps 1-4. Follow these rules strictly:

#### Section: Project Summary

Write a 2-4 sentence description based on:
- `package.json` → `name`, `description`
- `composer.json` → `name`, `description`
- `README.md` of the target project (first paragraph)
- Detected project type and main technologies

Format:
```markdown
## Project Summary

[Project name] is a [project type] built with [main technologies]. [Brief description of purpose based on README or package metadata].
```

#### Section: Testing Instructions

Format:
```markdown
### Testing Instructions

**Test framework(s):** [detected frameworks with versions]
**Test directory:** [detected test directories]

**Commands:**
- Run all tests: `[command from scripts]`
- Run specific test: `[framework-specific command]`

**Test types present:**
- [x] Unit tests — [location]
- [x] Integration tests — [location]
- [ ] E2E tests — not detected
```

If NO test configuration is found, write:
```markdown
### Testing Instructions

No test configuration detected. Testing setup is needed for this project.
```

#### Section: Code Style

Format:
```markdown
### Code Style

**Formatter:** [detected formatter]
**Linter:** [detected linter]

**Conventions:**
- Indentation: [tabs/spaces] ([size])
- Quotes: [single/double]
- Semicolons: [yes/no]
- Trailing commas: [style]
- Max line length: [number]
```

If NO style configuration is found, write:
```markdown
### Code Style

No linter or formatter configuration detected. Code style conventions are not enforced.
```

#### Section: Architectural Decisions

Format:
```markdown
### Architectural Decisions

**Architecture pattern:** [detected pattern]
**Project type:** [API / SPA / SSR / Monolith / Monorepo / etc.]

**Key structure:**
- Entry point: `[path]`
- Routes: `[path]`
- Models/Entities: `[path]`
- Controllers/Handlers: `[path]`
- Migrations: `[path]`

**State management:** [if frontend — detected approach]
**API pattern:** [REST / GraphQL / RPC / etc.]
```

#### Section: Development Environment Quirks

Use the output from Step 1 (identify_stack.py). Format:
```markdown
### Development Environment Quirks

#### Technology Stack
- **[Language]:** [version]
- **[Framework]:** [version]
- **[Database]:** [version]
- ...

#### Context7 Documentation References
Use these IDs with the `resolve-library-id` and `query-docs` Context7 tools:
- [Technology]: `[context7_id]` — [docs_url]
- ...
```

## Rules

1. **NEVER invent or assume data.** Every value written to `CLAUDE.md` must come from an actual file in the project. If a section cannot be determined from the codebase, state that explicitly (e.g., "No test configuration detected").
2. **ALWAYS run `identify_stack.py`** — never guess the stack manually.
3. **Preserve immutable sections.** Only populate the empty placeholder sections. Never modify workflow steps, non-negotiable rules, or any other existing content in `CLAUDE.md`.
4. **Only populate empty sections.** If a section already has content (not the placeholder text), do NOT overwrite it. Report to the user that the section already has content.
5. **Use the Section Population Rule.** Filling empty placeholder sections is an allowed "incorporation" under the CLAUDE.md rules — it is NOT an edit.
6. **Respect the Zero Deduction Policy.** If you cannot verify a data point, mark it as `[UNVERIFIED]` and ask the user.
