#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 23 Dec 2016

# Demonstrates basic pane syntax - creation, resizing and proportions

from tkinter import *
from tkinter import ttk

root = Tk()

panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)

frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
panedwindow.add(frame1, weight=1)  # (<first_frame>, <resizing_proportion>)
panedwindow.add(frame2, weight=4)

frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)
panedwindow.insert(1, frame3)  # Inserts the a new frame at index passed - (<position_index>, <frame_name>)
# Note: if no weight is provided, the width will remain fixed.

# Other useful syntax...
# panedwindow.forget(1)  # Removes the pane at the index passed - Does NOT delete this pane though.



root.mainloop()
