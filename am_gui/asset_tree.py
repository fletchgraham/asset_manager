"""Custom tk treeview class that displys the list of assets."""

from am_utils.prefs import Prefs
from am_utils.thumbnails import get_thumbnail

from tkinter import *
from tkinter import ttk

import os
from os import path as p

def filter(dictionaries, filters=[]):
    """filter a list of dictionaries. return a filtered list."""
    if not filters:
        return dictionaries

    if filters == ['Search']:
        return dictionaries

    filtered = []

    for d in dictionaries:
        tests = []
        for f in filters:
            test = 0
            for k in d:
                if f.lower() in d.get(k).lower():
                    test = 1
            tests.append(test)

        if not 0 in tests:
            filtered.append(d)

    return filtered

class AssetTree(ttk.Treeview):
    def __init__(self, parent=None, data_model=None):
        """for now, data_model is a list of paths."""
        ttk.Treeview.__init__(self, parent)

        self['columns'] = ('category', 'library')

        self.heading('#0', text='Name')
        self.heading('category', text='Category')
        self.heading('library', text='Library')

        self.column("#0", minwidth=128, width=400)
        self.column("category", minwidth=128, width=128, stretch=False)
        self.column("library", minwidth=128, width=128, stretch=False)

        self.refresh(data_model)
        self.icons = []

    def refresh(self, data_model, filters=[]):
        self.delete(*self.get_children())

        if not data_model:
            return

        filtered = filter(data_model.assets, filters=filters)

        for i in filtered:
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
