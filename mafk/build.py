import os, subprocess

from pathlib import Path
from mafk.utils import Config

def object(srcpath: Path):
    cfg = Config.get()

    dirpath = Path(srcpath).parent.absolute().relative_to(cfg.projpath)
    dirpath = "obj" / Path("/".join(dirpath.parts[1:]))
    dirpath = dirpath.absolute()
    filename = (dirpath / srcpath.stem).with_suffix(".o")

    os.makedirs(dirpath, exist_ok=True)
    subprocess.call([cfg.cc, "-std=" + cfg.std] + cfg.cflags + ["-o", filename, "-c", srcpath])
    print("compiled:", filename.name)

def project():
    cfg = Config.get()
    cfg: Config

    # compile each object file
    for srcname in cfg.projpath.rglob("*.c"):
        object(srcname)

    # link all object files together
    objs = list(map(lambda p: Path(p).absolute().relative_to(cfg.projpath), (cfg.projpath / "obj").rglob("*.o")))
    subprocess.call([cfg.cc, "-o", cfg.target] + objs)
    print("linked:", cfg.target)
