#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016

# Demonstrates packing with fill but also expanding to fill the window

from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text='Hello Tkinter', background='yellow').pack(fill=BOTH, expand=True)
ttk.Label(root, text='Hello Tkinter', background='green').pack(fill=BOTH, expand=True)
ttk.Label(root, text='Hello Tkinter', background='blue').pack(fill=BOTH)

root.mainloop()