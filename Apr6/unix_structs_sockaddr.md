###Structs

Socket descriptor: `int`
One of the first things you will call when making a connection:

```
struct addrinfo {
	int 			ai_flags; 		// AI_PASSIVE, AI_CANONNAME, etc.
	int 			ai_family; 		// AF_INET, AF_INET6, AF_UNSPEC
	int 			ai_socktype; 	// SOCK_STREAM, SOCK_DGRAM
 	int 			ai_protocol; 	// use 0 for "any"
 	size_t 			ai_addrlen; 	// size of ai_addr in bytes
 	struct sockaddr *ai_addr; 		// struct sockaddr_in or _in6
 	char 			*ai_canonname; 	// full canonical hostname
 	struct addrinfo *ai_next; 		// linked list, next node
};
```

**ai_next** points at the next element.

```
struct sockaddr {
	unsigned short	sa_family;		// Address family: AF_INET(IPv4) or AR_INET6(IPv6)
	char			sa_data[14];	// 14 bytes of protocol address
};
```

To deal with `struct sockaddr`, programmers created a parallel structure: `struct sockaddr_in`, where is _in stands for "Internet". `struct sockaddr_in` **can be cast** to a pointer to a `struct sockaddr` and vice-versa. Even though `connect()` wants a `struct sockaddr*`, you can still use a struct `sockaddr_in`.

```
struct sockaddr_in {
	short int			sin_family;		// Address family, AF_INET
	unsigned short int	sin_port;		// Port number
	struct in_addr		sin_addr;		// Internet address
	unsigned char		sin_zero[8];	// Same size as struct sockaddr
};

struct in_addr {
	uint32_t s_addr;
};
```

The same exists for IPv6:

```
struct sockaddr_in6 {
	u_int16_t		sin6_family;	// Address family, AF_INET6
	u_int16_t		sin6_port;		// Port number, Network Byte Order
	u_int32_t		sin6_flowinfo;	// IPv6 flow info
	struct in6_addr	sin6_addr;		// IPv6 address
	u_int32_t		sin6_scope_id;	// Scope ID
};

struct in6_addr {
	unsigned char	s6_addr[16];	// IPv6Address
};
```

There is another simple `struct sockaddr_storage` that is designed to be large enough to hold both IPv4 and IPv6 structs.

```
struct sockaddr_storage {
	sa_family_t ss_family;
	
	// Padding, implementation specific
	char	__ss_pad1[_SS_PAD1SIZE];
	int64_t	__ss_align;
	char	__ss_pad2[_SS_PAD2SIZE];
};
```


