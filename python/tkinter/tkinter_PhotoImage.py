#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 8 Dec 2016
# Script demostrating using tkinter's PhotoImage function to display an image.
# Note: This only works for GIF and PGM/PPM files.

from tkinter import *

def main():
    mainView = Tk()
    mainView.config(background='white')
    mainView.geometry('{}x{}'.format(300, 300))

    img = PhotoImage(file='tick.gif')
    imgLabel = Label(image=img)
    imgLabel.image = img
    imgLabel.pack()

    mainView.mainloop()

if __name__ == "__main__": main()