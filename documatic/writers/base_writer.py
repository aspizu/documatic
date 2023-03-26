from __future__ import annotations

from typing import IO, Any, Callable

from .. import doc


class BaseWriter:
    """Generic class that provides basic functionality for rendering documentation to a file.

    Extend this class to create a writer that renders documentation in a specific format
    such as markdown or HTML. The `extension` attribute must be set to the file-extension
    of the output format.

    `BaseWriter.WithIndent` provides a way to use context managers to manage indentation.

    Basic usage example:
      >>> with self.indent():
      >>>     ...

    This will first increment the indentation level, and when the scope of the `with`
    statement ends it will decrement the indentation level.

    More functionality can be added by implementing a function that returns a
    `BaseWriter.WithIndent` object with proper `enter_callback` and `leave_callback`
    functions.
    """

    extension: str
    """The file extension used for the output files (For example: ".md")"""

    class WithIndent:
        def __init__(
            self,
            writer: BaseWriter,
            enter_callback: Callable[[], None],
            leave_callback: Callable[[], None],
        ):
            """
            Args:
              enter_callback: Function to be called before indenting.
              leave_callback: Function to be called after dedenting.
            """
            self.enter_callback = enter_callback
            """Function to be called before indenting."""
            self.leave_callback = leave_callback
            """Function to be called after dedenting."""
            self.writer = writer

        def __enter__(self):
            self.enter_callback()
            self.writer.indent_level += 1

        def __exit__(self, *args: Any):
            self.writer.indent_level -= 1
            self.leave_callback()

    def __init__(self, module: doc.Module, file: IO[str], indent_width: int = 4):
        """
        Args:
          module: The module object whose documentation is to be rendered.
          file: Output file the documentation is rendered into.
          indent_width: The number of spaces to use for each level of indentation. Defaults to 4.
        """
        self.module = module
        """The module object whose documentation is to be rendered."""
        self.file = file
        """Output file the documentation is rendered into."""
        self.indent_level = 0
        """Current level of indentation."""
        self.indent_width = indent_width
        """The number of spaces to use for each level of indentation."""

    def write(self, string: str) -> None:
        """
        Write a string into the output file. The current indentation level will be
        inserted after each newline character in the string.
        """
        indentation = self.indent_level * self.indent_width * " "
        string = string.replace("\n", "\n" + indentation)
        self.file.write(string)

    def writeln(self, string: str) -> None:
        """
        Write a line into the output file. The current indentation level will be
        inserted before the line and after each newline character. A newline character
        will be appended to the end of the line.
        """
        indentation = self.indent_level * self.indent_width * " "
        string = string.replace("\n", "\n" + indentation)
        self.file.write(indentation + string + "\n")

    def indent(
        self,
        enter_callback: Callable[[], None] = (lambda: None),
        leave_callback: Callable[[], None] = (lambda: None),
    ):
        """Returns a `BaseWriter.WithIndent` object to be used in a `with` statement.

        Args:
          enter_callback: Function to be called before indenting.
          leave_callback: Function to be called after dedenting.
        """
        return BaseWriter.WithIndent(self, enter_callback, leave_callback)
