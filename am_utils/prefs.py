"""Deal with saved configs."""

import shelve
import os
from os import path as p

class Prefs:
    """A class to interface with a preference shelve."""
    # Find users home dir for defaults:
    home = p.expanduser('~')

    def __init__(self, location=home, foldername='.asset_manager'):
        location = p.join(location, foldername)
        if not p.exists(location):
            os.makedirs(location)

        self.file = p.join(location, 'settings')

    def get(self, key):
        prefs = shelve.open(self.file)
        try:
            value = prefs[key]
        except:
            value = None

        prefs.close()
        return value

    def set(self, key, value):
        prefs = shelve.open(self.file)
        prefs[key] = value
        prefs.close()

if __name__ == '__main__':

    test_prefs = Prefs(foldername='.test_prefs')
    test_prefs.set('name', 'Fletcher Graham')
    print(test_prefs.get('name'))
