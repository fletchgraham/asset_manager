from am_utils.prefs import Prefs

from tkinter import *
from am_gui.settings import SettingsDialog

def show_settings():
    popup = Toplevel()
    SettingsDialog(popup).pack()

root = Tk()

prefs = Prefs()

l = Label(text="Hello {}".format(prefs.get('name')))
l.pack()

p = Button(text="Preferences", command=show_settings)
p.pack()

b = Button(text="Exit", command=sys.exit)
b.pack()

root.mainloop()
