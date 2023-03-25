from typing import IO

from .. import doc


class BaseWriter:
    def __init__(self, module: doc.Module, file: IO[str], indent_width: int = 4):
        self.module = module
        self.file = file
        self.indent_level = 0
        self.indent_width = indent_width

    def write(self, string: str) -> None:
        self.file.write(string)

    def indent_write(self, string: str) -> None:
        indentation = self.indent_level * self.indent_width * " "
        self.file.write(indentation + string)

    def indent(self) -> None:
        self.indent_level += 1

    def dedent(self) -> None:
        self.indent_level -= 1
