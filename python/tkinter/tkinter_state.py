#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 13 Dec 2016
# Script below can be entered it the python prompt.
# This script demonstrates the command property of a button.

from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text='Click Me')
button.pack()
button.state(['disabled']) # Disables the button / greys it out.
root.mainloop()