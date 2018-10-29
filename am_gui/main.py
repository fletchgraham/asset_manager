from tkinter import *
from tkinter.ttk import *

from am_utils.prefs import Prefs
from am_utils.data_model import Model
from am_utils.crawler import crawl

from am_gui.asset_tree import AssetTree
from am_gui.settings import SettingsDialog

class MainApp(Frame):
    """The main window for the application"""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.info_text = StringVar()
        pad = 8

        # Frame out the main areas of the gui:
        self.toolbar = Frame(self)
        self.toolbar.grid(row=0, sticky=N+E+S+W, padx=pad, pady=pad)
        self.tree = AssetTree(self)
        self.tree.grid(row=1, sticky=N+E+S+W, padx=pad)
        self.infobar = Frame(self)
        self.infobar.grid(row=2, sticky=N+E+S+W, padx=pad, pady=pad)

        # Add weight to rows and columns so they stretch.
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add stuff to the toolbar:
        self.search_bar = Entry(self.toolbar)
        self.search_bar.pack(side=LEFT)
        self.search_bar.insert(0, "Search")

        refresh_btn = Button(self.toolbar, text="Refresh",
            command=self.refresh_tree)
        refresh_btn.pack(side=LEFT)

        open_btn = Button(self.toolbar, text="Open",
            command=self.tree.open_location)
        open_btn.pack(side=LEFT)

        settings_btn = Button(self.toolbar, text="Preferences",
            command=show_settings)
        settings_btn.pack(side=LEFT)

        # Add stuff to infobar:
        info_label = Label(self.infobar, textvariable=self.info_text)
        info_label.pack(side=LEFT, fill=X)

    def refresh_tree(self):
        """Clear the tree then re-crawl for assets."""
        
        self.info_text.set('Crawling asset folder...')

        prefs = Prefs()
        try:
            assets = crawl(prefs.get('root_folder'))
        except:
            assets = ['check your prefs']

        model = Model(assets)

        filters = []
        for f in self.search_bar.get().split(','):
            filters.append(f.strip())

        self.tree.refresh(model, filters=filters)

        # Update the infobar text.
        message = 'Found {} assets.'.format(len(self.tree.get_children('')))
        self.info_text.set(message)

# Some useful functions:

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

def return_refresh(event):
    main_app.refresh_tree()

# MAIN APP:

root = Tk()
center_window(root, 1440, 960)

main_app = MainApp(root)
main_app.pack(fill=BOTH, expand=True)

root.bind('<Return>', return_refresh)

style = Style(root)
style.configure('Treeview', rowheight=128)

root.mainloop()
