#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates implementation of radiobuttons in a Tkinter menu system.

from tkinter import *

root = Tk()
root.title('Menu System')
root.option_add('*tearOff', False)

menubar = Menu(root)
root.config(menu=menubar)

# Create top level menu bar items
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

# Implement menubar items
# (menu=<menubar_item>, label='<label_text'>)
menubar.add_cascade(menu=file, label='File')
menubar.add_cascade(menu=edit, label='Edit')
menubar.add_cascade(menu=help_, label='Help')

choice = IntVar()
edit.add_radiobutton(label='Edit in PyCharm', variable=choice, value=1)
edit.add_radiobutton(label='Edit in Eclipse', variable=choice, value=2)
edit.add_radiobutton(label='Edit in XCode', variable=choice, value=3)


root.mainloop()
