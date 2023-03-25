**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# transformer


 - [Transformer](#Transformer)



# `Transformer`


```py

class Transformer:
    ...
```

## `__init__`


```py

def __init__(self, module_path: Path):
    ...
```

## `transform`


```py

def transform(self):
    ...
```

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

def collect_attributes(self, node: ast.ClassDef, attributes: dict[str, str]):
    ...
```

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





