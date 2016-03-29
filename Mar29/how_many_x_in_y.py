import sys
import os

def find(type, dir):
    '''
    Receives 2 args: file postfix, directory.
    Returns amount of files of the postfix type in provided directory.

    Usage example:
        python3 how_many_x_in_y.py .jpg Documents
        24 files of .jpg type in Documents

        python3 how_many_x_in_y.py .c Dropbox
        63 files of .c type in Dropbox

        python3 how_many_x_in_y.py .pdf /
        6682 files of .pdf type in /
    '''
    home = os.path.expanduser('~')
    path = os.path.join(home, dir)
    i = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(type):
                i += 1
    return i

if __name__ == '__main__':
    type = sys.argv[1]
    dir  = sys.argv[2]
    i    = find(sys.argv[1], sys.argv[2])
    print("{0} files of {1} type in {2}".format(i, type, dir))

