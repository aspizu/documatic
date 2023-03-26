import ast
from pathlib import Path

from . import doc
from .doc_string import DocString


class Transformer:
    """Extract documentation from Python source-code into documentation objects."""

    def __init__(self, module_path: Path):
        """
        Args:
          module_path: Path to a Python source-code file.
        """
        self.module_path = module_path
        self.source = module_path.read_text()
        self.module_name = module_path.stem

    def transform(self) -> doc.Module:
        """Transforms the Python module into a documentation object."""
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

    def collect_attributes(self, class_: ast.ClassDef, attributes: dict[str, str]):
        """Collect atribute doc-strings from a `ast.ClassDef` node into `attributes`

        Looks for atribute assignments in the class's __init__ function."""
        name = ""
        for class_child in ast.iter_child_nodes(class_):
            if (
                isinstance(class_child, ast.FunctionDef)
                and class_child.name == "__init__"
            ):
                for initfunc_child in ast.iter_child_nodes(class_child):
                    if isinstance(initfunc_child, ast.Assign) and isinstance(
                        initfunc_child.targets[0], ast.Attribute
                    ):
                        name = initfunc_child.targets[0].attr
                    elif isinstance(initfunc_child, ast.Expr) and isinstance(
                        initfunc_child.value, ast.Constant
                    ):
                        if name:
                            attributes[name] = initfunc_child.value.value
                            name = ""
            # FIXME: Collect doc-strings from top-level attribute assignments or type-hints.
            # elif isinstance(class_child, ast.Assign) and isinstance(
            #     class_child.targets[0], ast.Attribute
            # ):
            #     name = class_child.targets[0].attr
            # elif isinstance(class_child, ast.Expr) and isinstance(
            #     class_child.value, ast.Constant
            # ):
            #     if name:
            #         attributes[name] = class_child.value.value
            #         name = ""

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
