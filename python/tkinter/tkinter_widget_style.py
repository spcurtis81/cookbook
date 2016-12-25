#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates creation of Tkinter style and mapping new styles to varying state

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Style')

button1 = ttk.Button(root, text='Button 1')
button2 = ttk.Button(root, text='Button 2')
button1.pack()
button2.pack()

# assigs the ttk Style to a variable
style = ttk.Style()

# print available styles
print('- Available Styles: {}'.format(style.theme_names()))

# Use a style
style.theme_use('classic')
style.theme_use('aqua') # Change back to normal

# Get style class for object
print('- Style class for button1: {}'.format(button1.winfo_class()))

# Change class style
style.configure('TButton', foreground='blue')

# Create new style inheriting from TButton
style.configure('Alarm.TButton', foreground='orange', font=('Arial', 24, 'bold'))

# Apply new alarm style to button2
button2.config(style='Alarm.TButton')

# Map more styles dependant on state
style.map('Alarm.TButton', foreground=[('pressed', 'pink'), ('disabled', 'grey')])


# Other useful syntax
print('- Style Layout Attributes for TButton: {}'.format(style.layout('TButton')))
print("- Style Attributes for an Object's Elements: {}".format(style.element_options('Button.label')))
print('- Look up current style: {}'.format(style.lookup('TButton', 'foreground')))

root.mainloop()
