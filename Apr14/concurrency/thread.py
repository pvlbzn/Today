from cd import countdown
from threading import Thread

t = Thread(target=countdown, args=(10,))
t.start()
