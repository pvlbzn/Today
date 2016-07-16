from time import sleep
from random import random
from threading import Thread, local

loc = local()

def bar():
    global g
    print('Global:\t{}'.format(g))
    print('Local:\t{}'.format(loc.v))

def foo():
    bar()


class Th(Thread):
    def run(self):
        global g
        sleep(random())
        g = self.getName()
        loc.v = self.getName()
        sleep(1)
        foo()

Th().start();
Th().start();
Th().start();