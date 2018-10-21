"""Dealing with asset images."""

from PIL import Image
from PIL import ImageDraw
from os import path as p
import os

def optimize_image(path_in, path_out, size=800):
    '''take in an image, resize it, and save it out.'''

    # If destination directory doesn't exist create it:
    dst_dir = p.dirname(path_out)
    if not p.exists(dst_dir):
        os.makedirs(dst_dir)

    src = path_in

    if not p.exists(src):
        img = Image.new('RGB', (size, size), color = (105, 0, 255))
        img.save(path_out)

    else:
        # Open the source image, size and resample, save it out.
        im = Image.open(path_in)
        im.thumbnail((size,size))
        im.save(path_out, "JPEG")

def process_thumbs(asset_paths, root_folder, hard=False):
    for path in asset_paths:
        src = p.join(path, p.basename(path) + '.jpg')
        dst = p.join(root_folder, '_thumbs', p.basename(path) + '.jpg')

        if not p.exists(dst) or hard:
            optimize_image(src, dst)
