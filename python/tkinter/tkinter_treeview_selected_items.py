#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates use of select mode and creating response to selection in Tkinter treeview.

from tkinter import *
from tkinter import ttk

def callback(event):
    pass

root = Tk()
root.title('Treeview Selection')

treeview = ttk.Treeview(root)
treeview.pack()

# Insert treeview items
treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')
# Insert sub-items
treeview.insert('item1', '0', 'subitem1', text='First Sub Item')
treeview.insert('item1', '1', 'subitem2', text='Second Sub Item')
# Insert image
logo = PhotoImage(file='python_logo.gif').subsample(10, 10)
treeview.insert('item2', 'end', 'python', text='Python', image=logo)
treeview.item('item2', open=True)

# Add a column called 'version'
# (columns='<col_id>')
treeview.config(columns='version')
treeview.column('version', width=50, anchor='center')

# Make main column width (id is automatically set to #0 by Python)
treeview.column('#0', width=150)

# Give column a heading
treeview.heading('version', text='Version')

# Set value in version column
# ('<mainCol_id>', '<setCol_id>', '<value2add>')
treeview.set('python', 'version', '3.5.1')

# Create treeview tags
# ('<item_id>', tags=('<tag_name>')
treeview.item('python', tags='software')

# Format using tag
treeview.tag_configure('software', background='yellow')

# Capture selection and run a function
# ('<<TreeviewSelection', '<function>')
treeview.bind('<<TreeviewSelection>>', callback)

root.mainloop()