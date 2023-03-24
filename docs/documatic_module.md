# documatic_module

Class for rendering a module's documentation

# class `DocumaticModule`

```py
class DocumaticModule:
    ...
```

Traverse a module's AST and render documentation into `file`

 - `path`: Path to module's source code.

 - `source`: Text content of the module's source code.

 - `root`: Root node of the module's AST.

## method `DocumaticModule.__init__`

```py
def __init__(self, module_path: Path, file: IO[str]):
    ...
```

Traverse a module's AST and render documentation into `file`




### Arguments:

 - `module_path`: Path to module's source code.

 - `file`: The output file to render documentation into.

## method `DocumaticModule.write_docstring`

```py
def write_docstring(self, node: ast.ClassDef | ast.Module | ast.FunctionDef | ast.AsyncFunctionDef):
    ...
```

Render doc-string of a node.

## method `DocumaticModule.get_function_signature`

```py
def get_function_signature(self, node: ast.FunctionDef) -> str:
    ...
```

Returns the signature of a function node.

## method `DocumaticModule.get_class_signature`

```py
def get_class_signature(self, node: ast.ClassDef) -> str:
    ...
```

Returns the signature of a class node.

## method `DocumaticModule.write`

```py
def write(self, o: Any):
    ...
```

Alias to `self.file.write()` for convinence.

## method `DocumaticModule.module_all`

```py
def module_all(self, node: ast.AST):
    ...
```

Render all child nodes.

## method `DocumaticModule.class_all`

```py
def class_all(self, class_name: str, node: ast.AST):
    ...
```

Render all child nodes.

## method `DocumaticModule.module`

```py
def module(self, node: ast.Module):
    ...
```

Render documentation for a module node.

## method `DocumaticModule.function_def`

```py
def function_def(self, node: ast.FunctionDef):
    ...
```

Render documentation for a function node.

## method `DocumaticModule.method_def`

```py
def method_def(self, class_name: str, node: ast.FunctionDef):
    ...
```

Render documentation for a method node.

## method `DocumaticModule.class_def`

```py
def class_def(self, node: ast.ClassDef):
    ...
```

Render documentation for a class node.

