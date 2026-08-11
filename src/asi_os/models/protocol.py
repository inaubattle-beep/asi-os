from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field


class ModelRequest(BaseModel):
    model_role: str
    messages: list[dict[str, Any]]
    temperature: float = Field(default=0.2, ge=0, le=2)


class ModelResponse(BaseModel):
    text: str
    model: str
    usage: dict[str, int] = Field(default_factory=dict)


class ModelProvider(ABC):
    @abstractmethod
    async def generate(self, request: ModelRequest) -> ModelResponse:
        raise NotImplementedError
