import ast
from pathlib import Path

from . import doc
from .doc_string import DocString


class Transformer:
    def __init__(self, module_path: Path):
        self.module_path = module_path
        self.source = module_path.read_text()
        self.module_name = module_path.stem

    def transform(self):
        return self.module(ast.parse(self.source))

    def module(self, node: ast.Module):
        _docstring = ast.get_docstring(node)
        summary = None
        description = None
        functions = {}
        classes = {}
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.FunctionDef):
                functions[child.name] = self.function(child)
            elif isinstance(child, ast.ClassDef):
                classes[child.name] = self.class_(child, "")
        if _docstring:
            docstring = DocString(_docstring)
            summary = docstring.summary
            description = docstring.description
        return doc.Module(self.module_name, summary, description, classes, functions)

    def function(self, node: ast.FunctionDef):
        _docstring = ast.get_docstring(node)
        summary = None
        description = None
        arguments = {}
        returns = None
        exceptions = {}
        if _docstring:
            docstring = DocString(_docstring)
            summary = docstring.summary
            description = docstring.description
            arguments = docstring.arguments
            returns = docstring.returns
            exceptions = docstring.exceptions
        return doc.Function(
            node.name,
            summary,
            description,
            arguments,
            returns,
            exceptions,
            self.get_function_signature(node),
        )

    def class_(self, node: ast.ClassDef, parents: str):
        _docstring = ast.get_docstring(node)
        summary = None
        description = None
        attributes = {}
        functions = {}
        classes = {}
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.FunctionDef):
                functions[child.name] = self.function(child)
            elif isinstance(child, ast.ClassDef):
                classes[child.name] = self.class_(child, parents + node.name + ".")
        if _docstring:
            docstring = DocString(_docstring)
            summary = docstring.summary
            description = docstring.description
            attributes = docstring.attributes
        self.collect_attributes(node, attributes)
        return doc.Class(
            parents + node.name,
            summary,
            description,
            attributes,
            functions,
            classes,
            self.get_class_signature(node),
        )

    def collect_attributes(self, node: ast.ClassDef, attributes: dict[str, str]):
        name = ""
        for initfunc in ast.iter_child_nodes(node):
            if isinstance(initfunc, ast.FunctionDef) and initfunc.name == "__init__":
                for stmt in ast.iter_child_nodes(initfunc):
                    if isinstance(stmt, ast.Assign) and isinstance(
                        stmt.targets[0], ast.Attribute
                    ):
                        name = stmt.targets[0].attr
                    elif isinstance(stmt, ast.Expr) and isinstance(
                        stmt.value, ast.Constant
                    ):
                        if name:
                            attributes[name] = stmt.value.value
                            name = ""

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
