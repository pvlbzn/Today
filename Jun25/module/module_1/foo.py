import os
from module_2 import bar


def run():
    print('Im foo')
    print(__name__)
    print(os.path.curdir)
    bar.run()