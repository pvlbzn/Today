import glob
import sys
import os


def find(dir, type, size):
    '''
    Takes 3 args: directory, type, size.
    Returns list of the filenames which passed condition.

    Usage example:
        python3 files_bigger_than.py Documents 15mb .pdf
        ['list', 'of', 'files']
    '''
    home = os.path.expanduser('~')
    path = os.path.join(home, dir)
    os.chdir(path)
    return [f for f in glob.glob('*'+type) if os.stat(f).st_size > int(size)]

if __name__ == '__main__':
    dir  = sys.argv[1]
    size = sys.argv[2]
    if size[len(size)-2:] == 'mb':
        size = size[:len(size)-2]
        size = int(size) / 1000
    type = sys.argv[3]

    print(find(dir, type, size))
