#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016

# Overview of Tkinter's place geometry manager

from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry('640x480+200+200')

ttk.Label(root, text='Yellow', background='yellow').place(x=100, y=50, width=100, height=50)
# 100 px from right, 50px down. Also uses relative height and width to keep the widget same proporitonal size
ttk.Label(root, text='Blue', background='blue').place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)
# % of current height and width
ttk.Label(root, text='Green', background='green').place(relx=0.5, x=100, rely=0.5, y=50)
# is % of of current window as previously however will then add x & y pixels on.
ttk.Label(root, text='Orange', background='orange').place(relx=1.0, x=-5, y=5, anchor='ne')

root.mainloop()
