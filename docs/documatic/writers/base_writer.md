**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# base_writer


 - [BaseWriter](#BaseWriter)

     - [BaseWriter.WithIndent](#BaseWriterWithIndent)
    


# `BaseWriter`


```py

class BaseWriter:
    ...
```

Generic class that provides basic functionality for rendering documentation to a file.


Extend this class to create a writer that renders documentation in a specific format
such as markdown or HTML. The `extension` attribute must be set to the file-extension
of the output format.

`BaseWriter.WithIndent` provides a way to use context managers to manage indentation.

Basic usage example:
```py
>>> with self.indent():
>>>     ...
```

This will first increment the indentation level, and when the scope of the `with`
statement ends it will decrement the indentation level.

More functionality can be added by implementing a function that returns a
`BaseWriter.WithIndent` object with proper `enter_callback` and `leave_callback`
functions.


### Attributes:

 - `module`: The module object whose documentation is to be rendered.

 - `file`: Output file the documentation is rendered into.

 - `indent_level`: Current level of indentation.

 - `indent_width`: The number of spaces to use for each level of indentation.



# `BaseWriter.WithIndent`


```py

class WithIndent:
    ...
```

### Attributes:

 - `enter_callback`: Function to be called before indenting.

 - `leave_callback`: Function to be called after dedenting.



## `__init__`


```py

def __init__(self, writer: BaseWriter, enter_callback: Callable[[], None], leave_callback: Callable[[], None]):
    ...
```

Args:


enter_callback: Function to be called before indenting.
 leave_callback: Function to be called after dedenting.


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

Args:


module: The module object whose documentation is to be rendered.
 file: Output file the documentation is rendered into.
 indent_width: The number of spaces to use for each level of indentation. Defaults to 4.


## `write`


```py

def write(self, string: str) -> None:
    ...
```

Write a string into the output file. The current indentation level will be


nserted after each newline character in the string.


## `writeln`


```py

def writeln(self, string: str) -> None:
    ...
```

Write a line into the output file. The current indentation level will be


nserted before the line and after each newline character. A newline character
will be appended to the end of the line.


## `indent`


```py

def indent(self, enter_callback: Callable[[], None], leave_callback: Callable[[], None]):
    ...
```

Returns a `BaseWriter.WithIndent` object to be used in a `with` statement.


### Arguments:

 - `enter_callback`: Function to be called before indenting.

 - `leave_callback`: Function to be called after dedenting.



