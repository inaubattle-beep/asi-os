from typing import Any

from .db import Database
from .model_gateway import ModelGateway
from .tools import ToolError, ToolRegistry


class Orchestrator:
    def __init__(self, settings: Any, db: Database) -> None:
        self.db = db
        self.model = ModelGateway(settings)
        self.tools = ToolRegistry(settings)

    async def run(self, task_id: str, goal: str, max_steps: int) -> dict[str, Any] | None:
        history: list[dict[str, Any]] = []
        for step in range(1, max_steps + 1):
            decision = await self.model.decide(goal, history)
            event = {"step": step, "decision": decision}

            if decision.get("type") == "finish":
                event["result"] = {"ok": True, "answer": decision.get("answer", "")}
                history.append(event)
                self.db.update_task(task_id, "completed", step, history)
                self.db.add_memory(task_id, "result", decision.get("answer", ""))
                return self.db.get_task(task_id)

            if decision.get("type") != "tool":
                event["result"] = {"ok": False, "error": "invalid decision"}
                history.append(event)
                self.db.update_task(task_id, "failed", step, history)
                return self.db.get_task(task_id)

            try:
                event["result"] = self.tools.execute(
                    decision["tool"], decision.get("args", {}))
            except (ToolError, KeyError, ValueError) as e:
                event["result"] = {"ok": False, "error": str(e)}

            history.append(event)
            self.db.update_task(task_id, "running", step, history)
            history = history[-6:]

        self.db.update_task(task_id, "failed", max_steps, history)
        return self.db.get_task(task_id)
