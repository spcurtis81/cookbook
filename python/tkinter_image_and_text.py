#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 8 Dec 2016

from tkinter import *
from tkinter import ttk


def main():

    root = Tk()  # Creates new top level widget and assigns to var 'root'
    label = ttk.Label(root, text="Hello, Ste!")
    label.config(background='yellow', foreground='blue')
    label.config(font=('Courier', 24, 'bold'))

    #PhotoImage can accept GIF and two others but not JPG
    logo = PhotoImage(file="python_logo.gif")
    label.config(image = logo)
    #Compound is used to decide what is displayed in a label.
    # label.config(compound = 'text') # This would change the label to the text.
    label.config(compound = 'center')

    label.pack()
    root.mainloop()


if __name__ == "__main__": main()