import os
import time
import shutil
import colorama
import sys
from colorama import Fore, Back, Style
from apps import *
from rich.markdown import Markdown
from rich import print
from threading import Thread


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
            "rf": self.remove_file,
            "open": self.open_file,
            "openapp": self.open_app,
            "rn" : self.rename_file,
            "cwd": self.current_work_dir,
            "help": self.help,
        }
        self.commands_keys = self.commands.keys()
        
        self.apps = {"texteditor": TextEditor, "time": TimeApp}
        self.apps_keys = self.apps.keys()
        colorama.init(autoreset=True)

    def path_customizer(self, path): 
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

    def current_work_dir(self):
        print(f"[{self.getcwd()}]")
        
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
                    if self.command[0] == "mf":
                        func(*self.command[1:], None)
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

    def mf(self, path, content, *args):
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
                if content == None:
                    content = ""
                f = open(path, "w")
                f.write(content)
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

    def ld(self, path=None, *args):
        if path == None:
            path = os.getcwd()
        else:
            path = self.path_customizer(path)
        isdir = os.path.isdir(path)
        if isdir:
            in_dir = os.listdir(path)
            print(" ")
            for i in in_dir:
                if os.path.isfile(os.path.join(path, i)):
                    print(i)
                elif os.path.isdir(os.path.join(path, i)):
                    print(Fore.CYAN + i)
                else:
                    print(Fore.GREEN + i) # if there is something else(undetected file)
                
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
        sys.exit()

    def remove_file(self, path, *args): 
            
        path = self.path_customizer(path)
        custom_path = str(path).split("/")
        is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )
        if is_parent_dir:
            isfile = os.path.isfile(path)
            if isfile:
                if custom_path[0] == "login_info.txt": 
                    print("Check again something went wrong (you cant delete this file)")
                else:
                    os.remove(path)
            else:
                print("Check again something went wrong (this file doesnt exists)")

        else:
            print("Check again something went wrong (this dir doesnt exists)")
            
            
    def remove_dir(self, path, param1, *args): 
        path = self.path_customizer(path)
        isdir = os.path.isdir(path)
        if isdir:
            if param1 == "r":
                shutil.rmtree(path)
            elif param1 == None:
                os.rmdir(path)
        else:
            print("Check again something went wrong (this dir doesnt exists)")

    def rename_file(self, path, new_path, *args):
        path = self.path_customizer(path)
        custom_path = str(path).split("/")
        is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )
        
        new_path = self.path_customizer(new_path)
        custom_path = str(new_path).split("/")
        new_is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )   
        if is_parent_dir and new_is_parent_dir:
            if os.path.exists(new_path):
                print("Check again something went wrong (the new path already exists)")
            else:
                os.rename(path, new_path)
        else:
            print("Check again something went wrong (this dir doesnt exists)")
    
    # def threading_(self, func, *args):
    #     Thread(target=func, args=args).start()
    
    def open_app(self, param1, *args):
        param1.lower()
        if param1 == "texteditor":
            TextEditor(None, "Untitled")
        elif param1 == "time":
            TimeApp()
        else:
            print("Check again something went wrong (this app doesnt exists)")
    
    def open_file(self, path):
        path = self.path_customizer(path)
        custom_path = str(path).split("/")
        is_parent_dir = os.path.isdir(
            os.path.join(f"{custom_path[0]}/{custom_path[1]}", *custom_path[2:-1])
        )
        if is_parent_dir:
            isfile = os.path.isfile(path)
            if isfile:
                TextEditor(path, custom_path[-1])
                
            else:
                print("Check again something went wrong (this file doesnt exists)")

        else:
            print("Check again something went wrong (this dir doesnt exists)")
            
    def help(self):
        markdown = open(os.path.join(self.usr_path, "..", "..", "readme.md"), "r").read()
        md = Markdown(markdown)
        print(md)
        

# TODO implement rich console