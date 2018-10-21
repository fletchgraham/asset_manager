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

Label(text="Assets:").grid(row=0, column=0)
Button(text="Refresh").grid(row=0, column=2)

tree = Treeview()
tree.grid(row=1, column=0, columnspan=4)

try:
    assets = crawl(prefs.get('root_folder'))
except:
    assets = ['check your prefs']
for i in assets:
    tree.insert('', 'end', text=i)

Button(text="Preferences", command=show_settings).grid(row=0, column=5)
Button(text="Exit", command=sys.exit).grid(row=1, column=5)

root.mainloop()
