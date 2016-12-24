#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates syntax for Tkinter text boxes, including editing, deleting of lines.

from tkinter import *

root = Tk()
root.title('Textbox')

text = Text(root, width=40, height=10)  # Width and height are in characters
text.pack()
text.config(wrap='word')  # word wrapping will wrap at nearest word end. Char will ignore word ends.

text.insert('1.0', 'This is the first line')  # 1 being the destination line and 0 being the destination index

root.mainloop()

# Other useful syntax...
# text.get('1.0', 'end')  # Gets text from line 1 index 0 to the end of the box.
# text.delete('1.0', '1.0 lineend')  # Delete from line 1 / ind 0 to line 1 end of line (not including new line char)
# text.delete('1.0', '3.0 lineened + 1 chars')  # Delete from line 1 / ind 0 to line 3 end including new line char
# text.replace('1.0', '1.0 lineend', 'This is the new first line')  # Replaces text on line one.
# text.config(state = 'disabled')  # Disables text editing