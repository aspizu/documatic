from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Class:
    name: str
    summary: str | None
    description: str | None
    attributes: dict[str, str]
    functions: dict[str, Function]
    classes: dict[str, Class]
    signature: str


@dataclass
class Function:
    name: str
    summary: str | None
    description: str | None
    arguments: dict[str, str]
    returns: str | None
    exceptions: dict[str, str]
    signature: str


@dataclass
class Module:
    name: str
    summary: str | None
    description: str | None
    classes: dict[str, Class]
    functions: dict[str, Function]
