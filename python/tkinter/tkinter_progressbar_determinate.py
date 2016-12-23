#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 23 Dec 2016

# Demonstrates creating an determinate progress bar in tkinter. This allows the progress bar to take values and
# display progress of task.

from tkinter import *
from tkinter import ttk

root = Tk()

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200) # Orient can also be VERTICAL
# maximum sets top 100% progress and value sets the current status.
progressbar.config(mode='determinate', maximum=11.0, value=4.2)
progressbar.pack()

# Other useful syntax
# progressbar.step() # Steps up the value by 1.0
# progressbar.step(<<value>>) # Steps by the value by the double passed.


root.mainloop()
