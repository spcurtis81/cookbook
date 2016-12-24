#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates how to implement a working scrollbar in Tkinter

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Scrollbars')

text = Text(root, width=40, height=10, wrap='word')
text.grid(row=0, column=0)
text.insert('1.0', "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like")

# Create scrollbar
scrollbar = ttk.Scrollbar(root, orient=VERTICAL)
scrollbar.grid(row=0, column=1, sticky='ns')

# Allow the text to tell the scrollbar where it's position is.
text.config(yscrollcommand=scrollbar.set)

root.mainloop()