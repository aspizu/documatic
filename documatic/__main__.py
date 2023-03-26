import argparse
import shutil
from pathlib import Path

from .transformer import Transformer
from .writers import MarkdownWriter, WriterType, available_writers


def main_command(
    input: Path | None,
    output: Path | None = None,
    writer: WriterType | None = None,
):
    if writer is None:
        writer = MarkdownWriter
    if input is None:
        for initfile in Path().glob("*/__init__.py"):
            input = initfile.parent
            break
        else:
            raise FileNotFoundError
    if output is None:
        output = Path("docs")
    shutil.rmtree(output, ignore_errors=True)
    output.mkdir(exist_ok=True)
    render_package(input, output, writer)


def render_package(input: Path, output: Path, writer: WriterType):
    print(f" - Rendering documentation for package: {input}")
    dir = output / input.stem
    dir.mkdir()
    for module in input.glob("*.py"):
        print(f" >>> - Rendering documentation for module: {module}")
        with (dir / f"{module.stem}{writer.extension}").open("w") as file:
            writer(Transformer(module).transform(), file)
    for subpackage in input.iterdir():
        if subpackage.is_dir() and (subpackage / "__init__.py").is_file():
            render_package(subpackage, dir, writer)


class Application(argparse.ArgumentParser):
    def __init__(self) -> None:
        super().__init__(
            prog="documatic",
            description="Easy to use documentation generator for Python.",
        )
        self.add_argument(
            "--input",
            type=self.parse_input,
            help=(
                "Path to a directory containing a Python package. "
                "This directory must contain an __init__.py file."
            ),
            default=None,
        )
        self.add_argument(
            "--output",
            type=self.parse_output,
            help="Path to a directory to render documentation into. Will be cleared. Defaults to docs/",
            default=Path("docs"),
        )
        self.add_argument(
            "--writer",
            help=(
                f"Writer used to render documentation files. "
                f"Available writers: {', '.join(available_writers.keys())}. "
                f"Defaults to MarkdownWriter."
            ),
            default=None,
        )
        namespace = self.parse_args()

        input: Path | None = namespace.input
        output: Path | None = namespace.output
        writer = available_writers[namespace.writer] if namespace.writer else None

        main_command(input, output, writer)

    def parse_input(self, argument: str) -> Path:
        path = Path(argument)
        if not path.exists():
            self.error(f"{path} does not exist.")
        if not path.is_dir():
            self.error(f"{path} is not a directory.")
        if not (path / "__init__.py").is_file():
            self.error(f"{path} does not contain an __init__.py file.")
        return path

    def parse_output(self, argument: str) -> Path:
        path = Path(argument)
        if path.exists() and not path.is_dir():
            self.error(f"{path} is not a directory.")
        return path


application = Application()
