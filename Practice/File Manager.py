from tkinter import *
import os
import csv
from tkinter import scrolledtext
import os.path
import json
import datetime

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def get_dirs(way):
    l = os.listdir(way)
    for i in l:
        path = way + i
        if os.path.isfile(path) == True:
            dirs.insert(END, "[FILE] " + i + " "*(100 - len(i) - 7) + str(modification_date(path))[0:str(modification_date(path)).rfind(".")])
        elif os.path.isdir(path) == True:
            dirs.insert(END, "[DIR] " + i + " "*(100 - len(i) - 7) + str(modification_date(path))[0:str(modification_date(path)).rfind(".")])
        else:
            dirs.insert(END, "[OTHER] " + i + " "*(100 - len(i) - 7) + str(modification_date(path))[0:str(modification_date(path)).rfind(".")])

def get_path(event):
    get_dirs(adress.get("1.0", END)[0:len(adress.get("1.0", END))-1])

window = Tk()
window.geometry("720x480")
window.resizable(width=False, height=False)
window.title("File Manager")

button1 = Button(master=window, text="<", width=2, height=1, padx=5, pady=1)
button1.place(x=20, y=20)

adress = Text(master=window, width = 75, height=2)
adress.place(x=60, y=20)

dirs = Listbox(master=window, width = 100, height=23)
dirs.place(x=60, y=80)

adress.bind("<FocusOut>", get_path)

window.mainloop()
