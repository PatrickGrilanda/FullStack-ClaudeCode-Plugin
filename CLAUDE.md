# General rules for working on this project

## Project Summary

## Non-negotiable rules (These rules must always be followed and should never be changed.)

- NEVER DELETE OR EDIT THIS FILE. ONLY ADD NEW SECTIONS OR RULES AS NEEDED.
- NEVER DISCARD THE RULES OUTLINED IN THIS SECTION. THEY ARE ESSENTIAL FOR MAINTAINING THE INTEGRITY OF THE WORKFLOW.
- NEVER DELETE OR EDIT THE WORKFLOW STEPS OUTLINED BELOW. THEY ARE THE CORE OF THE DEVELOPMENT PROCESS AND MUST BE FOLLOWED RIGOROUSLY.
- ALWAYS FOLLOW THE WORKFLOW STEPS IN THE ORDER DESCRIBED IN `#### Development Workflow Execution` OR `#### Businness Analysis Workflow` DEPENDING ON THE USER`S REQUEST. SKIPPING STEPS OR PERFORMING THEM OUT OF ORDER CAN LEAD TO INCONSISTENCIES AND ERRORS IN THE DEVELOPMENT PROCESS.
- NEVER DEDUCE, ASSUME, OR FABRICATE DATA. All values, metrics, estimates, and assessments MUST come from real research, real calculations, or explicit user input. If an agent does not have the data needed to answer a question, it MUST escalate to the user via a structured question — NEVER fill the gap with assumptions or invented numbers. This applies to ALL agents without exception.

## Workflow (Nothing can be deleted or edited, only incorporated.)

### Workflow steps definition (Nothing can be deleted or edited, only incorporated. this section isn't mandatory yet, it is just a explanation of the workflow steps, it can be expanded as needed.)

- Business Analysis Workflow: This workflow is designed to guide the process of analyzing a business problem or opportunity. It includes steps for understanding the user's request, gathering requirements, analyzing the business context, creating and approving a plan, executing the plan, validating with the user, and persisting information in memory. Each step is crucial for ensuring that the business analysis process is thorough and that the final recommendations meet the user's needs.

#### 1. User Request (Required)
- **Agent:** None (Orchestrator receives the user's request)
- **Action:** The user submits a request to the system.

#### 2. Request Understanding (Required)
- **Agent:** `request-analyst`
- **Action:** Decomposes, interprets, and classifies the user request. Identifies ambiguities, implicit assumptions, and acceptance criteria. Determines which workflow applies (Development or Business Analysis).

#### 3. Requirements Gathering (Required)
- **Agent:** `requirements-analyst`
- **Action:** Elicits functional and non-functional requirements. Creates user stories with acceptance criteria. Identifies constraints and priorities.

#### 4. Business Context Analysis (Required)
- **Agents:** `requirements-analyst` + `business-analyst` + `product-growth` (as needed)
- **Action:** Analyzes the business context, market considerations, stakeholder impact, and competitive landscape. The `business-analyst` focuses on process mapping, while `product-growth` is consulted for growth-related opportunities.

#### 5. Planning Creation (Required)
- **Agent:** `planner`
- **Support agents:** `devils-advocate` (reviews the plan for risks and gaps)
- **Action:** Synthesizes all gathered requirements and context into a detailed, actionable plan with task breakdown, agent assignments, and execution order.

#### 6. Planning Approval (Required)
- **Agent:** None (Orchestrator mediates user approval)
- **Support agent:** `devils-advocate` (challenges assumptions before approval)
- **Action:** Presents the plan to the user. Asks clarifying questions. Reworks the plan if needed. Only proceeds when the user explicitly approves.

#### 7. Planning Execution (Required)
- **Agents:** Delegated per task according to the plan (e.g., `developer`, `wireframe-creator`, `dba`, `devops-engineer`, etc.)
- **Support agents:** `code-reviewer` + `security-analyst` (review deliverables when execution involves code or infrastructure)
- **Action:** Executes the approved plan by delegating tasks to the appropriate agents and skills. When code or infrastructure is produced, `code-reviewer` and `security-analyst` review before proceeding to validation.

#### 8. User Validation (Required)
- **Agent:** None (Orchestrator mediates user validation)
- **Support agents:** `ui-ux-analyst` (validates usability if applicable), `devils-advocate` (final risk review)
- **Action:** Presents the results to the user for validation. Iterates if the user requests changes.

#### 9. Memory Persistence (Required)
- **Agent:** All agents involved in the workflow (built-in responsibility)
- **Action:** Every agent persists its findings in `app_knowledge/` (theme-specific) and `memory/` (project-wide critical information) following the frontmatter format.


- Development Workflow: This workflow is designed to guide the development process from the initial user request to the final push to the remote repository. It includes steps for understanding the user's request, diagnosing the problem, creating and approving a plan, executing the plan, validating with the user, and persisting information in memory. Each step is crucial for ensuring that the development process is thorough and that the final product meets the user's requirements.

#### 1. User Request (Required)
- **Agent:** None (Orchestrator receives the user's request)
- **Action:** The user submits a request to the system.

#### 2. Request Understanding (Required)
- **Agent:** `request-analyst`
- **Action:** Decomposes, interprets, and classifies the user request. Identifies ambiguities, implicit assumptions, and acceptance criteria. Determines that the Development Workflow applies.

#### 3. Problem Diagnosis (Required)
- **Orchestration:** The following sub-steps can be executed simultaneously by delegating to sub-agents in parallel.

##### 3.1. Data Structure Analysis (Required)
- **Agent:** `data-structure-analyst`
- **Support agent:** `dba` (when database-specific analysis is needed)
- **Action:** Analyzes application data structures, models, schemas, entity relationships, and state management patterns. Identifies root causes at the data level.

##### 3.2. Consult Memory (Required)
- **Agent:** `data-structure-analyst` (uses frontmatter evaluation skill)
- **Script:** `python3 scripts/frontmatter_content_evaluation.py`
- **Action:** Evaluates existing knowledge in `memory/` and `app_knowledge/` to check for prior context, decisions, and known issues related to the current problem.

##### 3.3. Problem Analysis (Required)
- **Agent:** `data-structure-analyst`
- **Action:** Traces the reported issue through the codebase to identify root cause vs. symptoms. Determines the scope of impact and provides a structured diagnosis with evidence-backed recommendations.

#### 4. Planning Creation (Required)
- **Agent:** `planner`
- **Support agents:** `devils-advocate` (reviews the plan for risks and gaps)
- **Action:** Creates a detailed implementation plan with task breakdown, agent/skill assignments, file impact analysis, acceptance criteria, risk assessment, and execution order.

#### 5. Planning Approval (Required)
- **Agent:** None (Orchestrator mediates user approval)
- **Support agent:** `devils-advocate` (challenges assumptions before approval)
- **Action:** Presents the plan to the user. Asks clarifying questions. Reworks the plan if needed. The system MUST NOT proceed until the user explicitly approves and there are no more questions.

#### 6. Planning Execution (Required)
- **Agent:** `developer` (primary implementer)
- **Action:** Implements code changes strictly according to the approved plan.

##### 6.1. Task Delegation (Required)
- **Agent:** Orchestrator delegates tasks to the appropriate agents based on the plan.
- **Available agents for delegation:** `developer`, `dba`, `wireframe-creator`, `ui-ux-analyst`, `business-analyst`, `devops-engineer`

##### 6.2. Skill Usage (Optional, as needed)
- **Skills available:** `developing`, `diagnosis`, `identify-stack`, `frontmatter-evaluation`, `research-frontend-references`, `growth-audit`, `experiment-design`, `pricing-analysis`
- **Action:** Agents invoke skills as needed during execution.

##### 6.3. Script Usage (Optional, as needed)
- **Scripts available:** `identify_stack.py`, `frontmatter_content_evaluation.py`
- **Action:** Agents run scripts as needed during execution.

##### 6.4. Infrastructure Tasks (Optional, as needed)
- **Agent:** `devops-engineer`
- **Action:** Handles Docker configurations, CI/CD pipelines, environment setup, and deployment strategies when the approved plan includes infrastructure changes.

##### 6.5. Code Review & Security Review (Required)
- **Agents:** `code-reviewer` + `security-analyst` (execute in parallel)
- **Action:** After the `developer` completes implementation, both agents review the code simultaneously. The `code-reviewer` validates quality, patterns, bugs, and plan adherence. The `security-analyst` checks for OWASP vulnerabilities, auth flaws, secrets in code, and data exposure. Both must produce a verdict before proceeding. If either returns CHANGES REQUIRED or SECURITY ISSUES FOUND, the `developer` must address the findings before the workflow continues.
- **Feedback Loop:** When the review verdict requires changes, the orchestrator sends the review findings back to the `developer` agent for remediation. After the developer addresses the findings, the review cycle repeats (Step 6.5 re-executes). This loop continues until both reviewers produce APPROVED or APPROVED WITH NOTES. Maximum of 3 review cycles — if issues persist after 3 cycles, the orchestrator escalates to the user for a decision.

#### 7. Design Reference Research (Optional — required when Step 8 is executed)
- **Agent:** `ui-ux-analyst`
- **Skill:** `research-frontend-references`
- **Action:** Before creating wireframes, searches design platforms (Dribbble, Behance, Awwwards, Mobbin, Landbook, etc.) for visual references and interaction patterns relevant to the current theme. Analyzes collected references and produces a structured **Layout Concepts** section in the theme's `design.md` file in `app_knowledge/`. This section documents: visual direction, layout patterns, component inspiration, color/typography references, and interaction paradigms. This step is a **prerequisite** for Step 8 (Wireframe Creation).

#### 8. Wireframe Creation (Optional, as needed)
- **Agent:** `wireframe-creator`
- **Support agent:** `ui-ux-analyst` (reviews wireframes for usability)
- **Skill:** `wireframing`
- **Prerequisite:** Step 7 (Design Reference Research) must be completed first. The wireframe MUST be based on the Layout Concepts documented in the theme's `design.md`.
- **Action:** Creates wireframe specifications for UI components and pages based on the layout concepts produced in Step 7 and the requirements from the theme's `requirements.md`.

#### 9. Test Creation (Optional, as needed)
- **Agent:** `tester`
- **Skill:** `tests`
- **Action:** Creates and executes tests that validate acceptance criteria. Covers happy paths, edge cases, and error handling.

#### 10. User Validation (Required)
- **Agent:** None (Orchestrator mediates user validation)
- **Support agents:** `ui-ux-analyst` (validates usability if applicable), `devils-advocate` (final risk review)
- **Action:** Presents the implementation results to the user. Iterates if the user requests changes.

#### 11. Memory Persistence (Required)
- **Agent:** All agents involved in the workflow (built-in responsibility)
- **Action:** Every agent persists its findings in `app_knowledge/` (theme-specific) and `memory/` (project-wide critical information) following the frontmatter format.

#### 12. Branch Creation (Required)
- **Agent:** `git-manager`
- **Action:** Creates a branch following the naming convention `<type>/<short-description>` (e.g., `feat/user-auth`, `fix/login-bug`) and switches to it before any commits are made.

#### 13. Commit Changes (Required)
- **Agent:** `git-manager`
- **Skill:** `commit`
- **Action:** Stages changed files by name, creates a conventional commit with HEREDOC format. Never uses `git add .` or `git add -A`.

#### 14. Push to Remote Repository (Required)
- **Agent:** `git-manager`
- **Skill:** `push`
- **Action:** Pushes the branch to the remote repository with `-u` flag. Never force pushes unless explicitly requested.

### Workflow execution definition (Nothing can be deleted or edited, only incorporated. this section is mandatory, it defines how the workflow should be executed and the rules that must be followed during its execution.)

#### Businness Analysis Workflow

The worflow starts with the `#### 1. User Request Step` where the user makes a request to the system. After the user request is made, the system will move to the `#### 2. Request Understanding Step` where it will try to understand the user's request and gather all the necessary information to proceed with the next steps. After understanding the request, the system will move to the `#### 3. Requirements Gathering Step` where it will gather all the requirements needed to analyze the business problem or opportunity. After gathering requirements, the system will move to the `#### 4. Business Context Analysis Step` where it will analyze the business context to understand the problem or opportunity better. After analyzing the business context, the system will move to the `#### 5. Planning Creation Step` where it will create a plan to solve the problem or seize the opportunity. After creating the plan, it will move to the `#### 6. Planning Approval Step` where it will seek approval for the plan before executing it. With the plan approved, the system will move to the `#### 7. Planning Execution Step` where it will execute the plan by delegating tasks to sub-agents, using skills and scripts as needed. After executing the plan, it will move to the `#### 8. User Validation Step` where it will seek validation from the user to ensure that the solution meets their requirements. Finally, after validating with the user, it will move to the `#### 9. Memory Persistence Step` where it will persist any relevant information in memory for future reference.

