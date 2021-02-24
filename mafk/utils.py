from glob import glob
from pathlib import Path

def walk_up(path: Path, top: Path):
    path = Path(path).absolute()
    top = Path(top).absolute()

    while path != top:
        yield path
        path = path.parent

def find_walk_up(pattern, startpath, endpath):
    for path in walk_up(startpath, endpath):
        for file in path.glob(pattern):
            return file

class Config:
    __loaded_cfg = None

    def __init__(self):
        self.cc = "gcc"
        self.std = "c99"
        self.projpath = Path().absolute()
        self.target = self.projpath.name

        self.cflags = ["-Wall", "-Wextra", "-Wpedantic", "-Wvla"]

    @staticmethod
    def loadfile(filepath):
        filepath = Path(filepath).absolute()

        cfg = Config()
        cfg.projpath = filepath.parent

        for line in open(filepath, "rt"):
            tokens = line.split()
            if len(tokens) == 0:
                continue
            elif tokens[0].upper() == "USE":
                cfg.cc = tokens[1]
            elif tokens[0].upper() == "STD":
                cfg.std = tokens[1]
            elif tokens[0].upper() == "TARGET":
                cfg.target = tokens[1]

        return cfg

    # loads config from some file named *.fmk or *.mafk
    @staticmethod
    def load():
        cfg = Config()

        files = list(glob("*.mfk"))
        if len(files) > 1:
            print("there must be exactly one mafk configuration file in one project.")
            exit(2)
        elif len(files) == 1:
            cfg = Config.loadfile(files[0])
        else:
            filepath = find_walk_up("*.mfk", ".", Path().absolute().root)
            if filepath is not None:
                # print("could not find any mafk config file. Using from above.")
                cfg = Config.loadfile(filepath)
            else:
                print("could not find any mafk config file. Using from template.")

        return cfg

    # loads config from file or returns cached config
    @staticmethod
    def get():
        if Config.__loaded_cfg is None:
            Config.__loaded_cfg = Config.load()
        return Config.__loaded_cfg
