####connect()

```
#include <sys/types.h>
#include <sys/socket.h>

int connect(int sockfd, struct sockaddr *serv_addr, int addrlen);
```

`sockfd` is a socket file descriptor, returned by the `socket()`.
`serv_addr` is a `struct sockaddr` containing the destination port and IP address.
`addrlen` is the length in bytes of the server address structure.

All of this info can be collected from the results of the `getaddrinfo()` call.



Lets make a socket connection to www.example.com, port 3490:

```
struct addrinfo hints, *res;
int sockfd;

memset(&hints, 0, sizeof hints);
hints.ai_family = AF_UNSPEC;
hints.ai_socktype = SOCK_STREAM;

getaddrinfo("www.example.com", "3490", &hints, &res);

sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

connect(sockfd, res->ai_addr, res->ai_addrlen);
```

<br>

####listen()

```
int listen(int sockfd, int backlog);
```

`sockfd` socket file descriptor from the `socket()` call.
`backlog` is the number of connections allowed on the incoming queue.

Incoming connections are going to waint in queue until you `accept()` them. Most systems limit this number to about 20, its ok to set it to 5-10.

`listen()` returns -1 and sets *errno* on error.

It works with a following sequence:

```
getaddrinfo();
socket();
bind();
listen();
// accept()
```

<br>

####accept()

Some machine try to `connect()` to your machine on a port that you are `listen()`ing to. This connection will be queued up waiting to be `accept()`ed. You call `accept()` and you tell it to get the pending connection. It will return a *new socket file descriptor`. The original one is still listening for more new connections, and the newly created one is finally ready to `send()` and `recv()`.

```
#include <sys/types.h>
#include <sys/socket.h>

int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
```

`sockaddr` usually a pointer to a local `struct sockaddr_storage`. This is wrehe the information about the incoming connection will go.

```
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define MYPORT "3490"			// Port
#define BACKLOG 10				// Number of pending connections queue

int main(void) {
	struct sockaddr_storage their_addr;
	socklen_t addr_size;
	struct addrinfo hints, *res;
	int sockfd, new_fd;
	
	// Imagine an error checking
	
	memset(&hints, 0, sizeof hints);
	hints.ai_family 	= AF_UNSPEC;
	hints.ai_socktype	= SOCK_STREAM;
	hints.ai_flags		= AI_PASSIVE;
	
	getaddrinfo(NULL, MYPORT, &hints, &res);
	
	// Make a socket, bind, listen.
	sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
	bind(sockfd, res->ai_addr, res->ai_addrlen);
	listen(sockfd, BACKLOG);
	
	// Accept an incomming connection.
	addr_size = sizeof their_addr;
	new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &addr_size);
```
