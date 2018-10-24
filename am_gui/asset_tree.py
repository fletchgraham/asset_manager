"""Custom tk treeview class that displys the list of assets."""

from am_utils.prefs import Prefs

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk

import os
from os import path as p

class AssetTree(ttk.Treeview):
    def __init__(self, parent=None, data_model=[]):
        """for now, data_model is a list of paths."""
        ttk.Treeview.__init__(self, parent)

        self['columns'] = ('category', 'library')
        self.refresh(data_model)
        self.icons = []

    def refresh(self, data_model):
        prefs = Prefs()
        r = prefs.get('root_folder')
        self.delete(*self.get_children())

        for i in data_model:
            head, name = p.split(i)
            head, category = p.split(head)
            head, library = p.split(head)

            # Make icons:
            thumb_path = p.join(r, '.am', 'thumbs', name + '.jpg')
            image = Image.open(thumb_path)
            image.thumbnail((120,120))
            icon = ImageTk.PhotoImage(image)

            # Icons must be added to a list lest they get garbage collected:
            self.icons.append(icon)

            self.insert(
                '',
                'end',
                text=name,
                image=self.icons[-1],
                values=(category, library)
                )

    def open_location(self):
        prefs = Prefs()
        r = prefs.get('root_folder')

        selected = self.selection()

        for i in selected:
            name = self.item(i, 'text')
            values = self.item(i, 'values')
            path = p.join(r, values[1], values[0], name)
            os.startfile(path)
