from am_utils.prefs import Prefs
from am_utils.crawler import crawl
import os

from tkinter import *
from tkinter.ttk import *
from am_gui.settings import SettingsDialog

def show_settings():
    popup = Toplevel()
    SettingsDialog(popup).grid(row=0, column=0, sticky=E)

root = Tk()

prefs = Prefs()

l = Label(text="Hello {}".format(prefs.get('name')))
l.pack()

tree = Treeview()
tree.pack()

try:
    assets = crawl(prefs.get('root_folder'))
except:
    assets = ['check your prefs']
for i in assets:
    tree.insert('', 'end', text=i)

p = Button(text="Preferences", command=show_settings)
p.pack()

b = Button(text="Exit", command=sys.exit)
b.pack()

root.mainloop()
