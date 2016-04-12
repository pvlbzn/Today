# Fibonacci as microservice.

from socket import *
from fib import fib

# Add a threading
from threading import Thread

def fib_server(address):
    # New TCP IPv4 socket
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # Bind it to the address
    sock.bind(address)
    # Listen with BACKLOG=5
    sock.listen(5)
    while True:
        # Accept a connection. It must be bound to an address
        # and listening for connection. Return value is a pair
        # (conn, address), where conn is a new socket object.
        client, addr = sock.accept()
        print("Connection", addr)
        # Pass a socket objet to a handler.
        # fib_handler(client)
        # Threading version:
        Thread(target=fib_handler, args=(client,), daemon=True).start()

def fib_handler(client):
    while True:
        # Recv data from the socket. The return value is a bytes obj
        # representing the data recvd. For the best match with hardware
        # and network, the value of bufsize should be a relatively small
        # power of 2, like, 4096.
        req = client.recv(128)
        if not req:
            break
        # Cast bytes to the int.
        n = int(req)
        # Compute fib
        result = fib(n)
        # Create response by incoding the result into ascii string in bytes.
        resp = str(result).encode('ascii') + b'\n'
        # Send response.
        client.send(resp)
    print("Close")

if __name__ == '__main__':
    fib_server(('', 25000))
