#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 25 Dec 2016

# Demonstrates how you can use Tkinter's file dialog method to initiate the file picker

from tkinter import filedialog

filename = filedialog.askopenfile()

print("Selected file's path: {}".format(filename.name))
