###getaddrinfo()

```
int geraddrinfo(const char *node,		// IP or "www.google.com"
				const char *service,	// Port number or "http"
				const struct addrinfo *hints,
				struct addrinfo **res);
```

`node` parameter is the host name to connect to(or IP). `service` is a port number or the name of a particular service from IANA Port List (/etc/services) like "http", "ftp", "telnet", etc. `hints` parameter points to a `struct addrinfo`. `res` gives you a pointer to a linked-list.

```
int status;
struct addrinfo hints;
struct addrinfo *servinfo;			// Will point ot the result

mamset(&hints, 0, sizeof hints);

hints.ai_family = AF_UNSPEC;		// Don't care about version
hints.ai_socktype = SOCK_STREAM;	// TCP

if ((status = getaddrinfo(NULL, "3490", &hints, &servinfo)) != 0) {
	fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
	exit(1);
}

// servinfo now points to a linked list of 1 or more struct addrinfos.
// Do smth

freeaddrinfo(servinfo);				// Free the linked-list
```

See `showip.c` in the same folder.
