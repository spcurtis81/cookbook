#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 17 Dec 2016

# Script demonstrates deleting content from entry1 and inserting in entry2

from tkinter import *
from tkinter import ttk

root = Tk()

entry1 = ttk.Entry(root, width=30)
entry1.pack()

entry2 = ttk.Entry(root, width=30)
entry2.pack()

def action():
    entry1.delete(0, END) # 1st parameter signifies start point, second is end point.
    entry2.insert(0, 'Enter your password') # 1st parameter is insert point, second is string to insert.

act = ttk.Button(root, text='Click Me', command=action).pack()

root.mainloop()