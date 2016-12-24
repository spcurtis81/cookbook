#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates syntax for Tkinter inserting images and other widgets into textboxes.

from tkinter import *

root = Tk()
root.title('Img in Textbox')

text = Text(root, width=40, height=10)  # Width and height are in characters
text.pack()
text.config(wrap='word')  # word wrapping will wrap at nearest word end. Char will ignore word ends.

text.insert('1.0', 'This is the first line\n')  # 1 being the destination line and 0 being the destination index
text.insert('2.0', 'This is the second line\n')

# Create two marks
text.mark_set('my_mark1', '1.end')  # Mark set at end of first line.
text.mark_set('my_mark2', 'end')  # Mark set at end of text box.

# Create image object
image = PhotoImage(file='python_logo.gif')

# Insert image in text box @ mark 1
text.image_create('my_mark1', image=image)

# Insert button @ mark 2
button = Button(text, text='Click Me')
text.window_create('my_mark2', window=button)

root.mainloop()