import urllib.request
import time

from multiprocessing.dummy import Pool as ThreadPool

# Basicaly, if a task is i/o bound it is kind of easy to solve.
# However if the task is CPU bound, it is not that easy to do.
#
#
#


def speed(t1):
    def timer(t2):
        print(t2 - t1)

    return timer


def fetch(n):
    print('running {} threads'.format(n))
    pool = ThreadPool(n)
    urls = [
        'http://stackoverflow.com/questions/',
        'http://stackoverflow.com/questions/',
        # ... 
        # repeat 200 times
        # ...
        'http://stackoverflow.com/questions/',
        'http://stackoverflow.com/questions/',
    ]
    stop = speed(time.time())
    result = pool.map(urllib.request.urlopen, urls)
    # Close and wait until its done.
    pool.close()
    pool.join()
    stop(time.time())


if __name__ == '__main__':
    fetch(1)
    # running 1 threads
    # 10.70187783241272

    fetch(8)
    # running 8 threads
    # 1.7693541049957275

    fetch(32)
    # running 32 threads
    # 0.7312910556793213

    fetch(128)
    # running 128 threads
    # 0.6293540000915527

    fetch(512)
    # running 512 threads
    # 0.9796891212463379
    # The more things to do, the more benefit will be from
    # the threads. In my case there were less than 512 req
    # which make this number of threads pointless.