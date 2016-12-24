#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates syntax for implementing and using tags in Tkinter textboxes

from tkinter import *

root = Tk()
root.title('Textbox')

text = Text(root, width=40, height=10)  # Width and height are in characters
text.pack()
text.config(wrap='word')  # word wrapping will wrap at nearest word end. Char will ignore word ends.
text.insert('1.0', 'This is the first line')  # 1 being the destination line and 0 being the destination index

text.tag_add('my_tag', '1.0', '1.0 wordend')  # ('<tag_name>' , '<start_line/ind>', '<end_line/ind>')
text.tag_configure('my_tag', background='yellow')  # ('<tag_name>', args)

root.mainloop()

# Other useful syntax...
# text.tag_names()  # Return all tags including 'sel' (selected text)
# text.tag_names('1.0) # Returns tag names covering line 1 / ind 0
# text.tag_ranges('<tag_name>')  # Returns line/ind from - to range for specified tag.
# text.tag_remove('tag_name', 'fromLine.ind', 'toLine.ind)  # Remove tag from a set area.
# text.replace('<tag_name.first>, '<tag_name.last>', '<New text>')  # Replace text in tag.
# text.tag_delete('<tag_name>')  # Delete a tag (not it's content).