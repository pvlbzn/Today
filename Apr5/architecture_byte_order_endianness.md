###Byte Order, htons(), htonl(), etc

Big-Endian and Little-Endian story short: everything with Intel or Intel-compatible processor, store bytes reversed, so `b3 4f` would be stored in memory as the sequential bytes `4f` followed by `b3`.

[Endianness](https://en.wikipedia.org/wiki/Endianness):
>Big-endian is the most common format in data networking; fields in the protocols of the Internet protocol suite, such as IPv4, IPv6, TCP, and UDP, are transmitted in big-endian order. For this reason, big-endian byte order is also referred to as network byte order. Little-endian storage is popular for microprocessors, in part due to significant influence on microprocessor designs by Intel Corporation. 

```
// The most significant byte is in the start
Big-Endian: 	128d => 1000 0000

// The least significant byte is in the start
Little-Endian: 	128d => 0000 0001
```

Big-Endian called **Network Byte Order**, the Little-Endian called **Host Byte Order**.

-

#### Functions
[**h**ost/**n**etwork][to][**s**hort/**l**ong] anatomy.

```
htons()		host to network short
htonl()		host to network long
ntohs()		network to host short
ntohl()		network to host long
```

In essence, you will want to convert the numbers to Network Byte Order before they go out on the wire, and convert them to Host Byte Order as they come in off the wire.
