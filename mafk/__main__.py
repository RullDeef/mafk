"""Usage: mafk command

    Where command is one of:
        new <proj>          generates new project
        build               builds current project
        clear               clears object files
"""

import sys
from mafk import new, build, clean

if len(sys.argv) == 1:
    print(__doc__)
elif sys.argv[1] == "new":
    new.project(sys.argv[2:])
elif sys.argv[1] == "build":
    build.project()
elif sys.argv[1] in ("clean", "clear"):
    clean.all()
else:
    print("no matching command found.")
    exit(1)
