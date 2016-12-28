#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016

# Demonstrates binding multiple events in tkinter

from tkinter import *
from tkinter import ttk

root = Tk()

label1 = ttk.Label(root, text='Label 1')
label2 = ttk.Label(root, text='Label 2')
label1.pack()
label2.pack()

# Binds an event for any mouse click on label 1
label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label'))
# Binds an event for left click (1) on label 1
label1.bind('<1>', lambda e: print('<1> Label'))

# Binds an event for left click on any root level object (lable 1 & 2)
root.bind('<1>', lambda e: print('<1> root'))

# Removes previous event binding on Label 1, leaving root binding only.
# label1.unbind('<1>')
# label1.unbind('<ButtonPress>')

# Bind an event to ALL windows within the root.
root.bind_all('<Escape>', lambda e: print('Escape!!'))

root.mainloop()
