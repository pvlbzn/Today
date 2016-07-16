from time import sleep
from random import random
from threading import Thread, local

import threading


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


class Worker(threading.Thread):
    nmsp = threading.local()
    def run(self):
        self.nmsp.val = 0
        for i in range(5):
            self.nmsp.val += 1
            print("thread: {0}, value: {1}".format(self.name, self.nmsp.val))

# Th().start();
# Th().start();
# Th().start();

w1 = Worker()
w2 = Worker()
w3 = Worker()

w1.start()
w2.start()
w3.start()

w1.join()
w1.join()
w1.join()