"""Dealing with asset images."""

from PIL import Image, ImageTk
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

    if not src:
        img = Image.new('RGB', (size, size), color = (105, 0, 255))
        img.save(path_out)

    else:
        # Open the source image, size and resample, save it out.
        im = Image.open(path_in)
        rgb_im = im.convert('RGB')
        rgb_im.thumbnail((size,size))
        rgb_im.save(path_out, "JPEG")

def process_thumbs(asset_paths, root_folder, hard=False):
    for path in asset_paths:

        # First choice of image to use:
        src = p.join(path, p.basename(path) + '.jpg')

        # Failing that, it'll grab the first image it finds:
        if not p.exists(src):
            src = 0
            for file in os.listdir(path):
                if p.splitext(file)[1].lower() in ['.jpg', '.jpeg', '.png', '.tif']:
                    src = p.join(path, file)

        dst = p.join(root_folder, '.am', 'thumbs', p.basename(path) + '.jpg')

        if not p.exists(dst) or hard:
            optimize_image(src, dst)

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
        image = Image.new('RGB', (size, size), color = (105, 0, 255))
        thumb = ImageTk.PhotoImage(image)

    # If a source was found, process it and assign it to the thumb variable:
    else:
        src = p.join(path, src)
        image = Image.open(src)
        image.convert('RGB')
        image.thumbnail((size,size))
        thumb = ImageTk.PhotoImage(image)

    return thumb # return the image object