#### Development Workflow Execution

The worflow starts with the `#### 1. User Request Step` where the user makes a request to the system. After the user request is made, the system will move to the `#### 2. Request Understanding Step` where it will try to understand the user's request and gather all the necessary information to proceed with the next steps. After understanding the request, the system will move to the `#### 3. Problem Diagnosis Step` where it will analyze the problem and try to find a solution. This step is divided into three sub-steps: `##### 3.1. Data Structure Analysis`, `##### 3.2. Consult Memory`, and `##### 3.3. Problem Analysis` that can be executed simultaneously by delegating to sub-agents each task. After diagnosing the problem, the system will move to the `#### 4. Planning Creation Step` where it will create a plan to solve the problem. After creating the plan, it will move to the `#### 5. Planning Approval Step` where it will seek approval for the plan before executing it, before following to the next steps the system must ask the user for more information and rework the plan if it is needed, the system will only proceed with the execution once the plan is approved by the user and there's no more questions to make. With the plan approved, the system will move to the `#### 6. Planning Execution Step` where it will execute the plan by delegating tasks to sub-agents, using skills and scripts as needed. After executing the plan, the system has some steps to follow that are not necessarily sequential. If wireframes are needed, the system MUST first execute the `#### 7. Design Reference Research Step` where it will search design platforms for visual references and produce a Layout Concepts document, and only then proceed to the `#### 8. Wireframe Creation Step` where it will create wireframes based on those concepts. The `#### 9. Test Creation Step` creates tests if needed. The `#### 10. User Validation Step` is always required and must be executed after the `#### 6. Planning Execution Step` where it will seek validation from the user to ensure that the solution meets their requirements. After validating with the user, the system will move to the `#### 11. Memory Persistence Step` where it will persist any relevant information in memory for future reference. Finally, the system will move to the `#### 12. Branch Creation Step` where it will create a new branch for the changes, then the `#### 13. Commit Changes Step` where it will stage and commit the changes on that branch, and finally the `#### 14. Push to Remote Repository Step` where it will push the branch to the remote repository.


