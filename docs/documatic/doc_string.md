**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# doc_string


 - [DocString](#DocString)



# `DocString`


```py

class DocString:
    ...
```

A class for parsing and storing information from a docstring.





### Attributes:

 - `summary`: The summary of the docstring, which is the first line of the docstring.

 - `description`: The description of the docstring, which is everything after the summary.

 - `returns`: The description of the return value specified in the docstring.



## `__init__`


```py

def __init__(self, doc: str, attributes: dict[str, str] | None):
    ...
```

Parse a google formatted doc-string.


### Arguments:

 - `doc`: The docstring to be parsed.

 - `attributes`: A dictionary of additional attributes. Defaults to None.



## `parse`


```py

def parse(self, doc: str):
    ...
```

