from __future__ import annotations

from typing import IO, Any, Callable

from .. import doc


class BaseWriter:
    class WithIndent:
        def __init__(
            self,
            writer: BaseWriter,
            enter_callback: Callable[[], None],
            leave_callback: Callable[[], None],
        ):
            self.enter_callback = enter_callback
            self.leave_callback = leave_callback
            self.writer = writer

        def __enter__(self):
            self.enter_callback()
            self.writer.indent_level += 1

        def __exit__(self, *args: Any):
            self.writer.indent_level -= 1
            self.leave_callback()

    def __init__(self, module: doc.Module, file: IO[str], indent_width: int = 4):
        self.module = module
        self.file = file
        self.indent_level = 0
        self.indent_width = indent_width

    def write(self, string: str) -> None:
        indentation = self.indent_level * self.indent_width * " "
        string = string.replace("\n", "\n" + indentation)
        self.file.write(string)

    def writeln(self, string: str) -> None:
        indentation = self.indent_level * self.indent_width * " "
        string = string.replace("\n", "\n" + indentation)
        self.file.write(indentation + string + "\n")

    def indent(
        self,
        enter_callback: Callable[[], None] = (lambda: None),
        leave_callback: Callable[[], None] = (lambda: None),
    ):
        return BaseWriter.WithIndent(self, enter_callback, leave_callback)
