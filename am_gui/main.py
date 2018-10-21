from tkinter import *
from am_gui.settings import SettingsDialog

def show_settings():
    popup = Toplevel()
    SettingsDialog(popup).pack()

root = Tk()

l = Label(text="Hello Fletcher")
l.pack()

p = Button(text="Preferences", command=show_settings)
p.pack()

b = Button(text="Exit", command=sys.exit)
b.pack()

root.mainloop()
