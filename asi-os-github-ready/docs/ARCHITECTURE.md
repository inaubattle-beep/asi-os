# ASI-OS Architecture

## Core mental model

| AI-OS concept | OS analogy |
|---|---|
| Model | cognitive compute |
| Agent | process |
| AgentTask | job/process request |
| Tool | device/service |
| Memory | storage |
| Agent Bus | IPC |
| Scheduler | CPU/resource scheduler |
| Policy Engine | security boundary |
| Workflow | process graph |
| Evaluation | test/telemetry subsystem |

## Planes

### Control plane
Identity, sessions, task submission, policy, scheduling.

### Intelligence plane
Planning, reasoning, routing, reflection, decision making.

### Agent plane
Specialized agents and agent lifecycle.

### Memory plane
Working/episodic/semantic/procedural memory and knowledge.

### Tool plane
Web, browser, shell, code execution, Git, databases, APIs, voice.

### Model plane
Provider adapters, model registry, router, embeddings, rerankers.

### Data plane
PostgreSQL, Redis, object storage, vector indexes.

### Security plane
Authentication, authorization, sandboxing, secrets, guardrails, audit.

### Observability plane
Logs, traces, metrics, evaluations, cost and quality.

## Dependency rule

Prefer dependencies toward stable contracts:

```text
API -> Runtime -> Domain Contracts
Agents -> Runtime/Contracts
Tools -> Contracts
Memory -> Contracts
Models -> Contracts
Security -> Contracts
```

Agents must not directly depend on a specific database or model provider.

## ADR index

- ADR-0001: Linux-first AI OS
- ADR-0002: Python-first orchestration
- ADR-0003: Model provider abstraction
- ADR-0004: AgentTask as universal unit
- ADR-0005: Capability-based tool permissions
- ADR-0006: Bounded autonomy
