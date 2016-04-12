####FaaS: Fibonacci as a Service

*Important note*: code from this session should **not** be used, because it is for learning purposes.

Source file with comments, imports, etc, in: `concurrency/server.py`

```
def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        fib_handler(client)

def fib_handler(client):
    while True:
        req = client.recv(128)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print("Close")
```

<br>

####Connect to it

```
nc localhost 25000

10
55

30
832040
```

Cool, it works, it is a good part. Bad part starts here:

```
// New netcat or telnet connection.
nc localhost 25000

10
// Nothing.
```

So it works one client at a time.

<br>

####Threading

```
def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        Thread(target=fib_handler, args=(client,), daemon=True).start()

def fib_handler(client):
    while True:
        req = client.recv(128)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print("Close")
```

Now server can handle multiple connections. 2 connected netcats works both well, `top` tool shows 3 #TH.


<br>

####Performance, GIL

Write a straightforward performance test for req per sec:

```
from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))

n = 0

from threading import Thread
def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, 'reqs/sec')
        n = 0
Thread(target=monitor).start()

while True:
    sock.send(b'1')
    resp =sock.recv(100)
    n += 1
```

Run it. Result on my machine is 25k reqs/sec. However, if you will connect to the server `nc localhost 25000` and ask to give your back a fib number number, say, 40, requests will drop down to 100 reqs/sec.

If you will run 1 test, performance will be 25k reqs/sec; 2 tests: 12.5k reqs/sec; 3 tests: 7k reqs/sec.

So, everything executes on one core. But there is something about GIL: when you run a lot of small tasks and one big task, GIL will prioritorise a CPU intensive one, thus, we can see 250 times drop off from 25k reqs/sec to 100 recs/sec. This is a GIL behaviour, not OS.



















