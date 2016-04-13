import time

def countdown(n):
        while n > 0:
            n -= 1

c = 20**6

start = time.time()
countdown(c)
end = time.time()

print(end-start)
