import os
import pathlib

# creates template .mfk configuration file
def template(filepath, target):
    with open(filepath, "wt") as file:
        file.write(f"""\
TARGET {target}
USE gcc
STD c99
""")

def project(args):
    if len(args) == 0:
        print("specify the name for the project")
        exit(2)

    path, args = args[0], args[1:]
    path = pathlib.Path(path)

    os.makedirs(path)
    os.makedirs(path / "src")

    template(path / "config.mfk", path.name)

    print("initialized new project")
