#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates implementation of a menu system in Tkinter and binding commands to menu items.

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

# Assign an item to a menu with a command
# <menu>.add_command(label='<label_name>', command=<action>)
file.add_command(label='New', command=lambda: print('New File'))
file.add_command(label='Open...', command=lambda: print('Open File'))

# Add an image to a menu item
logo = PhotoImage(file='python_logo.gif').subsample(10, 10)
file.entryconfig('Open...', image=logo, compound='left')

# Add nested menu systems
save = Menu(file)  # New menu, child of file menu
# <parent_menu>.add_cascade(menu=<menu_id>, label='<label_text>')
file.add_cascade(menu=save, label='Save')

# Add objects to new sub menu.
save.add_command(label='Save', command=lambda: print('Save'))
save.add_command(label='Save as...', command=lambda: print('Save As'))
save.add_command(label='Save All', command=lambda: print('Save All'))

root.mainloop()

# Other useful syntax
# <menu_name>.entryconfig('<item_label>', state='disabled')  # Disables menu item
# <menu_name>.delete('<item_label>')  # Deletes a menu item.
