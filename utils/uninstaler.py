import os
import shutil

def uninstaler(path):
    cwd = path
    inside = os.listdir(cwd)
    for file in inside:
        if os.path.isfile(os.path.join(cwd, file)):
            if file != "main.py":
                os.remove(os.path.join(cwd, file))
        elif os.path.isdir(os.path.join(cwd, file)):
            if file != "os":
                shutil.rmtree(os.path.join(cwd, file))