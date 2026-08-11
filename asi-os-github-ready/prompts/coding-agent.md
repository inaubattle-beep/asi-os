# Coding Agent Development Prompt

Implement one issue in ASI-OS.

Before coding:
- inspect the repository tree
- read relevant ADRs
- identify existing interfaces
- state the smallest design

During coding:
- make minimal changes
- preserve public contracts
- add unit/contract tests
- avoid secrets
- avoid broad permissions
- add explicit time/step limits to loops

Before finishing:
- run tests
- run lint/type checks
- inspect the diff
- summarize risks and follow-up work

Do not silently redesign unrelated components.
