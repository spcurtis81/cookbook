#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 8 Dec 2016

from tkinter import *
from tkinter import ttk


def main():

    root = Tk()  # Creates new top level widget and assigns to var 'root'
    label = ttk.Label(root, text="Hello, Ste!")
    label.config(foreground='blue', background='yellow')
    label.config(font=('Courier', 24, 'bold'))
    label.config(justify = CENTER)

    label.pack()
    root.mainloop()


if __name__ == "__main__": main()