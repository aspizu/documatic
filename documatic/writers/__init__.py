from typing import Type

from .base_writer import BaseWriter
from .html_writer import HTMLWriter
from .markdown_writer import MarkdownWriter

__all__ = ["BaseWriter", "HTMLWriter", "MarkdownWriter"]


WriterType = Type[BaseWriter]
