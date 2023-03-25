from typing import IO

from .. import doc
from . import BaseWriter


class MarkdownWriter(BaseWriter):
    def __init__(self, module: doc.Module, file: IO[str]):
        super().__init__(module, file)
        self.write_module(self.module)

    def write_module(self, module: doc.Module):
        self.writeln(
            f"**Auto-generated** using [documatic](https://github.com/aspizu/documatic)\n\n"
        )
        self.writeln(f"# {module.name}\n\n")

        def index_class(node: doc.Module | doc.Class):
            with self.indent():
                for class_ in node.classes.values():
                    self.writeln(
                        f" - [{class_.name}](#{class_.name.replace('.','')})\n"
                    )
                    index_class(class_)

        self.indent_level -= 1
        index_class(module)
        self.indent_level += 1
        self.writeln("\n")

        for function in module.functions.values():
            self.write_function(function)

        for class_ in module.classes.values():
            self.write_class(class_)

    def write_class(self, class_: doc.Class):
        self.writeln(f"# `{class_.name}`\n\n")
        self.writeln("```py\n")
        self.write(class_.signature)
        self.writeln("\n```\n")
        if class_.summary:
            self.writeln(class_.summary + "\n\n")
        if class_.description:
            self.writeln(class_.description + "\n")
        if class_.attributes:
            self.writeln("### Attributes:\n")
            for name, desc in class_.attributes.items():
                self.writeln(f" - `{name}`: {desc}\n")
            self.writeln("\n")
        for subclass in class_.classes.values():
            self.write_class(subclass)
        for function in class_.functions.values():
            self.write_function(function)

    def write_function(self, function: doc.Function):
        self.writeln(f"## `{function.name}`\n\n")
        self.writeln("```py\n")
        self.write(function.signature)
        self.writeln("\n```\n")
        if function.summary:
            self.writeln(function.summary + "\n\n")
        if function.description:
            self.writeln(function.description + "\n")
        if function.arguments:
            self.writeln("### Arguments:\n")
            for name, desc in function.arguments.items():
                self.writeln(f" - `{name}`: {desc}\n")
            self.writeln("\n")
        if function.returns:
            self.writeln("### Returns:\n")
            self.writeln(function.returns + "\n")
        if function.exceptions:
            self.writeln("### Raises:\n")
            for name, desc in function.exceptions.items():
                self.writeln(f" - `{name}`: {desc}\n")
            self.writeln("\n")
