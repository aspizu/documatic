import shutil
import sys
from pathlib import Path

from . import DocumaticModule


def dirmod(path: Path, out_dir: Path):
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir()
    for file in path.iterdir():
        if file.suffix == ".py":
            with open(out_dir / (file.stem + ".md"), "w") as out:
                DocumaticModule(file, out)
        elif file.is_dir():
            dirmod(file, out_dir / file.stem)


dirmod(Path(sys.argv[1]), Path("docs"))
