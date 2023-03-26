from typing import IO

from markdown_it import MarkdownIt

from .. import doc
from . import BaseWriter

md = MarkdownIt("commonmark", {"breaks": True, "html": True}).enable("table")


def md_render(text: str) -> str:
    html = md.render(text)  # type: ignore
    if html[-1] == "\n":
        return html[:-1]
    return html


class HTMLWriter(BaseWriter):
    """Writer for HTML.

    This class implements a Writer for rendering documentation in the HTML format.
    As doc-string descriptions are written in markdown, `markdown-it-py` is used
    to render the markdown text into HTML.

    A stylesheet link with the url `/style.css` will be added.
    """

    extension = ".html"

    def __init__(self, module: doc.Module, file: IO[str]):
        super().__init__(module, file, indent_width=0)
        self.write_module(self.module)

    def itag(self, opening_tag: str):
        closing_tag = opening_tag.split(" ")[0]
        return self.indent(
            lambda: self.writeln(f"<{opening_tag}>"),
            lambda: self.writeln(f"</{closing_tag}>"),
        )

    def tag(self, opening_tag: str, content: str = ""):
        closing_tag = opening_tag.split(" ")[0]
        self.writeln(f"<{opening_tag}>{content}</{closing_tag}>")

    def write_module(self, module: doc.Module):
        def write_index(node: doc.Module | doc.Class):
            if node.classes:
                with self.itag("ul"):
                    for class_ in node.classes.values():
                        self.tag("li", f'<a href="#">{class_.name}</a>')
                        write_index(class_)

        self.writeln("<!DOCTYPE html>")
        with self.itag('html lang="en"'):
            with self.itag("head"):
                self.writeln('<meta charset="UTF-8" />')
                self.writeln('<meta http-equiv="X-UA-Compatible" content="IE=edge" />')
                self.writeln(
                    '<meta name="viewport" content="width=device-width, initial-scale=1.0" />'
                )
                self.writeln('<link rel="stylesheet" href="/style.css" />')
                self.tag("title", module.name)
            with self.itag("body"):
                self.tag("h1", module.name)
                if module.summary:
                    self.writeln(md_render(module.summary))
                if module.description:
                    self.writeln(md_render(module.description))
                write_index(module)
                for class_ in module.classes.values():
                    self.write_class(class_)

    def write_class(self, class_: doc.Class):
        self.tag("h1", f"<code>{class_.name}</code>")
        self.tag("pre", f"<code>{class_.signature}</code>")
        if class_.summary:
            self.writeln(md_render(class_.summary))
        if class_.description:
            self.writeln(md_render(class_.description))
        if class_.attributes:
            self.tag("h3", "Atributes:")
            with self.itag("ul"):
                for name, desc in class_.attributes.items():
                    self.tag("li", f"<code>{name}</code>: {desc}")
        for function in class_.functions.values():
            self.write_function(function)
        for subclass in class_.classes.values():
            self.write_class(subclass)

    def write_function(self, function: doc.Function):
        self.tag("h2", f"<code>{function.name}</code>")
        if function.summary:
            self.writeln(md_render(function.summary))
        if function.description:
            self.writeln(md_render(function.description))
        if function.arguments:
            self.tag("h3", "Args:")
            with self.itag("ul"):
                for name, desc in function.arguments.items():
                    self.tag("li", f"<code>{name}</code>: {desc}")
