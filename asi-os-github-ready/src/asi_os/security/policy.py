from __future__ import annotations

from asi_os.core.contracts import AgentTask, PolicyDecision


class PolicyEngine:
    """Phase-1 deny-by-default policy stub."""

    def authorize(self, task: AgentTask, capability: str) -> PolicyDecision:
        if capability not in task.capabilities:
            return PolicyDecision(
                allowed=False,
                reason=f"capability not granted: {capability}",
            )
        return PolicyDecision(
            allowed=True,
            reason="capability explicitly granted",
        )
