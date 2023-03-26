# Documatic

Easy to use documentation generator for Python projects.

Documatic is an easy-to-use documentation generator for Python that helps
developers generate documentation for their Python packages. This documentation
generator supports both HTML and Markdown output, with the default output being
Markdown.

- [Usage](#usage)
- [Installation](#installation)

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

Install it using `pip`:

```
cd documatic
pip install -e .
```

To use the HTMLWriter, you need to install the `markdown-it-py` library:

```
pip install markdown-it-py
```

## Using the command-line

### Options:

- `-h, --help` - show the **help** message and exit
- `--input INPUT` - Path to a **directory** containing a Python package. This directory must contain an `__init__.py` file.
- `--output OUTPUT` - Path to a **directory** to render documentation into. Will be cleared. Defaults to `docs/`
- `--writer WRITER` - **Writer** used to render documentation files. Available writers: `HTMLWriter`, `MarkdownWriter`. Defaults to `MarkdownWriter`.
