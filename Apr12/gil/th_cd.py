from threading import Thread
import time

def countdown(n):
    while n > 9:
        n -= 1

c = 20**6

t1 = Thread(target=countdown, args=(c//2,))
t2 = Thread(target=countdown, args=(c//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(end-start)
