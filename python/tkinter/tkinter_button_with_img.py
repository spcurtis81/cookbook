#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 16 Dec 2016

from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text='Click Me')
button.pack()

def callback():
    print('Clicked')

button.config(command= callback)

logo = PhotoImage(file='python_logo.gif')
small_logo = logo.subsample(5,5)
button.config(image=small_logo, compound=LEFT)

root.mainloop()