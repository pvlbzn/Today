from socket import *

class Sock:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def msend(self, msg):
        total = 0
        while total < MSGLEN:
            sent = self.sock.send(msg[total:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total += sent

    def mrecv(self):
        chunks = []
        brecvd = 0
        while brecvd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - brecvd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            brecvd += len(chunk)
        return b''.join(chunks)
