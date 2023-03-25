from __future__ import annotations

import textwrap
from typing import TYPE_CHECKING

from rich import print  # type: ignore

if TYPE_CHECKING:
    ...


class DocString:
    def __init__(self, doc: str, attributes: dict[str, str] | None = None):
        self.summary = doc.splitlines()[0]
        self.description = None
        doc = textwrap.dedent(doc[len(self.summary) + 2 :])

        self.attributes: dict[str, str] = attributes or {}
        self.arguments: dict[str, str] = {}
        self.returns = None
        self.exceptions: dict[str, str] = {}

        self.parse(doc)

    def parse(self, doc: str):
        codeblock = False
        collector = None
        for line in (doc + "\n\n").splitlines():
            if collector is not None:
                if line[:2] != "  ":
                    collector = None
                    continue
                if collector in ("Attributes:", "Args:", "Raises:"):
                    name, desc = line[2:].split(": ")
                    {
                        "Attributes:": self.attributes,
                        "Args:": self.arguments,
                        "Raises:": self.exceptions,
                    }[collector][name] = desc
                elif collector == "Returns:":
                    if self.returns is None:
                        self.returns = line
                    else:
                        self.returns += "\n" + line
            elif line in ("Attributes:", "Args:", "Raises:", "Returns:"):
                collector = line
            else:
                if self.description is None:
                    self.description = ""
                if line.lstrip().startswith(">>>") or line.lstrip().startswith("..."):
                    if not codeblock:
                        codeblock = True
                        self.description += "```py\n"
                else:
                    if codeblock:
                        codeblock = False
                        self.description += "```\n"
                self.description += line + "\n"
        if self.description:
            self.description = self.description[:-1]