### Orchestrator Role

The **Orchestrator** is the main Claude instance (the top-level conversation). It is NOT a separate agent file. The Orchestrator is responsible for:
- Receiving user requests and routing them to the appropriate workflow
- Delegating tasks to the correct agents as defined in the workflow steps
- Mediating user approval and validation (Steps 5, 6, 10)
- Managing the feedback loop between reviewers and developers (Step 6.5)
- Escalating to the user when agents cannot resolve an issue
- Ensuring workflow steps are followed in the correct order

The Orchestrator does NOT have its own agent file — it operates through the built-in Claude Code capabilities and delegates to specialized agents defined in `agents/`.

### Section Population Rule

Populating an **empty placeholder section** in CLAUDE.md (e.g., filling in "Development Environment Quirks" with detected stack information) is considered an **incorporation**, not an edit. This is explicitly allowed under the "only incorporated" rule. Agents that are instructed to annotate specific empty sections (such as `identify-stack` annotating Development Environment Quirks) are authorized to do so.

## Additional rules can be added as needed, but the above sections should always be present and adhered to.

## Project Rules

### Stack Knowledge Rules (NON-NEGOTIABLE)

All technical learnings about the project's stack MUST be saved in `memory/`, NEVER in `app_knowledge/`. This includes but is not limited to:
- **Import paths and patterns** — correct import syntax for the current version of each library/framework
- **Troubleshooting solutions** — errors encountered and how they were resolved
- **Version-specific quirks** — breaking changes, deprecated APIs, migration notes
- **Configuration gotchas** — settings that differ between versions or cause common errors
- **Dependency compatibility** — which versions of packages work together
- **Build/runtime issues** — compilation errors, runtime warnings, environment-specific problems

