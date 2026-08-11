# ADR-0001: Linux-first AI OS

## Decision

Build ASI-OS as an AI-native operating environment above Linux first.

## Rationale

A new kernel would add enormous complexity before the agent runtime, memory, tools, and security model are proven. Linux already provides mature process, networking, storage, container, and GPU ecosystems.

A custom kernel/runtime may be evaluated later for specialized scheduling or hardware integration.
