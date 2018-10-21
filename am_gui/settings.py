from am_utils.prefs import Prefs

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

class SettingsDialog(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.p = parent
        self.prefs = Prefs()

        self.name = StringVar(self, value=self.prefs.get('name'))
        self.root_folder = StringVar(self, value=self.prefs.get('root_folder'))

        Entry(self, textvariable=self.name).grid(row=0, column=0, columnspan=2)
        Entry(self, textvariable=self.root_folder).grid(row=1, column=0, columnspan=2)

        Button(self, text='Save', command=self.save).grid(row=2, column=0)
        Button(self, text='Cancel', command=parent.destroy).grid(row=2, column=1)

    def save(self):
        name = self.name.get()
        self.prefs.set('name', name)

        showinfo(title='popup', message='Settings saved!')
        self.p.destroy()

if __name__ == '__main__':
    window = SettingsDialog()
    window.pack()
    window.mainloop()