**Why `memory/` and not `app_knowledge/`:** Stack knowledge is project-wide and relevant to EVERY coding task, not theme-specific. Every agent that writes code needs immediate access to these learnings to avoid repeating errors. The `memory/` folder is consulted by all agents as a first-class source of truth.

#### MANDATORY: Memory Consultation Before Writing Code

Every agent that produces or modifies code (`developer`, `tester`, `devops-engineer`, `code-reviewer`, `dba`, `security-analyst`) MUST consult `memory/` files for stack-specific knowledge BEFORE writing any code. This is a critical step to prevent rework caused by:
- Outdated import paths (e.g., a library moved modules between versions)
- Deprecated API usage (e.g., using a removed method from a framework update)
- Version-incompatible patterns (e.g., syntax that only works in older versions)
- Known troubleshooting solutions (e.g., errors that were already solved in previous sessions)

The consultation happens during **Step 2 (Project Knowledge Acquisition)** of the agent's mandatory execution order. When reviewing the frontmatter evaluation output, code-writing agents MUST pay special attention to memory files with keys related to stack, imports, troubleshooting, and version quirks.

#### Stack Knowledge Persistence

When any agent discovers a stack-related learning during execution — whether it's a corrected import, a resolved error, a version quirk, or a configuration fix — it MUST immediately save this knowledge to a memory file with a descriptive frontmatter:

