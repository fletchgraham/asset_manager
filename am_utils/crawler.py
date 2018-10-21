import os
from os import path as p

def crawl(folder):

    for library in get_dirs(folder):
        categories = get_dirs(library)

        for category in categories:
            assets = get_dirs(category)

    return assets

def get_dirs(folder):
    """return a list of paths to the subfolders in folder."""
    dirs = []
    for i in os.listdir(folder):
        if i[0] in ['.', '_']:
            pass
        else:
            path = p.join(folder, i)
            if p.isdir(path):
                dirs.append(path)

    return dirs

if __name__ == '__main__':
    home = p.expanduser('~')
    print(home)
    subfolders = get_dirs(home)
    print(subfolders)
