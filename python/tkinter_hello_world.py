#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 8 Dec 2016

from tkinter import *


def main():

    root = Tk()  # Creates new top level widget and assigns to var 'root'
    Label(root,
          text="Hello, Ste!").pack()  # Creates a label in the 'root' widget and uses the pack method to add it.
    root.mainloop()


if __name__ == "__main__": main()