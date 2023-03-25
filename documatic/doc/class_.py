from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Function


@dataclass
class Class:
    name: str
    summary: str | None
    description: str | None
    attributes: dict[str, str]
    functions: dict[str, Function]
    classes: dict[str, Class]
    signature: str
