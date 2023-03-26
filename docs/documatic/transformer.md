**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# transformer


 - [Transformer](#Transformer)



# `Transformer`


```py

class Transformer:
    ...
```

Extract documentation from Python source-code into documentation objects.





## `__init__`


```py

def __init__(self, module_path: Path):
    ...
```

### Arguments:

 - `module_path`: Path to a Python source-code file.



## `transform`


```py

def transform(self) -> doc.Module:
    ...
```

Transforms the Python module into a documentation object.





## `module`


```py

def module(self, node: ast.Module):
    ...
```

## `function`


```py

def function(self, node: ast.FunctionDef):
    ...
```

## `class_`


```py

def class_(self, node: ast.ClassDef, parents: str):
    ...
```

## `collect_attributes`


```py

def collect_attributes(self, class_: ast.ClassDef, attributes: dict[str, str]):
    ...
```

Collect atribute doc-strings from a `ast.ClassDef` node into `attributes`




Looks for atribute assignments in the class's __init__ function.


## `get_function_signature`


```py

def get_function_signature(self, node: ast.FunctionDef) -> str:
    ...
```

Returns the signature of a function node.





## `get_class_signature`


```py

def get_class_signature(self, node: ast.ClassDef) -> str:
    ...
```

Returns the signature of a class node.





