import tkinter as tk
from functools import partial
import time
from datetime import datetime, timedelta

def add_number(entry, number):
    entry.insert(tk.END, number)

def calculate(entry):
    problem = entry.get()
    eq = eval(problem)
    entry.delete(0, tk.END)
    entry.insert(tk.END, eq)
def main():
    root = tk.Tk()
    root.title(f"Calculator")

    root.geometry("550x500")
    root.minsize(550,500)
    root.maxsize(550,500)
    
    entry = tk.Entry(root, font=('calibri', 40, 'bold'))
    entry.grid(row=0, columnspan=4)
    
    button_7 = tk.Button(root, text="7", height=6, width=15, command= lambda: add_number(entry, 7))
    button_8 = tk.Button(root, text="8", height=6, width=15, command= lambda: add_number(entry, 8))
    button_9 = tk.Button(root, text="9", height=6, width=15, command= lambda: add_number(entry, 9))
    button_mul = tk.Button(root, text="*", height=6, width=15, command= lambda: add_number(entry, "*"))
    
    button_4 = tk.Button(root, text="4", height=6, width=15, command= lambda: add_number(entry, 4))
    button_5 = tk.Button(root, text="5", height=6, width=15, command= lambda: add_number(entry, 5))
    button_6 = tk.Button(root, text="6", height=6, width=15, command= lambda: add_number(entry,6))
    button_min = tk.Button(root, text="-", height=6, width=15, command= lambda: add_number(entry, "-"))
    
    button_1 = tk.Button(root, text="1", height=6, width=15, command= lambda: add_number(entry, 1))
    button_2 = tk.Button(root, text="2", height=6, width=15, command= lambda: add_number(entry, 2))
    button_3 = tk.Button(root, text="3", height=6, width=15, command= lambda: add_number(entry, 3))
    button_plu = tk.Button(root, text="+", height=6, width=15, command= lambda: add_number(entry, "+"))
    
    button_dot = tk.Button(root, text=".", height=6, width=15, command= lambda: add_number(entry, "."))
    button_0 = tk.Button(root, text="0", height=6, width=15, command= lambda: add_number(entry, 0))
    button_div = tk.Button(root, text="/", height=6, width=15, command= lambda: add_number(entry, "/"))
    button_euq = tk.Button(root, text="=", height=6, width=15, command= lambda: calculate(entry))
    
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_mul.grid(row=2, column=3)
    
    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_min.grid(row=3, column=3)
    
    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_plu.grid(row=4, column=3)
    
    button_dot.grid(row=5, column=0)
    button_0.grid(row=5, column=1)
    button_div.grid(row=5, column=2)
    button_euq.grid(row=5, column=3)
    
    root.config() 
    root.mainloop()
    

# TODO make stand alone app