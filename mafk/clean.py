from mafk.utils import Config
import subprocess

def all():
    executable = Config.get().target + ".exe"
    subprocess.call(["rm", "-rf", "obj", executable])
