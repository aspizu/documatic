"""
Script to extract API from Python source-code, meant to be passed to Chat GPT for code
generation.
"""

import ast
import sys
from pathlib import Path


def get_function_signature(source: str, node: ast.FunctionDef) -> str:
    """Returns the signature of a function node."""
    args: list[str] = []
    for arg in node.args.args:
        end = ""
        if arg.annotation:
            annotation = ast.get_source_segment(source, arg.annotation)
            end = f": {annotation}"
        args.append(arg.arg + end)
    end = ""
    if node.returns:
        return_type = ast.get_source_segment(source, node.returns)
        end = f" -> {return_type}"
    return f"def {node.name}({', '.join(args)}){end}:\n    ..."


def get_class_signature(node: ast.ClassDef) -> str:
    """Returns the signature of a class node."""
    return f"class {node.name}:\n    ..."


source = Path(sys.argv[1]).read_text()
node = ast.parse(source)


def tabprint(s: str, indent: int) -> None:
    indentation = "    " * indent
    print(indentation + s.replace("\n", "\n" + indentation) + "\n", end="")


def foo(node: ast.AST, indent: int = 0):
    for child in ast.iter_child_nodes(node):
        if isinstance(child, ast.FunctionDef):
            tabprint(get_function_signature(source, child) + "\n", indent)
        elif isinstance(child, ast.ClassDef):
            tabprint(get_class_signature(child) + "\n", indent)
            foo(child, indent + 1)


foo(node)
