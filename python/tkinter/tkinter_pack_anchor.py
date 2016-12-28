#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016

# Demonstrates using the Tkinter pack geometry manager.

from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text='Hello Tkinter', background='yellow').pack(side=LEFT, anchor='nw')
ttk.Label(root, text='Hello Tkinter', background='green').pack(side=LEFT, padx=10, pady=10)
ttk.Label(root, text='Hello Tkinter', background='blue').pack(side=LEFT, ipadx=10, ipady=10)

for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand=True)
    print(widget.pack_info())


root.mainloop()