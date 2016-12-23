#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 23 Dec 2016

# Demonstrate use of additional windows relating to the original root along with window management

from tkinter import *

root = Tk()

window = Toplevel(root)  # Toplevel is the syntax for creating a new window which is still bound to the root.
window.title('New Window')  # Changes the window header title.

# Set window size...
window.geometry('640x480+50+100')  # In pixels... ('<width>x<height>+<from_left>+<from_top')

# Limit resizing...
window.maxsize(640, 480)
window.minsize(200, 200)

# Brings window a visible level in front of root.
window.lift(root)


# Other useful syntax...
# State
# window.state('zoomed')  # Shows the window
# window.state('withdrawn')  # Hides the window (doesn't show in task bar)
# window.state('iconic')  # Minimises the dock or start menu
# window.state('normal')  # Normal view
# window.iconify()  # Minimise to dock
# window.deiconify() # Restore from dock

# Allow resizing of window
# window.resizable(False, False) # Parameters = (<vertical_BOOL>, <horizontal_BOOL>)

root.mainloop()



