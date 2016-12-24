#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 24 Dec 2016

# Demonstrates Tkinter canvas drawing shapes - raectagles, ovals, arcs and polygons

from tkinter import *

root = Tk()
root.title('Drawing a Line')

canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)

# Create a rectangle by specifying start and end coords (opposite corners)
rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfigure(rect, fill='yellow')

# Same as rectangle - coords of opposite corners of a virtual rectangle
oval = canvas.create_oval(160, 120, 480, 360)
canvas.itemconfigure(oval, fill='red')

# Create and modify an arc
arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfigure(arc, start=0, extent=180, fill='green')

# Create a triangle or any multipoint polygon = pass x/y coords
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill='blue')

root.mainloop()
