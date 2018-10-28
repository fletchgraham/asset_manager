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

    # Add a thumbnail image object to the dict:
    d['thumb'] = get_thumbnail(path, 120)

    return d

def get_thumbnail(path, size):
    """Search for, and load in the thumbnail from the given path."""

    thumb = 0 # Initialize a variable for the final thumb to return.

    # Get a list of images in the folder:
    imgs = []
    for i in os.listdir(path):
        if p.splitext(i)[1].lower() in ['.jpg', '.jpeg', '.png', '.tif']:
            imgs.append(i)

    src = 0 # Initialize a variable for the thumbnail source.

    # Intelligently pick an image from the folder:
    for i in imgs:
        if p.splitext(i)[0] == p.basename(path):
            src = i
            break
        else:
            src = imgs[-1]

    # Create a placeholder thumb if a source couldn't be found:
    if not src:
        thumb = Image.new('RGB', (size, size), color = (105, 0, 255))

    # If a source was found, process it and assign it to the thumb variable:
    else:
        src = p.join(path, src)
        image = Image.open(src)
        image.convert('RGB')
        image.thumbnail((size,size))
        thumb = ImageTk.PhotoImage(image)

    return thumb # return the image object

if __name__ == '__main__':
    test_path = r'C:\Users\Fletcher Graham\mayo\warehouse2\mayo\sets\estate'

    print(build_asset(test_path))
