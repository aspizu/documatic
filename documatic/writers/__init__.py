from typing import Type

from .base_writer import BaseWriter
from .html_writer import HTMLWriter
from .markdown_writer import MarkdownWriter

__all__ = ["BaseWriter", "HTMLWriter", "MarkdownWriter"]

WriterType = Type[BaseWriter]
"""Accepts any writer class including `BaseWriter`."""

available_writers = {
    "HTMLWriter": HTMLWriter,
    "MarkdownWriter": MarkdownWriter,
}
"""A dict of available writers to choose from. key is name of writer class."""
