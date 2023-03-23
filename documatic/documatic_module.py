"""Class for rendering a module's documentation"""

import ast
from pathlib import Path
from typing import IO, Any

from rich import print  # type: ignore

from .doc_string import DocString


class DocumaticModule:
    """Traverse a module's AST and render documentation into `file`"""

    def __init__(self, module_path: Path, file: IO[str]):
        """
        Args:
            module_path: Path to module's source code.
            file: The output file to render documentation into.

        Returns: Nothing.

        Raises:
            FileNotFoundError: If the module's file is not found.
        """
        self.path = module_path
        """Path to module's source code."""
        self.source = module_path.read_text()
        """Text content of the module's source code."""
        self.root = ast.parse(self.source)
        """Root node of the module's AST."""
        self.module_name = module_path.stem
        self.file = file
        """The output file to render documentation into."""
        self.module(self.root)

    def write_docstring(
        self,
        node: ast.ClassDef | ast.Module | ast.FunctionDef | ast.AsyncFunctionDef,
    ):
        """Render doc-string of a node."""
        _docstring = ast.get_docstring(node)
        if _docstring:
            docstring = DocString(_docstring)
            if docstring.summary:
                self.write(docstring.summary + "\n\n")
            if docstring.description:
                self.write(docstring.description + "\n\n")
            if docstring.args:
                self.write(f"### Arguments:\n\n")
            for name, desc in docstring.args:
                self.write(f" - `{name}`: {desc}\n\n")
            if docstring.attributes:
                self.write(f"### Attributes:\n\n")
            for name, desc in docstring.attributes:
                self.write(f" - `{name}`: {desc}\n\n")
            if docstring.raises:
                self.write(f"### Raises:\n\n")
            for name, desc in docstring.raises:
                self.write(f" - `{name}`: {desc}\n\n")

    def get_function_signature(self, node: ast.FunctionDef) -> str:
        """Returns the signature of a function node."""
        args: list[str] = []
        for arg in node.args.args:
            end = ""
            if arg.annotation:
                annotation = ast.get_source_segment(self.source, arg.annotation)
                end = f": {annotation}"
            args.append(arg.arg + end)
        end = ""
        if node.returns:
            return_type = ast.get_source_segment(self.source, node.returns)
            end = f" -> {return_type}"
        return f"def {node.name}({', '.join(args)}){end}:\n    ..."

    def get_class_signature(self, node: ast.ClassDef) -> str:
        """Returns the signature of a class node."""
        return f"class {node.name}:\n    ..."

    def write(self, o: Any):
        """Alias to `self.file.write()` for convinence."""
        self.file.write(str(o))

    def module_all(self, node: ast.AST):
        """Render all child nodes."""
        for node in ast.iter_child_nodes(node):
            if isinstance(node, ast.FunctionDef):
                self.function_def(node)
            if isinstance(node, ast.ClassDef):
                self.class_def(node)

    def class_all(self, class_name: str, node: ast.AST):
        """Render all child nodes."""
        for node in ast.iter_child_nodes(node):
            if isinstance(node, ast.FunctionDef):
                self.method_def(class_name, node)
            if isinstance(node, ast.ClassDef):
                self.class_def(node)

    def module(self, node: ast.Module):
        """Render documentation for a module node."""
        self.write(f"# {self.module_name}\n\n")
        self.write_docstring(node)
        self.module_all(self.root)

    def function_def(self, node: ast.FunctionDef):
        """Render documentation for a function node."""
        self.write(f"## function `{node.name}`\n\n")
        self.write(f"```py\n{self.get_function_signature(node)}\n```\n\n")
        self.write_docstring(node)

    def method_def(self, class_name: str, node: ast.FunctionDef):
        """Render documentation for a method node."""
        self.write(f"## method `{class_name}.{node.name}`\n\n")
        self.write(f"```py\n{self.get_function_signature(node)}\n```\n\n")
        self.write_docstring(node)

    def class_def(self, node: ast.ClassDef):
        """Render documentation for a class node."""
        self.write(f"# class `{node.name}`\n\n")
        self.write(f"```py\n{self.get_class_signature(node)}\n```\n\n")
        self.write_docstring(node)
        self.class_all(node.name, node)
