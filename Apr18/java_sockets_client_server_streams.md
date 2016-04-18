####Programming Sockets in Java

*Awesome Java trait is that I can find an article on Java from 1996 and it will be perfectly valid for today, at least for a Java 'low-level' things such as sockets.*

**Client socket**:

```
Socket clientsock;
try {
	clientsock = new Socket(host, port);
} catch (IOException ioe) {
	System.err.println(ioe.getMessage())
}
```

**Server socket**:

```
ServerSocket serversock;
try {
	serversock = new ServerSocket(port);
} catch (IOException ioe) {
	System.err.println(ioe.getMessage())
}
```

You have to create a socket object from the `ServerSocket` in order to listen for and **accept** connections form clients.

```
Socket clientsock = null;
try {
	ss = serversock.accept();
} catch (IOException ioe) {
	System.err.println(ioe.getMessage());
}
```

-

**Input streams** are used to read data from the server. **Output streams** are used to write data to the server.

```
InputStream in = socket.getInputStream();
OutputStream out = socket.getOutputStream();
```

Because these are ordinary streams, the same streams taht used to r/w file, they can be converted. It is possible to wrap the `OutputStream` with a `PrintStream`, so that can easily write text with methods like `println()`. `InputStream` can be wrapped with a `BufferedReader` via an `InputStreamReader`.

See `SocketClient.java`




















