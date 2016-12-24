#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates syntax for implementing and using marks in Tkinter text boxes.

from tkinter import *

root = Tk()
root.title('Textbox Marks')

text = Text(root, width=40, height=10)  # Width and height are in characters
text.pack()
text.config(wrap='word')  # word wrapping will wrap at nearest word end. Char will ignore word ends.

text.insert('1.0', 'Here is some text to preload the text box with')

text.mark_set('my_mark', 'end')  # Creates a mark at the end of the textbox
text.insert('my_mark', 'Text to be inserted at the mark')  # Inserts text at the mark specified

root.mainloop()

# Other useful syntax...
# text.mark_names()  # Returns a list of marks
# text.insert('insert', '<text_to_insert>')  # The inbuilt 'insert' mark will use current cursor position.
# text.mark_gravity('<mark_name>', 'right')  # Ensures inserts gravitate to the right.
# text.mark_unset('<mark_name>')  # Removes a mark.