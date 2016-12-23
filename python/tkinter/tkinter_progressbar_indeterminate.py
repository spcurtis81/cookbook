#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 23 Dec 2016

# Demonstrates creating an indeterminate progress bar in tkinter. Essentially, this is an animated bar to signify
# the program is doing something. It does not show how far through the taks it is.

from tkinter import *
from tkinter import ttk

root = Tk()

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200) # Orient can also be VERTICAL
progressbar.pack()
progressbar.config(mode='indeterminate')
progressbar.start() # Starts the animation of the widget
# progressbar.stop() # Stops the animation