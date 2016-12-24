#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Basic demonstration of Tkinter's canvas method

from tkinter import *

root = Tk()
root.title('Drawing a Line')

canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)

# Draw a straight line (a-b)
# (<start_x_coord>, <start_y_coord>, <end_x_coord>, <end_y_coord>)
line1 = canvas.create_line(20, 450, 620, 450, fill='blue', width=20)

# Draw a multi point line (a-b-c)
line2 = canvas.create_line(20, 430, 310, 300, 620, 430, fill='red', width=5)

# Make a line smoothed
line3 = canvas.create_line(20, 20, 310, 150, 620, 20, fill='green', width=5)
canvas.itemconfigure(line3, smooth=True)

root.mainloop()

# Other useful syntax
# canvas.coords(<object>)  # Get coordinates for a canvas object
# canvas coords(<object>, <new coords>) # Change object coords
# canvas.itemconfigure(line3, splinesteps=5)  # Adjust smoothness of a curve
# canvas.delete(<object>)
# canvas.delete(all)
