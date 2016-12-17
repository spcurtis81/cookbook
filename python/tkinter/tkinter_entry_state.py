#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 17 Dec 2016

# Demonstrates three states of an Entry field - disabled, not disabled and read only.

from tkinter import *
from tkinter import ttk

root = Tk()

entryP = ttk.Entry(root, width=30)
entryP.pack()
entryP.insert(0, 'This field is protected')
entryRW = ttk.Entry(root, width=30)
entryRW.pack()
entryRW.insert(0, 'This field can be edited')
entryR = ttk.Entry(root, width=30)
entryR.pack()
entryR.insert(0, 'This field is readonly')

entryP.state(['disabled'])
entryRW.state(['!disabled'])
entryR.state(['readonly'])
root.mainloop()
