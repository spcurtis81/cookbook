#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 18 Dec 2016

# NOTE: Spinbox is not available as a ttk widget.

from tkinter import *

root = Tk()

year = StringVar()
Spinbox(root, from_=1980, to=2020, textvariable=year).pack()

# Syntax
# <textvariable>.get() - returns the current value of the spinbox
# <textvariable>.set('<value>') - inserts a value into the spinbox.





