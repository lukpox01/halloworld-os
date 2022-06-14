import os, signal
import shutil
import requests
import zipfile
import sys
import io

class Updater:
    def __init__(self, latest_version):
        self.latest_version = latest_version

    def update(self):
        response = requests.get(
            f"https://github.com/lukas-beep/halloworld-os/releases/download/{self.latest_version}/halloworld-os.zip"
        )
        zipfile_ = zipfile.ZipFile(io.BytesIO(response.content))
        cwd = os.getcwd()
        self.uninstaler(cwd)
        zipfile_.extractall(cwd)
     
     
    def uninstaler(self, path):
        cwd = path
        e_path = path.split("\\")[-1]
        if e_path != "halloworld-os":
            sys.exit("please run this script in the main directory")
        inside = os.listdir(cwd)
        for file in inside:
            if os.path.isfile(os.path.join(cwd, file)):
                if file != "updater.exe":
                    os.remove(os.path.join(cwd, file))
            elif os.path.isdir(os.path.join(cwd, file)):
                if file != "os":
                    shutil.rmtree(os.path.join(cwd, file))
                    
Updater(sys.argv[1]).update()# sys.argv[1] is the latest version