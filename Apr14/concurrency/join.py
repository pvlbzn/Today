# How the threading.Thread.join() works.

from threading import Thread
import time

def p():
    for _ in range(3):
        time.sleep(1.)
        print('Printed')

print('With join()')
t = Thread(target=p)
t.start()
t.join()
print('1, should be printed after 3 \'Printed\'')

print('\nWithout join()')
t = Thread(target=p)
t.start()
print('2, will be printed first, I guess')
