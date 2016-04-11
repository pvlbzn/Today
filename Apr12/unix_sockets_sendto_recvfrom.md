####sendto(), recvfrom()

Since datagram sockets arent connected to a remote host, we need to provide the destination address:

**`sendto()`**:

```
int sendto(int sockfd, const void *msg, int len, unsigned int flags, const struct sockaddr *to, socklen_t tolen);
```

It is similar to `send()`. `to` is a pointer to a `struct sockaddr` which contains the destination IP address and port. `tolen` can be set to `sizeof *to` or `sizeof(struct sockaddr_storage)`.


**`recvfrom()`**:

```
int recvfrom(int sockfd, void *buf, int len, unsigned int flags, struct sockaddr *from, int *fromlen);
```

This is like `recv()` with: `from` is a pointer to a local `struct sockaddr_storage` with IP and port of the originating machine. `fromlen` is a pointer to a local int thath should be initialize to `sizeof *from` or `sizeof(struct sockaddr_storage)`.
