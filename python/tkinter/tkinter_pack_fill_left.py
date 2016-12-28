#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016

# Demonstrates using the Tkinter pack geometry manager to place widgets side by side.

from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text='Hello Tkinter', background='yellow').pack(side=LEFT)
ttk.Label(root, text='Hello Tkinter', background='green').pack(side=LEFT)
ttk.Label(root, text='Hello Tkinter', background='blue').pack(side=LEFT)

root.mainloop()