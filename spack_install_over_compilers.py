import os
import platform
import subprocess as sp
from pathlib import Path
from typing import List

import yaml


def get_compiler_specs() -> List[str]:
    subdir = "darwin" if platform.system() == "Darwin" else "linux"
    path = Path(os.environ["HOME"]) / ".spack" / subdir / "compilers.yaml"
    assert path.exists()
    assert path.is_file()
    compilers_contents_str = path.read_text(encoding="utf-8")
    compilers_contents = yaml.safe_load(compilers_contents_str)
    # from pprint import pprint
    specs = list()
    for compiler_dict in compilers_contents["compilers"]:
        compiler_inner_dict = compiler_dict["compiler"]
        # pprint(compiler_inner_dict)
        spec = compiler_inner_dict["spec"]
        specs.append(spec)
    return specs


if __name__ == "__main__":
    specs = get_compiler_specs()
    for spec in specs:
        _ = sp.run(["spack", "install", "berkeley-db", f"%{spec}"])
