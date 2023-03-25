**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# base_writer


 - [BaseWriter](#BaseWriter)

     - [BaseWriter.WithIndent](#BaseWriterWithIndent)
    


# `BaseWriter`


```py

class BaseWriter:
    ...
```

# `BaseWriter.WithIndent`


```py

class WithIndent:
    ...
```

## `__init__`


```py

def __init__(self, writer: BaseWriter, enter_callback: Callable[[], None], leave_callback: Callable[[], None]):
    ...
```

## `__enter__`


```py

def __enter__(self):
    ...
```

## `__exit__`


```py

def __exit__(self):
    ...
```

## `__init__`


```py

def __init__(self, module: doc.Module, file: IO[str], indent_width: int):
    ...
```

## `write`


```py

def write(self, string: str) -> None:
    ...
```

## `writeln`


```py

def writeln(self, string: str) -> None:
    ...
```

## `indent`


```py

def indent(self, enter_callback: Callable[[], None], leave_callback: Callable[[], None]):
    ...
```

