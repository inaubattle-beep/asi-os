from __future__ import annotations

from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TaskState(StrEnum):
    CREATED = "created"
    READY = "ready"
    RUNNING = "running"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TaskLimits(BaseModel):
    max_steps: int = Field(default=20, ge=1)
    max_wall_time_seconds: int = Field(default=600, ge=1)
    max_cost: float | None = Field(default=None, ge=0)


class AgentTask(BaseModel):
    task_id: UUID = Field(default_factory=uuid4)
    goal: str = Field(min_length=1)
    agent: str = Field(min_length=1)
    parent_task_id: UUID | None = None
    priority: int = Field(default=50, ge=0, le=100)
    state: TaskState = TaskState.CREATED
    context: dict[str, Any] = Field(default_factory=dict)
    capabilities: list[str] = Field(default_factory=list)
    limits: TaskLimits = Field(default_factory=TaskLimits)


class TaskResult(BaseModel):
    task_id: UUID
    status: TaskState
    summary: str = ""
    artifacts: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)
    metrics: dict[str, float] = Field(default_factory=dict)
    error: str | None = None


class Capability(BaseModel):
    name: str
    description: str = ""
    risk_level: RiskLevel = RiskLevel.LOW


class PolicyDecision(BaseModel):
    allowed: bool
    reason: str
    requires_approval: bool = False
