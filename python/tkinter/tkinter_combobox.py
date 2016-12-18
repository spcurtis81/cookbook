#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 18 Dec 2016


from tkinter import *
from tkinter import ttk

root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()
combobox.config(values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

root.mainloop()

# Addtional syntax
# <<textvariable>>.get() - gets the current value in the combobox
# <<textvariable>>.set('<<string>>') - to insert a value