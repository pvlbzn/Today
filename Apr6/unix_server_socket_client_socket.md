###Creating a Socket

When you clicked on the link, your browser did smth like:

```
# IPv4 streaming socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.some.page", 80))
```

When the connect completes, the socket `s` can be used to send in a req for the text of the page. The same socket will read the reply, and then be destroyed. Client sockets are noramally only used for one exchange.

```
# Server socket
ss = socket.socket()
# Bind the socket to a public host and port
ss.bind((socket.gethostname(), 80))
ss.listen(5)
```

`socket.gethostname()` socket will be visible to the outside world. `socket.bind(('localhost', 80))` would still have a "server" socket, but visible only for one machine.

The argument to `.listen()' tells the socket lib thath we want it to queue up as many as 5 connect requests before refusing outside connections.

```
while True:
	(clientsocket, address) = serversocket.accept()
	# Do smth with the client socket
	ct = client_thread(clientsocket)
	ct.run()
```

Server socket doesnt send any data nor receive any data, it just produces "client" sockets. [Source](https://erlerobotics.gitbooks.io/erle-robotics-python-gitbook-free/content/introduction_to_socket/creating_a_socket.html), however this isn't quite right.

####Server Socket, Client Socket
In TCP, client and server can send and receive. Destinction is in how the connection is created.

**Server Socket** - is created to `bind()` to a port and `listen()` for a `connect()` from a client. Server just *waits* for a conversation.

**Client Socket** - is created to `connect()` to a `listen()` server. The client *initiates* the connection.

[Source](https://www.quora.com/What-is-the-difference-between-client-socket-and-server-socket-in-computer-networking/answer/William-Emmanuel-Yu).
