# FullStack ClaudeCode Plugin

A comprehensive multi-agent workflow plugin for [Claude Code](https://claude.com/claude-code) that orchestrates 16 specialized agents, 12 skills, and 4 output styles through structured Development and Business Analysis workflows.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Configuration](#configuration)
- [Plugin Structure](#plugin-structure)
- [Agents](#agents)
- [Skills](#skills)
- [Output Styles](#output-styles)
- [Workflows](#workflows)
- [Modular Domain Knowledge](#modular-domain-knowledge)
- [Knowledge Persistence](#knowledge-persistence)
- [License](#license)

## Overview

This plugin transforms Claude Code into a full development and business analysis platform. Instead of a single AI assistant, it provides a team of specialized agents that collaborate through defined workflows, each with deep domain expertise and structured output templates.

**Key features:**

- **16 specialized agents** covering the full software lifecycle — from request analysis to git management
- **12 invocable skills** for targeted tasks like committing, testing, diagnosing, and wireframing
- **4 output styles** that adapt the orchestrator's behavior to the current workflow phase
- **56 modular domain files** loaded on demand to optimize context window usage
- **Two structured workflows** — Development (14 steps) and Business Analysis (9 steps)
- **Zero Deduction Policy** — agents never fabricate data; they research, calculate, or ask
- **Knowledge persistence** — findings are saved across sessions in `app_knowledge/` and `memory/`

## Installation

### From Marketplace

```bash
claude plugin install fullstack-claudecode-plugins/fullstack-claudecode-plugin
```

### Manual Installation

Clone the repository into your Claude Code plugins directory:

```bash
git clone git@github.com:PatrickGrilanda/FullStack-ClaudeCode-Plugin.git
```

Then add it as a plugin in Claude Code:

```bash
claude plugin add /path/to/FullStack-ClaudeCode-Plugin
```

## Configuration

### MCP Servers

The plugin uses two MCP servers defined in `.mcp.json`:

| Server | Purpose |
|---|---|
| **Context7** | Provides up-to-date documentation for any library/framework via `@upstash/context7-mcp` |
| **Sequential Thinking** | Structured step-by-step reasoning via `@modelcontextprotocol/server-sequential-thinking` |

**Context7 requires an API key.** After installation, edit `.mcp.json` and replace the placeholder:

```json
{
  "context7": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_CONTEXT7_API_KEY_HERE"],
    "env": {}
  }
}
```

Get your free API key at [context7.com](https://context7.com).

Sequential Thinking works out of the box with no configuration needed.

### Session Hooks

The plugin includes two `SessionStart` hooks (defined in `hooks/hooks.json`) that run automatically when a new Claude Code session begins:

1. **CLAUDE.md Auto-Population** — Scans the project and fills empty sections in `CLAUDE.md` (Project Summary, Code Style, Architectural Decisions, etc.)
2. **Risk Analysis** — Analyzes development rules for inconsistencies that could cause agent issues and documents risks with mitigations

These hooks spawn separate Claude instances and require no manual configuration.

## Plugin Structure

```
.
├── .claude-plugin/
│   ├── plugin.json          # Plugin manifest
│   └── marketplace.json     # Marketplace configuration
├── agents/                  # 16 specialized agents
│   ├── business_analyst.md
│   ├── business_analyst/domains/   # 10 domain files
│   ├── code_reviewer.md
│   ├── code_reviewer/domains/      # 10 domain files
│   ├── devils_advocate.md
│   ├── devils_advocate/domains/    # 10 domain files
│   ├── planner.md
│   ├── planner/domains/            # 10 domain files
│   ├── product_growth.md
│   ├── product_growth/domains/     # 6 domain files
│   ├── security_analyst.md
│   ├── security_analyst/domains/   # 10 domain files
│   ├── data_structure_analyst.md
│   ├── dba.md
│   ├── developer.md
│   ├── devops_engineer.md
│   ├── git_manager.md
│   ├── request_analyst.md
│   ├── requirements_analyst.md
│   ├── tester.md
│   ├── ui_ux_analyst.md
│   └── wireframe_creator.md
├── skills/                  # 12 invocable skills
│   ├── commit/
│   ├── developing/
│   ├── diagnosis/
│   ├── experiment_design/
│   ├── frontmatter_evaluation/
│   ├── growth_audit/
│   ├── identify_stack/
│   ├── pricing_analysis/
│   ├── push/
│   ├── research_frontend_references/
│   ├── tests/
│   └── wireframing/
├── styles/                  # 4 output styles
│   ├── workflow.md
│   ├── planning.md
│   ├── review.md
│   └── research.md
├── scripts/                 # Utility scripts
│   ├── frontmatter_content_evaluation.py
│   └── identify_stack.py
├── hooks/
│   └── hooks.json           # Session hooks
├── app_knowledge/           # Theme-specific knowledge (runtime)
├── memory/                  # Project-wide knowledge (runtime)
├── commands/                # Command definitions
├── CLAUDE.md                # Workflow rules and constraints
├── .mcp.json                # MCP server configuration
└── .gitignore
```

## Agents

### Workflow Agents

| Agent | Role | Workflow Step |
|---|---|---|
| `request-analyst` | Decomposes and classifies user requests, identifies ambiguities and acceptance criteria | Step 2 |
| `requirements-analyst` | Elicits functional/non-functional requirements, creates user stories | Step 3 |
| `data-structure-analyst` | Analyzes data models, schemas, entity relationships, and state management | Step 3.1 |
| `planner` | Creates implementation plans with WBS, CPM, PERT, risk assessment, MoSCoW | Step 4 |
| `devils-advocate` | Challenges assumptions, identifies risks, cognitive biases, and blind spots | Steps 4-6 |
| `developer` | Implements code changes based on approved plans | Step 6 |
| `dba` | Database-specific analysis, schema design, query optimization | Step 6.1 |
| `devops-engineer` | Docker, CI/CD, deployment strategies, environment setup | Step 6.4 |
| `code-reviewer` | Code quality gate — bugs, SOLID, performance, error handling, API design | Step 6.5 |
| `security-analyst` | Security gate — OWASP, STRIDE, CVSS scoring, CWE mapping, ASVS | Step 6.5 |
| `ui-ux-analyst` | Usability review, design reference research, accessibility | Steps 7, 10 |
| `wireframe-creator` | Creates wireframe specifications from requirements and layout concepts | Step 8 |
| `tester` | Creates and executes tests for acceptance criteria validation | Step 9 |
| `product-growth` | AARRR metrics, growth loops, experimentation, unit economics, pricing | Step 4 (Business) |
| `business-analyst` | SWOT, Porter's, BMC, Lean Canvas, PESTLE, TAM/SAM/SOM | Step 4 (Business) |
| `git-manager` | Branch creation, commits, and pushes | Steps 12-14 |

### High-Expertise Agents (with Modular Domains)

Six agents have deep domain expertise organized into individually loadable knowledge files:

| Agent | Domains | Frameworks |
|---|---|---|
| `security-analyst` | 10 | OWASP Top 10, STRIDE, DREAD, CVSS v3.1, CWE, ASVS, Attack Trees, Security Headers, SANS/CWE Top 25, Secure Code Review |
| `code-reviewer` | 10 | Code Smells, SOLID Violations, Cognitive Complexity, Review Standards, Refactoring Patterns, Clean Code, Severity Classification, Performance Anti-Patterns, Error Handling, API Design |
| `planner` | 10 | WBS, CPM, PERT, Reference-Class Forecasting, Estimation Techniques, Risk Quantification, RACI, MoSCoW, Dependency Management, Agile Planning |
| `business-analyst` | 10 | SWOT/TOWS, Porter's Five Forces, BMC, Lean Canvas, Value Chain, TAM/SAM/SOM, Stakeholder Analysis, BPMN, Competitive Analysis, PESTLE |
| `devils-advocate` | 10 | Cognitive Bias Detection, Pre-Mortem, Red Team, Dialectical Thinking, Assumption Mapping, Second-Order Thinking, Decision Quality, Inversion Thinking, Socratic Questioning, FMEA |
| `product-growth` | 6 | AARRR Metrics, Growth Loops, Experimentation, Unit Economics, Pricing Strategy, Funnel Optimization |

## Skills

Skills are invocable actions that agents use during workflow execution. Some can also be triggered directly.

| Skill | Description |
|---|---|
| `commit` | Creates conventional commits with HEREDOC format |
| `push` | Pushes branch to remote with `-u` flag |
| `developing` | Executes the implementation phase from an approved plan |
| `diagnosis` | Diagnoses problems through data structure and codebase analysis |
| `tests` | Creates and runs tests for acceptance criteria |
| `wireframing` | Creates wireframe specifications for UI components |
| `identify-stack` | Detects project tech stack and annotates CLAUDE.md with Context7 links |
| `frontmatter-evaluation` | Evaluates knowledge files so agents can select relevant themes |
| `research-frontend-references` | Searches design platforms for visual references and patterns |
| `growth-audit` | Full AARRR funnel audit with unit economics and opportunity scoring |
| `experiment-design` | Designs structured growth experiments with statistical requirements |
| `pricing-analysis` | Evaluates pricing models with competitive positioning and unit economics |

## Output Styles

Switch styles using `/output-style [style]` to adapt the orchestrator's behavior:

| Style | When to Use | Description |
|---|---|---|
| `workflow` | Default for all workflow execution | Enforces step-by-step execution, progress tracking, agent delegation, and approval gates |
| `planning` | Steps 4-5 or deep planning tasks | Structured task breakdowns with risk assessments, dependencies, and acceptance criteria |
| `review` | Step 6.5 or standalone reviews | Severity-rated findings with IDs, file:line references, and verdict system |
| `research` | Step 7 or technology evaluation | Structured research with sources, design references, and Context7 integration |

## Workflows

### Development Workflow (14 Steps)

The Development Workflow guides a complete feature or fix from request to deployment:

```
1. User Request
2. Request Understanding (request-analyst)
3. Problem Diagnosis (data-structure-analyst — parallel sub-steps)
   3.1 Data Structure Analysis
   3.2 Consult Memory
   3.3 Problem Analysis
4. Planning Creation (planner + devils-advocate)
5. Planning Approval (user approval gate)
6. Planning Execution (developer + delegated agents)
   6.1 Task Delegation
   6.2 Skill Usage
   6.3 Script Usage
   6.4 Infrastructure Tasks (devops-engineer)
   6.5 Code Review + Security Review (parallel, with feedback loop)
7. Design Reference Research (ui-ux-analyst) [optional]
8. Wireframe Creation (wireframe-creator) [optional]
9. Test Creation (tester) [optional]
10. User Validation (approval gate)
11. Memory Persistence
12. Branch Creation (git-manager)
13. Commit Changes (git-manager)
14. Push to Remote (git-manager)
```

**Review Feedback Loop (Step 6.5):** After the developer completes implementation, `code-reviewer` and `security-analyst` run in parallel. If either returns CHANGES REQUIRED, findings go back to the developer. This loop repeats up to 3 cycles before escalating to the user.

### Business Analysis Workflow (9 Steps)

The Business Analysis Workflow guides strategic analysis from request to recommendations:

```
1. User Request
2. Request Understanding (request-analyst)
3. Requirements Gathering (requirements-analyst)
4. Business Context Analysis (requirements-analyst + business-analyst + product-growth)
5. Planning Creation (planner + devils-advocate)
6. Planning Approval (user approval gate)
7. Planning Execution (delegated agents)
8. User Validation (approval gate)
9. Memory Persistence
```

## Modular Domain Knowledge

High-expertise agents use a two-layer architecture to optimize context window usage:

**Layer 1 — Core File (~10-15KB):** Contains the agent's identity, Domain Selection Matrix, output templates, constraints, and execution order. Always loaded.

**Layer 2 — Domain Files (~1-5KB each):** Individual framework knowledge files loaded on demand. Each agent has a Domain Selection Matrix that maps task types to required domains.

**Example:** When `security-analyst` receives a "Code security review" task, it loads only domains 1 (OWASP Top 10), 5 (CWE), and 10 (Secure Code Review) — not all 10 domains. This reduces context consumption by ~70% for focused tasks.

Each agent's core file includes a **Step 1.5: Load Relevant Domains** in its mandatory execution order, where it:
1. Identifies the task type
2. Consults the Domain Selection Matrix
3. Reads only the needed domain files
4. Loads additional domains on-demand if needed during execution

## Knowledge Persistence

The plugin maintains two knowledge stores that persist across sessions:

### `app_knowledge/` — Theme-Specific Knowledge

Organized by theme, each with exactly 3 files:

```
app_knowledge/<theme-name>/
  requirements.md   # What is needed and why
  design.md         # How it will be built
  decisions.md      # What was decided and the impact
```

### `memory/` — Project-Wide Knowledge

Concise, high-priority information relevant to the entire project:

- **Stack knowledge** (`stack-*` prefix) — Import paths, version quirks, troubleshooting solutions
- **Architectural decisions** — Project-wide patterns and conventions
- **Recurring issues** — Solutions to problems encountered across sessions

All code-writing agents consult `memory/` before writing any code to prevent repeating previously solved errors.

### Frontmatter System

Both knowledge stores use YAML frontmatter for efficient retrieval:

```yaml
---
key: unique-identifier
summary: One-line description of the file contents
---
```

The `frontmatter_content_evaluation.py` script indexes all knowledge files so agents can select relevant themes without reading full contents.

## License

MIT
