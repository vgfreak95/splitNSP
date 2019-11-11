# Author : VGFreak95
# Modified Date: 2019-11-11
# Purpose: Uses splitNSP module and makes it easier conceptually.

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk

import splitNSP
import os

#Initialize this global variable
currentlabel = ''

#Creation of the GUI
root = tk.Tk()
root.title('SplitGUI')
root.geometry('500x300')

#Gets the NSP file that is selected
def callFile():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("nsp files", "*.nsp")])
    label = tk.Label(text=str(filename))
    label.place(x=180, y=70)
    global currentlabel
    currentlabel = label['text']
    return filename

#Calls the splitCopy function from the SplitNSP module
def splitFile():
    global currentlabel
    splitNSP.splitCopy(currentlabel)

#Browse Button Properties
browseButton = tk.Button(root, text="Browse NSP", command=callFile).place(x=100,y=70)
#browseButton.grid(row=0)

#Split Button Properties
splitButton = tk.Button(root, text="Split File", command=splitFile).place(x=225,y=200)
#splitButton.grid(row=1, column=1)
root.mainloop()


