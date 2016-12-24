#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates creation, formatting and moving of treeview items in Tkinter.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Treeview')

treeview = ttk.Treeview(root)
treeview.pack()

# Insert treeview items
# ('', '<insert_ind>', '<id_name>', text='<text>') where '' is root
treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')

# Insert sub-items
treeview.insert('item1', '0', 'subitem1', text='First Sub Item')
treeview.insert('item1', '1', 'subitem2', text='Second Sub Item')

# Insert image
logo = PhotoImage(file='python_logo.gif').subsample(10, 10)
# ('<parent>', '<insert_ind>', '<id_name>', text, image)
treeview.insert('item2', 'end', 'python', text='Python', image=logo)

# Make item two default to open
treeview.item('item2', open=True)

# Create an item in 2 but move it to 3
treeview.insert('item2', 'end', 'subitem3', text='Third Sub Item')
# ('<item_id>', '<new_parent>', '<insert_ind>')
treeview.move('subitem3', 'item3', '0')
treeview.item('item3', open=True)

root.mainloop()

# Other useful syntax
# treeview.detach('<item_id>')  # Detaches item from view but not delete. Can be re-added using move.
# treeview.delete('<item_id>')  # Permanently deletes the item.