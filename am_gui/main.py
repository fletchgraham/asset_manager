from am_utils.prefs import Prefs
from am_utils.crawler import crawl
import os

from tkinter import *
from tkinter.ttk import *
from am_gui.settings import SettingsDialog

class AssetList(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        Label(self, text="Assets:").grid(row=0, column=0, sticky=W)
        Button(self, text="Refresh", command=self.refresh_tree).grid(row=0, column=1, sticky=E)

        self.tree = Treeview(self)
        self.tree.grid(row=1, column=0, columnspan=2, sticky=N+E+S+W)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def refresh_tree(self):
        prefs = Prefs()
        try:
            assets = crawl(prefs.get('root_folder'))
        except:
            assets = ['check your prefs']

        self.tree.delete(*self.tree.get_children())
        for i in assets:
            self.tree.insert('', 'end', text=i)

class ActionsMenu(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Button(self, text="Preferences", command=show_settings).grid(row=0)
        Button(self, text="Exit", command=sys.exit).grid(row=1)

        self.grid_columnconfigure(0, weight=1)
def show_settings():
    popup = Toplevel()
    SettingsDialog(popup).grid(row=0, column=0, sticky=E)

# MAIN APP:

root = Tk()

paned_window = Panedwindow(root, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)

treeview = AssetList(paned_window)
menu = ActionsMenu(paned_window)

paned_window.add(treeview, weight=4)
paned_window.add(menu, weight=1)

root.mainloop()
