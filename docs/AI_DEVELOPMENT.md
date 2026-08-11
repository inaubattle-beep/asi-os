# AI-Assisted Development Workflow

ASI-OS is intended to be developed with AI coding tools, but the AI is treated as an engineering accelerator rather than an authority.

## Recommended loop

```text
GitHub Issue
    |
    v
AI system-engineer agent
    |
    +--> inspect architecture
    +--> propose design
    +--> implement
    +--> write tests
    |
    v
Automated CI
    |
    +--> lint
    +--> type check
    +--> unit tests
    +--> security checks
    |
    v
Reviewer agent
    |
    v
Human approval
    |
    v
Merge
```

## Suggested AI roles

### 1. Architect agent
Produces an ADR and identifies interfaces, dependencies, risks, and acceptance criteria.

### 2. Coding agent
Implements one focused issue. It must not redesign the whole platform.

### 3. Test agent
Adds unit, contract, failure-mode, and regression tests.

### 4. Security/reviewer agent
Looks for privilege escalation, prompt injection, tool abuse, secret leakage, resource exhaustion, and unsafe autonomy.

### 5. Evaluation agent
Runs task benchmarks and compares the new implementation against the previous baseline.

## Prompt discipline

Give an AI coding tool:
- the issue
- relevant files
- architecture/ADR references
- explicit acceptance criteria
- commands it is allowed to run
- test requirements
- security constraints

Avoid prompts such as:

> "Build the entire ASI system autonomously."

Prefer:

> "Implement M1.2: add cancellation to AgentTask. Read docs/ARCHITECTURE.md and ADR-0002. Modify only the runtime/contracts needed for this issue. Add tests for cancellation, idempotency, and invalid transitions. Do not add provider-specific model code."

## Branch strategy

Use one branch per issue:

```text
main
  |
  +-- feat/task-cancellation
  +-- feat/model-router
  +-- feat/memory-store
  +-- feat/coding-agent
```

Keep pull requests small enough that a human can understand the complete diff.

## AI tool selection

Use AI coding tools for:
- repository exploration
- boilerplate
- test generation
- refactoring
- documentation
- code review
- debugging

Keep human ownership for:
- architecture decisions
- production credentials
- security policy
- high-risk tool permissions
- deployment approvals
- autonomy limits
