import tkinter as tk
from tkinter.scrolledtext import ScrolledText

    

def main(content = None):
    root = tk.Tk()
    root.title("ScrolledText Widget")

    root.geometry("700x600")
    root.minsize(300,300)

    st = ScrolledText(root, width=50,  height=10)
    st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    st.insert(tk.INSERT, "(you cant any way edit this)\n")
    if content != None:
        st.insert(tk.INSERT, content)
        
    st.configure(state ='disabled')   
    root.mainloop()
    