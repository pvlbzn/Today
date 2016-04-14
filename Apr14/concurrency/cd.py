import time

def countdown(n):
    while n > 0:
        print('t', n)
        n -= 1
        time.sleep(5)

