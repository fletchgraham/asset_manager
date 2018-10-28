"""Custom tk treeview class that displys the list of assets."""

from am_utils.prefs import Prefs
from am_utils.thumbnails import get_thumbnail

from tkinter import *
from tkinter import ttk

import os
from os import path as p

def filter(dictionaries, filters=[]):
    if not filters:
        return dictionaries

    filtered = []

class AssetTree(ttk.Treeview):
    def __init__(self, parent=None, data_model=None):
        """for now, data_model is a list of paths."""
        ttk.Treeview.__init__(self, parent)

        self['columns'] = ('category', 'library')
        self.refresh(data_model)
        self.icons = []

    def refresh(self, data_model, filters=[]):
        self.delete(*self.get_children())

        if not data_model:
            return

        remaining = []

        if not filters:
            remaining = data_model.assets
        else:
            for asset in data_model.assets:
                for filter in filters:
                    for key in asset:
                        if filter.lower() in asset.get(key).lower():
                            if not asset in remaining:
                                remaining.append(asset)

        for i in remaining:
            name = i.get('name')
            category = i.get('category')
            library = i.get('library')
            path = i.get('path')
            self.icons.append(get_thumbnail(path, 120))

            self.insert(
                '',
                'end',
                text=name,
                image=self.icons[-1],
                values=(category, library)
                )
            self.master.update()

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
