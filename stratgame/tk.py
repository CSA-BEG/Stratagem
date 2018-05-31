from tkinter import *
from tkinter import ttk
import os
root = Tk()
root.title('')
def clearscreen(*args):
    os.startfile(str(dir_path) + r'\Strategy.py')

def instructions(*args):
    os.startfile(str(dir_path)+r'\file.txt')
dir_path = os.path.dirname(os.path.realpath(__file__))
ttk.Label(root,text='Stratagem').grid(column=0,row=0,padx=5,pady=5)
mainframe = ttk.Frame(root, padding="6 6 6 6")
mainframe.grid(columnspan=1, row=1, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

clear=ttk.Button(mainframe,text='Start',command=clearscreen)
clear.grid(column=1,row=2,sticky=(N,W,E,S))
tut=ttk.Button(mainframe,text='Instructions',command=instructions)
tut.grid(column=2,row=2,sticky=(N,W,E,S))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()