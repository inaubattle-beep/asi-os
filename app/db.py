import json
import sqlite3
import uuid
from pathlib import Path
from typing import Any, Dict, Optional


class Database:
    def __init__(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        with sqlite3.connect(path) as c:
            c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                goal TEXT NOT NULL,
                status TEXT NOT NULL,
                step INTEGER NOT NULL DEFAULT 0,
                history TEXT NOT NULL DEFAULT '[]'
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                task_id TEXT,
                kind TEXT NOT NULL,
                content TEXT NOT NULL
            )""")

    def create_task(self, goal: str) -> Dict[str, Any]:
        tid = str(uuid.uuid4())
        with sqlite3.connect(self.path) as c:
            c.execute("INSERT INTO tasks(id,goal,status) VALUES(?,?,?)",
                      (tid, goal, "running"))
        return self.get_task(tid)

    def get_task(self, tid: str) -> Optional[Dict[str, Any]]:
        with sqlite3.connect(self.path) as c:
            c.row_factory = sqlite3.Row
            row = c.execute("SELECT * FROM tasks WHERE id=?", (tid,)).fetchone()
            if not row: return None
            d = dict(row)
            d["history"] = json.loads(d["history"])
            return d

    def update_task(self, tid: str, status: Optional[str] = None, step: Optional[int] = None, history: Optional[list] = None) -> None:
        task = self.get_task(tid)
        status = task["status"] if status is None else status
        step = task["step"] if step is None else step
        history = task["history"] if history is None else history
        with sqlite3.connect(self.path) as c:
            c.execute("UPDATE tasks SET status=?,step=?,history=? WHERE id=?",
                      (status, step, json.dumps(history), tid))

    def add_memory(self, task_id: Optional[str], kind: str, content: str) -> None:
        with sqlite3.connect(self.path) as c:
            c.execute("INSERT INTO memories VALUES(?,?,?,?)",
                      (str(uuid.uuid4()), task_id, kind, content))
