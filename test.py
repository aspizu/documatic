from pathlib import Path

from documatic.transformer import Transformer
from documatic.writers import MarkdownWriter

for each in Path("test").glob("*.md"):
    each.unlink(missing_ok=True)

for each in Path("test").glob("*.py"):
    with open(f"test/{each.stem}.md", "w") as file:
        MarkdownWriter(Transformer(each).transform(), file)
