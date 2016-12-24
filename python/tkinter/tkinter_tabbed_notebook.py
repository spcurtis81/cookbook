#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Script demonstrates how tkinter's notepad method can be used to create tabbed interfaces.

from tkinter import *
from tkinter import ttk

root = Tk()

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text='One')
notebook.add(frame2, text='Two')

ttk.Button(frame1, text='Click Me').pack()

frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text='Three')  # (<insert_position>, <insert_object>, <tab_text>)

root.mainloop()

# Other useful syntax...
# notebook.forget(1)  # Removes the tab index passed from view (Does NOT delete it)
# notebook.select()  # Gets the id of the notebook
# notebook.index(notebook.select())  # Returns the index of the current selected tab
# notebook.select(<index>)  # Select the tab indexed.
# notebook.tab(1, state='<state>')  # Changes the state of the tab e.g. disabled, hidden etc
# notebook.tab(1, 'text')  # Returns the text value. Can be replaced with other attributes (<tab_index, '<attribute>'
# notebook.tab(1)  # Returns a dictionary of all attributes and values