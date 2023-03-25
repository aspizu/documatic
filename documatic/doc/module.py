from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Class, Function


@dataclass
class Module:
    name: str
    summary: str | None
    description: str | None
    classes: dict[str, Class]
    functions: dict[str, Function]
