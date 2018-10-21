from am_utils.prefs import Prefs

from tkinter import *
from tkinter import ttk

class SettingsDialog(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        # Not sure how else to kill the parent later:
        self.p = parent

        # Retrieve the preferences from the shelve:
        self.prefs = Prefs()
        self.name = StringVar(self, value=self.prefs.get('name'))
        self.root_folder = StringVar(self, value=self.prefs.get('root_folder'))

        # Draw the labels:
        Label(self, text='Name:').grid(row=0, column=0, sticky=W)
        Label(self, text='Root Folder:').grid(row=1, column=0, sticky=W)

        # Draw the entry boxes:
        Entry(self, textvariable=self.name).grid(
            row=0, column=1, columnspan=2, sticky=E)
        Entry(self, textvariable=self.root_folder).grid(
            row=1, column=1, columnspan=2, sticky=E)

        # Draw the buttons:
        Button(self, text='Save', command=self.save).grid(row=2, column=0)
        Button(self, text='Cancel', command=parent.destroy).grid(row=2, column=1)

    def save(self):
        """Save the values in the text inputs to the prefs shelve."""
        self.prefs.set('name', self.name.get())
        self.prefs.set('root_folder', self.root_folder.get())
        self.p.destroy()

if __name__ == '__main__':
    window = SettingsDialog()
    window.pack()
    window.mainloop()
