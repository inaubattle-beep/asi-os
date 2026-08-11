# ASI-OS Engineering Roadmap

## Milestone strategy

Each milestone must produce a runnable artifact, tests, documentation, and an evaluation result. Avoid building ten subsystems in parallel.

| Milestone | Deliverable | Exit criterion |
|---|---|---|
| M0 | Architecture + contracts | ADRs accepted, CI green |
| M1 | AgentTask + runtime | deterministic agent lifecycle works |
| M2 | Model Fabric | providers can be swapped |
| M3 | Tool Fabric | tools are registered and permission checked |
| M4 | Memory | recall/store contract + persistence |
| M5 | Planner | task decomposition + bounded execution |
| M6 | Multi-agent bus | agents can delegate and receive results |
| M7 | Coding Agent | sandboxed code/test loop |
| M8 | Retrieval Agent | ingestion → retrieval → evidence |
| M9 | Calling Agent | approval-gated voice workflow |
| M10 | Observability | traces + evaluations |
| M11 | Production hardening | security, recovery, quotas |
| M12 | Autonomous workflows | long-running bounded goals |
| M13 | Controlled self-improvement | proposal → eval → approval → rollout |

## M0 — Foundations

- Define domain objects.
- Establish Python package layout.
- Add ruff, mypy, pytest.
- Add CI.
- Add threat model.
- Add ADR process.
- Define semantic versioning.

## M1 — Agent Kernel

Implement:

```text
Agent
AgentTask
TaskState
AgentState
Capability
Permission
TaskResult
```

Agent lifecycle:

```text
CREATED -> READY -> RUNNING -> WAITING -> COMPLETED
                                  |
                                  +-> FAILED
                                  +-> CANCELLED
```

Requirements:
- idempotent task IDs
- cancellation
- deadlines
- priority
- parent/child tasks
- structured results
- event log

## M2 — Model Fabric

Interfaces:

```text
ModelProvider
ModelRouter
ModelRequest
ModelResponse
ModelCapabilities
```

Routing factors:
- capability
- latency
- cost
- context length
- privacy
- availability
- quality tier

Never hard-code a provider into an agent.

## M3 — Tool Fabric

Every tool has:

```text
name
version
input_schema
output_schema
required_capabilities
risk_level
timeout
```

Tool calls pass through:

```text
Agent -> Policy -> Sandbox -> Tool -> Audit
```

High-risk actions require approval.

## M4 — Memory

Implement repository interfaces for:

- working memory
- episodic memory
- semantic memory
- procedural memory

Add:
- retention policy
- deletion/forgetting
- provenance
- tenant/agent scope
- access control

## M5 — Planning

Start with bounded planning, not unrestricted recursive autonomy.

```text
Goal
 -> Plan
 -> Task Graph
 -> Execute
 -> Verify
 -> Replan
```

Planner must have:
- max steps
- max cost
- max wall time
- allowed capabilities
- stop conditions

## M6 — Multi-Agent

Build an internal message bus.

Message envelope:

```json
{
  "message_id": "...",
  "from_agent": "...",
  "to_agent": "...",
  "task_id": "...",
  "type": "task.request",
  "payload": {},
  "deadline": "...",
  "trace_id": "..."
}
```

Add manager/worker/reviewer patterns.

## M7 — Coding Agent

First serious autonomous agent.

Workflow:

```text
Understand repo
 -> inspect requirements
 -> plan
 -> edit
 -> format/lint
 -> test
 -> inspect failure
 -> repair
 -> review
 -> produce patch
```

Sandbox requirements:
- isolated workspace
- CPU/RAM/time limits
- restricted network
- no production credentials
- audit all commands

## M8 — Retrieval Agent

Pipeline:

```text
Ingest
 -> parse
 -> chunk
 -> embed
 -> index
 -> retrieve
 -> rerank
 -> cite evidence
 -> synthesize
```

Retrieval should support keyword, vector, metadata, and graph strategies.

## M9 — Calling Agent

Architecture:

```text
User goal
 -> policy
 -> call plan
 -> human approval when required
 -> telephony provider
 -> speech recognition
 -> conversation agent
 -> tool actions
 -> transcript/audit
```

The system must explicitly distinguish informational calls from actions that commit the user/organization.

## M10 — Observability

Capture:
- task traces
- model latency
- token/cost metrics
- tool calls
- errors
- retries
- agent trajectory
- evaluation scores
- policy decisions

## M11 — Production Hardening

Add:
- authentication
- RBAC/ABAC
- secrets manager
- network policies
- rate limits
- quotas
- artifact signing
- backups
- disaster recovery
- supply-chain scanning

## M12 — Autonomous Workflows

Long-running workflow engine:

```text
Goal
 -> Planner
 -> Task graph
 -> Scheduler
 -> Agents
 -> Verification
 -> Recovery
 -> Completion
```

Autonomy must remain bounded by policy.

## M13 — Controlled Self-Improvement

The system may propose:
- prompt changes
- routing changes
- agent policy changes
- code changes
- workflow improvements

But deployment requires:

```text
Proposal
 -> isolated test
 -> benchmark
 -> regression check
 -> security check
 -> human/policy approval
 -> canary
 -> monitor
 -> rollout/rollback
```

## Definition of done

A feature is not complete until it has:

- implementation
- unit tests
- contract tests
- documentation
- observability
- security review
- failure handling
- resource limits
- evaluation where applicable
