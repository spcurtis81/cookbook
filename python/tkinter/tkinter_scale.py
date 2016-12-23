#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 23 Dec 2016

# Demonstrates use of a sliding scale widget to control a progress bar.

from tkinter import *
from tkinter import ttk

root = Tk()

value = DoubleVar()


progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200) # Orient can also be VERTICAL
# maximum sets top 100% progress and value sets the current status.
progressbar.config(mode='determinate', maximum=11.0)
progressbar.config(variable=value)
progressbar.pack()

# scale is tied to value variable, as is the progress bar, so as the scale is changed, the value of the prog bar
# is also changed.
scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=11.0)
scale.pack()

root.mainloop()
