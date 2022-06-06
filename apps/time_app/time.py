import tkinter as tk
from functools import partial
import time
from datetime import datetime, timedelta

def time_page(root):
    forget_page(root)
    page = tk.Frame(root)
    page.grid()
    def time_():
        string = time.strftime('%H:%M:%S  %m/%d/%Y')
        lbl.config(text = string)
        lbl.after(250, time_)
    
    lbl = tk.Label(page, font = ('calibri', 40, 'bold'),
                foreground = 'black')
    
    
    lbl.pack(anchor="center")
    time_()
    
def stopwatch_page(root):
    forget_page(root)
    page = tk.Frame(root)
    page.grid()
    time_ = datetime.strptime('00:00:00', '%H:%M:%S')
    
    def time_it(time_):
        time_ = time_ + timedelta(seconds=1)
        string = time_.strftime('%H:%M:%S')
        lbl.config(text = string)
        lbl.after(1000, time_it, time_)
    
    lbl = tk.Label(page, font = ('calibri', 40, 'bold'),
                foreground = 'black', text = '00:00:00')
    
    
    lbl.pack(anchor="center")
    time.sleep(.500)
    time_it(time_)
    
def timer_page(root):
    forget_page(root)
    page = tk.Frame(root)
    page.grid()
    hours = tk.StringVar(value=0)
    minutes = tk.StringVar(value=0)
    seconds = tk.StringVar(value=0)
    hour_box = tk.Spinbox(
        page,
        from_=00,
        to=24,
        textvariable=hours,
        wrap=True)
    
    minute_box = tk.Spinbox(
        page,
        from_=00,
        to=60,
        textvariable=minutes,
        wrap=True)
    
    second_box = tk.Spinbox(
        page,
        from_=00,
        to=60,
        textvariable=seconds,
        wrap=True)

    hour_box.pack(side=tk.LEFT)  
    minute_box.pack(side=tk.LEFT)
    second_box.pack(side=tk.LEFT)
    
    
    def time_it(time_): 
        if time_.strftime('%H:%M:%S') == '00:00:00':
            forget_page(root)
            return
        time_ = time_ - timedelta(seconds=1)
        string = time_.strftime('%H:%M:%S')
        lbl.config(text = string)
        lbl.after(1000, time_it,time_)
        
    def set_time():
        time_ = f"{hours.get()}:{minutes.get()}:{seconds.get()}"
        time_ = datetime.strptime(time_, "%H:%M:%S")
        time_it(time_)
        
    lbl = tk.Label(page, font = ('calibri', 40, 'bold'),
                foreground = 'black', text = '00:00:00')
    
    
    lbl.pack(anchor="center")
    time.sleep(.500)
    start = tk.Button(page, text="Start", command=lambda: set_time())
    start.pack()
    
def forget_page(root):
    slaves = root.grid_slaves()
    for slave in slaves:
        slave.grid_forget()
        slave.destroy()
    
def main():
    root = tk.Tk()
    root.title(f"Time")

    root.geometry("600x200")
    
    time_page(root)
    
    menubar = tk.Menu(root)
    menubar.add_command(label="Time", command=lambda: time_page(root))
    menubar.add_command(label="Stopwatch", command=lambda: stopwatch_page(root))
    menubar.add_command(label="Timer", command=lambda: timer_page(root))
    
    
    root.config(menu=menubar) 
    root.mainloop()
    

# TODO make stand alone app