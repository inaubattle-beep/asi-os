from __future__ import annotations

from dataclasses import dataclass, field

from asi_os.core.contracts import AgentTask, TaskResult, TaskState
from asi_os.runtime.agent import Agent


@dataclass
class InMemoryAgentRuntime:
    agents: dict[str, Agent] = field(default_factory=dict)

    def register(self, agent: Agent) -> None:
        if agent.name in self.agents:
            raise ValueError(f"agent already registered: {agent.name}")
        self.agents[agent.name] = agent

    async def execute(self, task: AgentTask) -> TaskResult:
        agent = self.agents.get(task.agent)
        if agent is None:
            return TaskResult(
                task_id=task.task_id,
                status=TaskState.FAILED,
                error=f"unknown agent: {task.agent}",
            )

        task.state = TaskState.RUNNING
        try:
            result = await agent.run(task)
        except Exception as exc:  # noqa: BLE001
            return TaskResult(
                task_id=task.task_id,
                status=TaskState.FAILED,
                error=str(exc),
            )

        return result
