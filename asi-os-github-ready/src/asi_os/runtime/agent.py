from __future__ import annotations

from abc import ABC, abstractmethod

from asi_os.core.contracts import AgentTask, TaskResult


class Agent(ABC):
    """Minimal contract for all ASI-OS agents."""

    name: str

    @abstractmethod
    async def run(self, task: AgentTask) -> TaskResult:
        """Execute a bounded task and return a structured result."""
        raise NotImplementedError
