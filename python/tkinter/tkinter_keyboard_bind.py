#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Demonstrates binding actions to keyboard presses.

from tkinter import *
from tkinter import ttk

root = Tk()


def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('character: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))


def shortcut(action):
    print(action)


# ('<event_type', <function_tobe_called>)
root.bind('<Command-c>', lambda e: shortcut('Copy'))
root.bind('<Command-v>', lambda e: shortcut('Paste'))

root.mainloop()
