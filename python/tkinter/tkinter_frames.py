#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 23 Dec 2016

# Demonstrates use of frames in tkinter.

from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root)
frame.pack()
frame.config(height=100, width=200)
frame.config(relief=RIDGE)  # Determines the border style

ttk.Button(frame, text='Click me!').grid()  # Note that an item inside a frame can have a different geometry manager.
frame.config(padding=(30, 15))

root.mainloop()
