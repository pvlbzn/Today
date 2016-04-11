# Cron running task for project automatization.
# TODO: Later on I want to add a some project analisys tools here.

import os
import datetime
from pathlib import Path

m = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

def get_name():
    '''
    Create folder name from the current date in format
    3 first letters of the month + number of the day.
    April 23 -> Apr23.
    '''
    now = datetime.datetime.now()
    # -1 because tuple has a zero-index.
    month = m[now.month - 1]
    day = now.day
    return month + str(day)

def create_folder(name):
    p = Path(name)
    if not p.exists():
        p.mkdir()

if __name__ == '__main__':
    abs = os.path.abspath(__file__)
    os.chdir(os.path.dirname(abs))
    create_folder(get_name())
