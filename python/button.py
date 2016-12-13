#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 13 Dec 2016
# Script below can be entered it the python prompt.
# This script demonstrates the command property of a button.

# Import modules
from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text='Click Me')
button.pack()

# Defines a function which will be called when the button is clicked.
def callback():
    print('Clicked')

# Applies an action when the button is clicked.
button.config(command=callback)

#>>> Clicked