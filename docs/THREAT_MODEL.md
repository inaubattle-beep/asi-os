# Threat Model

ASI-OS combines language models with tools and potentially persistent memory. Treat model output as untrusted input.

## Primary threats

1. Prompt injection through web pages/documents.
2. Tool abuse caused by malicious or incorrect model output.
3. Credential leakage through prompts, logs, memory, or generated code.
4. Data exfiltration through network-capable tools.
5. Supply-chain attacks in dependencies and containers.
6. Excessive autonomy / runaway task loops.
7. Cross-agent privilege escalation.
8. Cross-tenant memory leakage.
9. Destructive shell/database operations.
10. False or unverified autonomous decisions.

## Controls

- least privilege
- explicit capability grants
- isolated sandboxes
- network egress policies
- secrets never exposed to model context unless strictly necessary
- structured tool schemas
- time/step/cost limits
- approval gates
- audit logs
- provenance for retrieved knowledge
- independent evaluation
- dependency and container scanning
- deterministic test suites
- rollback and kill switches

## High-risk actions

Require human approval by default:

- production deployment
- destructive database operations
- financial transactions
- sending legally binding communications
- changing security controls
- changing agent permissions
- accessing highly sensitive data
