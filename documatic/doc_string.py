from __future__ import annotations

from typing import TYPE_CHECKING

from rich import print  # type: ignore

if TYPE_CHECKING:
    from rich.repr import RichReprResult


class DocString:
    """Parse a google format doc-string."""

    def __init__(self, doc: str):
        lines = doc.splitlines()
        self.summary: str | None = None
        """First line of the doc-string."""
        self.description: str | None = None
        """Any line in the doc-string that isn't the first or part of a section."""
        self.args: list[tuple[str, str]] = []
        """List of tuples for argument names and description."""
        self.raises: list[tuple[str, str]] = []
        """List of tuples for exception names and condition."""
        self.attributes: list[tuple[str, str]] = []
        """List of tuples for attribute names and description."""

        if len(lines) > 0 and lines[0] not in ("Args:", "Raises:", "Attributes:"):
            self.summary = lines[0]
            lines.pop(0)

        collect = ""
        for line in lines:
            if collect != "":
                if line == "":
                    collect = ""
                    continue
                if collect == "args":
                    collector = self.args
                elif collect == "raises":
                    collector = self.raises
                elif collect == "attributes":
                    collector = self.attributes
                else:
                    raise SyntaxError
                if ":" in line:
                    arg, desc = line.split(":")
                    collector.append((arg.lstrip(), desc.lstrip()))
                else:
                    v = collector[-1]
                    collector[-1] = (v[0], v[1] + line.lstrip())

            elif line == "Args:":
                collect = "args"
            elif line == "Raises:":
                collect = "raises"
            elif line == "Attributes:":
                collect = "attributes"
            else:
                if not self.description:
                    self.description = ""
                self.description = self.description + "\n" + line

    def __rich_repr__(self) -> RichReprResult:
        yield "summary", self.summary, None
        yield "description", self.description, None
        yield "args", self.args, []

    __rich_repr__.angular = True  # type: ignore
