from dataclasses import dataclass


@dataclass
class Function:
    name: str
    summary: str | None
    description: str | None
    arguments: dict[str, str]
    returns: str | None
    exceptions: dict[str, str]
    signature: str
