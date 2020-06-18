#Python Combobox Application
import tkinter as tk
from tkinter import ttk
win = tk.Tk()# Application Name
win.title("Python GUI App")# Label Creation
ttk.Label(win, text = "Choose the color:").grid(column = 0, row = 0)# Button Action
def click():
    action.configure(text = "chosen color is : " + numberChosen.get())# button Creation
    action = ttk.Button(win, text = "Click", command = click)
    action.grid(column = 1, row = 1)# Combobox Creation
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width = 12, textvariable = number)# Adding Values
numberChosen['values'] = ("Red", "Blue", "Green")
numberChosen.grid(column = 0, row = 1)
numberChosen.current()# Calling Main()
win.mainloop()