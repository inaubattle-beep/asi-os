# ASI-OS

**ASI-OS** is a research-oriented AI-native operating environment for coordinating foundation models, reasoning, agents, memory, tools, workflows, security, and evaluation.

> **Vision:** make intelligence a managed system resource: models are compute, agents are processes, tools are capabilities, memory is storage, and tasks are the unit of work.

This repository is an engineering roadmap and Phase-1 scaffold. It does **not** claim to implement AGI or ASI. The goal is to build a safe, modular platform that can host increasingly capable AI systems.

## Architecture

```text
Human / API / Voice / UI
          |
      AI OS API
          |
  +-------+--------+
  |                |
Agent Runtime   Workflow Engine
  |
  +---- Intelligence ----+
  | Planner              |
  | Reasoner             |
  | Decision Engine      |
  | Reflection/Evaluator |
  +----------------------+
          |
  +-------+-------+-------+
  |               |       |
 Agents         Memory   Models
  |               |       |
 Coding         RAG     LLM/VLM
 Research       Graph   Coding
 Retrieval      Episodic Reasoning
 Calling        Semantic Speech
 Browser        Procedural Embeddings
 Data
          |
       Tool Fabric
 Web / Browser / Shell / Git / DB / APIs / Voice
          |
 Infrastructure
 Linux / Containers / GPU / Storage / Network

Cross-cutting: Security • Identity • Policy • Observability • Evaluation
```

## Engineering principles

1. **OS layer over Linux first** — do not write a new kernel in Phase 1.
2. **Model-agnostic** — local and remote models behind one Model Fabric.
3. **Agents are managed processes** — lifecycle, state, permissions, resources.
4. **Tasks are first-class** — every autonomous action becomes an `AgentTask`.
5. **Memory is a subsystem** — working, episodic, semantic, procedural.
6. **Tools are capability-scoped** — no unrestricted agent access.
7. **Verification before autonomy** — test, evaluate, audit, then act.
8. **Human approval for high-impact actions** — production, destructive, financial, external communications.
9. **AI-generated code is reviewed and tested** — AI is a development accelerator, not an authority.
10. **Modular replacement** — every model, vector store, agent, or tool should be replaceable.

## Target stack

- **Python 3.12+** for orchestration and agent services
- **FastAPI** for control/API plane
- **Pydantic** for contracts
- **PostgreSQL** for durable state
- **Redis** for queues/cache
- **Object storage** for artifacts
- **Vector database** behind a repository interface
- **Docker** for isolation
- **OpenTelemetry** for traces
- **pytest + mypy + ruff** for quality
- **GitHub Actions** for CI
- **Kubernetes** later, when multi-node scheduling is required

The first implementation should keep infrastructure adapters behind interfaces so technologies can be changed without rewriting the agent kernel.

## Repository map

```text
docs/                 architecture, ADRs, roadmap, threat model
src/asi_os/
  core/               contracts and domain primitives
  runtime/            agent/task runtime
  intelligence/       planning, routing, decision engine
  memory/             memory interfaces
  models/             model provider/router interfaces
  tools/              capability/tool interfaces
  security/           policy and permission interfaces
  observability/      tracing/evaluation interfaces
  api/                FastAPI control plane
agents/               built-in agent specifications
tests/                unit and contract tests
prompts/              AI development prompts and engineering roles
infra/                Docker and future Kubernetes
.github/              CI, issue/PR templates, CODEOWNERS
```

## Development phases

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the complete system-engineering roadmap.

### Phase 0 — Foundations
- architecture and ADRs
- repository contracts
- CI
- security baseline
- local developer environment

### Phase 1 — AI OS Core
- `AgentTask`
- agent lifecycle
- task scheduler
- model router
- tool registry
- policy engine
- API

### Phase 2 — Memory
- working memory
- episodic memory
- semantic memory
- embeddings/retrieval
- knowledge graph

### Phase 3 — Tool Fabric
- filesystem
- shell sandbox
- web/browser
- Git
- databases
- external APIs
- voice/calling adapter

### Phase 4 — Specialized Agents
- manager
- coding
- research
- retrieval
- browser
- data
- calling
- security/reviewer

### Phase 5 — Multi-Agent Runtime
- agent message bus
- delegation
- task graphs
- resource scheduling
- verification/criticism

### Phase 6 — Autonomous Workflows
- long-running goals
- retries and recovery
- approval gates
- scheduled jobs
- policy-driven autonomy

### Phase 7 — Evaluation and Self-Improvement
- benchmark suites
- regression tests
- agent trajectory evaluation
- controlled improvement proposals
- canary deployment

## AI development workflow

Use AI coding tools as **pair programmers inside an engineering process**:

```text
Issue
  -> architecture/ADR
  -> AI implementation prompt
  -> small PR
  -> automated tests
  -> static/security checks
  -> human review
  -> merge
  -> evaluation
```

Prompts for the AI development agent are in [`prompts/`](prompts/).

## Safety boundary

ASI-OS is intended for research and controlled automation. Do not give an agent unrestricted credentials, production shell access, destructive database access, or unsupervised authority over high-impact external systems.

See [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md).

## Status

**Stage:** architecture + Phase-1 scaffold.

**Next milestone:** implement the domain contracts and a deterministic in-memory Agent Runtime before adding autonomous model calls.
