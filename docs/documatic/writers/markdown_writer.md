**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# markdown_writer


 - [MarkdownWriter](#MarkdownWriter)



# `MarkdownWriter`


```py

class MarkdownWriter:
    ...
```

Writer for markdown.


This class implements a Writer for rendering documentation in the markdown format.
As doc-string descriptions are written in markdown, it will simply render them as-is.


## `__init__`


```py

def __init__(self, module: doc.Module, file: IO[str]):
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

