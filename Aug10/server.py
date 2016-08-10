from socket import *


def start_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection:", addr)
        handle_conn(client)


def handle_conn(client):
    while True:
        # Buffer size
        req = client.recv(512)
        if not req:
            break
        resp = str(req, 'utf-8')
        client.send(resp.encode("ascii") + b'\n')


if __name__ == "__main__":
    addr = ('', 25000)
    start_server(addr)