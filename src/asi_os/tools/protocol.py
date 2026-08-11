from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from asi_os.core.contracts import Capability


class Tool(ABC):
    name: str
    capability: Capability

    @abstractmethod
    async def invoke(self, arguments: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError
