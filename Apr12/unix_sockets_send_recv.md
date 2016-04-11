####send(), recv()
These two are for communicating over stream sockets or connected datagram sockets. For unconnected datagram sockets see `sendto()` and `revcfrom()`.

The `send()` call:

```
int send(int sockfd, const void *msg, int len, int flags);
```

`sockfd` is the socket descriptor you want to send data to.
`msg` is a pointer to the data you want to send.
`len` is the length of that data in bytes.

```
char *msg = "Some info in the string.";
int len, bytes_sent;

...

len = strlen(msg);
bytes_sent = send(sockfd, msg, len, 0);
```

`send()` returns the number of bytes actually sent out - this might be less that the number you told it to send.

The `recv()`:

```
int recv(int sockfd, void *buf, int len, int flags);
```

`sockfd` is the socket descriptor to read from.
`buf` is the buffer to read the info into.
`len` is the max buff len.

`recv()` returns the number of bytes actually read into the buffer, or -1 on error, with errno set. It also can return 0 in case of the closed connection by remote side.
