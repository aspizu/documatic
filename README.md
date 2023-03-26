# Documatic

Easy to use documentation generator for [Python](https://www.python.org/)
projects.

Documatic is an easy-to-use documentation generator for Python that helps
developers generate documentation for their Python packages. This documentation
generator supports both HTML and [Markdown](https://daringfireball.net/projects/markdown/)
output, with the default output being Markdown.

Check out documatic's [documentation](/docs/documatic) generated by itself.

- [Basic usage example](#basic-usage-example)
- [Installation](#installation)
- [Using the command-line](#using-the-command-line)

## Basic usage example

After installing Documatic, you can generate the documentation for your Python
package just by running documatic in the root of your repository.

```
python -m documatic
```

That's it, no configuration needed - it will create a docs directory with the
documentation.

## Installation

To install Documatic, clone the repository from GitHub:

```
git clone https://github.com/aspizu/documatic
```

Install it using [pip](https://pypi.org/project/pip/):

```
cd documatic
pip install -e .
```

To use the HTMLWriter, you need to install the [markdown-it-py](https://github.com/executablebooks/markdown-it-py)
library:

```
pip install markdown-it-py
```

## Using the command-line

### Options:

- `-h, --help` - show the **help** message and exit
- `--input INPUT` - Path to a **directory** containing a Python package. This directory must contain an `__init__.py` file.
- `--output OUTPUT` - Path to a **directory** to render documentation into. Will be cleared. Defaults to `docs/`
- `--writer WRITER` - **Writer** used to render documentation files. Available writers: `HTMLWriter`, `MarkdownWriter`. Defaults to `MarkdownWriter`.

# Notes

The module responsible for parsing documentation, [doc_string](/documatic/doc_string.py),
has limitations and requires a strict format where sections are indented with 2
spaces and the summary is the first line of the description.

Unfortunately, using [ast](https://docs.python.org/3/library/ast.html) alone
does not allow for the inference of function return types unless a type-hint is
present in the signature. However, I have ideas for using the language server
from [pyright](https://github.com/microsoft/pyright) to get more information
about the code.

Additionally, the [HTMLWriter](/documatic/writers/html_writer.py) is unfinished
and does not have any styling.
