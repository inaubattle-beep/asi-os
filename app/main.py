from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, Optional

from .config import settings
from .db import Database
from .orchestrator import Orchestrator

app = FastAPI(title="ASI-OS", version="0.1.0")
db = Database(settings.db_path)
orchestrator = Orchestrator(settings, db)

class TaskRequest(BaseModel):
    goal: str
    max_steps: int | None = None

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok", "service": "asi-os"}

@app.post("/tasks")
async def create_task(req: TaskRequest) -> Optional[Dict[str, Any]]:
    if not req.goal.strip():
        raise HTTPException(400, "goal is required")
    task = db.create_task(req.goal)
    assert task is not None
    return await orchestrator.run(task["id"], req.goal, req.max_steps or settings.max_steps)

@app.get("/tasks/{task_id}")
def get_task(task_id: str) -> Optional[Dict[str, Any]]:
    task = db.get_task(task_id)
    if not task:
        raise HTTPException(404, "task not found")
    return task
