import os
import platform
from pathlib import Path

# import pyyaml


subdir = "darwin" if platform.system() == "Darwin" else "linuxx"
path = Path(os.environ["HOME"]) / ".spack" / subdir / "compilers.yaml"
assert path.exists()
assert path.is_file()
compilers_contents = path.read_text(encoding="utf-8")
