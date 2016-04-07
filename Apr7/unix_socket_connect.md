###socket()

```
#include <sys/types.h>
#include <sys/socket.h>

int socket(int domain, int type, int protocol);
```

Arguments allows to say what kind of socket you want: IPv[n], stream/datagram, TCP/UDP.

**PF_INET** - Protocol Family
**AF_INET** - Address Family

```
int s;

// Pretend we already filled out the hints struct
getaddrinfo("www.some.page", "http", &hints, &res);

s = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
```

`socket()` simply returns to uou a *socket descriptor*, or -1 on error.


###bind()

You might have to associate that socket with a port on your local machine. The port number *is used by the kernel to match an incoming packet* to a certain process's socket descriptor.

```
#include <sys/types.h>
#include <sys/socket.h>

int bind(int sockfd, struct sockaddr *my_addr, int addrlen);
```

`sockfd` it the *socket file descriptor* returned by `socket()`. `my_addr` is a pointer to a struct `sockaddr` that contains info about your address(port, IP). `addrlen` is the len in bytes of that addr.

```
struct addrinfo hints, *res;
int sockfd;

memset(&hints, 0, sizeof hints);
hints.ai_family = AF_UNSPEC;			// IPv4 or IPv6
hints.ai_socktype = SOCK_STREAM;
hints.ai_flags = AI_PASSIVE;			// Fill in IP for me

getaddrinfo(NULL, "3490", &hints, &res);

// Make a socket and take a file descriptor
sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

bind(sockfd, res->ai_addr, res->ai_addrlen);
```

If needed to connect to specific IP, drop the AI_PASSIVE and put an IP in for the first arg to `getaddrinfo()`.

And again, ports below 1024 are **reserved** unless you are the superuser. Max port number is (1<<16) - 1.