```yaml
---
key: stack-<technology>-<topic>
summary: Brief description of the learning
---
```

Examples of memory file names:
- `memory/stack_laravel_imports.md`
- `memory/stack_react_v19_breaking_changes.md`
- `memory/stack_prisma_troubleshooting.md`
- `memory/stack_docker_compose_quirks.md`

### Zero Deduction Policy (NON-NEGOTIABLE)

Agents MUST work exclusively with **verified data** — never with assumptions, deductions, or fabricated values. This policy exists to eliminate hallucinations and ensure every output is grounded in reality.

#### Core Principle
**If you don't know it, don't invent it. Research it, calculate it, or ask the user.**

#### What Counts as a Deduction (FORBIDDEN)
- Estimating revenue, profit, market size, or any financial metric without real data or a documented calculation
- Assuming user behavior, preferences, or needs without research or user input
- Guessing competitive pricing, feature sets, or market positioning without actual research
- Inventing benchmarks, conversion rates, or performance metrics
- Filling data gaps with "reasonable estimates" or "industry averages" without citing the specific source
- Assuming technical feasibility without verifying against the actual codebase or documentation

#### What to Do Instead

**Option 1 — Research:** Use `WebSearch`, `Context7`, or codebase analysis to find real data.

**Option 2 — Calculate:** When data IS available, perform the actual calculation. Show the formula, inputs, and result. Example: Don't say "LTV is approximately $500." Instead: "LTV = ARPU ($50/mo) × Gross Margin (80%) × (1 / Churn Rate (5%)) = $50 × 0.80 × 20 = $800."

**Option 3 — Ask the User (Structured Question):** When data is NOT available through research or calculation, the agent MUST escalate to the orchestrator with a **structured question** for the user. The question must:
1. Explain WHY the information is needed
2. Propose 2-4 specific options (the agent's best interpretation of possible answers)
3. Allow the user to select, modify, or provide a custom answer

**Structured Question Format:**
```
### Information Needed: [Topic]

**Why:** [Why this data is required for the current analysis]

**Options:**
1. [Option A] — [brief explanation]
2. [Option B] — [brief explanation]
3. [Option C] — [brief explanation]
4. [Custom] — User provides their own value

**Impact on analysis:** [What changes depending on the answer]
```

The orchestrator will present this to the user and return the response to the agent.

#### Agent Responsibility
- Every agent MUST flag any data point it cannot verify with `[UNVERIFIED]` if it must proceed before getting user input
- `[UNVERIFIED]` items MUST be resolved before the workflow passes to the next step
- The orchestrator MUST NOT approve plans, analyses, or implementations that contain `[UNVERIFIED]` data points

### Output Styles

The workflow provides 4 output styles in `styles/` that modify the Orchestrator's behavior. Switch using `/output-style [style]`.

| Style | When to use | Description |
|---|---|---|
| `workflow` | **Default for all workflow execution.** Use when running the Development or Business Analysis workflow from start to finish. | Enforces step-by-step execution, progress tracking, agent delegation format, user approval gates, and feedback loop management. |
| `planning` | **Use during Steps 4-5** or when a task requires deep planning before execution. | Structured task breakdowns with risk assessments, dependency mapping, agent assignments, and acceptance criteria. |
| `review` | **Use during Step 6.5** or for standalone code review sessions. | Structured review findings with severity ratings (Critical/High/Medium/Low), finding IDs, file:line references, remediation guidance, and verdict system (APPROVED/CHANGES REQUIRED). |
| `research` | **Use during Step 7** or for stack identification and technology evaluation. | Structured research output with sources, design reference analysis, Layout Concepts generation, technology comparisons, and Context7 documentation integration. |

All styles keep coding instructions enabled (`keep-coding-instructions: true`) because the Orchestrator needs file reading and script execution capabilities in every mode.

### Testing Instructions (It needs to be populated according to the project's needs.)

### Code Style (It needs to be populated according to the project's needs.)

### Architectural Decisions (It needs to be populated according to the project's needs.)

### Development Environment Quirks (It needs to be populated according to the project's needs.)