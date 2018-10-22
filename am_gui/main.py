from am_utils.prefs import Prefs
from am_utils.crawler import crawl
from am_utils.thumbnails import process_thumbs
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

        self.tree = Treeview(self)
        self.tree['columns'] = ('category', 'library')

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
        self.tree.delete(*self.tree.get_children())
        for i in assets:
            head, name = p.split(i)
            head, category = p.split(head)
            head, library = p.split(head)
            self.tree.insert('', 'end', text=name, values=(category, library))

class ActionsMenu(Frame):
    """Gui element for getting settings from the user."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        # Create the gui elements:
        p = Button(self, text="Preferences", command=show_settings)
        c = Button(self, text="Exit", command=sys.exit)
        t = Button(self, text="Thumbnails", command=make_thumbs)

        # Style and place the elements:
        p.grid(row=0)
        c.grid(row=1)
        t.grid(row=2)
        self.grid_columnconfigure(0, weight=1)

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

def make_thumbs():
    prefs = Prefs()
    root_folder = prefs.get('root_folder')
    assets = crawl(root_folder)
    process_thumbs(assets, root_folder, hard=True)

# MAIN APP:

root = Tk()
center_window(root, 800, 600)

paned_window = Panedwindow(root, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)

treeview = AssetList(paned_window)
menu = ActionsMenu(paned_window)

paned_window.add(treeview, weight=4)
paned_window.add(menu, weight=1)

root.mainloop()
