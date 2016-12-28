#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 28 Dec 2016

# Demonstrates how you can bind action to virtual events and create your own virtual events in Tkinter

from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

# ('<<event>>')
entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

# (<<virtualevent_name, sequence)
entry.event_add('<<NameLetters>>', 'S', 't', 'e')
entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
# ('<<virtualevent_name>>', action)
entry.bind('<<OddNumber>>', lambda e: print('Odd Number'))

# Print the sequence which triggers each virtual event.
print(entry.event_info('<<OddNumber>>'))
print(entry.event_info('<<NameLetters>>'))

# Progromatically trigger a virtual event
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

# To delete a virtual event...
# entry.event_delete('<<OddNumber>>')


root.mainloop()
