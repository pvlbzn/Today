####close(), shutdown()

```
close(sockfd);
```

Will prevent any more reads and writes to the socket. For more control over how the socket closes - use the `shutdown()`.

```
int shutdown(int sockfd, int how);
```

`sockfd` is the socket file descriptor which will be shated down, and `how`:

```
0		Further receives are disallowed
1		Further sends are disallowed
2		Further sends and receives are disallowed(like close())
```

`shutdown()` doesnt actually close the file descriptor, it changes its usability. To free a socket descriptor use `close()`.

<br>

####getpeername(), gethostname()

`getpeername()` is who are you:

```
#include <sys/socket.h>

int getpeername(int sockfd, struct sockaddr *addr, int *addrlen);
```

`gethostname()` is who I am:

```
#include <unistd.h>

int gethostname(char *hostname, size_t size);
```

