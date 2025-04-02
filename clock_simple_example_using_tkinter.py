import tkinter as tk
from tkinter import *
from time import strftime

root=tk.Tk()
root.title('clock')

def my_time():
    cur_time = strftime("%I : %M : %S %p")  ##p should be small
    clock_lb.config(text=cur_time)
    clock_lb.after(1000,my_time)
clock_lb=Label(root,text='clock',font=('',70),bg='white',fg='black',padx=10,pady=10)
clock_lb.pack()

my_time()

root.mainloop()
