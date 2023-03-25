**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# html_writer


 - [HTMLWriter](#HTMLWriter)



## `md_render`


```py

def md_render(text: str) -> str:
    ...
```

# `HTMLWriter`


```py

class HTMLWriter:
    ...
```

## `__init__`


```py

def __init__(self, module: doc.Module, file: IO[str]):
    ...
```

## `itag`


```py

def itag(self, opening_tag: str):
    ...
```

## `tag`


```py

def tag(self, opening_tag: str, content: str):
    ...
```

## `write_module`


```py

def write_module(self, module: doc.Module):
    ...
```

## `write_class`


```py

def write_class(self, class_: doc.Class):
    ...
```

## `write_function`


```py

def write_function(self, function: doc.Function):
    ...
```

