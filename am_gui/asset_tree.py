"""Custom tk treeview class that displys the list of assets."""

from tkinter import *
from tkinter import ttk

import os
from os import path as p

class AssetTree(ttk.Treeview):
    def __init__(self, parent=None, data_model=[]):
        """for now, data_model is a list of paths."""
        ttk.Treeview.__init__(self, parent)

        self['columns'] = ('category', 'library')
        self.refresh(data_model)

    def refresh(self, data_model):
        self.delete(*self.get_children())
        for i in data_model:
            head, name = p.split(i)
            head, category = p.split(head)
            head, library = p.split(head)
            self.insert('', 'end', text=name, values=(category, library))
