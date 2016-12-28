#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016

# Demonstrates implementation of callback function on tkinter button with use of a function and lambda

from tkinter import *
from tkinter import ttk

root = Tk()


def callback(string):
    print(string)


ttk.Button(root, text='First Name', command=lambda: callback('Stephen')).pack()
ttk.Button(root, text='Surname', command=lambda: callback('Curtis')).pack()
ttk.Button(root, text='Age', command=lambda: callback('Not telling')).pack()

root.mainloop()
