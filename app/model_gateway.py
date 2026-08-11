import json

import httpx
from typing import Any, Dict, List

SYSTEM = """You are the reasoning model inside ASI-OS.
Return JSON only. Never claim a tool was executed unless its result is supplied.
"""

class ModelGateway:
    def __init__(self, settings: Any) -> None:
        self.settings = settings

    async def decide(self, goal: str, history: List[Dict[str, Any]]) -> Any:
        if self.settings.model_mode == "mock":
            return self._mock(goal, history)

        payload = {
            "goal": goal,
            "history": history,
            "instruction": (
                "Choose one action. Return JSON with keys: "
                "type (tool|finish), tool, args, reason, answer. "
                "Available tools: write_file, read_file, shell."
            )
        }
        headers = {}
        if self.settings.model_api_key:
            headers["Authorization"] = f"Bearer {self.settings.model_api_key}"
        async with httpx.AsyncClient(timeout=120) as client:
            r = await client.post(
                self.settings.model_base_url.rstrip("/") + "/chat/completions",
                headers=headers,
                json={
                    "model": self.settings.model_name,
                    "messages": [
                        {"role": "system", "content": SYSTEM},
                        {"role": "user", "content": json.dumps(payload)}
                    ],
                    "temperature": 0.1
                }
            )
            r.raise_for_status()
            return json.loads(r.json()["choices"][0]["message"]["content"])

    def _mock(self, goal: str, history: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not history and "hello.txt" in goal.lower():
            return {"type":"tool","tool":"write_file",
                    "args":{"path":"hello.txt","content":"Hello from ASI-OS\n"},
                    "reason":"Create requested file."}
        return {"type":"finish","answer":f"Mock mode completed: {goal}"}
