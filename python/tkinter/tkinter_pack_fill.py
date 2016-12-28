#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016
# Demonstrates how Tkinter's pack geometry manager can be used to fill a space

from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text='Hello Tkinter', background='yellow').pack(fill=X)

root.mainloop()
