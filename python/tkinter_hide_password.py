#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 17 Dec 2016

from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)
entry.pack()
entry.config(show='*')


root.mainloop()