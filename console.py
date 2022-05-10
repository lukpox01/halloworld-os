import os
import time
import shutil


class Console:
    def __init__(self, path, user):
        self.user = user
        self.usr_path = path
        os.chdir(path)
        self.command = None
        self.sl_symobols = {"wfi": "[?] ", "wfc": "[{path}>] "}
        self.commands = {
            "mf": self.mf,
            "md": self.md,
            "cls": self.cls,
            "cd": self.cd,
            "exit": self.exit_,
            "ld": self.ld,
            "contentof": self.content_of_file,
            "rd": self.remove_dir,
            "rf": self.remove_file
        }
        self.commands_keys = self.commands.keys()

    def path_customizer(self, path):  # TODO more funcs
        path = path.replace("\\", "/")
        if path.find("~") != -1:
            path = path.replace("~", self.usr_path)
        else:
            path = os.path.join(os.getcwd(), path)

        path = path.replace("\\", "/")
        return path

    def getcwd(self):
        cwd = os.getcwd()
        cwd = cwd.split("\\")

        index = cwd.index(self.user)
        cwd = cwd[index:]
        cwd = os.path.join(*cwd)
        return cwd

    def command_input(self):
        while True:
            command = input(self.sl_symobols["wfc"].format(path=self.getcwd()))
            self.command = command.split(" ")
            clen = len(self.command)
            if self.command[0] in self.commands_keys:
                func = self.commands[self.command[0]]
                if clen == 1:
                    func()
                else:
                    func(*self.command[1:])

    def cls(self, *args):
        os.system("cls")

    def md(self, path, *args):
        path = self.path_customizer(path)

        custom_path = path.split("/")
        is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )
        if is_parent_dir:
            isdir = os.path.isdir(path)
            if isdir:
                print("Check again something went wrong (this dir already exists)")
            else:
                os.mkdir(path)
        else:
            print(
                "Check again something went wrong (you cant create multiple dirs at once)"
            )

    def mf(self, path, *args):
        path = self.path_customizer(path)
        custom_path = path.split("/")
        is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )
        if is_parent_dir:
            isdir = os.path.isfile(path)
            if isdir:
                print("Check again something went wrong (this file already exists)")
            else:
                f = open(path, "w")
                f.close()
        else:
            print("Check again something went wrong (this dir doesnt exists)")

    def cd(self, path, *args):
        path = self.path_customizer(path)
        isdir = os.path.isdir(path)
        if isdir:
            os.chdir(path)
        else:
            print("Check again something went wrong (this dir doesnt exists)")

    def ld(self, path=None, *args):  # TODO more dynamic
        if path == None:
            path = os.getcwd()
        else:
            path = self.path_customizer(path)
        isdir = os.path.isdir(path)
        if isdir:
            in_dir = os.listdir(path)
            print(" ")
            for i in in_dir:
                print(i)
            print(" ")
        else:
            print("Check again something went wrong (this dir does not exists)")

    def content_of_file(self, path, *args):
        path = self.path_customizer(path)
        custom_path = str(path).split("/")
        is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )
        if is_parent_dir:
            isfile = os.path.isfile(path)
            if isfile:
                with open(path, "r") as f:
                    content = f.readlines()
                    print(f"\nContent of file {custom_path[-1]}:\n")
                    for i in content:
                        print(i.rstrip())
                    print("")
            else:
                print("Check again something went wrong (this file doesnt exists)")

        else:
            print("Check again something went wrong (this dir doesnt exists)")

    def exit_(self, *args):
        print("Exiting...")
        time.sleep(1.20)
        self.cls()
        exit(0)

    def remove_file(self, path, *args): 
            
        path = self.path_customizer(path)
        custom_path = str(path).split("/")
        is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )
        if is_parent_dir:
            isfile = os.path.isfile(path)
            if isfile:
                os.remove(path)
            else:
                print("Check again something went wrong (this file doesnt exists)")

        else:
            print("Check again something went wrong (this dir doesnt exists)")
            
            
    def remove_dir(self, path, *args): 
        try:# just check if args[0] exists
            args[0] == "r"
            param1 = "r"
        except:
            param1 = None
        path = self.path_customizer(path)
        isdir = os.path.isdir(path)
        if isdir:
            if param1 == "r":
                shutil.rmtree(path)
            elif param1 == None:
                os.rmdir(path)
        else:
            print("Check again something went wrong (this dir doesnt exists)")

c = Console(
    "C:\\Users\\lukiy\\OneDrive\\Počítač\\programing\\halloworld-os\\os\\lukpox01",
    "lukpox01",
)

c.command_input()