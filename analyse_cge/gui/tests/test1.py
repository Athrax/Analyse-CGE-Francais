# Importing tkinter module
from tkinter import *

# Creating a tkinter window
root = Tk()

# Initialize tkinter window with dimensions 300 x 250
root.geometry('300x250')

# Creating a Button
btn = Button(root, text='Click me !', command=root.destroy)

# Set the position of button to coordinate (100, 20)
btn.place(x=0, y=0)

root.mainloop()