from typing import IO

from .. import doc
from . import BaseWriter


class MarkdownWriter(BaseWriter):
    def __init__(self, module: doc.Module, file: IO[str]):
        super().__init__(module, file)
        self.write_module(self.module)

    def write_module(self, module: doc.Module):
        self.indent_write(
            f"**Auto-generated** using [documatic](https://github.com/aspizu/documatic)\n\n"
        )
        self.indent_write(f"# {module.name}\n\n")

        def index_class(node: doc.Module | doc.Class):
            self.indent()
            for class_ in node.classes.values():
                self.indent_write(
                    f" - [{class_.name}](#{class_.name.replace('.','')})\n"
                )
                index_class(class_)
            self.dedent()

        self.dedent()
        index_class(module)
        self.indent()
        self.indent_write("\n")

        for function in module.functions.values():
            self.write_function(function)

        for class_ in module.classes.values():
            self.write_class(class_)

    def write_class(self, class_: doc.Class):
        self.indent_write(f"# `{class_.name}`\n\n")
        self.indent_write("```py\n")
        self.write(class_.signature)
        self.indent_write("\n```\n")
        if class_.summary:
            self.indent_write(class_.summary + "\n\n")
        if class_.description:
            self.indent_write(class_.description + "\n")
        if class_.attributes:
            self.indent_write("### Attributes:\n")
            for name, desc in class_.attributes.items():
                self.indent_write(f" - `{name}`: {desc}\n")
            self.indent_write("\n")
        for subclass in class_.classes.values():
            self.write_class(subclass)
        for function in class_.functions.values():
            self.write_function(function)

    def write_function(self, function: doc.Function):
        self.indent_write(f"## `{function.name}`\n\n")
        self.indent_write("```py\n")
        self.write(function.signature)
        self.indent_write("\n```\n")
        if function.summary:
            self.indent_write(function.summary + "\n\n")
        if function.description:
            self.indent_write(function.description + "\n")
        if function.arguments:
            self.indent_write("### Arguments:\n")
            for name, desc in function.arguments.items():
                self.indent_write(f" - `{name}`: {desc}\n")
            self.indent_write("\n")
        if function.returns:
            self.indent_write("### Returns:\n")
            self.indent_write(function.returns + "\n")
        if function.exceptions:
            self.indent_write("### Raises:\n")
            for name, desc in function.exceptions.items():
                self.indent_write(f" - `{name}`: {desc}\n")
            self.indent_write("\n")
