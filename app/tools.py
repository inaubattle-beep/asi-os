import subprocess
from pathlib import Path
from typing import Any, Dict


class ToolError(Exception):
    pass

class ToolRegistry:
    def __init__(self, settings: Any) -> None:
        self.root = Path(settings.workspace).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.timeout = settings.shell_timeout
        self.allowed_commands = {"python", "python3", "echo", "pwd", "ls", "cat"}

    def _safe_path(self, path: str) -> Path:
        p = (self.root / path).resolve()
        if p != self.root and self.root not in p.parents:
            raise ToolError("path escapes workspace")
        return p

    def execute(self, name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        if name == "write_file":
            p = self._safe_path(args["path"])
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(args["content"], encoding="utf-8")
            return {"ok": True, "path": str(p.relative_to(self.root))}
        if name == "read_file":
            p = self._safe_path(args["path"])
            return {"ok": True, "content": p.read_text(encoding="utf-8")}
        if name == "shell":
            command = args["command"].strip()
            executable = command.split()[0] if command else ""
            if executable not in self.allowed_commands:
                raise ToolError(f"command not allowed: {executable}")
            r = subprocess.run(command, shell=True, cwd=self.root,
                               capture_output=True, text=True, timeout=self.timeout, check=False)
            return {"ok": r.returncode == 0, "returncode": r.returncode,
                    "stdout": r.stdout[-6000:], "stderr": r.stderr[-6000:]}
        raise ToolError(f"unknown tool: {name}")
