"""Custom tk treeview class that displys the list of assets."""

from am_utils.prefs import Prefs
from am_utils.thumbnails import process_thumbs

from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

import os
from os import path as p

class AssetTree(ttk.Treeview):
    def __init__(self, parent=None, data_model=None):
        """for now, data_model is a list of paths."""
        ttk.Treeview.__init__(self, parent)

        self['columns'] = ('category', 'library')
        self.refresh(data_model)
        self.icons = []

    def refresh(self, data_model):
        self.delete(*self.get_children())

        if not data_model:
            pass

        else:
            for i in data_model.assets:
                name = i.get('name')
                category = i.get('category')
                library = i.get('library')
                self.icons.append(i.get('thumb'))

                self.insert(
                    '',
                    'end',
                    text=name,
                    image=self.icons[-1],
                    values=(category, library)
                    )

    def get_selected_paths(self):
        prefs = Prefs()
        r = prefs.get('root_folder')

        selected = self.selection()
        paths = []

        for i in selected:
            name = self.item(i, 'text')
            values = self.item(i, 'values')
            path = p.join(r, values[1], values[0], name)
            paths.append(path)

        return paths

    def open_location(self):
        selected = self.get_selected_paths()
        for path in selected:
            os.startfile(path)

    def selected_thumbs(self):
        prefs = Prefs()
        r = prefs.get('root_folder')
        paths = self.get_selected_paths()
        process_thumbs(paths, r, hard=True)
