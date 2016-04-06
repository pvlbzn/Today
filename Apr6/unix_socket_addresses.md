####IP Addresses
IP address "10.12.110.57".
`inet_pton()` converts an IP address in numbers-and-dots notation into either a `struct in_addr` or `struct in6_addr` depending on `AF_INET[6]`. `pton` stands for "presentation to network".

From string to binary representation:

```
struct sockaddr_in 	sa;
struct sockaddr_in6	sa6;

inet_pton(AF_INET,  "10.12.110.57", &(sa.sin_addr));
inet_pton(AF_INET6, "2001:db8:63d3:1::3490", &(sa6.sin6_addr));
```

Other way around:

```
char 	ip6[INET6_ADDRSTRLEN];		// Space to hold the IPv6 string
struct	sockaddr_in6 sa6;

inet_ntop(AF_INET6, &(sa6.sin6_addr), ip6, INET6_ADDRSTRLEN);

printf("The address is: %s\n", ip6);
```

`inet_ntop([type], [address], [pointer to a string to hold a result], [maxlen])`


####NAT
Network Address Translation.
Long story short: Provider gives me some IP and I connect to this IP lots of clients. This is possible because my local machine has local address like `192.168.n.n`. IPv6 has private networks too, they will start with `fdxx:`.
