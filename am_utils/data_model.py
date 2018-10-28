"""For dealing with asset data"""
import os
from os import path as p

from PIL import Image, ImageTk

class Model():
    """Class for interacting with asset data"""
    def __init__(self, paths):
        self.assets = []
        for path in paths:
            asset = build_asset(path)
            self.assets.append(asset)


def build_asset(path):
    """Build a dictionary based on the asset path.
    Assumes this structure: /assets/library/category/asset"""

    d = {} # Initialize the asset dictionary.

    # Extract the info we can get from the path itself:
    tail, d['name'] = p.split(path)
    tail, d['category'] = p.split(tail)
    tail, d['library'] = p.split(tail)
    d['path'] = path

    return d

if __name__ == '__main__':
    test_path = r'C:\Users\Fletcher Graham\mayo\warehouse2\mayo\sets\estate'

    print(build_asset(test_path))
