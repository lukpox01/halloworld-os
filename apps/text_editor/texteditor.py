import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from functools import partial
import os
import easygui

def open_new(st, root):
    st.delete(1.0, tk.END)
    root.title(f"Text editor - Untitled")

def open_file(path, root):
    with open(path, "r") as f:
        content = f.read()
    file_name = path.split("\\")[-1]
    root.title(f"Text editor - {file_name}")
    return content

def save_file(path, st):
    with open(path, "w") as f:
        f.write(st.get(1.0, tk.END))
        
def save_as(st, root):
    
    content = st.get(1.0, tk.END)
    st.delete(1.0, tk.END)
    
    path = easygui.filesavebox()
    with open(path, "w") as f:
        f.write(content)
    file_name = path.split("\\")[-1]
    root.title(f"Text editor - {file_name}")
            
     
def main(path, file_name):
    
    root = tk.Tk()
    root.title(f"Text editor - {file_name}")

    root.geometry("700x600")
    root.minsize(300,300)
    
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    
    st = ScrolledText(root, width=50,  height=10)
    
    
    save_file_command = partial(save_file, path, st)
    save_as_command = partial(save_as, st, root)
    open_new_command = partial(open_new, st, root)
    filemenu.add_command(label="Save", command=save_file_command)
    filemenu.add_command(label="Save as", command=save_as_command)
    filemenu.add_command(label="New", command=open_new_command)
    
    
    st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    if path != None:
        st.insert(tk.INSERT, open_file(path, root))
        
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar) 
    root.mainloop()