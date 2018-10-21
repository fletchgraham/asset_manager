from am_utils.prefs import Prefs

from tkinter import *
from tkinter.messagebox import showinfo

class SettingsDialog(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.p = parent
        self.prefs = Prefs()

        self.name = Entry(parent)
        self.name.pack()
        self.name.insert(0, self.prefs.get('name'))

        save_button = Button(self, text='Save', command=self.save)
        save_button.pack()

        cancel_button = Button(self, text='Cancel', command=parent.destroy)
        cancel_button.pack()

    def save(self):
        name = self.name.get()
        self.prefs.set('name', name)
        showinfo(title='popup', message='Settings saved!')
        self.p.destroy()

if __name__ == '__main__':
    window = SettingsDialog()
    window.pack()
    window.mainloop()
