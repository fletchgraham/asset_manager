from am_utils.prefs import Prefs
from am_utils.data_model import Model
from am_utils.crawler import crawl
from am_utils.thumbnails import process_thumbs
from am_gui.asset_tree import AssetTree
import os
from os import path as p

from tkinter import *
from tkinter.ttk import *
from am_gui.settings import SettingsDialog

class AssetList(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        # Create the Elements:
        l = Label(self, text="Assets:")
        b = Button(self, text="Refresh", command=self.refresh_tree)

        self.tree = AssetTree(self)

        # Style and place the elements:
        l.grid(row=0, column=0, sticky=W)
        b.grid(row=0, column=1, sticky=E)
        self.tree.grid(row=1, column=0, columnspan=2, sticky=N+E+S+W)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def refresh_tree(self):
        """Clear the tree then re-crawl for assets."""
        prefs = Prefs()
        try:
            assets = crawl(prefs.get('root_folder'))
        except:
            assets = ['check your prefs']

        model = Model(assets)
        self.tree.refresh(model, filters=[])

class ActionsMenu(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None, tree=None):
        Frame.__init__(self, parent)

        # Create the gui elements:
        p = Button(self, text="Preferences", command=show_settings).pack()
        o = Button(
            self,
            text="Open Location",
            command=tree.open_location
            ).pack()
        c = Button(self, text="Exit", command=sys.exit).pack()

def show_settings():
    """Display a dialog for editing settings."""
    popup = Toplevel()
    center_window(popup, 400, 400)
    SettingsDialog(popup).grid(row=0, column=0, sticky=E)

def center_window(window, w, h):
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    x = int((sw - w)/2)
    y = int((sh - h)/2)
    geom = '{}x{}+{}+{}'.format(w, h, x, y)
    window.geometry(geom)

# MAIN APP:

root = Tk()
center_window(root, 800, 600)

paned_window = Panedwindow(root, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)

treeview = AssetList(paned_window)
menu = ActionsMenu(paned_window, treeview.tree)

paned_window.add(treeview, weight=4)
paned_window.add(menu, weight=1)

style = Style(root)
style.configure('Treeview', rowheight=128)

root.mainloop()
