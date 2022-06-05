
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from functools import partial
import easygui

def open_new(event=None):
    global path, root, st
    st.delete(1.0, tk.END)
    root.title(f"Text editor - Untitled")

def open_file(path_,event=None):
    global path, root, st
    if path_ == False:
        path = easygui.fileopenbox()
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    file_name = path.split("\\")[-1]
    root.title(f"Text editor - {file_name}")
    st.delete(1.0, tk.END)
    st.insert(tk.INSERT, content)

def save_file(event=None):
    global path, root, st
    with open(path, "w", encoding="utf-8") as f:
        f.write(st.get(1.0, tk.END))
        
def save_as(event=None):
    global path, root, st
    content = st.get(1.0, tk.END)
    st.delete(1.0, tk.END)
    
    path = easygui.filesavebox()
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    file_name = path.split("\\")[-1]
    root.title(f"Text editor - {file_name}")
            
     
def main(path_, file_name):
    global path, root, st
    path = path_
    root = tk.Tk()
    root.title(f"Text editor - {file_name}")

    root.geometry("700x600")
    root.minsize(300,300)
    
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    editmenu = tk.Menu(menubar, tearoff=0)
    
    st = ScrolledText(root, width=50,  height=10, undo=True)
    
    
    save_file_command = partial(save_file)
    save_as_command = partial(save_as)
    open_new_command = partial(open_new)
    open_file_command = partial(open_file, False)
    filemenu.add_command(label="Save", command=save_file_command, accelerator="Ctrl+S")
    filemenu.add_command(label="Save as", command=save_as_command, accelerator="Ctrl+A")
    filemenu.add_command(label="New", command=open_new_command, accelerator="Ctrl+N")
    filemenu.add_command(label="Open", command=open_file_command, accelerator="Ctrl+O")
    
    editmenu.add_command(label="Undo", command=st.edit_undo, accelerator="Ctrl+Z")
    editmenu.add_command(label="Redo", command=st.edit_redo, accelerator="Ctrl+Y")

    # edit, redu shortcuts is built-in
    st.bind("<Control-a>", save_as_command)
    st.bind("<Control-s>", save_file_command)
    st.bind("<Control-n>", open_new_command)
    st.bind("<Control-o>", open_file_command)
    
    st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    if path != None:
        open_file(True)
        
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    root.config(menu=menubar) 
    root.mainloop()
    
main(None, "Untitled")

# TODO make stand alone app