#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 8 Dec 2016
# Creates a window with a label and two buttons. One button updates the label text with current date and the other with current time.

from tkinter import *
from tkinter import ttk
import datetime


class HelloApp:
    def __init__(self, master):
        self.label = ttk.Label(master, text="Hello!")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="Today's Date (UK)",
                   command=self.DateTime).grid(row=1, column=0)

        ttk.Button(master, text="Current Time",
                   command=self.yourName).grid(row=1, column=1)

    def DateTime(self):
        now = datetime.datetime.now()
        self.label.config(text=(now.day, '/', now.month, '/', now.year))

    def yourName(self):
        now = datetime.datetime.now()
        self.label.config(text=(now.hour, ':', now.minute, ':', now.second))


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__": main()