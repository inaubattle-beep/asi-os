# ADR-0002: AgentTask is the universal execution unit

## Decision

All agent work is represented as an `AgentTask`.

## Rationale

A common task contract makes scheduling, tracing, delegation, cancellation, evaluation, retries, and resource accounting consistent across coding, retrieval, research, calling, and future agents.
